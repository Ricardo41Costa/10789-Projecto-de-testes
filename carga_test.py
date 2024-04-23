import main
import mysql.connector
import time

if __name__ == "__main__":
    db = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password=""
    )

    main.use_database(db)
  
    cursor = db.cursor()
    id = 99
    start = time.time()

    print("Test 1: Inserir 1000 registos. ")

    for _ in range(1000):
        try:
            val = (id, "Teste" + str(id), 1)
            sql = "INSERT INTO produtos(id, nome, quantidade) VALUES (%s, %s, %s)"
            cursor.execute(sql, val)
            db.commit()
            
            print("Query: " + cursor.statement)

            id += 1
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
    
    end = time.time()

    print("Test 1 ended Timed passed: " + str(end - start))

    id = 99
    start = time.time()

    print("Test 2: Delete 1000 registos.")

    for _ in range(1000):
        try:
            val = (id, )
            sql = "DELETE FROM produtos WHERE id=%s"
            cursor.execute(sql, val)
            db.commit()
            
            print("Query: " + cursor.statement)

            id += 1
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
    
    end = time.time()

    print("Test 2 ended: "  + str(end - start))