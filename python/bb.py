import ambit
from ctypes import *
import pdb
import hexdump
from pprint import pprint
dev=ambit.libambit_enumerate()
ob=ambit.libambit_new(dev)

log_types = { "ambit_log_sample_type_periodic" : 0x0200,
    "ambit_log_sample_type_logpause" : 0x0304,
    "ambit_log_sample_type_logrestart" : 0x0305,
    "ambit_log_sample_type_ibi" : 0x0306,
    "ambit_log_sample_type_ttff" : 0x0307,
    "ambit_log_sample_type_distance_source" : 0x0308,
    "ambit_log_sample_type_lapinfo" : 0x0309,
    "ambit_log_sample_type_altitude_source" : 0x030d,
    "ambit_log_sample_type_gps_base" : 0x030f,
    "ambit_log_sample_type_gps_smal" : 0x0310,
    "ambit_log_sample_type_gps_tiny" : 0x0311,
    "ambit_log_sample_type_time" : 0x0312,
    "ambit_log_sample_type_swimming_turn" : 0x0314,
    "ambit_log_sample_type_swimming_stroke" : 0x0315,
    "ambit_log_sample_type_activity" : 0x0318,
    "ambit_log_sample_type_cadence_source" : 0x031a,
    "ambit_log_sample_type_position" : 0x031b,
    "ambit_log_sample_type_fwinfo" : 0x031c,
    "ambit_log_sample_type_unknown" : 0xf000
}

periodic = {'ambit_log_sample_periodic_type_abspressure': 13,
         'ambit_log_sample_periodic_type_altitude': 12,
         'ambit_log_sample_periodic_type_bikepodspeed': 9,
         'ambit_log_sample_periodic_type_bikepower': 31,
         'ambit_log_sample_periodic_type_cadence': 26,
         'ambit_log_sample_periodic_type_charge': 16,
         'ambit_log_sample_periodic_type_distance': 3,
         'ambit_log_sample_periodic_type_ehpe': 10,
         'ambit_log_sample_periodic_type_energy': 14,
         'ambit_log_sample_periodic_type_evpe': 11,
         'ambit_log_sample_periodic_type_gpsaltitude': 17,
         'ambit_log_sample_periodic_type_gpshdop': 19,
         'ambit_log_sample_periodic_type_gpsheading': 18,
         'ambit_log_sample_periodic_type_gpsspeed': 7,
         'ambit_log_sample_periodic_type_gpsvdop': 20,
         'ambit_log_sample_periodic_type_hr': 5,
         'ambit_log_sample_periodic_type_latitude': 1,
         'ambit_log_sample_periodic_type_longitude': 2,
         'ambit_log_sample_periodic_type_noofsatellites': 23,
         'ambit_log_sample_periodic_type_ruleoutput1': 100,
         'ambit_log_sample_periodic_type_ruleoutput2': 101,
         'ambit_log_sample_periodic_type_ruleoutput3': 102,
         'ambit_log_sample_periodic_type_ruleoutput4': 103,
         'ambit_log_sample_periodic_type_ruleoutput5': 104,
         'ambit_log_sample_periodic_type_sealevelpressure': 24,
         'ambit_log_sample_periodic_type_snr': 22,
         'ambit_log_sample_periodic_type_speed': 4,
         'ambit_log_sample_periodic_type_swimingstrokecnt': 32,
         'ambit_log_sample_periodic_type_temperature': 15,
         'ambit_log_sample_periodic_type_time': 6,
         'ambit_log_sample_periodic_type_verticalspeed': 25,
         'ambit_log_sample_periodic_type_wristaccspeed': 8,
         'ambit_log_sample_periodic_type_wristcadence': 21}

kount = {k:0 for k in log_types.keys()}
print ob.contents.device_info.serial
#ambit.libambit_log_read(ob,c1,c2,None,ob)

CB_COUNT = CFUNCTYPE(c_int, c_void_p, POINTER(ambit.ambit_log_header_t))
CB_FUNC = CFUNCTYPE(c_void_p, c_void_p, POINTER(ambit.ambit_log_entry_t))


def date_array(ent):
     ks=[k[0] for k in ent.utc_time._fields_]
     return [ent.utc_time.__getattribute__(k) for k in ks]

import math
def build_log(ent, tp):
        
        t =  [ k[0] for k in log_types.items() if k[1]==ent.type ][0]
       # pdb.set_trace() 
        #if kount[t] == 0:
        #    print t
        #    print_ctypes_obj(ent,indent=2)
        #print t
        #print print_ctypes_obj(ent.u)   
        #ks=[k[0] for k in ent.u._fields_] 
        #data = { k:ent.u.__getattribute__(k) for k in ks }
        #for k,v in data.items():
        #    if hasattr(v,"_fields_"):
        #        ks=[z[0] for z in v._fields_]
        #        data[k]={ z:v.__getattribute__(z) for z in ks }
        #print date_array(ent),t, data
        kount[t]+=1
        if t == "ambit_log_sample_type_gps_tiny":
            pass#gps_tiny(ent)
        if t == "ambit_log_sample_type_altitude_source":
            alt_source(ent)

def periodic_dum(ent):
   pass 

def gps_tiny(ent):
    lat=ent.u.gps_tiny.latitude*math.pi/180/10000000
    lon=ent.u.gps_tiny.longitude*math.pi/180/10000000
    ehpe=ent.u.gps_tiny.ehpe/100.0
    d=date_array(ent)
    data={"latitude":lat,"longitude":lon,"ehpe":ehpe,"date":d}
    print data



def alt_source(ent):
    src_type=ent.u.altitude_source.source_type
    alt_off=ent.u.altitude_source.altitude_offset
    press_off=ent.u.altitude_source.pressure_offset*10
    d=date_array(ent)
    data = { "type":src_type,"altitude_offset":alt_off,"pressure_offset":press_off, "date":d}
    print data


def print_ctypes_obj(obj, indent=0):
    for fname, fvalue in obj._fields_:
        if hasattr(fvalue, '_fields_'):
            print_ctypes_obj(fvalue, indent+4)
        else:
            print '{}{} = {}'.format(' '*indent, fname, getattr(obj, fname))

def callback(obj,log_entry):
        try:
            for i in range(log_entry.contents.header.samples_count):
                ent = log_entry.contents.samples[i]

                build_log(ent,"ambit_log_sample_type_gps_tiny")
                #    pdb.set_trace()
                #print hexdump.hexdump(buffer(ent)[:])
        except Exception,e:
            pdb.set_trace()    
             
def silence_cb(obj,log_c_entry):
        return 1
def close_all(o,i):
    ambit.libambit_close(o)
    ambit.libambit_free_enumeration(i)


c1=CB_COUNT(silence_cb)
c2=CB_FUNC(callback)


ambit.mydump(ob,c1,c2)
pprint(kount) 
close_all(ob,dev)

