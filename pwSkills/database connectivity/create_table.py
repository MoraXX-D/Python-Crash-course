import psycopg2

try:
    mydb = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="69420",
        database = "postgres"
    )
    print("connection successfull !",mydb)
    
    mydb.autocommit = True
    
    mycursor = mydb.cursor()
    mycursor.execute("""
        SELECT 1 FROM information_schema.tables 
        WHERE table_name = 'students' AND table_schema = 'public';
    """)
    exists = mycursor.fetchone()

    if not exists:
        # If the table does not exist, create it
        mycursor.execute("""
            CREATE TABLE students (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255),
                age INT,
                grade INT
            );
        """)
        print("Table 'students' created successfully.")
    else:
        print("Table 'students' already exists.")
        
    
    
except Exception as e:
    print("Error: ", e)

finally:
    if mydb:
        mycursor.close()
        mydb.close()
        print("PostgreSQL connection is close")