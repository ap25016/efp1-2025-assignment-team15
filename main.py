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

                while True:
                        storage_notifs = len(system.notifications) #η len μας δινει τον αριθμο των ειδοποιησεων
                        print(f"\nΕιδοποιήσεις Αποθήκευσης: {storage_notifs}") #ποσες ειδοποιησεις υπαρχουν
                        print("Ειδοποιήσεις Παραγγελιών: 0") #αλλο use case
                        print("Επιλέξτε Ενέργεια:")
                        print("1. Αποθήκευση Προϊόντων")
                        print("2. Εκτέλεση Παραγγελίας")
                        print("0. Έξοδος")
                        choice = input("Επιλογή: ")
                        
                        if choice == "1":
                            if storage_notifs == 0:
                                print("\nΔεν υπάρχουν παλέτες σε εκκρεμότητα!")
                                continue
                            new_notif = system.notifications[0] #αυτο μας δινει τη πρωτη ειδοποιηση που υπαρχει στο συστημα
                            
                            while new_notif.palettes: #αυτο κανει loop τη διαδικασια για όσο υπάρχουν παλέτες μέσα στην ειδοποίηση
                                print(f"\n{new_notif.notification_time.strftime('%H:%M:%S, %d-%m-%Y')}")
                                print("Προϊόντα προς Αποθήκευση:")
                                
                                for idx, p in enumerate(new_notif.palettes, 1): #αυτο δειχνει τη λιστα με τις παλετες απο την ειδοποιηση
                                    print(f"{idx}. Παλέτα: {p.barcode}, Κατηγορία: {p.category.category_name} "
                                          f"(ID: {p.category.category_id}), Κωδικός Ραφιού: {p.shelf.shelf_id}")
                                          
                                p_choice = input("Παρακαλώ επιλέξτε παλέτα για αποθήκευση: ")
                                try:
                                    p_idx = int(p_choice) - 1
                                    selected_palette = new_notif.palettes[p_idx]
                                    success = driver.confirm_placement(selected_palette, new_notif) #αυτο εκτελει την αποθηκευση των δεδομενων των παλετων και την ενημερωση του αποθεματος
                                    if success:
                                        new_notif.palettes.pop(p_idx) #αυτο αφαιρει τη παλετα απο τη λιστα
                                except (ValueError, IndexError):
                                    print("Μη έγκυρη επιλογή.")
                            print("\nΔεν υπάρχουν παλέτες σε εκκρεμότητα!") 
                            system.notifications.pop(0) #αυτο αφαιρει την ειδοποιηση απο το συστημα οταν δεν υπαρχουν αλλες παλετες σε αυτη
                            print("Γίνεται επιστροφή στο αρχικό μενού...")
                            break
                        
                        elif choice == "2":
                            print("\nΔεν υπάρχουν εκκρεμείς παραγγελίες!")
                        elif choice == "0":
                            print("\nΑντίο!")
                            break

        
        elif choice == "0":
            print("\nΠραγματοποιειται έξοδος από το σύστημα. Αντίο!")
            break

        else:
            print("\nΜη έγκυρη επιλογή.")


if __name__ == "__main__":
    main()

