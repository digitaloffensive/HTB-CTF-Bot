import nmap
import requests
import slack
import os
import sys
import subprocess

#slack chat function
def schat (arg1):
   client = slack.WebClient(token = "your_OA_Token_goes_here")
   response = client.chat_postMessage(
    channel = '#secbot',
    text = (arg1)
    )
   return;

if len(sys.argv) < 3:
    schat("Error IP not passed to Script\r\n")
    sys.exit(1)
schat("*HTB CTF Bot 1.0: Has been Started*\r" + "*User:* " + sys.argv[2] + " *Requested the asset* " + sys.argv[1] + " *to be enumerated*\r" + "*-=[ Scanning of:* " + sys.argv[1] + " *has started*\r")

# initialize the port scanner
nmScan = nmap.PortScanner()

# scan localhost for ports in range 21-443
nmScan.scan(sys.argv[1])

# run a loop to print all the found result about the ports
for host in nmScan.all_hosts():
     #print('Host : %s (%s)' % (host, nmScan[host].hostname()))
     #print('State : %s' % nmScan[host].state())
     sH = ('Host : %s (%s)' % (host, nmScan[host].hostname()))
     sHs = ('State : %s' % nmScan[host].state())
     #print (sH +"\r\n" + sHs + "\r\n")
     schat(sH +"\r\n" + sHs + "\r\n")
     
     for proto in nmScan[host].all_protocols():
      #   print('----------')
       #  print('Protocol : %s' % proto)
 
         lport = nmScan[host][proto].keys()
         data = sorted(lport)
         for port in data:
            pdata = ('port : %s\tstate : %s' % (port, nmScan[host][proto][port]['state']))
            client = slack.WebClient(token = "your_OA_Token_goes_here"")
            response = client.chat_postMessage(
            channel='#secbot',
            text = (pdata +"\r\n")
            )
schat("*-=[ Port Scaning of:* " + sys.argv[1] + " *has completed*\r")
if str(nmScan[sys.argv[1]].has_tcp(80)) == "True":
    cmd = ("python3 webenum.py " + sys.argv[1] + " 80" )
    proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
else:
    print ("not found")
