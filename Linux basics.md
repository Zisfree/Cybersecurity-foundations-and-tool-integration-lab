# Linux Core Concepts nd Lab Notes

"""THESE WERE MY HAND WRITTEN NOTES I JUST MADE A.I. CONVERT IT INTO TEXT""" --- Typed it cause u might think I just used an AI :P.


## 1. Linux File System Hierarchy (FSH)
Everything starts at `/` which is the top-level root filesystem. Here is how the directories break down:
* `/bin` - contains essential command binaries.
* `/boot` - contains static bootloader, kernel executable, and files required to start Linux OS.
* `/dev` - contains device files. Access to every hardware device.
* `/etc` - contains local system config files. For installed apps might also be here.
* `/home` - each user has a sub-directory here for storage.
* `/lib` - shared library files that are required for system boot.
* `/media` - for external removable media like USBs.
* `/mnt` - temporary mount point for regular filesystems.
* `/opt` - optional files such as third-party tools.
* `/root` - home directory for the root user.
* `/sbin` - this directory contains executables used for system administration (binary system files).
* `/tmp` - used to store temporary files. Deleted on reboot or any time without warning.
* `/usr` - contains executables, libraries, man files etc.
* `/var` - contains variable data such as log files, email in-boxes, web app related files, cron files etc.

Most people choose Linux cause they are free and open source where the source code is available. Popular distros are Ubuntu, Fedora, CentOS, Debian, and Red Hat Enterprise Linux. Debian uses the Advanced Package Tool (apt) management system to handle software updates and security patches. It is super stable and reliable, and its updates live up to 5 years which is very important for servers. Kali Linux is Debian-based but specialized for cyber security.

### 2. Shells, Terminals, nd Environments
Shell is basically the Linux terminal used to open directories and run hardware devices in the OS. The most common one is BASH (Bourne-Again Shell) which is part of the GNU project. Other shells exist too like Tsh, Csh, Ksh, Zsh, and Fish. 

A Terminal Emulator is just software that emulates a terminal. It converts a GUI app into text-based command-line interfaces (CLI). Some can run multiple independent terminals separate from each other using tabs, just like web browsers.

When looking at the command prompt description, it usually looks like `<username>@<hostname>:<current_directory>`. 
* If you see a `$` symbol, it means you are an unprivileged ordinary user.
* If you see a `#` symbol, it means you are logged in as root and are privileged.
The environment variable `PS1` controls exactly how your command prompt looks in the terminal frame. If we upload and run a shell on a targeted system (meaning a reverse shell or bind shell to act as a bridge between our host and the target), we might not see the username or hostname. This might be due to the PS1 variable not being set correctly. You can always check your `~/.bash_history` file in the user's home directory to see the exact commands you used.

## 3. System Info nd Diagnostic Commands
These are the basic tools used in everyday Linux tasks to check system details and statuses:
* `whoami` - displays current username.
* `id` - returns user's identity and groups.
* `hostname` - sets or prints the name of the current host.
* `uname` - prints basic info about the OS and hardware system.
* `pwd` - returns walking (working) directory name.
* `ifconfig` - a utility used to view the IP address of the network.
* `ip` - utility to show or manipulate routing, network devices, interfaces, and tunnels.
* `netstat` or `ss` - shows network stats, connection statuses, and sockets.
* `ps` - shows currently running process status.
* `who` - displays who is logged in right now.
* `env` - a command to display environment variables or set them.
* `lsblk` - lists block devices (like storage drives usable by the system).
* `lsusb` - lists connected USB devices.
* `lsof` - lists opened files.
* `lspci` - lists PCI devices and hardware standard buses used to connect multiple hardware parts into one system.

If you ever forget how to use options or parameters for a tool, you can use `--help` or `-h` (like `ls --help` or `curl -h`). There is also a tool called `apropos` that searches the man-pages and shows a short description of what a command does.

## 4. Storage Block Sizes nd File Permissions
When you run the `ls -l` command, it shows permissions, links, owners, and sizes. A directory block size usually shows up as `4096` bytes (4KB), which is the size of the block used to store that folder's info. 
Memory is organized into buffers (small caches). If you choose 1KB blocks and have a file that is 1.5KB, the system will use 2 blocks and show the file size as 2KB anyway. Larger blocks mean more storage waste for small files, but larger blocks can improve system performance. Common block sizes are 1KB, 2KB, 4KB, 8KB, 16KB, and 32KB. Running `ls -l --block-size=M` doesn't change the actual files, it just changes how the sizes are displayed to you.

For file permissions, a line looks like `drwxr-xr-x`. 
* The first letter `d` means it is a directory (a regular file shows a hyphen `-`).
* The next parts break down into Owner/User, Group, and Others. 
* `rwx` means read, write, and execute permissions. For example, if owner has `rwx` they can do everything, if group has `r-x` they can only read and execute but not write, and others might be `r-x` too.

