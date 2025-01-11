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
        SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'pwSkills';
    """)
    exists = mycursor.fetchone()
    
    if not exists:
        # If the database does not exist, create it
        mycursor.execute("CREATE DATABASE pwSkills;")
        print("Database 'pwSkills' created successfully.")
    else:
        print("Database 'pwSkills' already exists.")
    
except Exception as e:
    print("Error: ", e)

finally:
    if mydb:
        mycursor.close()
        mydb.close()
        print("PostgreSQL connection is close")