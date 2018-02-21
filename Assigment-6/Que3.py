# -*- coding: utf-8 -*-
lines=sc.textFile('/user/maria_dev/foodratings63666.txt')
ex2RDD = lines.map(lambda line: line.split(“,”))
ex3RDD = ex2RDD.map(lambda line : [line[0], line[1], int(line[2]), line[3], line[4], line[5]])
print ex3RDD.take(5)