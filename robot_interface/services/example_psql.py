PGHOST='localhost'
PGDATABASE='rocket'
PGUSER='rocket'
PGPASSWORD='123'


import psycopg2
import sys, os
import numpy as np
import pandas as pd
import example_psql as creds
import pandas.io.sql as psql

## ****** LOAD PSQL DATABASE ***** ##


# Set up a connection to the postgres server.
conn_string = "host="+ PGHOST +" port="+ "5432" +" dbname="+ PGDATABASE +" user=" + PGUSER \
+" password="+ PGPASSWORD
conn=psycopg2.connect(conn_string)
print("Connected!")

# Create a cursor object
cursor = conn.cursor()


def load_data(schema, table):

    sql_command = "SELECT * FROM {}.{};".format(str(schema), str(table))
    print(sql_command)

    # Load the data
    data = pd.read_sql(sql_command, conn)

    print(data.shape)
    return (data)


if __name__ == "__main__":
    load_data('public','mytable')
