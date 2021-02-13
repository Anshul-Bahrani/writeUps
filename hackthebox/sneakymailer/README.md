### SneakyMailer ###

export IP=10.10.10.197


Edited the /etc/hosts file to get the url up and working...

Found a comment in the source code of the home page...

<!-- need to add Register link to Sidebar for /pypi/register.php -->

Trying to register..on that url and forgot to run nmap and gobuster stuff so doing that..maybe will also run gobuster on /pypi

Looking at the information in the teams page:
1) All the mails have firstnamelastname@sneakymailer.htb format..
2) The default user of which we logged in is:Haley Kennedy