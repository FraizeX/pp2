import psycopg2
from config import load_config
config = load_config()

def insert_or_update():

    name = input("Name: ")
    
    try:
        with psycopg2.connect(**config) as conn:

            with conn.cursor() as cur:                                                                
                cur.execute("SELECT id FROM phone_book WHERE name = %s", (name,))
                row = cur.fetchone()

                if row:                                                                             #Check username for existance  
                    phone_number = input("Phone number: ")
                    user_id = row[0]
                    cur.execute("UPDATE phone_book SET phone_number = %s WHERE id = %s",
                                (phone_number, user_id))  

                else:                                                                               #If not get new data     
                    phone_number = input("Phone number: ")
                    
                    cur.execute("INSERT INTO phone_book(name, phone_number) VALUES(%s, %s) RETURNING id",
                                (name, phone_number))
                    row = cur.fetchone()
                    user_id = row[0]

                conn.commit()
                return user_id
            
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return None


user = insert_or_update()
if user:
    print("success, ID:", user)
else:
    print("Fail")