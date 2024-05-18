import random
import time

# Daftar nama umum di Amerika
nama_umum = [
    # Nama dari Amerika
    "James", "Mary", "John", "Patricia", "Robert", "Jennifer",
    "Michael", "Linda", "William", "Elizabeth", "David", "Barbara",
    "Richard", "Susan", "Joseph", "Jessica", "Thomas", "Sarah",
    "Charles", "Karen",
    # Nama dari Indonesia dan Asia Tenggara
    "Andi", "Siti", "Budi", "Dewi", "Agus", "Rina",
    "Bayu", "Intan", "Rizki", "Fitri", "Yanto", "Wati",
    "Joko", "Sri", "Hendra", "Ayu", "Rudi", "Maya",
    "Ali", "Lina", "Tono", "Desi", "Ahmad", "Nur",
    "Umar", "Ratna", "Hadi", "Ani"
]
# fungsi menghasilkan nomor HP acak
def generatePhoneNumber():
    return ''.join(random.choice("0123456789") for _ in range(12))

# fungsi membuat list kontak dengan nama dan nomor HP acak
def createContactList(nomorKontak):
    kontak = []
    nama_terpakai = {}

    for _ in range(nomorKontak):
        nama = random.choice(nama_umum)
        if nama in nama_terpakai:
            nama_terpakai[nama] += 1
            nama_final = f"{nama}{nama_terpakai[nama]}"
        else:
            nama_terpakai[nama] = 1
            nama_final = nama
        
        nomor_hp = generatePhoneNumber()
        kontak.append({"namaKontak": nama_final, "nomorHP": nomor_hp})

    return kontak

# Panggil fungsi createContactList
jumlah_kontak = 2000
daftar_kontak = createContactList(jumlah_kontak)


# print daftar kontak
for kontak in daftar_kontak:
    print("Nama Kontak:", kontak["namaKontak"], ", Nomor HP:", kontak["nomorHP"])

# Mengurutkan daftar kontak berdasarkan nama kontak
daftar_kontak_sorted = sorted(daftar_kontak, key=lambda x: x["namaKontak"])

# fungsi pencarian dengan algoritma linear search
def linearSearch(daftar_kontak, nama_kontak):
    for kontak in daftar_kontak:
        if kontak["namaKontak"] == nama_kontak:
            return kontak
    return "Nama kontak tidak ditemukan."

# fungsi pencarian dengan algoritma sequensial search
def binarySearch(daftar_kontak, nama_kontak):
    low = 0
    high = len(daftar_kontak) - 1

    while low <= high:
        mid = (low + high) // 2
        if daftar_kontak[mid]["namaKontak"] == nama_kontak:
            return daftar_kontak[mid]
        elif daftar_kontak[mid]["namaKontak"] < nama_kontak:
            low = mid + 1
        else:
            high = mid - 1
    return "Nama kontak tidak ditemukan."

# fungsi pencarian dengan algoritma binary search
def sequentialSearch(daftar_kontak, nama_kontak):
    for kontak in daftar_kontak:
        if kontak["namaKontak"] == nama_kontak:
            return kontak
    return "Nama kontak tidak ditemukan."


# Meminta pengguna memasukkan nama kontak yang ingin dicari
nama_cari = input("\nMasukkan nama kontak yang ingin dicari: ")

# Mencari nama kontak linear Search
hasil_Linear = linearSearch(daftar_kontak, nama_cari)
if isinstance(hasil_Linear, dict):
    print("\nKontak ditemukan:")
    print("Nama Kontak:", hasil_Linear["namaKontak"], ", Nomor HP:", hasil_Linear["nomorHP"])
else:
    print("\n", hasil_Linear)

# Mencari nama kontak menggunakan Sequential Search
hasil_sequential = sequentialSearch(daftar_kontak_sorted, nama_cari)
if isinstance(hasil_sequential, dict):
    print("\nKontak ditemukan (Sequential Search):")
    print("Nama Kontak:", hasil_sequential["namaKontak"], ", Nomor HP:", hasil_sequential["nomorHP"])
else:
    print("\n", hasil_sequential)

# Mencari nama kontak menggunakan Binary Search
hasil_binary = binarySearch(daftar_kontak_sorted, nama_cari)
if isinstance(hasil_binary, dict):
    print("\nKontak ditemukan (Binary Search):")
    print("Nama Kontak:", hasil_binary["namaKontak"], ", Nomor HP:", hasil_binary["nomorHP"])
else:
    print("\n", hasil_binary)

# Fungsi untuk mengukur waktu eksekusi
def measure_time(search_function, arr, x):
    start_time = time.time()
    search_function(arr, x)
    end_time = time.time()
    return (end_time - start_time) * 1000  # Waktu dalam milidetik

# Tes dengan 1000 pencarian
search_count = 1000
linear_times = []
binary_times = []
sequential_times = []

for _ in range(search_count):
    search_contact = random.choice(daftar_kontak)["namaKontak"]
    
    # Linear Search
    linear_times.append(measure_time(linearSearch, daftar_kontak, search_contact))
    
    # Binary Search
    binary_times.append(measure_time(binarySearch, daftar_kontak_sorted, search_contact))
    
    # Sequential Search
    sequential_times.append(measure_time(sequentialSearch, daftar_kontak, search_contact))

# Rata-rata waktu eksekusi
avg_linear_time = sum(linear_times) / search_count
avg_binary_time = sum(binary_times) / search_count
avg_sequential_time = sum(sequential_times) / search_count

print("\nHasil pengukuran waktu eksekusi:")
print(f"Rata-rata waktu pencarian Linear Search: {avg_linear_time:.4f} ms")
print(f"Rata-rata waktu pencarian Binary Search: {avg_binary_time:.4f} ms")
print(f"Rata-rata waktu pencarian Sequential Search: {avg_sequential_time:.4f} ms")