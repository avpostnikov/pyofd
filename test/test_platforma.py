# -*- coding: utf-8 -*-

import unittest
import pyofd.providers.platforma
import pyofd

class PlatformaTest(unittest.TestCase):
    valid_receipt_items = [
            pyofd.ReceiptEntry(title='КАРАМЕЛЬ ЧУПА ЧУПС ФРУКТОВАЯ В' , qty='2'    , price='7.19' , subtotal='14.38'),
            pyofd.ReceiptEntry(title='БАНАНЫ ВЕС'                     , qty='1.035', price='53.90', subtotal='55.79'),
            pyofd.ReceiptEntry(title='КРУАССАНЫ 7 DAYS МИНИ КАКАО 30' , qty='1'    , price='96.90', subtotal='96.90'),
            pyofd.ReceiptEntry(title='СЫРОК-СУФЛЕ ГЛАЗИР.ВАНИЛЬ Б.Ю.' , qty='6'    , price='44.90', subtotal='269.40'),
            pyofd.ReceiptEntry(title='СЫРОК ГЛ. Б.Ю.АЛЕКСАНДРОВ 26%'  , qty='1'    , price='31.43', subtotal='31.43'),
            pyofd.ReceiptEntry(title='СЫРОК ГЛ. Б.Ю.АЛЕКСАНДРОВ 26%'  , qty='1'    , price='31.43', subtotal='31.43'),
            pyofd.ReceiptEntry(title='ДРАЖЕ ТИК ТАК МЯТА/АПЕЛЬСИН 16' , qty='1'    , price='45.00', subtotal='45.00'),
            pyofd.ReceiptEntry(title='ДРАЖЕ ТИК ТАК МЯТА/АПЕЛЬСИН 16' , qty='1'    , price='45.00', subtotal='45.00'),
            pyofd.ReceiptEntry(title='ЙОГУРТ РАСТИШКА 3% КЛУБНИКА 11' , qty='2'    , price='17.99', subtotal='35.98'),
            pyofd.ReceiptEntry(title='ХЛЕБ РЖАНОЙ БУЛОЧНАЯ №1 ПОДОВЫ', qty='1'    , price='14.90', subtotal='14.90'),
            pyofd.ReceiptEntry(title='ХЛЕБ РЖАНОЙ НАР.415Г КР'        , qty='1'    , price='24.90', subtotal='24.90'),
            pyofd.ReceiptEntry(title='ЯЙЦО КИНДЕР СЮРПРИЗ ИЗ МОЛОЧ.Ш' , qty='2'    , price='78.90', subtotal='157.80'),
        ]

    def setUp(self):
        self.provider = pyofd.providers.platforma.ofdPlatforma()

    def test_provider_invalid(self):
        self.assertIsNone(self.provider.validate(signature=0, cash_machine_no=0, receipt_no=0))

    def test_provider_minimal(self):
        self.assertIsNotNone(self.provider.validate(signature=504931317, cash_machine_no=8710000100186516, receipt_no=136682))

    def test_valid_parse(self):
        result = self.provider.validate(signature=504931317, cash_machine_no=8710000100186516, receipt_no=136682)
        self.assertEqual(self.valid_receipt_items, result)

    def test_provider(self):
        receipt = pyofd.OFDReceipt(signature=504931317, cash_machine_no=8710000100186516, receipt_no=136682)

        result = receipt.load_receipt()

        self.assertEqual(True, result)
        self.assertIs(receipt.provider.__class__, self.provider.__class__)
        self.assertEqual(self.valid_receipt_items, receipt.items)