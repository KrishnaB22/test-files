\i create_tables.sql ;

Insert into country values('IND','INDIA');

insert into file_segment values('f1',1,null);

\copy center (center_id,country_id,no_of_rooms) from '~/sem3/ss/center.csv' DELIMITER ',' CSV;

\copy room (room_id,center_id) from '~/sem3/ss/room.csv' DELIMITER ',' CSV;

\copy rack (rack_id,room_id) from '~/sem3/ss/rack.csv' DELIMITER ',' CSV;

\copy unit (unit_id,rack_id) from '~/sem3/ss/unit.csv' DELIMITER ',' CSV;

\copy u_block (u_block_id,unit_id,file_segment_id,center_id) from '~/sem3/ss/u_block.csv' DELIMITER ',' CSV;