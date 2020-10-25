If you want to do it through a shell you could mount it using ftpfs, which is one of my favorite ways since I get the controls as if it were local files.


mkdir -p ~/mnt/ftpfs
curlftpfs <username>@<server> ~/mnt/ftpfs
cd ~/mnt/ftpfs/
ls

You should now be able to list your files.