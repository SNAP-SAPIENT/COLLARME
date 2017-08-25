# SNAP ideationa nd background for the project:

https://docs.google.com/document/d/1q9E0ONyW5gtDKlLlyuCDKHlbFd3WrH208S0N4GcMjY8/edit

# Resources for Wipy 2.0:

http://docs.micropython.org/en/latest/wipy/wipy/tutorial/index.html

# PinOut diagram for Pysense:

https://docs.pycom.io/chapter/datasheets/boards/pysense.html

# Tutorial to hook up Pysense and Wipy:

https://www.youtube.com/watch?v=I5Qsuz6fEAA

# Pymakr Plugin for Atom :

https://atom.io/packages/pymakr

## Instructions:

-  Use the Pyamkr Plugin on Atom to create a project folder and have your boot.py, main and
    pymakr.conf files.
- Create a /lib folder inside to drop your sensor libraries downloaded from here: https://github.com/pycom/pycom-libraries/tree/master/pysense
- Plug the USB power cable to the power micro USB slot on the pysense and to the USB slot on your laptop. Switch the WiFi to the wlan-<pycom> ssid.
- Credentials : ssid: wlan-<your wipy>
                pwd: www.pycom.io

                login credentials if you were to telnet into the wipy:
                username: micro
                pwd: python
- sync your project folder once connected to the wipy. The main.py file should automatically run.  should this not happen, execute the command : execfile("filename.py")
- The output of the sensor values in the same project folder.
