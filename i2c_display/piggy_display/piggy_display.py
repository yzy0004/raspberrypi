#!/usr/bin/env python

#RASPBERRY PI VERSION

from lib_oled96 import ssd1306
from time import sleep
from PIL import ImageFont, ImageDraw, Image
font = ImageFont.load_default()

from smbus import SMBus
i2cbus = SMBus(1)

oled = ssd1306(i2cbus)
draw = oled.canvas

padding = 2
shape_width = 20
top = padding
bottom = oled.height - padding - 1

draw.rectangle((0, 0, oled.width-1, oled.height-1), outline=1, fill=0)
draw.text((1,1), 'Hi Piggy', font=font, fill=1)
draw.text((1,14), 'Good Morning', font=font, fill=1)
oled.display()

sleep(6)
oled.onoff(0)

oled.cls()
