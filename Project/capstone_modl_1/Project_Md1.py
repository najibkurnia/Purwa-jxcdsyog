from prettytable import PrettyTable 
import sys

pemain = [
    {"nama": "Mbappe","posisi": "Penyerang","asal_negara": "Prancis","gaji": 3000000000,},
    {"nama": "Vinicius","posisi": "Penyerang","asal_negara": "Brazil","gaji": 3300000000,},
    {"nama": "Rodrygo ","posisi": "Penyerang","asal_negara": "Brazil","gaji": 1700000000,},
    {"nama": "Valverde","posisi": "Tengah","asal_negara": "Spanyol","gaji": 2250000000,},
    {"nama": "Bellingham","posisi": "Tengah","asal_negara": "Inggris","gaji": 3100000000,},
    {"nama": "Camavinga","posisi": "Tengah","asal_negara": "Prancis","gaji": 1300000000,},
    {"nama": "Rudiger","posisi": "Bertahan","asal_negara": "Jerman","gaji": 400000000,},
    {"nama": "Asensio","posisi": "Bertahan","asal_negara": "Spanyol","gaji": 10000000,}
]

header_pemain = ["Nama", "Posisi", "Asal Negara","Gaji"]


def tampilkan_pemain(data): 
  table = PrettyTable() 

  table.field_names = header_pemain 

  for pemain in data:
      table.add_row(pemain.values()) 

  print(table) 

def validate_nama(): 
  while True:
    nama = input("Masukkan nama pemain : ") 
    return nama
    
def get_pemain_by_nama(): #menampilkan semua pemain
  while True:
    nama = validate_nama()

    pemain = cari_pemain(nama)
    if not pemain:
      if not lanjutkan("Apakah Anda masih ingin mencari pemain lainnya?"):
        break
      else:
        continue

    else:
      print("\nBerikut adalah data pemain yang Anda cari")
      tampilkan_pemain([pemain])
      if not lanjutkan("Apakah Anda masih ingin mencari pemain lainnya?"):
        break


#----------------------------------------------------------------------------------------------------------------------

def get_pemain(): 
    if not pemain:
        print("Tidak ada data pemain.")
    else:
        tampilkan_pemain(pemain)

def get_gaji_terkecil(pemain):
   
    pemain_terkecil = pemain[0]  

    for pemain_item in pemain:
        if pemain_item["gaji"] < pemain_terkecil["gaji"]:
            pemain_terkecil = pemain_item 

    return pemain_terkecil

def get_gaji_terbesar(pemain):
    
    pemain_terbesar = pemain[0]  
  
    for pemain_item in pemain:
        if pemain_item["gaji"] > pemain_terbesar["gaji"]:
            pemain_terbesar = pemain_item  

    return pemain_terbesar

def bubble_sort_asc(field="gaji"):
    data = pemain.copy()
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j][field] > data[j+1][field]:
                
                data[j], data[j+1] = data[j+1], data[j]
    
    return data

def bubble_sort_desc(field="gaji"):
    data = pemain.copy()
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j][field] < data[j+1][field]:
                data[j], data[j+1] = data[j+1], data[j]
    
    return data

def get_biaya_gaji():
        while True:
            try:
                print("\n|=============== Menu Mencari Gaji Pemain ==================|")
                print("1. Tampilkan Gaji Terkecil")
                print("2. Tampilkan Gaji Terbesar")
                print("3. Urutkan Gaji Pajak dari yang Terkecil")
                print("4. Urutkan Gaji Pajak dari yang Terbesar")
                print("5. Kembali ke Menu Lihat Daftar pemain")            
                print("|===========================================================|")

                pilihan = int(input("Pilih menu (1-5): "))

                if pilihan == 1:
                    pemain_terkecil = get_gaji_terkecil(pemain)
                    print("\npemaindengan Pajak Terkecil:")
                    tampilkan_pemain([pemain_terkecil])  # Menampilkan  terkecil
                elif pilihan == 2:
                    pemain_terbesar = get_gaji_terbesar(pemain)
                    print("\npemain dengan Pajak Terbesar:")
                    tampilkan_pemain([pemain_terbesar])  # Menampilkan terbesar
                elif pilihan == 3:
                    print("\npemain diurutkan berdasarkan Pajak Terkecil:")
                    tampilkan_pemain(bubble_sort_asc())  
                elif pilihan == 4:
                    print("\npemain diurutkan berdasarkan Pajak Terbesar:")
                    tampilkan_pemain(bubble_sort_desc())  
                elif pilihan == 5:
                    menu_read()
                else:
                    print("Pilihan tidak valid. Silakan pilih lagi.")
            except ValueError:
                print("Pilihan tidak valid. Silakan pilih lagi.")

