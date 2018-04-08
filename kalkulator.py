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

def tanya():
    tanya = input("\n\tKembali ke Menu Kalkulator? (y/n)")
    if tanya == "y":
        kalkulator()
    elif tanya == "n":
        exit
    else :
        print ("\n\tMaaf Pilihan Tidak Tersedia!")
kalkulator()
