#FOR LOOP -> Pengulangan print / formula
#nama_buah = ['apel', 'jeruk', 'strawberry', 'anggur', 'lemon', 'markisa']
#for buah in nama_buah:
    #print (buah)
    #print ("---")
#print ('done')

#FOR RANGE -> pengulangan dengan range angka
# range (start, stop, set)
#for i in range (1, 20, 2):
    #print(i)

# QUIZ
#nama_pelanggan = ['divi', 'listya', 'nadi', 'nita', 'lala']
#for pelanggan in nama_pelanggan:
    #print (pelanggan)

#Jawaban Quiz yang bener
#count = int(input("Berapa Data: "))

#nama_pelanggan = []
#umur_pelanggan = []

#for i in range(count):
    #print("Data ke{}". format(i+1))
    #nama = input("Nama : ")
    #umur = int(input("Umur: "))

    #nama_pelanggan.append(nama)
    #umur_pelanggan.append(umur)

#for i in range(len(nama_pelanggan)):
    #print('Pelanggan {} berusia {}'. format(nama_pelanggan[i], umur_pelanggan[i]))

# CONTINUE -> ngeprint kalo sesuai statement
#for i in range(5):
    #if i == 2:
        #continue
    #print(i)

# BREAK -> stop ngeprint kalo kondisi sesuai
#for i in range(5):
    #if i == 2:
        #break
    #print(i)

# CONTINUE WITH 2 CONDITIONS
#for i in range(5):
    #if i == 2 or i == 3:
        #continue
    #print(i)

# NESTED LOOP
#for i in range(3):
#    print("i: {}". format(i))
#    for j in range (3):
#        print("j: {}". format(j))

for baris in range(5):
    for kolom in range(5):
        print("{}.{}". format(baris+1, kolom+1), end=" ")
    print()

x = [1,2,3,4,5]
y = [2,4,3,5,6]
z = 0

for i in x:
    for j in y:
        if i == j:
            z=z+1
print(z)

