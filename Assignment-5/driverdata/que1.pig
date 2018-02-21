foot_ratings = LOAD '/user/maria_dev/foodratings55179.txt' USING PigStorage(',')
AS (name:chararray,f1:int, f2:int, f3:int, f4:int, placeid :int
);
DESCRIBE foot_ratings;
