import mysql.connector

def use_database(db):
    cursor = db.cursor()
    sql = """USE mercado;"""
    cursor.execute(sql)

def show_data(db):
    cursor = db.cursor()
    sql = "SELECT * FROM produtos"
    cursor.execute(sql)
    results = cursor.fetchall()
    
    if cursor.rowcount < 0:
        print("There is not any data")
    else:
        for data in results:
            print(data)

def delete_teste(db):
    try:
        cursor = db.cursor()
        sql = "DELETE FROM produtos WHERE nome LIKE 'Teste%'"
        cursor.execute(sql)
        db.commit()
        print("{} data successfully deleted".format(cursor.rowcount))
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    except ValueError:
        print("Please make sure you have entered valid values.")

if __name__ == "__main__":
    db = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password=""
    )

    use_database(db)
  
    cursor = db.cursor()
    id = 1

    try:
        #Criar um registo normal e verificar q os dados desse registo são os esperados.
        val = (id, "Teste1", 1)
        sql = "INSERT INTO produtos(id, nome, quantidade) VALUES (%s, %s, %s)"
        cursor.execute(sql, val) 
        print("{} data Inserted".format(cursor.rowcount))
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

    try:    
        #Criar um registo com um id duplicado.
        val = (id, "Teste1", 1)
        sql = "INSERT INTO produtos(id, nome, quantidade) VALUES (%s, %s, %s)"
        cursor.execute(sql, val) 
        print("{} data Inserted".format(cursor.rowcount))
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))   

    try:
        #Apagar um registo existente.
        sql = "DELETE FROM produtos WHERE id=%s"
        val = (id, )
        cursor.execute(sql, val)
        db.commit()
        print("{} data successfully deleted".format(cursor.rowcount))
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

    try:
        #Apagar um registo inexistente.
        sql = "DELETE FROM produtos WHERE id=%s"
        val = (id, )
        cursor.execute(sql, val)
        db.commit()
        print("{} data successfully deleted".format(cursor.rowcount))
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

    #Inserir 10 registos.
    for _ in range(10):
        try:
            val = (id, "Teste" + str(id), 1)
            sql = "INSERT INTO produtos(id, nome, quantidade) VALUES (%s, %s, %s)"
            cursor.execute(sql, val) 
            id += 1
            print("{} data Inserted".format(cursor.rowcount))
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
    
    show_data(db)
    delete_teste(db)