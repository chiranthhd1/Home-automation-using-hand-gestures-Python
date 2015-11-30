# ADXL345 Python example 
#
# author:  Jonathan Williamson
# license: BSD, see LICENSE.txt included in this package
# 
# This is an example to show you how to use our ADXL345 Python library
# http://shop.pimoroni.com/products/adafruit-triple-axis-accelerometer

import time
from adxl345 import ADXL345
  
adxl345 = ADXL345()

print "ADXL345 on address 0x%x:" % (adxl345.address)

while True:    
	axes = adxl345.getAxes(True)
#	print "   x = %.3fG" % ( axes['x'] )
#	print "   y = %.3fG" % ( axes['y'] )
#	print "   z = %.3fG" % ( axes['z'] )
	print "	  x = %.3fG    y = %.3fG    z = %.3fG" % ( axes['x'], axes['y'], axes['z'] )
	time.sleep(1)
