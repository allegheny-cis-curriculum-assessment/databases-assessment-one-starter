"""An assessment for the Databases course."""

import sqlite3

from pathlib import Path
from evalugator import constants, run, test

"""
Introduction: Read This First!

A team at a newspaper is building a content management system (CMS) to manage
and publish news stories to its website using a stack including Python. The
team chose SQLITE3 as a database for its system, and needs to migrate data from
a previous CMS into their new one. To do testing, they’ve put together 3
tables:

- authors
- stories
- metadata

To make sure the migration and technology are up to par, the developers need to
test the ability of the new system to migrate files and display all relevant
story data including story author(s), titles, and relevant metadata information
on a site front page. This demonstration must also provide the ability to
change an author’s status given an author’s last name and ID number.

You will implement two key deliverables in this assessment:

- a SQLITE3 database constructed from comma separated values files (CSV) located
  in the data/ folder, storing the database called "news_data.db" in the db/ folder
- a complete Python program to complete the tasks outlined below; note that some of
  functions in this program rely on the output of others to complete their task(s)

At a high level, this program should complete the following operations, roughly
in order:

- connect to the database using the completed function in create_or_connect_db
- create a database cursor to use to execute prepared statements in the functions
  that populate the file
- use the query_prolific_author function to find the author who has published the
  most stories, returning their ID number from the authors table
- use the ID number gained in the previous step to implement a function to
  join all tables in the database to produce a listing of stories published
  by this author in the format (each on a new line) of:

        STORY DATE NEWSPAPER SECTION STORY TITLE FIRST NAME LAST NAME [STATUS]

  In practice, this looks like the following:

        2007-03-01 [Education] "Assessments: Why We Do Them" G. Wiz [INACTIVE]

- complete a function to obtain an author's first and last name via query using
  author ID number from a previous step
- change the status of this author to ACTIVE using a function to update the authors
  table to reflect change in status (the most prolific author is INACTIVE)

"""

"""
Part Zero

Instructions:

Using the sqlite3 CLI program, import the 3 files from the data/ folder  to create
representative database tables:

  - create `metadata` from `metadata.csv`
  - create `stories` from `stories.csv`
  - create `authors` from `authors.csv`
"""

"""
Part One

Instructions:

Implement the create_or_connect_db function to open the database created
from CSV data.

Function specification:

- Accepts the name of the database as a string
- Creates a SQLITE3 connection to the file name at correct file location
- Returns the successful connection

"""


def create_or_connect_db(dbname: str = "") -> sqlite3.Connection:
    """Creates or connects to the database; preferably just connects"""
    db_path = Path(dbname)
    conn = sqlite3.connect(db_path)
    return conn


"""
Part Two

Instructions:

Construct a query to complete the following function which queries the metadata
table of the database to find the author with the most entries.

Function specification:

- Constructs a query to determine which author in the table has authored the
  most stories

"""


def query_prolific_author(cursor: sqlite3.Cursor, mode: str = "DESC") -> int:
    """Finds author ID of most prolific author"""
    cursor.execute(
        f"""SELECT author_id FROM metadata
                     GROUP BY author_id
                     ORDER BY count(author_id) {mode}"""
    )
    individual = cursor.fetchone()
    return individual[0]


"""
Part Three

Instructions:

Construct a query to complete the following function which queries all three
tables joined to produce a listing of the most prolific author's stories, returning
the fields:

    STORY DATE NEWSPAPER SECTION STORY TITLE FIRST NAME LAST NAME

Function specification:

- Constructs a query which joins all three tables on the id fields of each table
  and returns the requested data

"""


def query_stories_by_author(cursor: sqlite3.Cursor, author_id: int = 1) -> list:
    """Find all stories by a given author by ID, return relevant data"""
    cursor.execute(
        """SELECT date, section, title, fname, lname FROM stories
                      LEFT JOIN metadata ON stories.id = metadata.id
                      INNER JOIN authors ON metadata.author_id = authors.id
                      WHERE metadata.author_id = ?""",
        (author_id,),
    )
    return [
        f'{date} [{section}] "{title}" {fname} {lname}'
        for date, section, title, fname, lname in cursor.fetchall()
    ]


"""
Part Four

Instructions:

Complete a query which returns the fname and lname of any author by ID number; here,
we should use the most prolific author's ID number (gained in a previous step) to
query the database.

Function specification:

- Constructs a query which returns the fname and lname fields for the provided
  author_id

"""


def query_author_by_id(cursor: sqlite3.Cursor, author_id: int = 1) -> str:
    """Finds the author name by ID only"""
    cursor.execute("SELECT fname, lname FROM authors WHERE id = ?", (author_id,))
    records = cursor.fetchall()
    return f"{records[0][0]} {records[0][1]}"


"""
Part Five

Instructions:

Construct a query to update an author to a new status given the correct author id.
For the purposes of this assessment, use the ID of the most prolific author and
set their status to ACTIVE.

Function specification:

- Constructs a query which updates the authors table to set status of the author
  whose ID matches the author_id parameter
- Sets the status equal to a string value (status) passed to the function

"""


def update_author_status(
    conn: sqlite3.Connection,
    cursor: sqlite3.Cursor,
    author_id: int = 1,
    status: str = "INACTIVE",
) -> dict:
    """Change status of an author to value of status string"""
    cursor.execute("UPDATE authors SET status = ? WHERE id = ?", (status, author_id))
    conn.commit()
    response = {"author": author_id, "status": status, "updated": False}
    if cursor.rowcount == 1:
        response["updated"] = True
    return response


# Do not edit any of the source code below this line {{{

if __name__ == "__main__":
    separator = constants.markers.Separator
    assessment_outputs = run.do_runs()
    test_outputs = test.do_tests()
    for assessment_output, test_output in zip(assessment_outputs, test_outputs):
        print(str(assessment_output) + separator + str(test_output))

# }}}
