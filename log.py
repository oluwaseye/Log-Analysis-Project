# !/usr/bin/env python

import psycopg2

DATABASE = "news"

first_request = "What are the most popular articles of all time?"

first_query = "SELECT articles.title, COUNT(*) as views FROM articles \
               JOIN log ON log.path LIKE '%200%' \
               GROUP BY articles.title, log.path ORDER BY views DESC LIMIT 3 "

second_request = "Who are the most popular article authors of all time?"

second_query = "SELECT authors.name, count(*) as views\
           	    FROM articles \
           	    JOIN authors\
           	    ON articles.author = authors.id \
                JOIN log \
                ON articles.slug = substring(log.path, 10)\
                WHERE log.status LIKE '%200 OK%'\
                GROUP BY authors.name ORDER BY views DESC;"

third_request = "On which days more than 1% of the requests led to error?"

third_query =  "SELECT to_char(log_data.day, 'Mon DD, YYYY') AS Day, \
				CONCAT(ROUND((100.0*log_data.error/log_data.total_data), 2), '%' ) AS Percentage \
     			FROM  (SELECT count(id) AS total_data, date_trunc('day', time) AS day, \
     			SUM(CASE WHEN log.status = '404 NOT FOUND' THEN 1 else 0 END) AS error FROM log GROUP BY day) AS log_data \
     			WHERE ROUND((100.0*log_data.error/log_data.total_data), 3) > 1;"

