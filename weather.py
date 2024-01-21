from machine import Pin, SPI
import time

MOSI_PIN = 15
MISO_PIN = 12
CLK_PIN = 14
CS_PIN = 13
SPI_CH = 1

spi = SPI(SPI_CH, sck=Pin(CLK_PIN), mosi=Pin(MOSI_PIN), miso=Pin(MISO_PIN), baudrate=100000)

cs = Pin(CS_PIN, Pin.OUT)
cs.high()

msg = bytearray()
msg.append(0x00|0x20)
msg.append(0x90)

cs.low()
spi.write(msg)
cs.high()
time.sleep(0.1)

while True:
    cs.low()
    val = spi.read(4, 0x80|0x40|0x28)
    cs.high()

    val_xl = val[1]
    val_l = val[2]
    val_h = val[3]

    press_val = (val_h << 16) | ( val_l << 8 ) | val_xl
    press = press_val / 4096
    print("Pressure: {:.1f}hPa".format(press))
    time.sleep(1)
