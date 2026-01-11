'''
Tugas 2 
Iqbal Fadhlillah 
101012380434
TTX - 47 - 01
'''

'''
No . 1 
Buat program untuk menampilkan bilangan ganjil dan genap mulai dari 1 sampai 
dengan 20 selanjutnya simpan dalam list.
'''

genap = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
ganjil = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print('List pada bilangan genap', genap)
print('List pada bilangan ganjil', ganjil)

'''
No . 2 
Buat dictionary dengan ketentuan sebagai berikut:
Lihat pada LMS
'''

dictionary = { "Thriller":1982, 
               "Back in Black":1980, 
               "The Dark Side of The Moon":1973, 
               "The Bodyguard":1992,
               "Bat Out of Hell":1977,
               "Their Greatest Hits (1971-1975)":1976
             }
#no 1 Tampilkan setiap nilai yang ada pada dictionary tersebut
print(dictionary.values())
#no 2 Tampilkan nilai untuk data “The Dark Side of the Moon”
print(dictionary['The Dark Side of The Moon'])
#no 3 Tambahkan data pada dictionary “Soulvaki” dengan nilai 1993
dictionary["Soulvaki"] = 1993
print(dictionary)
#no 4 Hitung banyaknya value pada dictionary 
print('jumlah values nya adalah', len(dictionary.values()))
#no 5 Check 1992 terdapat pada dictionary kemudian print pesan “Data 1992 ditemukan”
search = 1992
if search in dictionary.values():
    print("Data 1992 ditemukan")
else:
    print("Data 1992 tidak ditemukan")