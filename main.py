from models import Shelf, Palette, ProductCategory
import services
from models import Notification, Driver


print("=== Σύστημα Διαχείρισης Αποθήκης (UML-based) ===")
    
def main():
    print("=== ΡΥΘΜΙΣΗ ΣΥΣΤΗΜΑΤΟΣ ΔΙΑΧΕΙΡΙΣΗΣ ΑΠΟΘΗΚΗΣ ===")

    print("\n--- Ρύθμιση Κατηγορίας Προϊόντος ---")
    category_id = input("Δώστε ID Κατηγορίας (π.χ. C1): ")
    category_name = input("Δώστε Όνομα Κατηγορίας (π.χ. Electronics): ")
    product_inventory = input ("Δώσε απόθεμα προιόντος)") 
    cat_electronics = (category_id, category_name, product_inventory)


    print("\n--- Ρύθμιση Κύριου Ραφιού ---")
    shelf_id = int(input("Δώστε Barcode ID για το κύριο ράφι (π.χ. 101): "))
    shelf_inventory = int(input("Δώστε χωρητικότητα: "))
    shelf_a1 = Shelf(shelf_id, shelf_inventory)


    print("\n--- Ρύθμιση Εναλλακτικού Ραφιού ---")
    shelf_id = int(input("Δώστε Barcode ID για το εναλλακτικό ράφι (π.χ. 102): "))
    shelf_inventory = int(input("Δώστε χωρητικότητα: "))
    shelf_alt = Shelf(shelf_id, shelf_inventory)

    print("\n--- Ρύθμιση Προσωπικού & Συστήματος ---")
    driver_id= int(input("Δώστε ID Οδηγού: "))
    first_name= input("Δώστε Όνομα Οδηγού: ")
    last_name = input("Δώστε Επίθετο Οδηγού: ")
    driver = Driver(driver_id, first_name, last_name)
    
    n_id = int(input("Δώστε ID Συστήματος Ειδοποιήσεων (π.χ. 505): "))
    notif = Notification(n_id)

    print("\n" + "="*40)
    print("Η ΑΡΧΙΚΟΠΟΙΗΣΗ ΟΛΟΚΛΗΡΩΘΗΚΕ")
    print("="*40)

while True:
        barcode = input("\nΣκανάρετε Barcode παλέτας (ή 'exit' για τερματισμό): ")
        if barcode.lower() == 'exit':
            break

        new_palette = Palette(barcode, cat_electronics)

        # Βήμα 1: Έλεγχος στο shelf_a1 (check_fullness -> bool)
        if shelf_a1.check_fullness() == True:
            shelf_a1.add_palette_to_list(new_palette)
            msg = f"Η παλέτα {new_palette.barcode} τοποθετήθηκε στο {shelf_a1.shelf_name}. Counter: {shelf_a1.set_shelf_inventory}"
            services.notification_service_lib(notif, msg)
            
        # Βήμα 2: Αν το πρώτο είναι γεμάτο, έλεγχος στο shelf_alt (Alternative Fragment)
        elif shelf_alt.check_fullness() == True:
            print(f"Ειδοποίηση: Το {shelf_a1.shelf_name} είναι πλήρες.")
            shelf_alt.add_palette_to_list(new_palette)
            msg = f"Η παλέτα {new_palette.barcode} μεταφέρθηκε στο {shelf_alt.shelf_name}. Counter: {shelf_alt.set_shelf_inventory}"
            services.notification_service_lib(notif, msg)
            
        # Βήμα 3: Αν όλα είναι γεμάτα
        else:
            msg = f"ΣΦΑΛΜΑ: Όλα τα ράφια είναι γεμάτα! Ειδοποιήστε τον οδηγό {driver.name}."
            services.notification_service_lib(notif, msg)