def add_pemain():
    while True:
        nama = validate_nama()

        if nama_exist(nama):
            print("Pemain Anda sudah terdaftar.")
            continue

        posisi = input("Masukkan Posisi Pemain: ").capitalize()
        
        gaji = int(input("Masukkan gaji pemain : "))
        new_data = {
            "posisi": posisi,
            "gaji": gaji,
        }

        tampilkan_pemain([new_data])
        validasi = input("Apakah Anda yakin ingin menambahkan data ini? (Y/N):").upper()

        if(validasi == "Y"):
          pemain.append(new_data)

          print("Data pemain berhasil ditambahkan.\n")
          if not lanjutkan("Apakah Anda ingin menambahkan data pemain lainnya?"):
            break
        
        else:
          if not lanjutkan("Apakah Anda masih ingin menambahkan data pemain?"):
            break

def menu_read():
    while True:
        try:
            print("\n|================ List ====================|")
            print("\t1. Menampilkan Semua Pemain")
            print("\t2. Mencari Gaji Pemain")
            print("\t3. Kembali ke Menu Utama")
            print("|=========================================|")

            pilihan = int(input("Pilih menu (1-3): "))

            if pilihan == 1:
                print("\nBerikut adalah daftar semua Pemain")
                get_pemain()
            elif pilihan == 2:
                get_biaya_gaji()
            elif pilihan == 3:
                main_menu()
            else:
                print("Pilihan tidak valid. Silakan pilih lagi")

        except ValueError:
            print("Pilihan tidak valid. Silakan pilih lagi")

#----------------------------------------------------------------------------------------------------------------------

def nama_exist(nama): 
    if any(data["nama"] == nama for data in pemain):
        return True
    else:
        return False

def lanjutkan(konfirmasi):
  while True:
    validasi = input(konfirmasi + " (Y/N): ").upper()

    if validasi == "Y":
        return True
    
    elif validasi =='N':
        return False
    
    else:
        print("Pilihan Tidak Valid.")

def menu_create():
    while True:
        try:
            print("\n|=============== Menu Tambah Pemain =====================|")
            print("1. Tambah Data Pemain")
            print("2. Kembali ke Menu Utama")
            print("|===========================================================|")

            pilihan = input("Pilih menu (1-2): ")

            if pilihan == "1":
                add_pemain()
            elif pilihan == "2":
                main_menu()
            else:
                print("Pilihan tidak valid. Silakan pilih lagi.")
        except ValueError:
            print("Pilihan tidak valid. Silakan pilih lagi.")

#----------------------------------------------------------------------------------------------------------------------

def cari_pemain(nama_cari, data = pemain):
    for item in data:
        if item["nama"] == nama_cari: 
            return item  

    print("Pemain dengan nama tersebut tidak ditemukan.")
    return None  

