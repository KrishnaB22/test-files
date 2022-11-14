drop table country,center,room,rack,unit,u_block,users,files,file_segment CASCADE;

create table country(country_id char(3) primary key, name varchar(64));

create table center(center_id char(16) primary key, country_id char(3) references country(country_id)
                   , no_of_rooms int);

create table room(room_id char(16) primary key, center_id char(16) references center(center_id));

create table rack(rack_id char(16) primary key, room_id char(16) references room(room_id));

create table unit(unit_id char(16) primary key, rack_id char(16) references rack(rack_id));


-- 

create table users(username varchar(128) primary key, space_allowed bigint, used_space bigint);

create table files(file_id char(16) primary key, file_name varchar(64), 
                  username varchar(128) references users(username)  , 
                size bigint, no_of_copies int, country varchar(3));


create table file_segment(file_segment_id varchar(16) primary key, segment_no int,
                          file_id char(16) references files(file_id)  );

create table u_block(u_block_id char(16), unit_id char(16) references unit(unit_id)  , 
                    file_segment_id  varchar(16) references file_segment(file_segment_id),center_id char(16));