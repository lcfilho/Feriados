from sys import argv
from datetime import date
import re

class Frdos:

    def __init__(self,ano1):  
           
        self.ano1 = ano1
        self.pascoa() 
        self.carnaval() 
        self.sextasanta()        
        self.corpuscristi()  
        self.tela()       

      
    def pascoa(self):
        self.ano2 = re.sub('[^0-9]','',self.ano1)
        self.ano = int(self.ano2)
        if self.ano>1583 and self.ano<2099:
            a = self.ano % 19
            b = self.ano // 100
            c = self.ano % 100
            d = b // 4
            e = b % 4
            f = (b + 8) // 25
            g = (b - f + 1) // 3
            h = (19 * a + b - d - g + 15) % 30
            i = c // 4
            k = c % 4
            l = (32 + 2 * e + 2 * i - h - k) % 7
            m = (a + 11 * h + 22 * l) // 451
            self.mes = (h + l - 7 * m + 114) // 31
            self.dia = 1 + (h + l - 7 * m + 114) % 31        
            self.pascoa = date(self.ano, self.mes, self.dia)
            
            
        else:
            return False  
        return False

         
    def carnaval(self):
        if self.ano>1583 and self.ano<2099:
            self.carnaval = date.fromordinal(self.pascoa.toordinal() - 47)       
        return False

  
    def sextasanta(self):
        if self.ano>1583 and self.ano<2099:
            self.sextasanta = date.fromordinal(self.pascoa.toordinal() - 2)    
        return False

 
    def corpuscristi(self):
        if self.ano>1583 and self.ano<2099:
            self.corpuscristi = date.fromordinal(self.pascoa.toordinal() + 60)
        return False

    
    def tela(self):
        if self.ano>1583 and self.ano<2099:
            print("CARNAVAL: {}".format(self.carnaval.strftime('%d/%m/%Y')))
            print('PÁSCOA: {}'.format(self.pascoa.strftime('%d/%m/%Y')))
            print("CORPUS CHRISTI: {}".format( self.corpuscristi.strftime('%d/%m/%Y')))
            print("SEXTA FEIRA SANTA: {}".format( self.sextasanta.strftime('%d/%m/%Y')))
        return False 

if __name__ == "__main__":
   
    ano = Frdos(argv[1])
    