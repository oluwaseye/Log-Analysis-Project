#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import psycopg2

DATABASE = 'news'


def query_results(sql_query):
    db = psycopg2.connect(database=DATABASE)
    c = db.cursor()
    c.execute(sql_query)
    results = c.fetchall()
    db.close()
    return results


def print_results(query):
    for i in xrange(len(query)):
        title = query[i][0]
        result = query[i][1]
        print '\t' + '%s - %s' % (title, result)


dictonary = \
    {'\nWhat are the most popular articles of all time?':
        "SELECT title, CONCAT(COUNT(*), ' views') AS view_count,\
        COUNT(*) AS views FROM\
    articles JOIN log ON articles.slug = substring(log.path, 10)\
                GROUP BY title ORDER BY views DESC LIMIT 3;",
     '\nWho are the most popular article authors of all time?':
         "SELECT authors.name, CONCAT(COUNT(*), ' views') AS view_count,\
                COUNT(*) AS views\
                FROM articles \
                JOIN authors\
                ON articles.author = authors.id \
                JOIN log \
                ON articles.slug = substring(log.path, 10)\
                WHERE log.status LIKE '200 OK'\
                GROUP BY authors.name ORDER BY views DESC;",
     '\nOn which days did more than 1 percent of the requests led to errors?': "SELECT to_char(log_data.day, 'Mon DD, YYYY') AS Day, \
        CONCAT(ROUND((100.0*log_data.error/log_data.total_data), 2), '%' ) AS\
        Percentage FROM\
        (SELECT COUNT(id) AS total_data, date_trunc('day', time)\
          AS day,SUM(CASE WHEN log.status = '404 NOT FOUND' THEN 1 else 0 END)\
          AS error FROM log GROUP BY day) AS log_data \
          WHERE ROUND((100.0*log_data.error/log_data.total_data), 3) > 1;"}

for (request, query) in dictonary.items():
    print request
    print_results(query_results(query))
    print '\n'
