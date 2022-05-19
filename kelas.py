######################################################
# Nama file: kelas.py
######################################################

# mendefinisikan kelas
class persegi(object):
   def __init__(self, s):
      
      
      
   def hitungVolume(self):
      return self.panjang * self.lebar * self.tinggi

def main():
   # membuat objek pertama
   kotak1 = Kotak(l=6, p=4, t=3)

   # menggunakan objek pertama
   print("Objek kotak1")
   print("panjang\t: ", kotak1.panjang)
   print("lebar\t: ", kotak1.lebar)
   print("tinggi\t: ", kotak1.tinggi)
   print("Volume\t= ", kotak1.hitungVolume())

   # membuat objek kedua
   kotak2 = Kotak(5, 3, 2)

   # menggunakan objek kedua
   print("\nObjek kotak2")
   print("panjang\t: ", kotak2.panjang)
   print("lebar\t: ", kotak2.lebar)
   print("tinggi\t: ", kotak2.tinggi)
   print("Volume\t= ", kotak2.hitungVolume())

if __name__ == "__main__":
   main()