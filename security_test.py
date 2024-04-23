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

    try:
        print("Test 1: Criar um registo normal e verificar q os dados desse registo são os esperados.")

        val = (id, "Teste1", 1)
        sql = "INSERT INTO produtos(id, nome, quantidade) VALUES (%s, %s, %s)"
        cursor.execute(sql, val) 
        db.commit()

        print("Query: " + cursor.statement)
        
        assert cursor.rowcount == 1

        print("Teste 1 Success \n")
    except mysql.connector.Error as err:
        print("Test 1 Failed \n")
    except AssertionError:
        print("Test 1 Failed \n")

    try:    
        print("Test 2: Criar um registo com um id duplicado.")

        val = (id, "Teste1", 1)
        sql = "INSERT INTO produtos(id, nome, quantidade) VALUES (%s, %s, %s)"
        cursor.execute(sql, val)
        db.commit()

        print("Query: " + cursor.statement)
        
        assert cursor.rowcount == 0

        print("Teste 2 Success \n")
    except mysql.connector.Error as err:
        print("Test 2 Success \n")
    except AssertionError:
        print("Test 2 Failed \n")

    try:
        sql = "DELETE FROM produtos WHERE id=%s"
        val = (id, )
        cursor.execute(sql, val)
        db.commit()
    except mysql.connector.Error as err:
        print("Test 3 Failed \n")
    except AssertionError:
        print("Test 3 Failed \n")