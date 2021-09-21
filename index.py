from socket import *
import time
import sys
import pyfiglet
out = pyfiglet.figlet_format("SATYA'S SCANNER",font="slant")
print(out)
startTime = time.time()
try:
#if __name__ == '__main__':
   target = input('Enter website url without-https&http or IP ')
   t_IP = gethostbyname(target)
   print ('Starting scan on host: ', t_IP)
except KeyboardInterrupt:
    print("\n\tYOU're QUITTING THE PROGRAM")
    sys.exit()
try:
   for i in range(75, 81):
      s = socket(AF_INET, SOCK_STREAM)
      
      conn = s.connect_ex((t_IP, i))
      if(conn ==0) :
         print("-" * 40)   
         print ('\t Port %d: OPEN' % (i,))
         print("-" * 40)
      else:
         print ('\t Port %d: CLOSED' % (i,))
      s.close()
   print("Time taken:", time.time() - startTime)
#errors are given
except KeyboardInterrupt:
		print("\n Exitting Program !!!!")
		sys.exit()
except socket.gaierror:
		print("\n Hostname Could Not Be Resolved !!!!")
		sys.exit()
except socket.error:
		print("\ Server not responding !!!!")
		sys.exit()
