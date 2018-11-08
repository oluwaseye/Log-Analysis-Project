# Log Analysis

## Project
A tool that generates a report from a database and presents the information.

### Project Overview
The project was to create the following reports from the **News** database.
- Which articles have been accessed the most? 
- The most popular article authors of all time
- The days did more than 1% of requests lead to errors


### Requirements
**Please make sure you have the following configured on your machine.**

- [Python 3](https://www.python.org/download/releases/3.0/) -  An interpreted high-level programming language.
- [PostgreSQL](https://www.postgresql.org/) -  An object-relational database management system (ORDBMS)
- Command line:  Windows Command-line interface or Unix Command-line interface

**Note**: Though this project was created on an ubuntu virtual machine, it is not required for you to run it.

### Requirements

#### Variable:
* **dictionary** The variable holds the a dictionary of the request and their corresponding sql query.

#### Functions:
* **query_results():** Accepts a sql query as a parameter, connects to the PostgreSQL database and returns the result.

* **print_results():** Accepts the result from the query_results function, formats and presents the report.

#### Process
Loop through the dictonary and print out the request then run the print_results function by parsing the query_results function as parameter and each query as paramter of the query_results function
```
 for (request, query) in dictonary.items():
    print request
    print_results(query_results(query))
    print '\n'`
```

###  Running the application
The database includes three tables:
- Authors table
- Articles table
- Log table

**Follow the steps below to access the code of this project**:
1. Clone this repository.
2. Open your command-line/terminal and navigate to the repo location.
 11.  Import the database with this command  `psql -d news -f newsdata.sql`
 11. Use this command `python log.py` to run the python program.


###  Troubleshooting
If your command prompt does not run the `python` command.

**Mac & Linux**
You can refer to this [link](https://www.cyberciti.biz/faq/bash-python-command-not-found/ "link")

**Windows** : You will have to manually check your environment variables and add the python executable to your  SYSTEM PATH. You can refer to this [link](https://stackoverflow.com/questions/13596505/python-not-working-in-command-prompt?answertab=votes#tab-top "link") for help. Though this link helps with Python v2, it is the same process for v3.

You can not seem to run the PostgreSQL command `psql` in your command-line interface

**Windows & Linux**
Here is a helpful [resource](https://www.enterprisedb.com/es/docs/en/9.3/instguide/Postgres_Plus_Advanced_Server_Installation_Guide.1.32.html "resource")

**Mac**
Click here for the [resource](https://launchschool.com/blog/how-to-install-postgresql-on-a-mac "resource")