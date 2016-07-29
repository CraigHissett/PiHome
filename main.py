import lcd_lib
import smbus
import time
import socket
import fcntl
import struct

PiLCD = lcd_lib.lcd()

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', ifname[:15])
        )[20:24])
    except IOError:
        return "N/A"


def main():
  # Main program block

  while True:
    #Check for any other commands from serial, web etc

    # Send some text
    PiLCD.lcd_display_string("Raspberry Pi         ",1)
    PiLCD.lcd_display_string("I2C LCD              ",2)
    PiLCD.lcd_display_string("LAN: " + get_ip_address('eth0'),3)
    PiLCD.lcd_display_string("WLAN: " + get_ip_address('wlan0'),4)

    time.sleep(2)

if __name__ == '__main__':

  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    PiLCD.lcd_clear
