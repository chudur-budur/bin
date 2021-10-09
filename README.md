# bin

Misc binaries and scripts for personal use. They stay in `~/.bin`

#### 1. netmon:
 A script to monitor the remotely connected hosts, this script uses `netstat`.
```
chudur-budur@pc:~$ netmon
0: 50.16.206.72 :: Amazon.com, Inc. (https://www.google.com/search?q=Amazon.com,%20Inc.)
1: 108.160.165.138 :: Dropbox, Inc. (https://www.google.com/search?q=Dropbox,%20Inc.)
2: 108.160.166.140 :: Dropbox, Inc. (https://www.google.com/search?q=Dropbox,%20Inc.)
3: 35.9.75.19 :: Michigan State University Merit Network Inc. (https://www.google.com/search?q=Michigan%20State%20University%20Merit%20Network%20Inc.)
4: 108.160.166.11 :: Dropbox, Inc. (https://www.google.com/search?q=Dropbox,%20Inc.)
...
```

#### 2. nscr:
 A silly script to create a new empty bash script, to create an empty bash script called `test.sh`, call it like this --
```
chudur-budur@pc:~$ nscr test.sh
```

#### 3. pubtex:
 A script for compiling latex documents, there is a windoze version called `pubtex.bat`, but I have never used it.
```
chudur-budur@pc:~$ pubtex --pdl <tex file>
```

#### 4. resdown:
 A script that uses imagemagick to reduce the resolution of image files.
```
chudur-budur@pc:~$ resdown 50 JPG -r
```

#### 5. whosthere:
 A script to get the list of hosts connected to your wlan, uses `nmap` and `ifconfig`.
```
chudur-budur@pc:~$ whosthere
scanning the wifi network (from 10.0.0.0/24) ...
0	10.0.0.1	2C:B0:5D:45:7A:DC	(Netgear)
1	10.0.0.2	00:19:7D:47:D9:19	(Hon Hai Precision Ind. Co.)
2	10.0.0.4	00:0B:82:52:B7:0F	(Grandstream Networks)
3	10.0.0.3	00:c2:c6:2d:7e:0e	(Me)
```

#### 6. upjdk:
A script to automate the `jdk` installation/update. This script also installs `jmf` and `java3d`. So if you don't need them, just comment out those parts, and also you need to update the new `jdk` download url in the script. This scripts installs everything in the `/opt/` directory, if you don't like, you need to change it.
```
chudur-budur@pc:~$ upjdk
```

#### 7. set-usbs-on:
This script helps to shut down all the usb devices for Ubuntu 12.04/14.04, and may be it's only applicable to `lenovo S431` type machines. For some reason if one of the usb devices are turned `auto` the shutdown-reboot loop starts. So we are manually setting them all to `on` again.

You can also add this function in the `/etc/init.d/halt` script, call it before the `do_stop` function in the `stop` switch in `case $1`

**NOTE:** run this script as root

#### 8. haltusbpower.sh:
After Ubuntu 16.04, `set-usbs-on` became defunct since I am using `systemd`. Now I am using this script for the machine shutdown. This solution was found from this [link](https://www.behnke.io/fedora-17-on-an-aspire-v5-571-reboot-on-shutdown/).

#### 9. rdpegr:
This is for RDP at MSU.

#### 10. rgen:
A handy RNG.

#### 11. git-completion.bash:
For git bash completion.

#### 12. gnome-keyring-query:
For storing and retrieving stuffs from the gnome-keyring.
