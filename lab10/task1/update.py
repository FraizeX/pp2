import psycopg2
from config import load_config


def update_name(id, name):
    """ Update phone_book based on the id """
    
    updated_row_count = 0

    sql = """ UPDATE phone_book
                SET name = %s
                WHERE id = %s"""
    
    config = load_config()
    
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                
                # execute the UPDATE statement
                cur.execute(sql, (id, name))
                updated_row_count = cur.rowcount

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return updated_row_count


def update_phone(id, phone_number):
    """ Update phone_book based on the id """
    
    updated_row_count = 0

    sql = """ UPDATE phone_book
                SET phone_number = %s
                WHERE id = %s"""
    
    config = load_config()
    
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                
                # execute the UPDATE statement
                cur.execute(sql, (id, phone_number))
                updated_row_count = cur.rowcount

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return updated_row_count

if __name__ == '__main__':
    operation = input("""What you want update?
                         n - name
                         p - phone
                      """)
    if operation == "n":
        id = input("Write id: ")
        name = input("Write name: ")
        update_name(id, name)
    elif operation == "p":
        id = input("Write id: ") 
        phone_number = input("Write phone: ")
        update_phone(id, phone_number)
        