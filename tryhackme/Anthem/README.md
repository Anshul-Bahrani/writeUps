# Anthem

export IP=10.10.171.9


robots.txt:
UmbracoIsTheBest!

# Use for all search robots
User-agent: *

# Define the directories not to crawl
Disallow: /bin/
Disallow: /config/
Disallow: /umbraco/
Disallow: /umbraco_client/

Authors of 2 articles on the website:
Jane Doe
James Orchard Halliwell 

maybe ssh?


found these wierd flag type things on the website:
THM{L0L_WH0_US3S_M3T4}
THM{G!T_G00D}
THM{L0L_WH0_D15}
THM{AN0TH3R_M3TA}


so the poem which was there in the our favorite manager was referenced to solomon grundy which i knew but didnt thought that it has to do with the administrator of the page:solomon grundy

and the email was:SG@anthem.com
(From the first post)

turns out you can remotely access a machine using xfreerdp
xfree -remote dekstop protocol

xfreerdp /u:$USERNAME /p:$PASSWORD /v:$MACHINE_IP

found the user.txt:THM{N00T_NO0T}

for admin pass:hint included that to check hidden files so open file->view on the navbar->show hidden files...found backup->restore but could not access it...changed the permissions of it...which i didnt knew and refered optional's youtube vid....

so whenever we dont have certain file permissions look for if we can change the file permissions....like in this case i was logged in as SG, so i changed the file permissions as:right click the file->security->add a person->type SG->tick on the check box for full access, allow and save the changes...

Admin pass:
tried logging in to the administrator folder in users in C:
asked me for the pass and i provided it:

ChangeMeBaby1MoreTime

Found the root.txt in the dekstop:
THM{Y0U_4R3_1337}