<?php
##########################################
## HTB SLackBot v1.0 DigitalOffensive
## This file is for the intitial scan
##########################################
# Values passed by Slack
#########################################
#token= your token <-- fidn in slack or tcpdump is your friend
#team_id=
#team_domain=
#enterprise_id
#enterprise_name=
#channel_id=  channel id it came from
#channel_name= channel name it came from
#user_id= user id it came from
#user_name= user id it came from
#command= commadn executed ie. /scan
#text= data to be ran by the command
#response_url=
#trigger_id=


//Make sure it is your app connecting to you by validating token
if ($_POST["token"] == "your_token_goes_here") {
	echo 'User: ' . htmlspecialchars($_POST["user_name"]) . ' Requested me to enumerate ' . htmlspecialchars($_POST["text"]) . '!';
} else {
	echo "You tried to execute a script without being authorized!";
	die;
}
//Validate input is equal to a IP address and launch the python scan in the background
if (filter_var($_POST["text"], FILTER_VALIDATE_IP)) {
	$cmd = ("python3 scan.py "  . $_POST["text"] . " " .  $_POST["user_name"] . "> /dev/null 2>/dev/null &");
	exec($cmd);
} else {
	echo($_POST["text"] . 'is not a valid IP address, please enter a valid IP');
	die;
}
?>
