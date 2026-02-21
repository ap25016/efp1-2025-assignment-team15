from services import WarehouseSystem
from datetime import datetime
now = datetime.now().strftime("%H:%M:%S, %d-%m-%Y")

def main():
    system = WarehouseSystem()
    print("Καλωσήρθατε στο σύστημα διαχείρισης της αποθήκης!")
   
    while True:
        print("\n--- Παρακαλώ επιλέξτε ---")
        print("1. Μενού Υπαλλήλου Παραλαβης")
        print("2. Μενού Οδηγού")
        print("0. Έξοδος")

        choice = input("Επιλογή: ")
        #~-~-~-~-~-~-~-~-~-~-~-~-~-~-ΤΟ USE CASE 1 ΞΕΚΙΝΑΕΙ ΑΠΟ ΕΔΩ-~-~-~-~-~-~-~-~-~-~-~-~-~-~#
        if choice == "1":
            print("\nΠαρακαλώ εισάγετε τα στοιχεια σας:")
            try:
                employee_id = int(input("ID Υπαλλήλου: "))
            except ValueError:
                print("\nΜη έγκυρο ID!")
                continue
            first_name = input("Όνομα: ")
            last_name = input("Επώνυμο: ")

            employee = system.find_employee(employee_id, first_name, last_name)
            if employee is None:
                print("\nΤα στοιχεία δεν αναγνωρίζονται!")
                continue  
            else:
                print("\nΕπιτυχής Σύνδεση!")

                while True:
                 print("\nΕπιλέξτε Ενέργεια:")
                 print("1. Νέα Παραλαβή")
                 print("2. Διαχείριση Φθοράς")
                 print("0. Έξοδος")
                 choice = input("Επιλογή: ")

                 if choice == "1":
                    new_palettes = [] # Οι παλέτες που σαρώνονται θα μπουν σε μία λίστα για την μετέπειτα αποθήκευσή τους
                    while True:
                        print("\nΝέα Παραλαβή:")
                        print("1. Σάρωση Barcode")
                        print("2. Χειροκίνητη Καταχώρηση")
                        print("3. Ολοκλήρωση Παραλαβης")
                        recept_choice = input("Επιλογή: ")

                        if recept_choice == "1":
                            print("\nΤεχνικό Σφάλμα!")

                        elif recept_choice == "2":
                            print("\nΠαρακαλώ εισάγετε τα ακόλουθα στοιχεία: ")
                            barcode = input("Barcode: ")
                            category_name = input("Κατηγορία Προιόντος: ")
                            category_name = system.find_category_by_name(category_name) #Το συστημα επιβεβαιώνει ότι η κατηγορία υπάρχει
                            if category_name:
                                new_palette = system.add_palette(barcode, category_name) #Η παλέτα καταχωρειται στο σύστημα και αυτόματα παίρνει αρχικό status=standby
                                new_palettes.append(new_palette) #Η παλέτα που μόλις σαρώθηκε μπαίνει στη λίστα για τη μετέπειτα αποθήκευση
                                print(f"\nΗ καταχώρηση της παλέτας {barcode} έγινε με επιτυχία!")
                            else:
                                print(f"\nΗ κατηγορία δεν βρέθηκε!")
                        
                        elif recept_choice == "3":
                            if not new_palettes: # αν δεν σαρώθηκε καμία παλέτα (και έτσι η λιστα είναι άδεια)...
                                break #...τότε δεν γίνεται τίποτα
                            notification = system.add_notification() #αλλιώς, δημιουργείται η ειδοποίηση για την αποθήκευση!
                            for np in new_palettes:
                                shelf = system.get_available_shelf() #το σύστημα βρίσκει διαθέσιμο ράφι
                                if shelf: #αν βρεθεί διαθέσιμο ράφι από το σύστημα
                                    notification.add_palette_to_list(np, shelf) #τότε η ειδοποίηση το συνδέει με τις παλέτες προς αποθήκευση
                                else:
                                    print(f"\nΔεν βρέθηκε διαθέσιμο ράφι!")
                            print("\nΕπιτυχής ολοκλήρωση παραλαβής!")
                            print(f"Η παραλαβη ολοκληρώθηκε στις {now}.")
                            break

                 elif choice == "2":
                    print("\nΛυπούμαστε, η συγκεκριμένη λειτουργία του συστήματος δεν έχει ολοκληρωθεί ακόμα!")

                 elif choice == "0":
                    print("\nΑντίο!")
                    break
                 else:
                    print("\nΜη έγκυρη επιλογή.")



        #~-~-~-~-~-~-~-~-~-~-~-~-~-~-ΤΟ USE CASE 2 ΞΕΚΙΝΑΕΙ ΑΠΟ ΕΔΩ-~-~-~-~-~-~-~-~-~-~-~-~-~-~#
        elif choice == "2":
            print("\nΠαρακαλώ εισάγετε τα στοιχεια σας:")
            try:
                driver_id = int(input("ID Οδηγού: "))
            except ValueError:
                print("\nΜη έγκυρο ID!")
                continue
            first_name = input("Όνομα: ") 
            last_name = input("Επώνυμο: ") 

            driver = system.find_driver(driver_id, first_name, last_name)
            if driver is None:
                print("\nΤα στοιχεία δεν αναγνωρίζονται!")
                continue  
            else:
                print("\nΕπιτυχής Σύνδεση!")

        
        elif choice == "0":
            print("\nΠραγματοποιειται έξοδος από το σύστημα. Αντίο!")
            break

        else:
            print("\nΜη έγκυρη επιλογή.")


if __name__ == "__main__":
    main()