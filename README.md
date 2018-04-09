## use pyhton 3.4.2

## function yang nantinya akan ditampilkan sebagai menu utama saat program dijalankan, parameter 'kalkulator' yang nanti akan dipanggil saat dieksekusi
```javascript
def kalkulator():
    print("\n\t======================================")
    print("\tProgram Kalkulator Sederhana")
    print("\t========================================")
    print("\n\t1. Penjumlahan")
    print("\n\t2. Pengurangan")
    print("\n\t3. Perkalian")
    print("\n\t4. Pembagian")
    print("\t========================================")
    print("\tSilahkan Pilih 1-4")
    print(" ")
```
## pilihan untuk memanggil menu-menu yang akan ditampilkan
```javascript
    pilih = input("\tMasukkan Pilihan : ")
    if pilih == "1":
        tambah()
    elif pilih == "2":
        kurang()
    elif pilih == "3":
        kali()
    elif pilih == "4":
        bagi()
    else:
        print("\tMaaf Pilihan yang Anda Masukkan Tidak Tersedia!")
        print("\tSilahkan Ulangi Kembali")
        tanya()
```
## fungsi-fungsi yang dipanggil ketika memasukkan sebuah pilhan
```javascript
def tambah():
    print("\t1. Penjumlahan")
    k = int(input("\tx="))
    s = int(input("\ty="))
    ks = k+s
    print ("\tx+y=",ks)
    tanya()

def kurang():
    print("\t2. Pengurangan")
    k = int(input("\tx="))
    s = int(input("\ty="))
    ks = k-s
    print ("\tx-y=",ks)
    tanya()

def kali():
    print("\t3. Perkalian")
    k = int(input("\tx="))
    s = int(input("\ty="))
    ks = k*s
    print ("\tx*s=",ks)
    tanya()

def bagi():
    print("\t4. Pembagian")
    k = int(input("\tx="))
    s = int(input("\ty="))
    ks = k/s
    print ("\tx/s=",ks)
    tanya()
```
## jika diperhatikan, di setiap akhir script fungsi-fungsi di atas, ada script tanya(), maksudnya adalah ketika selesai menjalankan satu program kita akan ditawarkan pertanyaan apakah akan memainkan progam lagi atau tidak, script-nya seperti ini
```javascript
def tanya():
    tanya = input("\n\tKembali ke Menu Kalkulator? (y/n)")
    if tanya == "y":
        kalkulator()
    elif tanya == "n":
        exit
    else :
        print ("\n\tMaaf Pilihan Tidak Tersedia!")
```
## perintah untuk memanggil function menu utama
```javascript
kalkulator()
```
## Demikian penjelasan singkat dari saya, semoga bermanfaat. Selamat mencoba...
