FROM mysql
ADD prestashop_hm.sql /docker-entrypoint-initdb.d
CMD ["mysqld", "--character-set-server=utf8", "--collation-server=utf8_general_ci"]
