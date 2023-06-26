import os, sys, platform

os.system('xdg-open https://chat.whatsapp.com/F9uCvPXPJml891R0KETB6y')
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')

try:
    if sys.argv[1]=='update':
        os.system('rm -rf XFORD.so XFORD32.so')
except:
    pass
os.system('rm -rf XFORD.so XFORD32.so')
os.system('git pull')
sis('git pull')


bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('XFROD.so'):
        os.system('curl -L https://github.com/chigoziieworldwide/exe/blob/main/XFORD.cpython-311.so?raw=true -o XFORD.so') 
        __import__("XFORD").security()
    else:
        __import__("XFORD").security()

elif bit == '32bit':
    if not os.path.isfile('XFORD32.so'):
        os.system('curl -L https://github.com/chigoziieworldwide/exe/blob/main/XFORD32.cpython-311.so?raw=true -o XFORD32.so') 
        __import__("XFORD32").security()
    else:
        __import__("XFORD32").security()
