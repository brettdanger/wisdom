## Wisdom Backend

Wisdom Backend is a Massive Open Online Course (MOOC) aggregation engine that is extensible for providers and courses. It will collect data from any providers enabled in the ```config.yaml``` list. It will also save the data into any storage engines enabled in the ```config.yaml``` file.

###Currently Supported Providers:

- Coursera

###Currently Supported Storage Engines:

-  Any [SQLAlchemy supported RDBMS/Dialects](http://docs.sqlalchemy.org/en/rel_0_9/dialects/index.html) including:
    -  Drizzle
    - Firebird
    - Microsoft SQL Server
    - MySQL (tested)
    - Oracle
    - PostgreSQL (tested)
    - SQLite
    - Sybase
- MongoDB

###Currently working on:
    
- edX provider engine
- Elastic Search storage engine (for some cool NLP stuff)

###Purpose:

Even though there are several MOOC lists and rating sites out there, none of them are very good.  I also want to build a full-stack site with ratings and collaboration tools, this is step 1.  Others are welcome to use to build something cool, please contribute storage engines or provider engines if you build them.  You can follow my progress on the full stack site at brettdangerfield.com.

##Installation:

1. Clone the repo, then activate the virtualenv with ```virtualenv .``` *assuming you have virtualenv installed*
2. Activate the virtualenv ```source bin/activate```
3. Install the PIP packages ```pip install - r requirements.txt```
4. Configure the config.yaml to include your settings for your DB engine
5. If you are using a SQL RDBMS, set your connection string in the config file and run ```python storage/sql_setup/db_setup.py``` to create the tables and schemas
6. Enable your providers and engines by adding them to the config file
7. Collect the Data and fill your databases with ```python collect_data.py```
8. Profit


##Testing:

1. You can run  ```nosetests --with-coverage``` to run the unit tests.

