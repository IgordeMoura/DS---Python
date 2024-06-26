drop database avaliacao;
create database avaliacao;

use avaliacao;

create table tbl_leds(
    id int not null auto_increment primary key,
    led varchar (30),
    criado_em datetime
);

select * from tbl_leds;