import psycopg2
import csv
from config import load_config

config = load_config()
def insert_from_csv(csv_file):
    """Insert data from a CSV file into the database."""
    try:
        with open(csv_file, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            data = [tuple(row) for row in reader]
            print("Data read from CSV:", data)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return id

def insert_many_values(phone_book_list):
    """ Insert values into the phone book  """

    sql = "INSERT INTO phone_book(name, phone_number) VALUES(%s, %s)"
    rows = []

    try:
        with psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement

                for values in phone_book_list:
                    cur.execute("INSERT INTO phone_book(name, phone_number) VALUES(%s) RETURNING *", values)

                # obtain the inserted rows
                rows = cur.fetchall()

                # commit the changes to the database
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return rows

if __name__ == '__main__':
    insert_from_csv("csv_file.csv")