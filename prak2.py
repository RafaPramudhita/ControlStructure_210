def evaluasi_kinerja(nilai):
    if nilai >= 90:
        return "Kinerja sangat baik"
    elif nilai >= 80:
        return "Kinerja sangat baik"
    elif nilai >= 70:
        return "Kinerja baik"
    elif nilai >= 60:
        return "Kinerja rata-rata"
    else:
        return "Kinerja kurang"
    
#contoh penggunaan
nilai = int(input("Masukkan nilai persentase siswa: "))
print(evaluasi_kinerja(nilai))

