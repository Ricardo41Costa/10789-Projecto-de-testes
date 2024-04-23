import main
import mysql.connector

if __name__ == "__main__":
    db = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password=""
    )

    main.use_database(db)
  
    cursor = db.cursor()
    id = 99

    print("Test 1: Inserir 10 registos. \n")

    for _ in range(10):
        try:
            val = (id, "Teste" + str(id), 1)
            sql = "INSERT INTO produtos(id, nome, quantidade) VALUES (%s, %s, %s)"
            cursor.execute(sql, val)
            db.commit()
            
            print("Query: " + cursor.statement)

            id += 1
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        
    main.search_data(db , "Teste")

    print("Test 2: Update 10 registos. \n")
    
    for _ in range(10):
        try:
            val = ("Tesste" + str(id), 1, id)
            sql = "UPDATE produtos SET nome=%s, quantidade=%s WHERE id=%s"
            cursor.execute(sql, val) 
            db.commit()
            
            print("Query: " + cursor.statement)

            id += 1
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))

    
    main.search_data(db , "Tesste")

    id = 99

    print("Test 3: Delete 10 registos. \n")
    
    for _ in range(10):
        try:
            val = (id, )
            sql = "DELETE FROM produtos WHERE id=%s"
            cursor.execute(sql, val) 
            db.commit()
            
            print("Query: " + cursor.statement)

            id += 1
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))

    
    main.search_data(db , "Tesste")

