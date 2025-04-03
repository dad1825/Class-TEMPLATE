"""
Description:
    This class is the Utility class for both of the repair order and sql classes.
    functions in this class contain both properties from each and therefore
    needed to go in a different python file.
"""
from repairOrderClass import RepairOrder
from SqliteConnector import SqliteConnector


class Utility(object):

    def __init__(self):
        pass

    @classmethod
    def start_of_program(cls):
        SqliteConnector.create_table()
        # print("Debug: Checking for a created table")
        x = 0
        while x <= 0:
            print("---------------------Main Menu---------------------\n")
            interface_choices = ["1 : Enter a Repair Order ",
                                 "2 : View all Repair orders ",
                                 "3 : View Reports by month",
                                 "4 : Delete entry",
                                 "5 : Totals",
                                 "6 : Export DB",
                                 # "8 : Testing",
                                 "9 : Quit"]
            for i in interface_choices:
                print(i)
            start_of_choices = input("\nPlease make a selection, and press Enter: \n")
            if start_of_choices == "1":
                Utility.insert_ro()
            if start_of_choices == "2":
                Utility.view_ro_history()
            if start_of_choices == "3":
                Utility.view_ro_by_month()
            if start_of_choices == "4":
                Utility.delete_ro()
            if start_of_choices == "5":
                Utility.get_totals()
            if start_of_choices == "6":
                Utility.export_db()
            # Uncomment for testing and adding a new module.
            '''    
            if start_of_choices == "8":
                pass
            '''
            if start_of_choices == "9":
                x = 1
                SqliteConnector.close_cursor()
                # repairorder.close_cursor()
                print("Goodbye")
            # print("Debug: Main loop running")

    @classmethod
    def insert_repairorder(cls):
        # print("Debug: Insert Repair order Called")
        # Take input for the constructor.
        date = input("Enter the date yyyy-mm-dd : ")
        gross = input("Enter the gross '0.00' : ")
        our_cut = input("Enter the 43% '0.00' : ")
        workers_comp = input("Enter the WA '0.00' :  ")
        misc = input("Enter any misc charges '0.00' : ")
        total = input("Enter the total '0.00' : ")
        notes = input("Enter any Notes, up to 300 char : ")
        # Populate repair order instance.
        repairOrder = RepairOrder(date, gross, our_cut, workers_comp, misc, total, notes)
        # Call repr for conformation.
        print("\n")
        print(repairorder.__repr__)
        confirm = input("\nInsert this new Repair Order?\n0 = Yes\n1 = Reenter\n2 = Return to Main Menu:\n ")
        if confirm == "0":
            try:
                insert_command = """INSERT INTO repairorders(date, gross, our_cut,
                                            workers_comp, misc, total, notes)
                                            VALUES(?, ?, ?, ?, ?, ?, ?) """
                insert_values = [repairorder.date, repairorder.gross, repairorder.our_cut,
                                 repairorder.workers_comp, repairorder.misc, repairorder.total,
                                 repairorder.notes]
                SqliteConnector.cursor.execute(insert_command, insert_values)
                SqliteConnector.commit_cursor()
                print("\nrepairorder entered successfully!!!")
            # except mysql.connector.errors.DataError:
            except:
                print("\nPlease enter data with appropriate format\nDate YYYY-MM-DD\nNumeric Values 0.00\n")
                Utility.insert_repairorder()
        elif confirm == "1":
            Utility.insert_repairorder()
        else:
            pass
        # print("Debug: Inserted")

    @classmethod
    def view_repairorder_history(cls):
        Utility.repairorder_summary(SqliteConnector.select_all_from_table)

    @classmethod
    def view_repairorder_by_month(cls):
        month = input("Enter the two digit month to filter repairorders by month: ")
        insert_command = "select * from repairorders where date like '%2019-" + month + "%';"
        Utility.repairorder_summary(insert_command)

    @classmethod
    def delete_repairorder(cls):
        insert_command = SqliteConnector.select_all_from_table
        Utility.repairorder_summary(insert_command)
        entry_to_delete = input("Enter a date to delete the entry: ")
        try:
            commands = "DELETE FROM repairorders WHERE Date = \"" + entry_to_delete + "\";"
            SqliteConnector.simple_query(commands)
            insert_command = SqliteConnector.select_all_from_table
            Utility.repairorder_summary(insert_command)
            SqliteConnector.commit_cursor()
        # Bare exception used for the time being.
        except:
            print("Unknown Error")
            Utility.start_of_program()

    @classmethod
    def get_totals(cls):
        x = 0
        while x <= 0:
            interface_choices = ["1 : Year to date Totals ",
                                 "2 : Year to date Averages",
                                 "3 : Monthly Totals",
                                 "4 : Monthly Averages",
                                 "9 : Quit"]
            for i in interface_choices:
                print(i)
            start_of_choices = input("\nPlease make a selection, and press Enter: \n")
            if start_of_choices == "1":
                insert_command = "select round(sum(gross),2), round(sum(our_cut),2), " \
                                 "round(sum(total),2) from repairorders where date like '%2019%';"
                SqliteConnector.cursor.execute(insert_command)
                db_response = SqliteConnector.cursor.fetchall()
                for i in db_response:
                    print("---------------------------------------------------")
                    print("\nGross total : \n$" + str(i[0]))
                    print("\n")
                    print("Our Taxable income : \n$" + str(i[1]))
                    print("\n")
                    print("Total deposited in the bank : \n$" + str(i[2]))
                    print("\n")
                    print("---------------------------------------------------")
            if start_of_choices == "2":
                insert_command = "select round(avg(gross),2), round(avg(our_cut),2), " \
                                 "round(avg(total),2) from repairorders where date like '%2019%';"
                SqliteConnector.cursor.execute(insert_command)
                db_response = SqliteConnector.cursor.fetchall()
                for i in db_response:
                    print("---------------------------------------------------")
                    print("\nGross total : \n$" + str(i[0]))
                    print("\n")
                    print("Our Taxable income : \n$" + str(i[1]))
                    print("\n")
                    print("Total deposited in the bank : \n$" + str(i[2]))
                    print("\n")
                    print("---------------------------------------------------")
            if start_of_choices == "3":
                month = input("Enter the two digit month to filter repairorders by month: ")
                insert_command = "select round(sum(gross),2), round(sum(our_cut),2), " \
                                 "round(sum(total),2) from repairorders where date like '%2019-" + month + "%';"
                SqliteConnector.cursor.execute(insert_command)
                db_response = SqliteConnector.cursor.fetchall()
                for i in db_response:
                    print("---------------------------------------------------")
                    print("\nGross total : \n$" + str(i[0]))
                    print("\n")
                    print("Our Taxable income : \n$" + str(i[1]))
                    print("\n")
                    print("Total deposited in the bank : \n$" + str(i[2]))
                    print("\n")
                    print("---------------------------------------------------")
                    pass
            if start_of_choices == "4":
                month = input("Enter the two digit month to filter repairorders by month: ")
                insert_command = "select round(avg(gross),2), round(avg(our_cut),2), " \
                                 "round(avg(total),2) from repairorders where date like '%2019-" + month + "%';"
                SqliteConnector.cursor.execute(insert_command)
                db_response = SqliteConnector.cursor.fetchall()
                for i in db_response:
                    print("---------------------------------------------------")
                    print("\nGross AVG : \n$" + str(i[0]))
                    print("\n")
                    print("Our Taxable income : \n$" + str(i[1]))
                    print("\n")
                    print("AVG deposited in the bank : \n$" + str(i[2]))
                    print("\n")
                    print("---------------------------------------------------")
                    pass
            if start_of_choices == "9":
                x = 1

    @classmethod
    def repairorder_summary(cls, insert_command):
        SqliteConnector.cursor.execute(insert_command)
        repairorder_history = SqliteConnector.cursor.fetchall()
        # print("The total number of repairorders are : ", repairorder.cursor.rowcount)
        print("____________________________________________\n")
        for i in repairorder_history:
            # print("|ID :     ", i[8])
            print("|Date :   ", i[0])
            print("|Gross :  ", i[1])
            print("|40% :    ", i[2])
            print("|WA :     ", i[3])
            print("|Misc :   ", i[4])
            print("|Total :  ", i[5])
            print("________________________\n")

    @classmethod
    def export_db(cls):
        with open('repairorders.csv', 'w+') as write_file:
            write_file.write("|     Date    | Gross |Our Cut|  WA   |  Misc |Total: | Notes:\n")
            for row in SqliteConnector.cursor.execute('SELECT * FROM repairorders'):
                write_file.write(str(row) + "\n")
