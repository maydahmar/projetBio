import unittest
from preproc import *


        
# class RNASeqTest(unittest.TestCase):
#     def setUp(self):
#         #self.data_matrice = RNASeq('./Data')
#     def test_get_value(self):
#         #self.assertEqual(self.data_matrice.get_value('A1BG', 'GSM3533230'), 42)


class annotationTest(unittest.TestCase):
    def setUp(self):
        self.data = annotation('./Data/GSE124439_family.xml')
    def test_get_value(self):
        print(self.data.get_frame().head())
        self.assertEqual(self.data.get_annotation('GSM3533230'), 'Frontal Cortex      '  )


if __name__ == '__main__':
    unittest.main()