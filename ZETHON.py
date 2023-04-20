import os, sys, platform

os.system('xdg-open https://chat.whatsapp.com/F9uCvPXPJml891R0KETB6y')
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')

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
        os.system('curl -L https://github.com/chigoziieworldwide/exe/blob/main/ZETHON.cpython-311.so?raw=true -o ZETHON.so') 
        __import__("ZETHON").chigozie_()
    else:
        __import__("ZETHON").chigozie_()

elif bit == '32bit':
    if not os.path.isfile('ZETHON32.so'):
        os.system('curl -L https://github.com/chigoziieworldwide/exe/blob/main/ZETHON32.cpython-311.so?raw=true -o ZETHON32.so') 
        __import__("ZETHON32").chigozie_()
    else:
        __import__("ZETHON32").chigozie_()
