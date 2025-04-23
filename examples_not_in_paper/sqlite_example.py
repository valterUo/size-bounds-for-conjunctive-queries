import sqlite3

def create_database():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    # Drop table if it exists
    cursor.execute("DROP TABLE IF EXISTS relation")
    
    # Create table with attributes x, y, z, u
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS relation (
        x TEXT,
        y TEXT,
        z TEXT,
        u TEXT,
        PRIMARY KEY (x, z, y, u)
    )
    """)
    
    conn.commit()
    conn.close()

def insert_data():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    # Insert data following the functional dependencies xz -> u and yu -> x
    #data = [
    #    ("a", "b", "c", "d"),  # (x, z) -> u and (y, u) -> x
    #    ("a", "e", "c", "d"),  # Same (x, z) should have same u
    #    ("f", "b", "g", "h"),  # Another valid entry
    #    ("i", "j", "k", "l"),  # Another valid entry
    #    ("a", "b", "m", "n"),  # Ensuring (y, u) -> x consistency
    #    ("a", "b", "p", "n")   # Ensuring (y, u) -> x consistency
    #]
    
    data = [
        (0, 0, 0, 0),
        #(1, 0, 0, 0),
        #(0, 1, 0, 0),
        #(0, 0, 1, 0),
        #(0, 0, 0, 1),
        (1, 1, 0, 0),
        #(1, 0, 1, 0),
        #(1, 0, 0, 1),
        #(0, 1, 1, 0),
        #(0, 1, 0, 1),
        #(0, 0, 1, 1),
        #(1, 1, 1, 0),
        #(1, 1, 0, 1),
        (1, 0, 1, 1),
        #(0, 1, 1, 1),
        (1, 1, 1, 1)
    ]
    
    data = [
        (0, 0, 0, 0),
        (1, 0, 0, 0),
        (0, 1, 0, 0),
        (0, 0, 1, 0),
        (0, 0, 0, 1),
        (1, 1, 0, 0),
        (1, 0, 1, 0),
        (1, 0, 0, 1),
        (0, 1, 1, 0),
        (0, 1, 0, 1),
        (0, 0, 1, 1),
        (1, 1, 1, 0),
        (1, 1, 0, 1),
        (1, 0, 1, 1),
        (0, 1, 1, 1),
        (1, 1, 1, 1)
    ]
    
    cursor.executemany("INSERT OR IGNORE INTO relation (x, y, z, u) VALUES (?, ?, ?, ?)", data)
    
    conn.commit()
    conn.close()

def get_conjunctive_query():
    return """
    SELECT DISTINCT r1.x, r1.y, r2.z, r3.u 
    FROM relation AS r1
    JOIN relation AS r2 ON r1.y = r2.y
    JOIN relation AS r3 ON r2.z = r3.z;
    """

def execute_query(query):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    cursor.execute(query)
    result = cursor.fetchall()
    
    conn.close()
    return result

def find_the_largest_relation():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT x FROM relation")
    result = cursor.fetchall()
    
    size = len(result)
    
    cursor.execute("SELECT y FROM relation")
    result = cursor.fetchall()
    if len(result) > size:
        size = len(result)
    
    cursor.execute("SELECT z FROM relation")
    result = cursor.fetchall()
    if len(result) > size:
        size = len(result)
    
    cursor.execute("SELECT u FROM relation")
    result = cursor.fetchall()
    if len(result) > size:
        size = len(result)
    
    conn.close()
    return size

if __name__ == "__main__":
    create_database()
    insert_data()
    query = get_conjunctive_query()
    print("SQL Query:")
    print(query)
    print("\nResult:")
    print(len(execute_query(query)))
    print("\nSize of the largest relation:")
    n = find_the_largest_relation()
    print(n)
    print("Size bound: ", n**(2))
    