def update_pemain():
    while True:
        tampilkan_pemain(pemain)
        nama = validate_nama()

        pemain_data = cari_pemain(nama)

        if pemain_data is None:
            print("Pemain tidak ditemukan.")
            if not lanjutkan("Apakah Anda ingin mencari nama lainnya?"):
                break
            else:
                continue

        
        print("\nData pemain yang akan diubah:")
        tampilkan_pemain([pemain_data])

        if not lanjutkan("Apakah Anda yakin ingin mengubah data pemain ini?"):
            if not lanjutkan("Apakah Anda ingin mencoba mengubah pemain lain?"):
                break
            else:
                continue

        while True:
            print("\n|===============Pilih data yang ingin diubah:===============|")
            print("1. Posisi")
            print("2. Gaji")
            print("3. Kembali")
            print("|==============================================================|")

            pilihan = int(input("Pilih nomor (1-3): "))

            if pilihan == 1:
                posisi = input("Masukan Posisi Baru :").capitalize()
                pemain_data["posisi"] = posisi

            elif pilihan == 2:
                gaji = int(input("gaji : "))
                pemain_data["gaji"] = gaji

            elif pilihan == 3:
                print("Kembali ke pilih pemain.")
                break

            else:
                print("Pilihan tidak valid, silakan pilih lagi.")
                continue

            print("\nData pemain yang telah diperbarui:")
            tampilkan_pemain([pemain_data])

            if not lanjutkan(f"Apakah Anda ingin mengubah detail lain dari pemain ini?"):
                break

        if not lanjutkan("Apakah Anda ingin mengubah data pemain lainnya?"):
            break
#----------------------------------------------------------------------------------------------------------------------

def hapus_pemain():
    while True:
        tampilkan_pemain(pemain)
        nama = validate_nama()

        pemain_data = cari_pemain(nama)
        if pemain_data is None:
            print("Pemain dengan nama tersebut tidak ditemukan.")
            if not lanjutkan("Apakah Anda ingin mencari nama lainnya?"):
                break
            else:
                continue

        print("\nData pemain yang akan dihapus:")
        tampilkan_pemain([pemain_data])

        if not lanjutkan("Apakah Anda yakin ingin menghapus data pemain ini?"):
            if not lanjutkan("Apakah Anda ingin mencoba menghapus pemain lain?"):
                break
            else:
                continue

        pemain.remove(pemain_data)
        print(f"Pemain bernama {nama} telah dihapus.")

        if not lanjutkan("Apakah Anda ingin menghapus pemain lainnya?"):
            break

def menu_delete():
    while True:
        try:
            print("\n|=============== Menu Hapus Pemain =====================|")
            print("1. Hapus Data Pemain")
            print("2. Kembali ke Menu Utama")
            print("|===========================================================|")

            pilihan = int(input("Pilih menu (1-2): "))

            if pilihan == 1:
                hapus_pemain()
            elif pilihan == 2:
                main_menu()
            else:
                print("Pilihan tidak valid. Silakan pilih lagi.")
        except ValueError:
                print("Pilihan tidak valid. Silakan pilih lagi.")

#----------------------------------------------------------------------------------------------------------------------


def menu_update():
    while True:
        try:
            print("\n|=============== Menu Update Pemain =====================|")
            print("1. Ubah Data Pemain")
            print("2. Kembali ke Menu Utama")
            print("|===========================================================|")

            pilihan = int(input("Pilih menu (1-2): "))

            if pilihan == 1:
                update_pemain()
            elif pilihan == 2:
                main_menu()
            else:
                print("Pilihan tidak valid. Silakan pilih lagi.")
        except ValueError:
            print("Pilihan tidak valid. Silakan pilih lagi.")

def main_menu():
    while True:
        try:
            print("\n|================ Manager ==================|")
            print("\t1. Lihat Daftar Pemain")
            print("\t2. Menambah Daftar Pemain")
            print("\t3. Mengubah Daftar Pemain")
            print("\t4. Menghapus Daftar Pemain")
            print("\t5. Keluar Program")
            print("|===========================================|")

            pilihan = int(input("\nPilih menu (1-5): "))

            if pilihan == 1:
                menu_read()
            elif pilihan == 2:
                menu_create()
            elif pilihan == 3:
                menu_update()
            elif pilihan == 4:
                menu_delete()
            elif pilihan == 5:
                print("\n Terima kasih \n    Exit \n")
                sys.exit()
            else:
                print("Pilihan tidak valid. Silakan pilih lagi.")
        
        except ValueError:
            print("Pilihan tidak valid. Silakan pilih lagi.")
main_menu()
