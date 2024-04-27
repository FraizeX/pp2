import psycopg2
from config import load_config


def delete_phone_book(name):
    """ Delete part by name """

    rows_deleted  = 0
    sql = 'DELETE FROM phone_book WHERE name = %s'
    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the UPDATE statement
                cur.execute(sql, (name,))
                rows_deleted = cur.rowcount

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return rows_deleted


def delete_data_by_phone(name):
    config = load_config()
    try:
        conn = psycopg2.connect(**config)
        cur = conn.cursor()

        sql = "DELETE FROM phone_book WHERE name = %s"
        
        cur.execute(sql, (name,))

        conn.commit()
        
        print("Deleted")

        cur.close()
        conn.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)


string = input("Enter name which you want to delete: ")
if __name__ == '__main__':
    deleted_rows = delete_phone_book(string)
    delete_data_by_phone(string)
    print('The number of deleted rows: ', deleted_rows)