## 5. Managing Files nd Text Editing
To move around and manage stuff in the terminal:
* Pressing `TAB` twice will autocomplete or list out matching directories/files starting with that letter. 
* A single dot `.` represents the current directory, and a double dot `..` represents the parent directory.
* `touch <name>` - creates a fresh empty file like `touch inform.txt`.
* `mkdir <name>` - makes a new directory. Using `mkdir -p` allows you to create a parent directory structure cleanly.
* `mv <file> <destination>` - moves or renames a file, like `mv info.txt information.txt`. It just updates the path, it doesn't change the file size.
* `cp <source> <destination>` - copies a file to a new directory.

For editing files, common text editors are Vi, Vim, and Nano. 
To use nano, you just type `nano filename.txt`. It has a simple interface called a pager. At the bottom, it shows short commands where the caret `^` stands for the Ctrl key (so `^X` means Ctrl+X to exit). You save by pressing Ctrl+O and hitting enter to confirm the filename. To just view a file without editing, you use `cat filename.txt`.

## 6. Finding Files nd SSH Connections
To search for things on the OS, we use `which`, `find`, or `locate`.
* `which` - lets us determine if a system has specific tools available on it like cURL, netcat, wget, python, go, or gcc. For example: `which nc` or `which cat`.
* `find` - allows us to filter files by size, date, etc. The format is `find <location> <options>`. For example:
  `find / -type f -name "*.conf" -user root -size +20k -newermt 2026-01-01 -exec ls -al {} \; 2>/dev/null`
  Here, `-type f` defines a regular file, `-name` matches the file name/extension, `-user root` checks the owner, `-size +20k` checks files larger than 20 KiB, and `-newermt` finds files newer than that date. The `-exec` part uses curly brackets `{}` as placeholders for the results, and the backslash escapes the semicolon so the shell doesn't break.
* `locate` - much faster way to search because it works on a local database of existing files and folders. But you have to update the database first by running `sudo updatedb`.

For connecting to targets over the network, we use SSH (Secure Shell). It is a protocol that allows a client to access a remote system and execute commands without needing any GUI layout. You connect using the command:
`ssh htb-student@<IP_address>`

## 7. File Descriptors nd Redirection (The Magic Numbers)
Another way to handle inputs and outputs is through Redirection. A File Descriptor (FD) in Unix/Linux is a reference maintained by the kernel that allows the system to manage Input/Output operations. It acts like a unique identifier or a "magic number" the kernel provides to the program instead of dealing with complex memory addresses or full file paths.
By default, three file descriptors are open for a data stream:
1. Data stream for input -> `STDIN (0)`
2. Data stream for output -> `STDOUT (1)`
3. Data stream for errors -> `STDERR (2)`

We use pipes `|` to redirect STDOUT from one program straight into another tool (like grep or wc). `grep` is the most common filtering tool that filters out content from STDOUT according to how we define it. 
For example, if we run:
`find / -name "*.conf" 2>/dev/null | grep systemd | wc -l`
This will search for all config files, redirect all the standard errors (`2>`) to `/dev/null` (which acts as a black hole so the screen stays clean), then pipe the output to `grep systemd` to filter only lines containing "systemd", and finally pipe that to `wc -l` (word count line option) to count the total number of results obtained.


## 8. STDIN, STDOUT, nd STDERR Mechanics
When u run `cat` without specifying a file, the terminal just hangs waiting for input. Whatever u type into it is your standard input `STDIN (FD 0)`. Once u hit enter, the terminal echoes it back as standard output `STDOUT (FD 1)`.

If u run a command like `find /etc -name shadow`, u get hit with two types of data:
* Clear paths like `/etc/shadow` are standard outputs `STDOUT (FD 1)`.
* "Permission denied" warnings are standard errors `STDERR (FD 2)`.

We can clean our screen by targeting these file descriptors directly:
* `find /etc -name shadow 2>/dev/null` - this dumps all the STDERR stream into the null device black hole so u only see good results.
* `find /etc -name shadow 1>/dev/null` - this does the exact opposite nd removes all standard outputs leaving only the raw error messages on the screen.

## 9. Output Handling nd Stream Splitting
U can split outputs into different files depending on the stream type:
* `find /etc -name shadow 2>/dev/null > results.txt` - hides errors nd saves only the good outputs into results.txt inside your current working directory.
* `find /etc -name shadow 2> error.txt 1> stdout.txt` - saves errors nd successful hits into completely separate files at the same time.

## 10. Redirection Operators nd Appending
* The `>` sign denotes output redirection. If u use a single `>` to save data, it automatically overwrites the file without asking u first. 
* To prevent data loss, use `>>` to append data to the end of an existing file like:
  `find /etc -name passwd >> stdout.txt 2>/dev/null`
