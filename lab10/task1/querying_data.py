import psycopg2
from config import load_config

def get_values_by_id():
    """ Retrieve data from the phone book """
    config  = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id, name, phone_number FROM phone_book ORDER BY id")
                print("The number of parts: ", cur.rowcount)
                row = cur.fetchone()

                while row is not None:
                    print(row)
                    row = cur.fetchone()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def get_values_by_name():
    """ Retrieve data from the phone book """
    config  = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id, name, phone_number FROM phone_book ORDER BY name")
                print("The number of parts: ", cur.rowcount)
                row = cur.fetchone()

                while row is not None:
                    print(row)
                    row = cur.fetchone()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        

def get_values_by_phone():
    """ Retrieve data from the phone book """
    config  = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id, name, phone_number FROM phone_book ORDER BY phone")
                print("The number of parts: ", cur.rowcount)
                row = cur.fetchone()

                while row is not None:
                    print(row)
                    row = cur.fetchone()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    operation = input("""In what order should sort?
                         i - id
                         n - name
                         p - phone_number
                      """)
    if operation == 'i':
        get_values_by_id()
    if operation == 'n':
        get_values_by_name()
    if operation == 'p':
        get_values_by_phone()