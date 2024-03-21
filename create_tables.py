import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    """
    Description: This function is responsible for creating and connecting to the sparkifydb. 
    It first connects to the default database, creates the sparkifydb with UTF8 encoding, 
    and then connects to the sparkifydb. It returns the connection and cursor to sparkifydb.

    Arguments:
        None

    Returns:
        cur: The cursor object for sparkifydb.
        conn: The connection to sparkifydb.
    """
    
    # connect to default database
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()    
    
    # connect to sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()
    
    return cur, conn


def drop_tables(cur, conn):
    """
    Description: This function drops each table in the Sparkify database using the queries in the drop_table_queries list.

    Arguments:
        cur: The cursor object.
        conn: The connection to the Sparkify database.

    Returns:
        None
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Description: This function creates each table in the Sparkify database using the queries in the create_table_queries list.

    Arguments:
        cur: The cursor object.
        conn: The connection to the Sparkify database.

    Returns:
        None
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    Description: This function first connects to the Sparkify database, drops all the tables if they exist, 
    creates all necessary tables, and then closes the connection.

    Arguments:
        None

    Returns:
        None
    """
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()