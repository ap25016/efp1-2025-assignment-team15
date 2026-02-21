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

        self._next_driver_id = 201 # Internal counter for driver IDs
        self._next_notification_id = 401 # Internal counter for notification IDs
        self._next_shelf_id = 301 # Internal counter for shelf IDs
        self._next_employee_id = 101 # Internal counter for employee IDs
        #Όπως στο μάθημα

        self._seed_demo_data() 
        

     def _seed_demo_data(self) -> None:
         """Δημιουργεί έτοιμα δεδομένα για τις δοκιμές."""
         self.add_employee(101, Μαρία, Παπαδοπούλου) #Όπως στο σενάριο στο README
         self.add_driver(201, Δημήτρης, Νικολάου) #Όπως στο σενάριο στο README
         Ηλεκτρονικά = self.add_category("CAT-001", "Ηλεκτρονικά", 2)
         self.add_palette("2345678901", Ηλεκτρονικά)
         self.add_palette("3456789012", Ηλεκτρονικά)

     def add_employee(self, employee_id: int, first_name: str, last_name: str) -> Employee:
        employee = Employee(employee_id, first_name, last_name)
        self.employees.append(employee) # Πρόσθεση υπαλλήλου στη λίστα
        self._next_employee_id += 1 
        return employee

     def add_driver(self, driver_id: int, first_name: str, last_name: str) -> Driver:
        driver = Driver(self._next_driver_id, first_name, last_name)
        self.drivers.append(driver) # Πρόσθεση οδηγού στη λίστα
        self._next_driver_id += 1 
        return driver

     def add_category(self, category_id: str, category_name: str, product_inventory: int) -> ProductCategory:
        category = ProductCategory(category_id, category_name, product_inventory)
        self.categories.append(category) # Πρόσθεση κατηγορίας στη λίστα
        return category

     def add_palette(self, barcode: str, category: ProductCategory) -> Palette:
        palette = Palette(barcode, category)
        self.palettes.append(palette) # Πρόσθεση παλέτας στη λίστα
        return palette

     """def add_palette(self, title: str, date: str, time: str, capacity: int) -> ClassSession:
        session = ClassSession(self._next_session_id, title, date, time, capacity)
        self.sessions.append(session) # Add session to the list
        self._next_session_id += 1 # Increment session ID for next session
        return session"""

     """def add_palette(self, title: str, date: str, time: str, capacity: int) -> ClassSession:
        session = ClassSession(self._next_session_id, title, date, time, capacity)
        self.sessions.append(session) # Add session to the list
        self._next_session_id += 1 # Increment session ID for next session
        return session"""

     def find_employee(self, employee_id: int, first_name: str, last_name: str) -> Employee | None:
        for e in self.employees:
            if (e.employee_id == employee_id and 
                e.first_name == first_name and 
                e.last_name == last_name): #Match found!
                return e
        return None # No match found

     def find_driver(self, driver_id: int, first_name: str, last_name: str) -> Driver | None:
        for d in self.drivers:
            if (d.driver_id == driver_id and 
                d.first_name == first_name and 
                d.last_name == last_name): #Match found!
                return d
        return None # No match found

   
