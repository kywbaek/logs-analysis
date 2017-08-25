#!/usr/bin/env python3

import psycopg2
import sys


def create_view():
    DB = psycopg2.connect("dbname=news")
    c = DB.cursor()
    c.execute("CREATE VIEW articles_log AS(SELECT author, title, articles.id AS art_id, slug, path, log.id AS log_id FROM articles, log WHERE log.path LIKE '/article/' | | articles.slug | | '%')")
    DB.close()


def question1():
    DB = psycopg2.connect("dbname=news")
    c = DB.cursor()
    c.execute(
        "SELECT title, COUNT(*) AS views FROM articles_log GROUP BY title ORDER BY views DESC LIMIT 3")
    solution = [('"' + tup[0] + '" - ' + str(tup[1]) + ' views' + '\n')
                for tup in c.fetchall()]
    DB.close()
    return solution


def question2():
    DB = psycopg2.connect("dbname=news")
    c = DB.cursor()
    c.execute("SELECT name, COUNT(*) AS views FROM articles_log, authors WHERE authors.id = articles_log.author GROUP BY name ORDER BY views DESC")
    solution = [(tup[0] + ' - ' + str(tup[1]) + ' views' + '\n')
                for tup in c.fetchall()]
    DB.close()
    return solution


def question3():
    DB = psycopg2.connect("dbname=news")
    c = DB.cursor()
    c.execute("SELECT * from (SELECT log.time:: date AS day, ROUND(100.0 * (SUM(CASE WHEN status SIMILAR TO '(4|5)%' THEN 1 ELSE 0 END)) / COUNT(*), 1) AS errors FROM log GROUP BY day) AS errors_all WHERE errors > 1.0")
    solution = [(str(tup[0]) + ' - ' + str(tup[1]) + '% errors' + '\n')
                for tup in c.fetchall()]
    DB.close()
    return solution


def main():
    # use sys.argv to get the output file path
    # get solutions text and write/append them into text file.
    create_view()
    out_file_path = sys.argv[1]
    solutions = [question1(), question2(), question3()]
    for sol in solutions:
        out_text = ''.join(sol) + '\n'
        with open(out_file_path, 'a') as out_f:
            out_f.write(out_text)


if __name__ == "__main__":
    main()
