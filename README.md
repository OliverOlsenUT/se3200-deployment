# Recommended Switch Games
An application to display, edit, add, and delete recommended switch games from the database. Documentation based on https://github.com/csse3200/markdown-example.

## Resource

**Game**

Attributes:

* name (string)
* review (string)
* genres (string)
* cost (double)
* esrb_rating (string)

## Schema

```sql
CREATE TABLE games (
id INTEGER PRIMARY KEY,
name TEXT,
review TEXT,
genres TEXT,
cost DOUBLE,
esrb_rating TEXT);
```

## REST Endpoints

Name                           | Method | Path
-------------------------------|--------|------------------
Retrieve game collection | GET    | /games
Retrieve game member     | GET    | /games/*\<id\>*
Create game member       | POST   | /games
Update game member       | PUT    | /games/*\<id\>*
Delete game member       | DELETE | /games/*\<id\>*