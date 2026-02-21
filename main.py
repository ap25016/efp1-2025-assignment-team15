from services import WarehouseSystem

def main():
    system = WarehouseSystem()
    print("Καλωσήρθατε στο σύστημα διαχείρισης της αποθήκης!")
   
    while True:
        print("\n--- Παρακαλώ επιλέξτε ---")
        print("1. Μενού Υπαλλήλου Παραλαβης")
        print("2. Μενού Οδηγού")
        print("0. Έξοδος")

        choice = input("Επιλογή: ")
        #ΤΟ USE CASE 1 ΞΕΚΙΝΑΕΙ ΑΠΟ ΕΔΩ
        if choice == "1":
            print("Παρακαλώ εισάγετε τα στοιχεια σας:")
            employee_id = input("ID Υπαλλήλου: ")
            first_name = input("Όνομα: ")
            last_name = input("Επώνυμο: ")

            employee = system.find_employee(employee_id, first_name, last_name)
            if employee is None:
                print("Τα στοιχεία δεν αναγνωρίζονται")
                continue  
            else:
                print("Επιτυχής Σύνδεση!")




        #ΤΟ USE CASE 2 ΞΕΚΙΝΑΕΙ ΑΠΟ ΕΔΩ
        elif choice == "2":
            print("Παρακαλώ εισάγετε τα στοιχεια σας:")
            driver_id = input("ID Οδηγού: ") 
            first_name = input("Όνομα: ") 
            last_name = input("Επώνυμο: ") 

            driver = system.find_driver(driver_id, first_name, last_name)
            if driver is None:
                print("Τα στοιχεία δεν αναγνωρίζονται")
                continue  
            else:
                print("Επιτυχής Σύνδεση!")

        
        elif choice == "0":
            print("Πραγματοποιειται έξοδος από το σύστημα. Αντίο!")
            break

        else:
            print("Μη έγκυρη επιλογή.")

