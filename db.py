from mysql.connector import connect, MySQLConnection
from mysql.connector import Error


class Database:
    create_questions_table = """
    create table if not exists questions(
        id int auto_increment,
        content text not null,
        score int not null,
        primary key(id)
    )
    """
    create_keys_table = """
    create table if not exists keyss(
        id int auto_increment,
        content text not null,
        primary key(id)
    )
    """
    create_users_table = """
    create table if not exists users(
        id int auto_increment,
        score int not null,
        content text not null,
        primary key(id)
    )
    """
    insert_question = "insert into questions(id, score, content) values (%s, %s, %s)"
    insert_key = "insert into keyss(id, content) values (%s, %s)"
    insert_user = "insert into users(id, score, content) values (%s, %s, %s)"

    select_user = "select * from users where id = %s"
    select_question = "select * from questions where id = %s"
    select_key = "select * from keyss where id = %s"

    def __init__(self, host_name: str, user_name: str, user_password: str, db_name: str):
        try:
            self.connection = connect(
                host=host_name,
                user=user_name,
                passwd=user_password,
                database=db_name
            )
            print("Connection to db is successful.")
        except Error as e:
            try:
                if "Unknown database" in e.__str__():
                    self.connection = connect(
                        host=host_name,
                        user=user_name,
                        passwd=user_password
                    )
                    self.execute_query(f"create database {db_name}")
            except Error as e:
                print(f"The error {e} occurred.")
        self.execute_query(Database.create_questions_table)
        self.execute_query(Database.create_users_table)
        self.execute_query(Database.create_keys_table)

    def execute_query(self, query, params=None):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, params)
            self.connection.commit()
            print("Query has been executed successfully.")
        except Error as e:
            print(f"The error {e} occurred.")

    def execute_read_query(self, query, params=None):
        cursor = self.connection.cursor()
        result = None
        try:
            cursor.execute(query, params)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"The error '{e}' occurred")

    def add_user(self, id: int, score: int, content: str):
        self.execute_query(Database.insert_user, (id, score, content))

    def add_question(self, id: int, score: int, content: str, key: str):
        self.execute_query(Database.insert_question, (id, score, content))
        self.execute_query(Database.insert_key, (id, key))

    def get_user(self, id: int):
        return self.execute_read_query(Database.select_user, (id, ))

    def get_question(self, id: int):
        return self.execute_read_query(Database.select_question, (id, ))

    def get_key(self, id: int):
        return self.execute_read_query(Database.select_key, (id, ))

# This is the creation of Database, "localhost" is the address of our sql. "mysql" and "mysql" are username and password
# "case_4" is name of database.
db = Database("localhost", "mysql", "mysql", "case_4")

# Adding of question to database
# 1 is id, 2 is score, "Question 1" is text of question, "no" is correct answer(key)
db.add_question(1, 2, "Question 1", "no")
db.add_question(2, 6, "Question 2", "yes")
db.add_question(3, 4, "Question 3", "no")

# Adding of question to database,
# 1 is id, 6 is current score, "{...}" is additional info, e.g. correct or wrong answers
db.add_user(1, 6, "{...}")

# Get question from database
question = db.get_question(1)
print(question)

question = db.get_question(1)
print(question)

question = db.get_question(1)
print(question)

# Get user from sql
user = db.get_question(1)
print(db.get_user(1))