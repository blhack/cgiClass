#Python CGI class at heatsync labs

first enable the cgi module in apache
```
sudo a2enmod cgi
```

restart apache
```
service apache2 restart
```

Put your python files in:

```
/usr/lib/cgi-bin/
```

Put your HTML files in:

```
/var/www/html
```


You will have to run the following command to launch the mysql editing program

```
mysql -u root -p
```

Some useful mysql commands are things like:

```
create database twitterClone;
use twitterClone;
create table tweets(user text,tweet text,time int);
insert into tweets(user,tweet) values("blhack","Just eating a sandwich");
```

If you get a permission denied error, you need to set execute permissions on the python file you are trying to run.  Do:

```
chmod +x filename.py
```
