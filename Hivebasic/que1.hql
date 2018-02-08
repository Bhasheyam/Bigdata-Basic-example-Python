CREATE DATABASE IF NOT EXISTS MyDB;
use MyDB;
CREATE TABLE IF NOT EXISTS MyDb.foodratings (
name STRING COMMENT ' name',
food1 INT COMMENT ' food1 description',
food2 INT COMMENT ' food2 description',
food3 INT COMMENT ' food3 descrition',
food4 INT COMMENT ' food4 descrition',
id INT COMMENT 'id')
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';
STORED AS TEXTFILE;