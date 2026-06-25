# What is SQLi?
- Sqli is a vulnerability exploitation using which a hacker can inject SQL code which can get it to access the back-end server.

### Commands used in Mysql to do SQLi:
- login in database `mysql -u <username> -p<password> -P <port> -h <host>`
- list databases `show databases`
- select the database `use <database name>`
- list tables `show tables`
- coulumn details in table `describe <table name>`
- view content inside table `select*from <table name>`
- to order content in table `select*from <table> order by <column>`
- to give condition `select*from <table> where <ex:username = 'admin'>`

## Attacking a website:
- SQL is mostly done on a login page or any given typing space or URL.
- Since, booleon works same as python in sql so here AND and OR operators work same.
- When we write admin' or '1'='1 this makes the whole username true.(use ' in even)
- We can use -- or # to quote out the text afterwords.
- We can guess the table no. by inputting numbers or anything as such-> `' union select 1,2,3,_,_-- `. Underscore means we can add numbers if we dont get any result and so on unti output is shown.
- user() and database() to see the the username of the host and databases on the server.
- The Information_schema table contains every database's information and the tables and columns inside it.
- to access the information_schema we can type `' union select table_name,table_schema from information_schema.tables where table_schema='<database>'-- `. Here table_schema is the name of databases inside the server and '.' is analougus to '/' in linux.
- to check the local privilages to load a file we use `' union select grantee,privilege_type, from information_schema.user_privileges-- `.
- if we have the privilages we can use commands like `'union select lead_file("/etc/passwd")-- ` which will open the /etc/passwd directory in the website.
- We can also write a file using outfile command `' union select 'writing in file' into outfile '/var/www/html/index.php'-- ` and then run it using URL where it shows something like this->
index.php?0=type_here_to_get_output_ex:pwd.

## CTF
- I get inside a site its a corporate site and is a messaging site. I as a pentester have to find flaws in it using sqli.
- First I see a login page. There I could do nothing cause nothing worked so I went to the site's register page.
- I had to register using my useenrmae a password and a code. Everything was fine except the code must have a boolean system to verify it cause username and password wont use it.
- So I tried using `a random# ` on it and it did not work so I used `a random or '1'='1` which worked and i got registered.
- Next i loggend into the page and found a serachbox which was the only vulnerable thing. So I tested it using `' union select 1,2,3-- ` and it worked as expected(on my first try).
- Then I tried some code like user() into it and found the username and databse().
- after that using `' union select table_name,table_schema from information_schema.tables where table_schema='<database>'-- ` and running other commands into this(such as changing table_name to column name  and .tablesto .columns so I could get the access to column list) I got to the username and password of admin.
- The next part was a bit new to me as we had to use burp-suite and other stuff(saw this in the writup cause i couldn't do anything after that) so I left this like that.
