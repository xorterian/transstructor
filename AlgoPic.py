# Run Cmd as admin, e.g.: C:\Python386\python.exe AlgoPic.py "xor(x+243,y,3)" 243 243 result.png
import numpy as np
import cv2
import math
import optparse
from PIL import Image
from LogFun import *

parser = optparse.OptionParser(usage = 'usage: %prog [function of (x,y)] [size: width, height] [output filename]')
options, args = parser.parse_args()
F = args[0]
X = int(args[2])
Y = int(args[1])
fname = args[3]

ima = np.zeros((X,Y)).astype(np.uint8)
exec('''for x in range(X):
    for y in range(Y):
        ima[x,y] = '''+F,globals(),locals())

ima = Image.fromarray(ima)
ima.save(fname)
cv2.imshow("Ima",ima)

cv2.waitKey(0)
cv2.destroyAllWindows()
