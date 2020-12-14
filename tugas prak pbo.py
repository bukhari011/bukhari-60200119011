class pramuka:
    nama = ''
    tku = ''
    semester = ''

    def __init__(self, nama):
        self.nama = nama

    def get_semester(self, semester):
        self.semester = semester

    def get_tku(self, tku):
        self.tku = tku

    def hasil(self):
        print('mahasiswa atas nama %s\nadalah  mahasiswa semester %s\ndengan pangkat  %s' % (self.nama, self.semester, self.tku))

p = pramuka('Bukhari')
p.get_semester('tiga')
p.get_tku('Garuda')
p.hasil()
print(' ')
