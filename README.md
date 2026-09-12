# MINI_PROJECT_1_Muhammad-Thoriq-Kamil

Nama: Muhammad Thoriq Kamil<br>
NIM: 2609116047<br>
Sistem informasi Kelas B 26'

# SISTEM PENGELOLAAN DATA PASIEN OPNAME DI RUMAH SAKIT
Program berjalan dalam bentuk menu pilihan berulang (menggunakan while True) sampai pengguna memilih menu Keluar. Setiap data pasien disimpan sebagai satu list dengan struktur:<br>
[No. RM, Nama, Umur, Ruangan]<br>
program menggunakan 4 operasi CRUD yaitu:<br>
Create(tambah)--> tambah data pasien<br>
Read(lihat)--> tampilkan seluruh data pasien<br>
Update(ubah)--> ubah data pasien<br>
Delete(hapus)--> hapus data pasien<br>

berikut adalah bentuk dari flowchartnya:<br>
<img width="423" height="296" alt="Screenshot 2026-09-12 203936" src="https://github.com/user-attachments/assets/6b0a7ddf-aa0c-4f9a-a58a-3fa3efc0c18c" />

berikut merupakan implementasi dan bentuk output dari CREATE atau menambah data yang disertai dengan validasi looping ketika user memasukkan input yang tidak sesuai:<br>
<img width="960" height="600" alt="image" src="https://github.com/user-attachments/assets/29ea120c-c492-48fd-b981-142c2688915d" /> <br>
program dibuat menggunakan looping while true dan if else untuk membuat sistem memastikan input user sesuai, dan juga menggunakan program True False untuk memastikan nomor rekam medis pasien yang kita tambahkan tidak terdoble.

selanjutnya merupakan implementasi dan bentuk output dari READ atau tampilan seluruh data pasien:<br>
<img width="960" height="600" alt="Screenshot 2026-09-12 215747" src="https://github.com/user-attachments/assets/acd5485e-a118-45f5-8623-6fea236ce128" /><br>
program dibuat menggunakan IF ELSE untuk membuat output berbeda, yaitu ketika data kosong output akan print bahwa data tidak ada sedangkan ketika data pasien dalam list daftar_pasien memang ada, output akan print data pasien

lalu implementasi dan bentuk output dari UPDATE atau mengubah data yang sudah ada:<br>
<img width="960" height="600" alt="Screenshot 2026-09-12 215910" src="https://github.com/user-attachments/assets/513ee0ee-f5a9-490d-9a37-186f5dd15f39" /> <br>
program dimulai dengan IF ELSE, IF data tidak ada maka akan mengeluarkan output bahwa data untuk diubah tidakada,lalu looping ke program menu awal sedangkan ELSE akan masuk ke while True berikutnya berupa input nama,umur,ruangan, program ini berjalan sama seperti saat di menu 1 atau program CREATE, program juga menggunakan if not yaitu untuk pada keadaan data di daftar_pasien ada tetapi input no.rm dari user tidak sesuai dengan yang terdapat di list daftar_pasien sehingga progam mengeluarkan input bahwa no.rm tidak ditemukan

setelah itu, implementasi dan bentuk output dari DELETE atau menghapus data yang sudah ada:<br>
<img width="960" height="600" alt="Screenshot 2026-09-12 220014" src="https://github.com/user-attachments/assets/e234ba8f-f542-4e0d-96b5-c91e8c482e9b" /><br>
program dimulai dengan IF ELSE untuk membuat validasi(input salah maka ulang dan jika benar lanjut) lanjut masuk ke while True untuk membuat loop kesesuaian no.rm yang diinput dengan data yang sudah ada, dan program menggunakan for i in range(len(daftar_pasien)) hal ini berarti menyatakan i adalah jumlah pasien di daftae pasien yang dimulai dengan indeks 0, lalu membuat if untuk memastikan apakah no.rm di posisi i sama dengan yang diinput user, lalu menggunakan del untuk menghapus data sesuai dengan indeks yang direkam program melalui no,rm yang diinput user.

dan semua program itu akan selalu looping ke menu awal, dan untuk mengakhiri program user perlu menekan 5 untuk keluar dan menyelesaikan program.<br>
<img width="960" height="600" alt="Screenshot 2026-09-12 222838" src="https://github.com/user-attachments/assets/ab661310-93d2-43e1-a27c-a1d21f24fd92" />
