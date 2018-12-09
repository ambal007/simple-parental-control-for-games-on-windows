#!c:\Python27\python.exe
import time,os

while (1):
  time.sleep(10)
  txt='\n'.join( [x[:-1] for x in os.popen('type exclam.txt')] )
  print txt

  if txt.count('!' )>0:
    print 'RESTART!!!'
    os.system('del exclam.txt')
    os.system('c:\\users\\ambal\\shutdown.exe /r')
    

