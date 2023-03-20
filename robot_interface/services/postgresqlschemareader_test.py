import pprint

import psycopg2

import postgresqlschemareader


def main():

    """
    Test and demonstrate the functions of the postgresqlschemareader module.
    """

    print("--------------------------")
    print("| codedrome.com          |")
    print("| Read PostgreSQL Schema |")
    print("--------------------------\n")

    try:

        conn = psycopg2.connect("dbname=rocket host='localhost' user='rocket' password='123'")

        tables = postgresqlschemareader.get_tables(conn)
        print("codeinpython Tables\n===================\n")
        postgresqlschemareader.print_tables(tables)

        columns = postgresqlschemareader.get_columns(conn, "rocket_kitchens", "item_analysis")
        print("Columns in Table\n=======================\n")
        postgresqlschemareader.print_columns(columns)

        tree = postgresqlschemareader.get_tree(conn)
        print("Database codeinpython\n=====================\n")
        postgresqlschemareader.print_tree(tree)
        print()
        pprint.pprint(tree)

        conn.close()

    except psycopg2.Error as e:

        print(type(e))

        print(e)


main()
