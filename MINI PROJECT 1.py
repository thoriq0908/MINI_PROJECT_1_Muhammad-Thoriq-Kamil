print(" Database pasien opname rumah sakit")
daftar_pasien = []

while True:
    print("================================")
    print(" MENU PILIHAN ")
    print("================================")
    print("1. Tambah data pasien")
    print("2. Tampilkan seluruh data pasien")
    print("3. Ubah data pasien")
    print("4. Hapus data pasien")
    print("5. Keluar")
    pilihan =(input("Masukkan pilihan anda (1/2/3/4/5): "))

    if pilihan != "1" and pilihan != "2" and pilihan != "3" and pilihan != "4" and pilihan != "5":
        print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")

    if pilihan == "1":
        print()
        print("--Tambah data pasien--")

        while True:
            nomor = input("Masukkan nomor rekam medis pasien: ")
            if nomor.isdigit():
                nomor_rm = int(nomor)
                break
            else:
                print("Nomor rekam medis harus berupa angka, silahkan input kembali")

        rm_ada = False
        for pasien in daftar_pasien:
            if pasien[0] == nomor_rm:
                rm_ada = True
                break
        if rm_ada:
            print("Nomor rekam medis " + str(nomor) + " sudah ada. Silakan masukkan nomor yang berbeda.")

        else:
            while True:
                nama = input("Masukkan nama pasien: ")
                if nama != "":
                    break
                else:
                    print ("Nama tidak boleh kosong, silahkan input kembali")

            while True:
                umur = input("Masukkan umur pasien: ")
                if umur.isdigit():
                    umur = int(umur)
                    break
                else:
                    print("Umur harus berupa angka, silahkan input kembali")

            while True:
                ruangan = input("Masukkan ruangan pasien: ")
                if ruangan != "":
                    break
                else:
                    print("Ruangan tidak boleh kosong, silahkan input kembali")

            daftar_pasien.append([nomor_rm, nama, umur, ruangan])
            print("Data pasien berhasil ditambahkan.")

    elif pilihan == "2":
        print()
        print("--Tampilkan seluruh data pasien--")
        if len(daftar_pasien) == 0:
            print("Belum ada data pasien yang tersimpan.")
        else:
            print("No. RM".ljust(9) + "Nama".ljust(20) + "Umur".ljust(7) + "Ruangan".ljust(20))
            print("-" * 56)
            for pasien in daftar_pasien:
                nomor_rm = pasien[0]
                nama = pasien[1]
                umur = pasien[2]
                ruangan = pasien[3]
                baris = str(nomor_rm).ljust(9) + nama.ljust(20) + str(umur).ljust(7) + ruangan.ljust(20)
                print (baris)
            print("-" *56)
            print("Jumlah pasien Opname saat ini:" +str(len(daftar_pasien)))

    elif pilihan == "3":
        print()
        print("--Ubah data pasien--")
        if len(daftar_pasien) == 0:
            print("Belum ada data pasien yang tersimpan.")
        else:
            while True:
                nomor = input("Masukkan nomor rekam medis pasien yang ingin diubah: ")
                if nomor.isdigit():
                    nomor_rm = int(nomor)
                    break
                else:
                    print("Nomor rekam medis harus berupa angka, silakan input kembali")

            pasien_ditemukan = False
            for i in range(len(daftar_pasien)):
                if daftar_pasien[i][0] == nomor_rm:
                    pasien_ditemukan = True
                    while True:
                        nama = input("Masukkan nama baru pasien: ")
                        if nama != "":
                            break
                        else:
                            print("Nama tidak boleh kosong, silahkan input kembali")

                    while True:
                        umur = input("Masukkan umur baru pasien: ")
                        if umur.isdigit():
                            umur = int(umur)
                            break
                        else:
                            print("Umur harus berupa angka, silahkan input kembali")

                    while True:
                        ruangan = input("Masukkan ruangan baru pasien: ")
                        if ruangan != "":
                            break
                        else:
                            print("Ruangan tidak boleh kosong, silahkan input kembali")

                    daftar_pasien[i] = [nomor_rm, nama, umur, ruangan]
                    print("Data pasien berhasil diubah.")
                    break

            if not pasien_ditemukan:
                print(f"Nomor rekam medis {nomor_rm} tidak ditemukan.")

    elif pilihan == "4":
        print()
        print("--Hapus data pasien--")
        if len(daftar_pasien) == 0:
            print("Belum ada data pasien yang tersimpan.")
        else:
            while True:
                nomor = input("Masukkan nomor rekam medis pasien yang ingin dihapus: ")
                if nomor.isdigit():
                    nomor_rm = int(nomor)
                    break
                else:
                    print("Nomor rekam medis harus berupa angka, silakan input kembali")

            idx_hapus = -1
            for i in range(len(daftar_pasien)):
                if daftar_pasien[i][0] == nomor_rm:
                    idx_hapus = i
                    break

            if idx_hapus != -1:
                del daftar_pasien[idx_hapus]
                print(f"Data pasien dengan nomor rekam medis {nomor_rm} berhasil dihapus.")
            else:
                print(f"Nomor rekam medis {nomor_rm} tidak ditemukan.")

    elif pilihan == "5":
        print("Terima kasih, program selesai.")
        break