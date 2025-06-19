import threading

class Barcode:
    LENGTH = 10
    
    def __init__(self, start_number=1):
        self.serial = start_number
        self.lock = threading.Lock()        

    def get_one(self):        
        self.serial += 1
        padded_serial = f'{self.serial:0{Barcode.LENGTH}d}'
        return padded_serial
    
    def get_many(self, count:int) -> list:
        barcodes = []
        with self.lock:            
            for i in range(count):
                barcodes.append(self.get_one())
        return barcodes