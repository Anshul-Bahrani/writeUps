### Pickle Rick ###

export IP=10.10.16.57

found the username from the website:R1ckRul3s

robots.txt: found Wubbalubbadubdub

trying ssh....permission denied...need a rsa key :(

did a little digging and found assets folder tried in the url and found some gifs and images which may be used for other directories of the website ....maybe or maybe some stegnography on the images using the wierd text i found on robots?

no luck with steghide so i dont think thats the way :(
.
.
.

ok so gobuster found login.php and guess whos login and pass i have :D

i have a command line input...and some other files like creatures or something

did ls:
found these contents:
Sup3rS3cretPickl3Ingred.txt
assets
clue.txt
denied.php
index.html
login.php
portal.php
robots.txt


tried cat but its disabled along with other file openers...
tried ls /home found:
rick
ubuntu



BIIIIIIIG brain time: :DDDDDD

did : http://$MACHINE_IP/Sup3rS3cretPickl3Ingred.txt

and printed the file this clicked because i found assets earlier and was browsing through it but didnt had an luck and when i lsedd into the command line found that 'Sup3rS3cretPickl3Ingred.txt' was in the same directory as assets..... so i did http://$MACHINE_IP/assets/../Sup3rS3cretPickl3Ingred.txt and it worked 

Contents of Sup3rS3cretPickl3Ingred.txt:
mr. meeseek hair

also did the same for clue.txt and it said:
Look around the file system for the other ingredient.

(p.s. will continue after having my milk...makes you stronger ehh :D
...


.
.

anddd done)


well found a base64 hash in the source code:

Vm1wR1UxTnRWa2RUV0d4VFlrZFNjRlV3V2t0alJsWnlWbXQwVkUxV1duaFZNakExVkcxS1NHVkliRmhoTVhCb1ZsWmFWMVpWTVVWaGVqQT0==

after about 5-6 decryptions with base64 found this:rabbit hole ::DDDD

again trying that clue.txt's order :D...trying to find a file to let me in...and i need a rsa key for that so trying:
find / 2>&1 /dev/null | grep -i "rsa"

found:/etc/ssh/ssh_host_rsa_key
maybe helpful

and i forgot i cant cat so i dont think thats it.

the deniel.php showed that only the real rick can access that page....but i tried curl with -A rick no luck so instead trying to wget and check what it actually needs :D

bit of a bummer...took some help from a writeup...and i was trying that for so long but in the wrong directory :(...sad..

cd /home/rick/;ls -ltr;pwd and i worked

less /home/rick/"second ingredients" and i got the second ingredient:
1 jerry tear


final part is easy as i can execute any command as root (got from sudo -l):

sudo ls -ltr /root

there is our 3rd.txt :D

sudo less /root/3rd.txt

3rd ingredients: fleeb juice


overall the room was very easy but i f'ed up ofc, and took a little help from the writeups but i am making progress which is always better :D

i was doing the right thing on the wrong folder that shows that actually there are 100s of ways one can sidetrack and get lost somewhere else :D

gudnyt for now :D