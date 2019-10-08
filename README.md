# HTB-CTF-Bot
Project I created to create a HTB bot for teams to use for working on challenges.

This project has alot of moving parts and is still far from a beta release. I have started to add modules and work on testing while developing the code.  Currently this is use at your own risk. You will need to do some manually configuration as this is not offered as an official slack app, meaning you will need to host your own backend and create your own / commands.

Technology pre-requisits
- Server where you can run a web server with php and python.
- This was developed on Ubuntu 18.
- nmap installed
- openvpn
- additional HTB account

Python Requirements
- Python 3
- pip3
- slack web client
- python-nmap

Slack
- Create a channel for your bot
- Give the bot the ability to create, write, message
- Get token
- Get incoming web hook
- Create slack / commands for each function. IE. /scan 
-- ./scan 10.10.10.157
--- this will call http://myhost/scap.php?=

Running:

Make sure you are connected to the HTB vpn
copy all files to /var/www/html
make files executable
Use common sense in securing them <-- No pentesting has been done to assure it cant be abused at current time :). Your Welcome!
Create / commands in your slac instance
Enter your slack channel and type the command /scan 10.10.10.x (replace x with host to scan)
