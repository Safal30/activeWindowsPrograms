#modules
import subprocess
import os

cmd = 'WMIC PROCESS get Caption,Commandline' #cmd
proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE) #subprocess shell
for line in proc.stdout:
    print line 

a = input("Complete") #stops program
