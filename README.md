# PiHome
Code Repo for my Raspberry Pis I am using at home.

I currently have a Pi B+ in a little enclusre wired to a 20x4 lcd screen via i2c.
I would like to use this as a little display device; display notes (left via webserver?), calendar information etc.
Eventually I would love to expand the hardware to include further features.
One day I may even add a Mic and Speaker and start playing with Jasper on it - until the I shall have a play around :)

lcd.py - handles the i2c lcd screen functions. Look to perhaps rewrite the functions into a more user friendly Class.

functions.py - To write - a handler for any incoming commands. Commands can come from 

main.py - currently a just displays the IP addresses of the LAN and WLAN connections.
In the future will launch a webserver and also monitor a serial input for commands. Also add bluetooth module as a serial input.
Bluetooth could allow for a child friendly app to be written for my son's tablet to allow for interaction.
