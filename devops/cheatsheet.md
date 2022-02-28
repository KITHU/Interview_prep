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