class Kotak(object):
  def __init))(self, p, l, t):
    self.panjang = p
    self.lebar = l
    self.tinggi = t
    
  def hitungVolume(self):
    return self.panjang * self.lebar * \
           self.tinggi
 
  def cetakData(self):
    print("panjang\t: ", self.panjang)
    print("lebar\t: ", self.lebar)
    print("tinggi\t: ", self.tinggi)
    
  def cetakVolume(self):
    print("Volume\t= ", self.hitungVolume())
    
# mendefinisikan kelas turunan (subclass)
class kotakWarna(kotak):
  def __init__(self, p, l, t, w):
    # memanggil kotak.__init__()
    super(KotakWarna, self).__init__(p, l, t)
    # menambah atribut baru
    self.warna = w
    
def main():
  # membuat objek KotakWarna
  kotakwarna1 = KotakWarna(6, 5, 4, "merah")

  #menggunakan objek
  kotakwarna1.cetakData()
  kotakwarna1.cetakVolume()
  
if __name__ == "__main__":
  main()

