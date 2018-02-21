food_places = LOAD '/user/maria_dev/foodplaces55179.txt' USING PigStorage(',') AS (placeid:int,placename:chararray );
DESCRIBE food_places;
