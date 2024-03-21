# Summary

In this project, I am going to be using Python and SQL to build an ETL pipeline for a music streaming app. This pipeline will transfer data from JSON logs and song data into a Postgres database with a star schema. This will allow the analytics team at Sparkify to easily query their data and understand what songs users are listening to.

# To run my script you will need to do the following:

Run create_tables.py to create the database and tables, dropping any existing tables if necessary. This script imports SQL queries from sql_queries.py. Use etl.py to run the main script and to load the data in the Postgres Table. Finally, use test.ipynb to query the tables and ensure they contain the appropriate data.

A few of the files or folders that I did not mention in running my scripts include the data folder and etl.ipynb notebook. The data folder contains the data in json format for the folders while the ipython notebook was used in the development of my etl.py file.
