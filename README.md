_Logs Analysis_
============

## Project Overview :
You've been hired onto a team working on a newspaper site. The user-facing newspaper site frontend itself, and the database behind it, are already built and running. You've been asked to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, your code will answer questions about the site's user activity.

The program you write in this project will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.

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

- VIEW used - articles_log :
```sql
CREATE VIEW articles_log AS
SELECT author, title, articles.id AS art_id, slug, path, log.id AS log_id
FROM articles, log
WHERE log.path LIKE '/article/' || articles.slug;
```

## Usage :
1. The virtual machine.
    - Use Vagrantfile provided in vagrant directory for VM
2. Setup the "news" database.
    - Download newsdata.zip file from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
    - Unzip newsdata.zip to extract newsdata.sql
    - run `psql -d news -f newsdata.sql`
3.  The program.
    - run `./run.sh`
    - Check the solution from output.txt in output directory.
