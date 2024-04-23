import mysql.connector
import os

#cursor = database.cursor()

def create_db(db):
    try:
        cursor = db.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS mercado")

        print("Database Created Successful !!!")
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    except:
        print("Unable to create database Product")
        exit()

def create_table(db):
    try:
        cursor = db.cursor()
        sql = """CREATE TABLE IF NOT EXISTS produtos(
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255),
        quantidade INT
        )
        """
        cursor.execute(sql)

        print("Table Created Successful !!!")
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    except:
        print("Unable to create Table Product")
        exit()

def use_database(db):
    cursor = db.cursor()
    sql = """USE mercado;"""
    cursor.execute(sql)

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def insert_data(db):
    try:
        cursor = db.cursor()
        nome = input("Enter product name: ")
        amount = int(input("Enter product amount: "))

        val = (nome, amount)
        sql = "INSERT INTO produtos(nome, quantidade) VALUES (%s, %s)"
        cursor.execute(sql, val)
        
        db.commit()
        print("{} data Inserted".format(cursor.rowcount))
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    except ValueError:
        print("Please make sure you have entered valid values.")
        insert_data(db)

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

def update_data(db):
    try:
        cursor = db.cursor()
        show_data(db)
        id = int(input("Choose product id: "))
        name = input("New Name: ")
        amount = int(input("New amount: "))

        sql = "UPDATE produtos SET nome=%s, quantidade=%s WHERE id=%s"
        val = (name, amount, id)
        cursor.execute(sql, val)
        db.commit()
        print("{} data successfully changed".format(cursor.rowcount))
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    except ValueError:
        print("Please make sure you have entered valid values.")
        update_data(db)

def delete_data(db):
    try:
        cursor = db.cursor()
        show_data(db)
        id = int(input("Choose product id: "))
        sql = "DELETE FROM produtos WHERE id=%s"
        val = (id, )
        cursor.execute(sql, val)
        db.commit()
        print("{} data successfully deleted".format(cursor.rowcount))
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    except ValueError:
        print("Please make sure you have entered valid values.")
        delete_data(db)

def search_data(db, keyword = ""):
    try:
        cursor = db.cursor()
        if keyword == "":
            keyword = input("Keyword: ")
        sql = "SELECT * FROM produtos WHERE nome LIKE %s"
        val = ("%{}%".format(keyword), )
        cursor.execute(sql, val)
        results = cursor.fetchall()
        
        if cursor.rowcount < 0:
            print("There is not any data")
        else:
            for data in results:
                print(data)
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    except ValueError:
        print("Please make sure you have entered valid values.")

def show_menu(db):
    print("=== APPLICATION DATABASE PYTHON ===")
    print("1. Insert Data")
    print("2. Show Data")
    print("3. Update Data")
    print("4. Delete Data")
    print("5. Search Data")
    print("0. Exit")
    print("------------------")
    menu = input("Choose menu> ")

    clear()

    if menu == "1":
        insert_data(db)
    elif menu == "2":
        show_data(db)
    elif menu == "3":
        update_data(db)
    elif menu == "4":
        delete_data(db)
    elif menu == "5":
        search_data(db)
    elif menu == "0":
        exit()
    else:
        print("Wrong option!")

if __name__ == "__main__":
    db = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password=""
    )

    create_db(db)
    use_database(db)
    create_table(db)
  
    while(True):
        show_menu(db)