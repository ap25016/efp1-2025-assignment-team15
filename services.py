from models import Shelf, Palette, ProductCategory, Notification, Driver

class WarehouseSystem:
     def __init__(self):
        self.categories: list[ProductCategory] = [] # Λίστα για αποθήκευση κατηγοριών προιόντων
        self.shelves: list[Shelf] = [] # Λίστα για αποθήκευση ραφιών
        self.palettes: list[Palette] = [] # Λίστα για αποθήκευση παλετών
        self.palette_statuses: list[PaletteStatus] = [] # Λίστα για αποθήκευση καταστάσεων παλετών
        self.drivers: list[Driver] = [] # Λίστα για αποθήκευση οδηγών
        self.employees: list[Employee] = [] # Λίστα για αποθήκευση υπαλλήλων
        #Just in case

        self._next_driver_id = 1 # Internal counter for driver IDs
        self._next_notification_id = 1 # Internal counter for notification IDs
        self._next_shelf_id = 1 # Internal counter for shelf IDs
        self._next_employee_id = 1 # Internal counter for employee IDs
        #Όπως στο μάθημα

        self._seed_demo_data() 

   
