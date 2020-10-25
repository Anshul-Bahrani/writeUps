### WonderLand ###

export IP=10.10.109.221


Gobuster showed a dir named r....guessed it would be r/a/b/b/i/t...and it was

it said open a door and walk in so trying gobuster on that...

meanwhile the img dir showed 2 alice_door files, onw with jpg and the other with png so trying stegcracker on the jpg file see if it helps...


Fpund this strange login i guess on the wen server on the rabbit path:

alice:HowDothTheLittleCrocodileImproveHisShiningTail

Trying ssh, it worked....


found root.txt and some poem python file...all owned by root...

2 more users found in /etc/passwd:

alice:x:1001:1001:Alice Liddell,,,:/home/alice:/bin/bash
hatter:x:1003:1003:Mad Hatter,,,:/home/hatter:/bin/bash
rabbit:x:1002:1002:White Rabbit,,,:/home/rabbit:/bin/bash


sudo -l revealed :

User alice may run the following commands on wonderland:
    (rabbit) /usr/bin/python3.6 /home/alice/walrus_and_the_carpenter.py

sudo -u rabbit /usr/bin/python3.6 /home/alice/walrus_and_the_carpenter.py

the python file used random as an import and used it to randomize some lines of the poem:

created a random.py file and had a function named choice...got a rabbit's shell


# Upside down:

i can access the user.txt in the root's dir bt cannot access the root.txt in my home dir:

# User.txt:
thm{"Curiouser and curiouser!"}

password.txt:WhyIsARavenLikeAWritingDesk?


# Root.txt:
thm{Twinkle, twinkle, little bat! How I wonder what you’re at!}