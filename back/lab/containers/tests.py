from django.test import TestCase
from lab.containers import helpers 

class TestBarcodeGeneration(TestCase):
    serial = helpers.Barcode()
    
    def create_single_barcode(self):
        
        barcode = self.serial.get_one()
        print(barcode)
        self.assertEqual(len(barcode),10)
        
    def create_multiple_barcodes(self):
        number_of_barcodes = 20
        barcodes = self.serial.get_many(number_of_barcodes)
        # correct number of barcodes
        self.assertEqual(len(barcodes),number_of_barcodes)
        # all barcodes are unique
        self.assertEqual(len(barcodes),len(set(barcodes)))