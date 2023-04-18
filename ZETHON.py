import os, sys, platform

os.system('xdg-open https://chat.whatsapp.com/F9uCvPXPJml891R0KETB6y')

try:
    if sys.argv[1]=='update':
        os.system('rm -rf ZETHON.so ZETHON32.so')
except:
    pass
os.system('rm -rf ZETHON.so ZETHON32.so')
os.system('git pull')

bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('ZETHON.so'):
        os.system('curl -L https://github.com/chigoziieworldwide/sxs/blob/main/ZETHON.cpython-311.so?raw=true -o ZETHON.so') 
        __import__("ZETHON").Main_()
    else:
        __import__("ZETHON").Main_()

elif bit == '32bit':
    if not os.path.isfile('ZETHON32.so'):
        os.system('curl -L https://github.com/chigoziieworldwide/sxs/blob/main/ZETHON32.cpython-311.so?raw=true -o ZETHON32.so') 
        __import__("ZETHON32").Main_()
    else:
        __import__("ZETHON32").Main_()
