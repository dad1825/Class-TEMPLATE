"""
Author: DadOfReno - Dad1825@outlook.com
Description:
    This is the main.py file for the repair order tracker.
    Associated Files:
        Utility.py
        SqliteConnector.py
        MysqlConnector.py
        repairOrderClass.py
        repairorder.db
        READ ME.txt
"""
from Utility import Utility

if __name__ == '__main__':

    print("\n_________________Repair Order Tracker____________v 1.0a")
    print("""
                        _____________________________________________________
                      |     _       ____              ____                  |
             _______  |    | |     |  _ \ _ __ ___   |  _ \ ___             |
            / _____ | | _  | |_____| |_) | '__/ _ \  | |_) / _ \            |
           / /     || || |_| |_____|  __/| | | (_) | |  _ < (_) |           |
  ________/ /      || | \___/      |_|   |_|  \___/  |_|_\_\___/            |
 |         |-------|| |                                                     |
(|         |     -.|| |_______________________                              |
 |  ____   \       ||_________||____________  |             ____      ____  |
/| / __ \   |______||     / __ \   / __ \   | |            / __ \    / __ \ |\
\|| /  \ |_______________| /  \ |_| /  \ |__| |___________| /  \ |__| /  \|_|/
   | () |                 | () |   | () |                  | () |    | () |
    \__/                   \__/     \__/                    \__/      \__/
  \n""")

    Utility.start_of_program()
