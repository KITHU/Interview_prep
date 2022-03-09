## IPTABLES CONFIGURATIONS

- sudo iptables -I INPUT 2 -p tcp --dport 443 -j ACCEPT
- sudo iptables -I INPUT 2 -p tcp --dport 80 -j ACCEPT
- sudo iptables-save > /etc/iptables/rules.v4     OR
- sudo bash -c "iptables-save > /etc/iptables/rules.v4 "

## Mysql | MariaDb

- sudo mysql
- show databases;
- use db name
- show tables
- mysqldumb -u username -p db-name > dump_name.sql
- mysqldumb -u username -p new-db-name < dump_name.sql

## Copy from server to local

```
copy a file named file_dump.sql from server home directory to local machine current directory

```

- scp user@ip_address:~/file_dump.sql ./

```
copy a file named file_dump.sql from local  machine to server

```
- scp ./file_dump.sql user@ip_address:~/