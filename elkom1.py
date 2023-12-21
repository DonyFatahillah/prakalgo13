nilai = [85, 90, 78, 92, 88]

rata_rata = sum(nilai) / 5

print(f"Nilai : {nilai}")

print(f"Rata Ratanya : {rata_rata}")

nilaisiswa = [siswa for siswa in nilai if siswa > rata_rata]
print(f"Siswa Di Atas Rata Rata : {nilaisiswa}")