* The `<` sign denotes standard input redirection. For example, `cat < results.txt` feeds the file content into cat as an input stream instead of reading it normally.

## 11. Advanced Inputs (Heredocs nd Herestrings)
U can generate files directly inside the command line using a "Here Doc" notation:
```text
cat << EOF > filename.txt
here doc > write whatever text u want here
here doc > you can add multiple lines
here doc > EOF
```
The marker `EOF` stands for End of File. Hitting enter after typing it terminates the stream and creates the file cleanly in your directory. U can also use `<<<` as a here-string to push short text bits straight into a stream.

## 12. Advanced Pipeline Processing (Pipes nd More)
Pipes `|` let us redirect the STDOUT of one tool directly into another program to chain workflows. The most common filter tool used in chains is `grep`.
* `find /etc -name "*.conf" 2>/dev/null | grep systemd | wc -l` - loops a find search, screens out text matching "systemd", and passes it to `wc -l` to count how many lines of results were captured.

## 13. File Inspectors nd Pagers
When viewing big datasets without opening bulky text editors, use pagers:
* `more` - basic reader for reading outputs page-by-page. Running `cat /etc/passwd | more` lets u scroll user IDs, GIDs, and default shell listings without cluttering the screen. Hit `Q` to quit.
* `less` - way more functional than more. It opens files in a completely distinct buffer space. Its output doesn't stay behind in your active terminal scrollback once u close it.
* `head` - prints the first lines of a target file. Defaults to 10 lines if u don't give an option flag like `head /etc/passwd`.
* `tail` - does the exact opposite of head and prints the bottom lines of a file.

## 14. Core Sorting nd String Cutting
* `sort` - sorts file details alphabetically or numerically to give a clearer overview. Like running `cat /etc/passwd | sort`.
* `grep -v` - excludes specific strings. We use `cat /etc/passwd | grep -v "false/nologin"` to exclude standard users who have system accounts disabled. This strips out daemon accounts so we only look at real, exploitable user profiles.
* `cut` - cuts out specific chunks of lines separated by delimiters. Use `-d` to set the delimiter (like a colon `:`) and `-f` to specify the fields u want. For example:
  `cat /etc/passwd | grep -v "nologin" | cut -d":" -f1,2`
  This prints out just fields 1 and 2 (username and password flag) for active accounts.
* `tr` - string pager utility used to replace or remove characters from lines. For instance, `tr ":" " "` replaces colons with clean blank spaces.

## 15. Structural Formatting (Column nd Awk)
* `column` - creates structured column views from messy raw files. For example:
  `cat /etc/passwd | grep -v "nologin" | tr ":" " " | column -t`
  This turns colon-separated user data into a clean tabular form.
* `awk` - the ultimate pattern tool for sorting data fields easily. If files have too many columns, awk lets u print exactly what u need. For instance, `$1` prints the first field and `$NF` targets the last field on the line:
  `cat /etc/passwd | grep -v "nologin" | tr ":" " " | awk '{print $1, $NF}'`
  This prints just the username and their default shell path side-by-side.

## 16. Regular Expressions (RegEx Blueprints)
RegEx is like crafting perfect blueprints for matching text patterns inside target files using metacharacters (symbols representing digits, letters, etc.). It helps us group and extract what we need using different brackets:
* `()` - parenthesis are used to group parts of a regex path together.
* `[]` - square brackets define character classes or specific matching targets. For example, running `grep -E "Port 2[254]"` catches text containing Port 22, Port 25, or Port 24.
* `{}` - curly brackets define quantifiers to control how often a pattern repeats.
* `|` - serves as an OR operator to flag matches if either expression hits.
* `*` - functions like an AND mechanic, showing matches only if both conditions are present in the expression line.

## 17. Direct Stream Editing (Sed)
* `sed` - a stream editor tool used to modify text on the fly across a whole file or standard I/O stream. It uses the `s` flag for substitution and the `g` flag for a global replacement across all matches. For instance:
  `sed 's/bin/me/g'`
  This matches every string instance of "bin" across the entire text stream and switches it to "me" automatically.

## 18. Core Directory nd Directory Execution Logic
* `chmod` - sets user permissions using octal numerical values or bit notations where Read = 4, Write = 2, and Execute = 1.
  Summing the active bits together creates the octal values. For instance, `chmod 754 shell` sets User to 7 (4+2+1 = rwx), Group to 5 (4+1 = r-x), and Others to 4 (4 = r--).
* U can also change configurations symbolically using operators like `chmod a+r shell` so all user tiers gain read rights.
* **Directory Rule:** The key to navigating inside a directory is having the **execute (x)** permission set on that folder. Without it, users get a "Permission Denied" message and cannot explore inside, even if they have admin privileges. To modify files inside a directory, u must have **write (w)** privileges on that folder.

