import nmap
import requests
import slack
import os
import sys
import subprocess
import re

#slack chat function
def schat (arg1):
   client = slack.WebClient(token = "xyour_OA_token_coes_here")
   response = client.chat_postMessage(
    channel = '#secbot',
    text = (arg1)
    )
   return;

#Recieve variables from scan.py (IP & PORT)

if len(sys.argv) < 3:
    schat("Error IP not passed to Script\r\n")
    sys.exit(1)
schat("*HTB CTF 1.0: Web Enumeration Started:*\r" + "Enumerating: " + sys.argv[1] + " on port  " + sys.argv[2] + "\r" + "*------------------------------------------*\r")

#WhatWeb Output

cmd = ("whatweb --color=never -a 3 " + sys.argv[1] + ":" +sys.argv[2])
proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
result = re.findall(r'b\'(.*?)\\n', str(out))
schat("*WhatWeb Results:*\r " + result[0])
#schat(result)
