# Importing the necessary module for MySQL connectivity
import mysql.connector as sql

# Establishing a connection to the MySQL database
conn = sql.connect(host='localhost', user='root', passwd='root', database='grocery_shop')

# Checking if the connection is successful
if conn.is_connected():
    print('Successfully connected')
    c = conn.cursor()  # Creating a cursor for executing SQL queries

    # Main menu for the Grocery Shop Management System
    print('Grocery Shop Management System')
    print('1. Login')
    print('2. Exit')
    choice = int(input('Enter your choice: '))

    if choice == 1:
        # User authentication
        user_name = input('Enter your user name: ')
        password = input('Enter your password: ')

        while user_name == 'abc' and password == '1234':
            print('Connected successfully')
            print('Grocery Shop')
            
            # Sub-menu for various operations
            print('1. Customer details')
            print('2. Product details')
            print('3. Worker details')
            print('4. See all customer details')
            print('5. See all product details')
            print('6. See all worker details')
            print('7. See one customer details')
            print('8. See one product details')
            print('9. See one worker details')
            print('10. Exit')
            
            choice = int(input('Enter the choice: '))

            # Adding a new customer record to the database
            if choice == 1:
                cust_name = input('Enter your name: ')
                phone_no = int(input('Enter your phone number: '))
                cost = float(input('Enter your cost: '))
                sql_insert = "INSERT INTO customer_details VALUES ({}, '{}', {})".format(phone_no, cust_name, cost)
                c.execute(sql_insert)
                conn.commit()
                print('Data is updated')

            # Adding a new product record to the database
            elif choice == 2:
                product_name = input('Enter product name: ')
                product_cost = float(input('Enter the cost: '))
                sql_insert = "INSERT INTO product_details VALUES ('{}', {})".format(product_name, product_cost)
                c.execute(sql_insert)
                conn.commit()
                print('Data is updated')

            # Adding a new worker record to the database
            elif choice == 3:
                worker_name = input('Enter your name: ')
                worker_work = input('Enter your work: ')
                worker_age = int(input('Enter your age: '))
                worker_salary = float(input('Enter your salary: '))
                phone_no = int(input('Enter your phone number: '))
                sql_insert = "INSERT INTO worker_details VALUES ('{}', '{}', {}, {}, {})".format(
                    worker_name, worker_work, worker_age, worker_salary, phone_no)
                c.execute(sql_insert)
                conn.commit()
                print('Data is updated')

            # Viewing all customer details
            elif choice == 4:
                t = conn.cursor()
                t.execute('SELECT * FROM customer_details')
                record = t.fetchall()
                print("\nCustomer Details are as follows:")
                print("Phone \t Name \t Cost")
                for i in record:
                    print("{} \t {} \t {}".format(i[0], i[1], i[2]))
                print()

            # Viewing all product details
            elif choice == 5:
                t = conn.cursor()
                t.execute('SELECT * FROM product_details')
                record = t.fetchall()
                print("\nProduct Details are as follows:")
                print("Name \t Cost")
                for i in record:
                    print("{} \t {}".format(i[0], i[1]))
                print()
                
            # Viewing all worker details
            elif choice == 6:
                t = conn.cursor()
                t.execute('SELECT * FROM worker_details')
                record = t.fetchall()
                print("\nWorker Details are as follows:")
                print("Name \t Work \t Age \t Salary \t Phone")
                for i in record:
                    print("{} \t {} \t {} \t {} \t {}".format(i[0], i[1], i[2], i[3], i[4]))
                print()

            # Viewing details of a specific customer
            elif choice == 7:
                a = input('Enter customer name: ')
                t = 'SELECT * FROM customer_details WHERE cust_name = "{}"'.format(a)
                c.execute(t)
                v = c.fetchall()
                print("\nCustomer Details are as follows:")
                print("Phone \t Name \t Cost")
                for i in v:
                    print("{} \t {} \t {}".format(i[0], i[1], i[2]))
                if len(v) == 0:
                    print("No record found with name {}".format(a))
                print()

            # Viewing details of a specific product
            elif choice == 8:
                a = input('Enter product name: ')
                t = 'SELECT * FROM product_details WHERE product_name = "{}"'.format(a)
                c.execute(t)
                v = c.fetchall()
                print("\nProduct Details are as follows:")
                print("Name \t Cost")
                for i in v:
                    print("{} \t {}".format(i[0], i[1]))
                if len(v) == 0:
                    print("No record found with name {}".format(a))
                print()

            # Viewing details of a specific worker
            elif choice == 9:
                a = input('Enter worker name: ')
                t = 'SELECT * FROM worker_details WHERE worker_name = "{}"'.format(a)
                c.execute(t)
                v = c.fetchall()
                print("\nWorker Details are as follows:")
                print("Name \t Work \t Age \t Salary \t Phone")
                for i in v:
                    print("{} \t {} \t {} \t {} \t {}".format(i[0], i[1], i[2], i[3], i[4]))
                if len(v) == 0:
                    print("No record found with name {}".format(a))
                print()

            elif choice == 10:
                exit()

            else:
                print('Invalid choice, try again')

    elif choice == 2:
        exit()
