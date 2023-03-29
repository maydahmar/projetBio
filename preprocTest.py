import unittest
from preproc import *


        
class RNASeqTest(unittest.TestCase):
    def setUp(self):
        self.data_matrice = RNASeq('./Data')
    #def test_get_value(self):
    #    self.assertEqual(self.data_matrice.get_value('A1BG', 'GSM3533230'), 42)
    #def test_mean(self):
    #    print(self.data_matrice.calculate_mean().shape)
   # def test_std(self):
    #    print(self.data_matrice.calculate_std().shape)
    #def test_cv(self):
    #    print(self.data_matrice.calculate_cv().shape)
    #def test_hist(self):
        #print(self.data_matrice.print_hist())
    #def test_center( self):
    #    print(self.data_matrice.center_data())
    def test_pca(self):
        self.data_matrice.calculate_pca()


class annotationTest(unittest.TestCase):
    def setUp(self):
        self.data = annotation('./Data/GSE124439_family.xml')
    def test_get_value(self):
        self.assertEqual(self.data.get_annotation('GSM3533230'), 'Frontal Cortex      '  )


if __name__ == '__main__':
    unittest.main()