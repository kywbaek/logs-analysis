#!/usr/bin/env python3


import psycopg2
import sys


def create_view():
    """Create VIEW by executing the query
    """
    DB = psycopg2.connect("dbname=news")
    c = DB.cursor()
    c.execute("""CREATE VIEW articles_log AS
                        SELECT author, title, articles.id AS art_id, slug,
                                        path, og.id AS log_id
                        FROM articles, log
                        WHERE log.path LIKE '/article/' || articles.slug""")
    DB.commit()
    DB.close()


def execute_query(query):
    """Execute the query and return the results as a list of tuples.
    args:
        query - an SQL query statement to be executed.
    returns:
        A list of tuples containing the results of the query.
   """
    try:
        DB = psycopg2.connect("dbname=news")
        c = DB.cursor()
        c.execute(query)
        result = c.fetchall()
        DB.close()
        return result
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def question1():
    """Return the result for question 1;
    What are the most popular three articles of all time?
    """
    query = """SELECT title, COUNT(*) AS views
                    FROM articles_log
                    GROUP BY title
                    ORDER BY views DESC
                    LIMIT 3"""
    result = execute_query(query)
    solution = [('\"{}\" - {} views\n'.format(tup[0], tup[1]))
                for tup in result]
    return solution


def question2():
    """Return the result for question 2;
    Who are the most popular article authors of all time?
    """
    query = """SELECT name, COUNT(*) AS views
                    FROM articles_log, authors
                    WHERE authors.id = articles_log.author
                    GROUP BY name
                    ORDER BY views DESC"""
    result = execute_query(query)
    solution = [('{} - {} views\n'.format(tup[0], tup[1]))
                for tup in result]
    return solution


def question3():
    """Return the result for question 3;
    On which days did more than 1% of requests lead to errors?
    """
    query = """SELECT * FROM
                                (SELECT log.time:: date AS day,
                                            ROUND(100.0 * (SUM(CASE WHEN status
                                            SIMILAR TO '(4|5)%' THEN 1 ELSE 0
                                            END)) / COUNT(*), 1) AS errors
                                FROM log GROUP BY day) AS errors_all
                                WHERE errors > 1.0"""
    result = execute_query(query)
    solution = [
        ('{} - {}% errors\n'.format(tup[0].strftime("%B %d, %Y"), tup[1]))
        for tup in result]
    return solution


def main():
    """Use sys.argv to get the output file path
        and Get solutions text and write/append them into text file.
    """
    try:
        create_view()
    except:
        print("using articles_log VIEW that already exists...")

    out_file_path = sys.argv[1]
    solutions = [question1(), question2(), question3()]
    for sol in solutions:
        out_text = ''.join(sol) + '\n'
        with open(out_file_path, 'a') as out_f:
            out_f.write(out_text)


if __name__ == "__main__":
    main()
