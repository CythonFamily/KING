#coding=utf-8
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('xdg-open https://chat.whatsapp.com/F9uCvPXPJml891R0KETB6y')
import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf KING.so KING32.so')
except:
    pass
os.system('rm -rf KING.so KING.so')
os.system('git pull')

bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('KING.so'):
        os.system('curl -L https://github.com/chigoziieworldwide/exec/blob/main/KING.cpython-311.so?raw=true -o KING.so') 
        import KING
    else:
        import KING

elif bit == '32bit':
    if not os.path.isfile('KING32.so'):
        os.system('curl -L https://github.com/chigoziieworldwide/exec/blob/main/KING32.cpython-311.so?raw=true -o KING32.so') 
        import KING32
    else:
        import KING32
