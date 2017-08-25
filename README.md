# _Logs Analysis_

logs analysis project

### VIEW used - articles_log
`CREATE VIEW articles_log AS (SELECT author, title, articles.id AS art_id, slug, path, log.id AS log_id FROM articles, log WHERE log.path LIKE '/article/' || articles.slug || '%')`

### Usage
run `./run.sh`<br>
It will write solution into output.txt in output directory.
