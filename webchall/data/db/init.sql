create database arangdb;
use arangdb;

create user 'arangdb_admin'@'%' identified by 'th1s_1s_4dm1n_p4ssw0rd';

create table user (
   userseq int not null auto_increment primary key,
   userid varchar(50), 
   userpw varchar(50)
) default character set utf8 collate utf8_general_ci;

create table flag (
   flag varchar(255)
) default character set utf8 collate utf8_general_ci;

insert into flag values("gachon{th1s_1s_s1mp1e_sqli_vu1n}");
insert into user (userid, userpw) values("admin", "adm1n_p4ssw0rd");
insert into user (userid, userpw) values("guest", "guest");

grant select, insert on arangdb.user to 'arangdb_admin'@'%';
grant select on arangdb.flag to 'arangdb_admin'@'%';
flush privileges;