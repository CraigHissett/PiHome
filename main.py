import lcd
import time

def main():
  # Main program block

  # Initialise display
  lcd.lcd_init()

  while True:
    # Send some text
    lcd.lcd_string("Pi Home",LCD_LINE_1)
    lcd.lcd_string("Awaiting Command",LCD_LINE_2)
    lcd.lcd_string("LAN: " + lcd.get_ip_address('eth0'),LCD_LINE_3)
    lcd.lcd_string("WLAN: " + lcd.get_ip_address('wlan0'),LCD_LINE_4)

    time.sleep(2)

if __name__ == '__main__':

  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    lcd.lcd_byte(0x01, LCD_CMD)
