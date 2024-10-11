import psycopg2

def create_table():
    conn = psycopg2.connect(dbname="studentdb",user="postgres",password="admin9282",host="localhost",port="5432")
    cur = conn.cursor()
    cur.execute("create table students(student_id serial primary key,name text,address text,age int,number text)")
    print("Table created successfully")
    conn.commit()
    conn.close()

def insert_data():
    # code to accept data from the user
    name = input("Enter name: ")
    address = input("Enter address: ")
    age = input("Enter age: ")
    number = input("Enter number: ")
    conn = psycopg2.connect(dbname="studentdb", user="postgres", password="admin9282", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute("insert into students(name,address,age,number) values (%s,%s,%s,%s)",(name, address, age, number))
    print("Data inserted successfully")
    conn.commit()
    conn.close()

def read_data():
    conn = psycopg2.connect(dbname="studentdb", user="postgres", password="admin9282", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute("SELECT * FROM students;")
    students = cur.fetchall()
    print("Displaying all student records:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, Address: {student[2]}, Age: {student[3]}, Phone Number: {student[4]}")
    conn.close()

def update_data():
    student_id = input("Enter the ID of the student to be updated: ")

    # Connect to the database
    conn = psycopg2.connect(dbname="studentdb", user="postgres", password="admin9282", host="localhost", port="5432")
    cur = conn.cursor()

    # Available fields to update
    # Field name and prompt
    fields = {
        "1": ("name", "Enter the new name: "),
        "2": ("address", "Enter the new address: "),
        "3": ("age", "Enter the new age: "),
        "4": ("number", "Enter the new phone number: ")
    }

    print("Which field would you like to update")
    # Loop through all the fields
    for key in fields:
        # Print the field name
        print(f"{key}: {fields[key][0]}")
    # Accept the choice from user
    field_choice = input("Enter the number of the field you want to update: ")

    # If the choice is present, then get the field name i.e name age to be updated
    # on the basis of above choice
    if field_choice in fields:
        field_name, prompt = fields[field_choice]
        # prompt. the user to enter the new value for field
        new_value = input(prompt)

        # Constructing and executing the SQL update statement
        sql = f"UPDATE students SET {field_name} = %s WHERE student_id = %s"
        cur.execute(sql, (new_value, student_id))

        print(f"{field_name} updated successfully.")
    else:
        print("Invalid choice.")

    # Commit changes and close the connection
    conn.commit()
    conn.close()

def delete_data():
    # Prompt the user for the ID of the student to be deleted
    student_id = input("Enter the ID of the student to be deleted: ")

    # Connect to the database
    conn = psycopg2.connect(dbname="studentdb", user="postgres", password="admin9282", host="localhost", port="5432")
    cur = conn.cursor()

    # Check if the student exists
    cur.execute("SELECT * FROM students WHERE student_id = %s", (student_id,))
    student = cur.fetchone()

    if student:
        # Show details of the student to be deleted
        print(
            f"Student to be deleted: ID: {student[0]}, Name: {student[1]}, Address: {student[2]}, Age: {student[3]}, Phone Number: {student[4]}")

        # Ask for confirmation
        confirmation = input("Are you sure you want to delete this student? (yes/no): ")
        if confirmation.lower() == 'yes':
            # Perform the deletion
            cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
            print("Student record deleted.")
        else:
            print("Deletion cancelled.")
    else:
        print("Student not found.")

    # Commit changes and close the connection
    conn.commit()
    conn.close()


while True:
    print("\\nWelcome to the Student Management System")
    print("1. Create Table")
    print("2. Insert Data")
    print("3. Read Data")
    print("4. Update Data")
    print("5. Delete Data")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        create_table()
    elif choice == '2':
        insert_data()
    elif choice == '3':
        read_data()
    elif choice == '4':
        update_data()
    elif choice == '5':
        delete_data()
    elif choice == '6':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
