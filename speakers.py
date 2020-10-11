#from playsound import playsound
import os
import subprocess

def play_file(file):
   # playsound(file, True)
    #os.spawnl(os.P_NOWAIT, "mpg123 " + file)
    print("PATH!!!! " + os.popen("pwd").read()) 
    subprocess.Popen(["mpg123", file])
#playsound()
