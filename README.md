###board 
* raspebery pi + microcontroller
    * http://elinux.org/RPi_Serial_Connection
    
* arduino yun
    latence sur port serie interne ?
* android device sous linux ?

### devices 
* montre ambit3 
    * https://github.com/openambitproject/openambit 
    
* capteur co2
* capteur o3
* capteur o2
* barometre + temperature
* ecran i2c lcd 

* argos radio device ?
    TBD

### tools
    * ctypes
    * https://code.google.com/p/ctypesgen/ 

###mode de fonctionnement
~en fontion du device inseré (detection via udev)
* arduino raspberry pi
    *   simple proto port serie arduino for sensor value
        ```
    { id="co2","x":value_x,"y":value_y}
        ```

* watches
     * usb openambit crappy C wrapper and ctype (arch dependent)
     * some message yet to be decoded..  (cardio .)

* TODO

* mesure capteur
* envoie sur argos



