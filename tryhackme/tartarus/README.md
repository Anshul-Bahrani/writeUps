### Tartarus ###

it has a default apache web server...maybe i will get the version of apache and its old?

robots.txt contents:
User-Agent: *
Disallow : /admin-dir

I told d4rckh we should hide our things deep.



found credentials and user files in admin-dir...maybe to use hydra to brute force..but where?

nmap showed ftp is open and anonymous login is allowed 

tried brute forcing ssh with the files i got...got nowhere so took help from the video :(...

turns out ftp had a hidden directory "..." , got a txt file with:
/sUp3r-s3cr3t
this is a login page so this is where i have to brute force :D

so john hammond is incredible ofc....he used python to brute force...guess i will do the same...thats so satisfying not using tools and creating ur own scripts :D

found the username and pass:

enox : P@ssword1234

file upload is available...so going for standard rev_shell

uploaded my rev_shell but unable to access it just yet..

meanwhile ssh bruteforcing stopped and so luck with that


tried gobuster on /super_whatever found images and it had uploads...and there was my rev_shell ran and i got a rev shell as www-data ofc

ls /home :
cleanup
d4rckh
thirtytwo


cd /home/d4rckh
cat user.txt:
0f7dbb2243e692e3ad222bc4eff8521f

found many things now:
cleanup.py file in d4rckh's dir:
cleanup's dir was empty:

thirtytwo's dir had note.txt:
Hey 32, the other day you were unable to clone my github repository. 
Now you can use git. Took a while to fix it but now its good :)

~D4rckh

so from here till root nothing too great but i should have known the things that i did..took a lot of help from john's vids so i guess thta should be it for today:
final root flag:
7e055812184a5fa5109d5db5c7eda7cd

honestly not very happy with myself...had to work a lot and currently not doing that so maybe tommorow will be bttr :(
