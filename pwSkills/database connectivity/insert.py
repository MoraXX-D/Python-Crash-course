import psycopg2

try:
    # Connect to the PostgreSQL server and the 'postgres' database
    mydb = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="69420",
        database="postgres"
    )
    print("Connection successful!", mydb)
    
    # Enable autocommit for the INSERT command
    mydb.autocommit = True
    
    # Create a cursor object
    mycursor = mydb.cursor()

    # Insert data into the 'students' table in the 'pwskills' schema
    mycursor.execute("""
        INSERT INTO pwSkills.students (id, name, age, grade)
        VALUES (1, 'Suresh', 23, 87);
    """)
    print("Record inserted successfully into 'students' table.")

except Exception as e:
    print("Error:", e)

finally:
    if mydb:
        if mycursor:  # Check if cursor was created before closing
            mycursor.close()
        mydb.close()  # Close the connection
        print("PostgreSQL connection is closed.")
