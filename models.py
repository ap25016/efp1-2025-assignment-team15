from datetime import datetime

from enum import Enum, auto
class PaletteStatus(Enum):
    STANDBY = "standby"
    STORED = "stored"
    INTRANSIT = "in transit"

class ProductCategory:
    def __init__(self, category_id: str, name: str, inventory: int = 0):
        self.category_id = category_id
        self.category_name = name
        self.product_inventory = inventory

    def update_stock(self, amount: int):
        self.product_inventory += amount
        print(f"Απόθεμα κατηγορίας {self.category_name} ενημερώθηκε: {self.product_inventory}")

class Shelf:
    def __init__(self, shelf_id: int, capacity: int = 10):
        self.shelf_id = shelf_id
        self.shelf_inventory = 0
        self.capacity = capacity

    def check_fullness(self) -> bool:
        return self.shelf_inventory >= self.capacity

    def set_shelf_inventory(self, amount: int):
        self.shelf_inventory += amount
        print(f"Ράφι {self.shelf_id} περιεχόμενο: {self.shelf_inventory}/{self.capacity}")

class Palette:
    def __init__(self, barcode: str, category: ProductCategory):
        self.barcode = barcode
        self.category = category
        self.arrival_time = datetime.now()
        self.placement_time = None
        self.palette_status = PaletteStatus.STANDBY
        self.shelf = None

    def save_data(self, shelf: Shelf):
        self.shelf = shelf
        self.placement_time = datetime.now()
        self.palette_status = PaletteStatus.STORED
        print(f"Δεδομένα παλέτας {self.barcode} αποθηκεύτηκαν στη βάση.")

class Notification:
    def __init__(self, notification_id: int):
        self.notification_id = notification_id
        self.notification_time = datetime.now()
        self.palettes = []

    def add_palette_to_list(self, palette: Palette, shelf: Shelf):
        palette.shelf = shelf
        self.palettes.append(palette)

    def print_list(self):
        print(f"--- Λίστα Ειδοποίησης {self.notification_id} ---")
        for p in self.palettes:
            print(f"Παλέτα: {p.barcode} | Κατηγορία: {p.category.category_name} | Ράφι: {p.shelf.shelf_id}")

    def reassign_shelf(self, palette: Palette, new_shelf: Shelf):
        print(f"Εναλλακτική Ροή: Αλλαγή θέσης για την παλέτα {palette.barcode}")
        palette.shelf = new_shelf
        print(f"Νέο προτεινόμενο ράφι: {new_shelf.shelf_id}")

class Driver:
    def __init__(self, driver_id: int, first_name: str, last_name: str):
        self.driver_id = driver_id
        self.first_name = first_name

    def open_notification(self, notification: Notification):
        print(f"Ο οδηγός {self.first_name} άνοιξε την ειδοποίηση.")
        notification.print_list()

    def confirm_placement(self, palette: Palette, notification: Notification):
        if palette.shelf.check_fullness():
            print(f"Σφάλμα: Το ράφι {palette.shelf.shelf_id} είναι γεμάτο!")
            return False
        
        palette.save_data(palette.shelf)
        

        palette.category.update_stock(1)
        

        palette.shelf.set_shelf_inventory(1)
        
        print(f"Η τοποθέτηση της παλέτας {palette.barcode} ολοκληρώθηκε επιτυχώς.")
        return True

class Employee:
    def __init__(self, employee_id, first_name: str, last_name: str):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
    

