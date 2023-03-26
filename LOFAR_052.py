#coding=utf-8

import os, sys, platform

os.system('rm -rf Lofar.so Lofar.so')

try:

    if sys.argv[1]=='update':

        os.system('rm -rf Lofar.so Lofar.so')

except:

    pass

bit = platform.architecture()[0]

if bit == '64bit':

    if not os.path.isfile('Lofar.so'):

        os.system('curl -L https://github.com/LOFAR_052/executables/blob/main/Sarfraz.cpython-311.so?raw=true -o Sarfraz.so') 

        import Lofar

    else:

        import Lofar

elif bit == '32bit':

    if not os.path.isfile('Lofar32.so'):

        os.system('curl -L https://github.com/LOFAR_001/executables/blob/main/Sarfraz32.cpython-311.so?raw=true -o Sarfraz32.so') 

        import Lofar

    else:

        import Lofar

