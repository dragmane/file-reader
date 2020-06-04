from datetime import datetime
import sys
import time
import os
def main():
  while  2 != 5:
    cmd = '\033[1;34;40m(+_+)\x1b[1;32m '
    ai = str(cmd)
    try:
      now = datetime.now()
      t = now.strftime('%H')
      h= int(t)-12
      x = {'hello':'\033[1;34;40m[A.i]\x1b[1;32m hi','how are you':ai+'fine and you','fine':ai+'bright day isn‘t it','what is time':ai+now.strftime(str(h)+':%M:%S'),'time':ai+now.strftime(str(h)+':%M:%S'),'help':ai+'system commnds or my interaction','stopwatch':ai+'starting','bye':ai+'bye','ok':ai+'thanks','clear':ai+'clearing','date':ai+now.strftime('%d:%m:%Y'),'yes':ai+'ok','hi':ai+'hi'}
      s = input("\033[1;31;40m[USER]\033[0m \033[1;32;40m")
      print(x[str(s)])
      if 'bye' in s:
        time.sleep(1)
        sys.exit()
      elif 'stopwatch' in s:
        print(ai+'begining')
        sec = 0
        while 2 != 5:
          try :
            time.sleep(1)
            sec += 1
            mins = sec/60
            hour = mins/60
            os.system('clear')
            print(ai+str(hour)+':'+str(mins)+':'+str(sec))
          except KeyboardInterrupt:
            print(ai+'total time was '+str(t))
            print(main())
      elif 'clear' in s:
        time.sleep(1)
        os.system('clear')
      else:
        print(main())
    except KeyError:
      print(ai+"\033[3;31;40m[-]\033[0m i don't get")
    except KeyboardInterrupt:
      print('\n'+ai+'you pressed ctrl + c\n'+ai+'use ctrl + z')
print(main())
