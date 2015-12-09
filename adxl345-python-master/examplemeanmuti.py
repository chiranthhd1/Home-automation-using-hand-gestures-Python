# ADXL345 Python example 
#
# author:  Jonathan Williamson
# license: BSD, see LICENSE.txt included in this package
# 
# This is an example to show you how to use our ADXL345 Python library
# http://shop.pimoroni.com/products/adafruit-triple-axis-accelerometer

import time
from adxl345 import ADXL345
a=0.888
from datetime import datetime  

adxl345 = ADXL345()

print "ADXL345 on address 0x%x:" % (adxl345.address)
file = open("deviceoff1.csv",'w')
filex = open("xvalue.csv",'w')
filey = open("yvalue.csv",'w')
filez = open("zvalue.csv",'w')
filexy = open("xyvalue.csv",'w')
filexz = open("xzvalue.csv",'w')
fileyz = open("yzvalue.csv",'w')
filexyz = open("xyzvalue.csv",'w')








while True:
	axes = adxl345.getAxes(True)
#	print "   x = %.3fG" % ( axes['x'] )
#	print "   y = %.3fG" % ( axes['y'] )
#	print "   z = %.3fG" % ( axes['z'] )
	print datetime.now().strftime('%H:%M:%S')
	print " 	x = %.3f    y = %.3f    z = %.3f" % ( axes['x'], axes['y'], axes['z'] )
	if axes['x'] >= a:
			filex.write(" %s,%.3f,%.3f,%.3f\n" % (datetime.now().strftime('%H:%M:%S'),axes['x'],axes['y'],axes['z']))
	elif axes['y'] >= a:
			filey.write(" %s,%.3f,%.3f,%.3f\n" % (datetime.now().strftime('%H:%M:%S'),axes['x'],axes['y'],axes['z']))
	elif axes['z'] >= a:
		filez.write(" %s,%.3f,%.3f,%.3f\n" % (datetime.now().strftime('%H:%M:%S'),axes['x'],axes['y'],axes['z']))
	elif axes['y'] and axes['x'] >= a:
		filexy.write(" %s,%.3f,%.3f,%.3f\n" % (datetime.now().strftime('%H:%M:%S'),axes['x'],axes['y'],axes['z']))
	elif axes['x'] and axes['z'] >= a:
		filexz.write(" %s,%.3f,%.3f,%.3f\n" % (datetime.now().strftime('%H:%M:%S'),axes['x'],axes['y'],axes['z']))
	elif axes['y'] and axes['z'] >= a:
		fileyz.write(" %s,%.3f,%.3f,%.3f\n" % (datetime.now().strftime('%H:%M:%S'),axes['x'],axes['y'],axes['z']))
	elif axes['y']  and axes['x'] and axes['z'] >= a:
		filexyz.write(" %s,%.3f,%.3f,%.3f\n" % (datetime.now().strftime('%H:%M:%S'),axes['x'],axes['y'],axes['z']))
	else:
		print "fuckyou!"

#	or  axes['y'] or axes['x'])  >= x:
#		file.write(" %s,%.3f,%.3f,%.3f\n" % (datetime.now().strftime('%H:%M:%S'),axes['x'],axes['y'],axes['z']))
	
		time.sleep(.5)
