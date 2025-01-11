import psycopg2

try:
    # Connect to the PostgreSQL server
    connection = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="69420"
    )
    
    print("Connection successful:", connection)
    
    # Create a cursor object
    cursor = connection.cursor()
    
    # Execute a query to list all databases
    cursor.execute("SELECT datname FROM pg_database;")
    
    print("Databases in PostgreSQL:")
    for db in cursor.fetchall():
        print(db[0])  # Each `db` is a tuple; print the first element (database name)
    
except Exception as error:
    print("Error connecting to PostgreSQL server:", error)

finally:
    # Close the connection
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
