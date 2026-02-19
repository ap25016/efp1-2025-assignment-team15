def external_validator_lib(barcode: str):
    """Προσομοίωση εξωτερικής βιβλιοθήκης ελέγχου barcode"""
    return len(barcode) > 0
def notification_service_lib(notif_obj, message: str):
    """Προσομοίωση εξωτερικής βιβλιοθήκης ειδοποιήσεων"""
    print(f"\n>>> [NOTIF-ID: {notif_obj.notif_id}] {message}")
