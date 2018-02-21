# -*- coding: utf-8 -*-
lines=sc.textFile('/user/maria_dev/foodratings63666.txt')
ex2RDD = lines.map(lambda line: line.split(“,”))
ex3RDD = ex2RDD.map(lambda line : [line[0], line[1], int(line[2]), line[3], line[4], line[5]])
ex4RDD = ex3RDD.filter(lambda line :int(line[2]) < 25)
ex5RDD = ex4RDD.map(lambda x: (x[0], x))
ex6RDD = ex5RDD.sortByKey(True)
print ex6RDD.take(5)