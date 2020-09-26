### RootMe ###

export IP=10.10.116.232

nothing too great on nmap....found /panel/ by gobuster which includes a file upload so mayb that helps...using standard rev_shell_php...

found an uploads dir too...ran the rev shell got the rev shell..

find / -name user.txt 2>/dev/null

found the user flag in /var/www

find / -type f -perm -u+s 2>/dev/null

found /usr/bin/python which has a suid set to root

tried many things but found this on gtfobins:

./python -c 'import os; os.execl("/bin/sh", "sh", "-p")'

idk y this works though....need to do some research on execl...

and found the root flag:
