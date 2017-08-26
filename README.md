_Logs Analysis_
============

## Project Overview :
You've been hired onto a team working on a newspaper site. The user-facing newspaper site frontend itself, and the database behind it, are already built and running. You've been asked to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, your code will answer questions about the site's user activity.

The program will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.

### "news" Database Structure :

| Table | Descriptions | Columns |
|--------|-----------------|------------|
| **articles** | includes the articles | author, title, slug, lead, time, id |
| **authors** | includes informationa about the authors of articles | name, bio, id |
| **log** | includes one entry for each time a user has accessed the site | path, ip, method, status, time, id |

### Questions to answer :
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Approach :
- Use Python module **psycopg2** to query a mock **PostgreSQL** database and fetch the results to be written in output file.

- VIEW used - article_views :
```sql
CREATE VIEW article_views AS
SELECT articles.title, authors.name AS author, log.views
FROM articles INNER JOIN
    (SELECT path, COUNT(*) AS views
    FROM log
    GROUP BY path) AS log
ON '/article/' || articles.slug = log.path
LEFT JOIN authors
ON articles.author = authors.id;
```

## Usage :
1. The virtual machine.
    - From the command line, navigate to the folder containing the Vagrantfile
    - Power up the virtual machine by typing: `vagrant up` note: this may take a couple minutes to complete
    - Once the virtual machine is done booting, log into it by typing: `vagrant ssh`
2. Setup the "news" database.
    - Download newsdata.zip file from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
    - Unzip newsdata.zip to extract newsdata.sql
    - From the command line, type `psql -d news -f newsdata.sql`
3.  The program.
    - From the command line, type `./run.sh`
    - Check the solution from output.txt in output directory.
