# -*- coding: utf-8 -*-

lines=sc.textFile('/user/maria_dev/foodratings63666.txt')
ex2RDD = lines.map(lambda line: line.split(“,”))
print ex2RDD.take(5)