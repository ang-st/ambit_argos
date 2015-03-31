###board 
* raspebery pi + microcontroller
    * http://elinux.org/RPi_Serial_Connection
    
* arduino yun
    latence sur port serie interne ?
* android device sous linux ?

* ![setup1](img/ambit_setup.jpg)
* ![schema](img/schem_1.jpg)

### devices 
* montre ambit3 
    * https://github.com/openambitproject/openambit 
    
* capteur co2
* capteur o3
* capteur o2
* barometre + temperature
* ecran i2c lcd 

* argos 
    * 248 bits per message including checksum 
    * unidirectionnal
    * 2/4 emitting window / day 
    

### tools
    * ctypes
    * https://code.google.com/p/ctypesgen/ 

### mode de fonctionnement
~en fontion du device inseré (detection via udev)
* arduino raspberry pi
    *   simple proto port serie rpi <-> arduino  pour les valeurs de sensors.

* ambit watche
     * usb openambit crappy C wrapper and ctype (arch dependent)
     * "some message yet to be decoded.."  (cardio .)

### TODO

* interface !!
* mesure capteur
* envoi sur argos
    * http://www.argos-system.org/web/en/293-become-a-user.php
    



