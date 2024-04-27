import psycopg2
from config import load_config

config = load_config()
def insert_values(name, phone_number):
    """ Insert a values into the phone_book """

    sql = """INSERT INTO phone_book (name, phone_number)
             VALUES(%s, %s) RETURNING id;"""
    
    id = None
    
    try:
        with psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(sql, (name, phone_number))

                # get the generated id back                
                rows = cur.fetchone()
                if rows:
                    id = rows[0]

                # commit the changes to the database
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return id

def insert_many_values(phone_book_list):
    """ Insert multiple values into the phone book  """

    sql = "INSERT INTO phone_book (name, phone_number) VALUES(%s, %s)"
    rows = []

    try:
        with psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement

                for value in phone_book_list:
                    cur.execute("INSERT INTO phone_book (name, phone_number) VALUES(%s, %s) RETURNING *", value)

                # obtain the inserted rows
                rows = cur.fetchall()

                # commit the changes to the database
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return rows

if __name__ == '__main__':
    name = input("Write name: ")
    phone_number = str(input("Write phone number: "))
    insert_values(name, phone_number)
    