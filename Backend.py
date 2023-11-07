# To run this program, make sure to have mysql.conector module installed in your environment
# To install it, run the command "pip install mysql.connector" in your terminal
import mysql.connector

class Backend:
    create_table_sql = "CREATE TABLE IF NOT EXISTS employees ( Id INT AUTO_INCREMENT PRIMARY KEY,firstname VARCHAR(30),lastname VARCHAR(30),employeeRank VARCHAR(12),email VARCHAR(30),password VARCHAR(30))"
    db_args = {
        "host" : 'localhost',
        "port" : "3306",     
        "user" : 'root',
        "passwd" : 'your_password', #Replace this with your own password
    }

    # Functin to create the database
    def create_database(self, name):
        connection = mysql.connector.connect(**self.db_args)
        # Creating a cursor object to interact with the database
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {name}")
        connection.close()


    def __init__(self, database_name):
        self.create_database(database_name)
        self.db_args["database"] = database_name
        # Establishing a connection to the created database
        self.connection = mysql.connector.connect(**self.db_args)
        self.my_cursor = self.connection.cursor()
        
        # Executing the SQL statement to create the employee table
        self.my_cursor.execute(self.create_table_sql)
        # Applying the changes
        self.connection.commit()
    

    # Creating a new employee
    def create_employee(self,firstname, lastname, rank, email, password):
        try:
            self.my_cursor.execute("INSERT INTO employees (firstname, lastname, employeeRank, email, password) VALUES (%s,%s,%s,%s,%s)",(firstname,lastname,rank,email,password))
            self.connection.commit()
        except mysql.connector.Error as error:
            print(f"An error occured while attempting to create the employee {error}")

    # Fetching all employees
    def fetch_all_employees(self):
        try:
            self.my_cursor.execute("SELECT * FROM employees") # Fetching all employees from the database
            employees = []
            for x in self.my_cursor:
                employee = {
                    'Id': x[0],
                    'firstname': x[1],
                    'lastname': x[2],
                    'rank': x[3],
                    'email': x[4],
                    'password': x[5]
                }
                employees.append(employee) #Adding the employee objects to an iterable list
            return employees
        except mysql.connector.Error as error:
            print(f"Couldn't fetch employees {error}")

    # Removing and employee
    def remove_employee(self,id):
        try:
            
            self.my_cursor.execute("DELETE FROM employees WHERE Id = %s", (id,)) # Executing a DELETE statement to remove the employee with the specified 'id'
            self.connection.commit()#Saving the changes to the database
            print(f"Employee with ID {id} removed successfully.")
        except mysql.connector.Error as error:
            print(f"Error while removing employee with ID {id}: {error}")

    # Promoting an employee
    def promote_employee(self,id,new_rank):
        try:
            
            self.my_cursor.execute("UPDATE employees SET employeeRank = %s WHERE Id = %s", (new_rank, id,))# Executing an UPDATE statement to change the employee's rank
            self.connection.commit() #Saving the changes to the database
            print(f"Employee with ID {id} has been promoted to {new_rank}.")
        except mysql.connector.Error as error:
            print(f"Error while promoting employee with ID {id}: {error}")

if __name__ == "__main__":
    backend = Backend("example_database") # Instatiating the Backend class.Passing the database name as a parameter to the class
    
    backend.create_employee("Brian","Were","Supervisor","bryanwere174@gmail.com","password") # Creating an employee.Pass credentials to the function

# Fetching employees from database
    employees = backend.fetch_all_employees()
    for x in employees:
        print(x)

    backend.promote_employee(1,"Admin")  # To promote an amployee,pass the empoyee Id and the new rank

    backend.remove_employee(1) # Pass the employee Id to delete them
