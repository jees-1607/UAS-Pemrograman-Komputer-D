import math
def menu_awal():    
    kuliah = ["Jeremia Stephanus", "190402158", "Pemrograman Komputer D"]
    print(kuliah)
    
    a = "\n1. Hipotenusa Segitiga"
    b = "\n2. Tinggi segitiga"
    c = "\n3. Alas Segitiga"
    d = "\n4. Keluar"
    print(a,b,c,d)
    pilih_menu = int(input("\n Masukkan pilihan : "))
    if pilih_menu == 1:
        hipotenusa_segitiga()
    elif pilih_menu == 2:
        tinggi_segitiga()
    elif pilih_menu == 3:
        alas_segitiga() 
    else:
        keluar_program()

def hipotenusa_segitiga():
    alas_segitiga = int(input("\nNilai alas dari segitiga: "))
    tinggi_segitiga = int(input("\nNilai tinggi dari segitiga: "))
    hitung_hipotenusa = int(math.sqrt(tinggi_segitiga ** 2 + alas_segitiga ** 2))
    print(f"\nSisi miring atau hipotenusa = {hitung_hipotenusa}\n")
    menu_awal()

def tinggi_segitiga():
    hipotenusa_segitiga = int(input("\nNilai sisi miring/hipotenusa dari segitiga: "))
    alas_segitiga = int(input("\nNilai alas dari segitiga: "))
    hitung_tinggi = int(math.sqrt(hipotenusa_segitiga ** 2 - alas_segitiga ** 2))
    print(f"\nTinggi segitiga = {hitung_tinggi}\n")
    menu_awal()

def alas_segitiga():
    tinggi_segitiga = int(input("\nNilai tinggi dari segitiga: "))
    hipotenusa_segitiga = int(input("\nNSilai sisi miring/hipotenusa dari segitiga: "))
    hitung_alas = int(math.sqrt(hipotenusa_segitiga ** 2 - tinggi_segitiga ** 2))
    print(f"\nAlas segitiga = {hitung_alas}\n")
    menu_awal()

def keluar_program():
    print("\n Terima Kasih\n ")

menu_awal()
