### Year Of The Rabbit ###

export IP=10.10.5.112

Found /assets...

in that...RickRolled.mp4 and style.css

RickRolled was a rabbithole....

style.css included:

 /* Nice to see someone checking the stylesheets.
     Take a look at the page: /sup3r_s3cr3t_fl4g.php
  */

The page gave a message to disable javascript and then redirected to "Never Gonna give you up video.."

After disabling js:
Love it when people block Javascript...
This is happening whether you like it or not... The hint is in the video. If you're stuck here then you're just going to have to bite the bullet!
Make sure your audio is turned up!

and an another mp4....with same video...Litrally same video :/...another rabithole...


Turns out it was not a rabbit hole...the audio between the song said:
    “I’ll put you out of your misery **burp** you’re looking in the wrong place”

BurpSUite captured an intermediate request while accessing super secret:
GET /intermediary.php?hidden_directory=/WExYY2Cv-qU HTTP/1.1


Got a png file called Hot_Babe.png...
cant use steghide becuase its a png file.....
so cat and strings is the way to go:
Found:
Eh, you've earned this. Username for FTP is ftpuser                                                                            
One of these is the password:

[21][ftp] host: 10.10.5.112   login: ftpuser   password: 5iez1wGXKfPKQ

Found Eli's_Creds.txt which included...brainfuck's encoded data:

User: eli

Password: DSpDiM1wAEwid

There is another user on the machine and im guess she has the user.txt file:
gwendoline

So apparently when u login with ssh this message pops up:

1 new message
Message from Root to Gwendoline:

"Gwendoline, I am not happy with you. Check our leet s3cr3t hiding place. I've left you a hidden message there"

END MESSAGE


/usr/games/s3cr3t

Your password is awful, Gwendoline. 
It should be at least 60 characters long! Not just MniVCQVhQHUNI
Honestly!

Yours sincerely
   -Root

# User.txt:
THM{1107174691af9ff3681d2b5bdb5740b1589bae53}

So this was wierd....i was allowed to run vi on user.txt as any person just not root...so found this:
sudo -u#-1 vi user.txt...and since -1 dosent exist we opened vi as root...
:!/bin/bash and we get the root shell....


# Root.txt:
THM{8d6f163a87a1c80de27a4fd61aef0f3a0ecf9161}

Referred a good amount of writeups but i learnd many things so all good... :D