import unittest
from feriadoscalculados import Frdos



class TestFrdos(unittest.TestCase):   

   def test_start(self): 
      
      self.assertEqual(Frdos('2019asd').ano, 2019)   
   
   def test_pascoa(self):         
       self.assertTrue(Frdos('20asd').ano1,'21/04/2019')
        
    
   def test_carnaval(self):
     
      self.assertTrue(Frdos('2019asd').ano1,'05/03/2019')
   
   def test_sextasanta(self):
      
      
      self.assertTrue(Frdos('2019asd').ano1,'19/04/2019')

   def test_corpuscristi(self):
     
      self.assertTrue(Frdos('2019asd').ano1,'20/06/2019')
   
   def test_corpuscristi_2(self):

      self.assertIsNotNone('2017czsdadsx',msg=None)
      
   
if __name__ == '__main__':

    unittest.main()