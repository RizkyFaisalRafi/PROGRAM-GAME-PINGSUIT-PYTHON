
# Membuat import library random yang menghasilkan elemen secara acak
import random

# Tambahkan 2 variable tampungan yaitu skor_player dan skor_komputer
skor_player = 0
skor_komputer = 0

# Menambahkan rule permainan (Escape Characters)
print("Manusia\tvs\tGajah\t=\tGajah Win")
print("Semut\tvs\tManusia\t=\tManusia Win")
print("Gajah\tvs\tSemut\t=\tSemut Win")

# Gunakan perulangan while karena akan dilakukan looping terus menerus sampai ada yang mendapatkan skor 3 poin
while(True):
    # Buat variaber player yg bersifat inputan dan bot yg menggunakan library random dengan method choice()
    # yang digunakan untuk memilih secara acak dari variabel temp_list
    player = input("Masukan pilihan (gajah, manusia, semut)")
    temp_list = ["gajah", "manusia", "semut"]
    bot = random.choice(temp_list)
    print(f"bot mendapatkan {bot}\n")

# Percabangan pertama dilakukan pengecekan jika hasil inputan player dan bot sama.
    if player == bot:
        print(
            f"Kamu dan komputer sama sama memilih {player}, skor kamu {skor_player} dan skor komputer {skor_komputer}")

# Percabagan kedua dilakukan pengecekan hasil pingsut apabila player adalah pemenang, jika menang akan mendapatkan poin tambahan 1
# dan jika total poin sudah sama dengan 3 maka perulangan akan berhenti
    elif((player == "gajah" and bot == "manusia") or (player == "manusia" and bot == "semut") or (player == "semut" and bot == "gajah")):
        skor_player += 1  # skor_player = skor_player + 1
        if skor_player != 3:
            print(
                f"Selamat kamu menang, pertahankan, skor kamu {skor_player} dan skor komputer {skor_komputer}")
        else:
            print(
                f"Hore kamu menang atas komputer, selamat yaa! skor kamu {skor_player} dan skor komputer {skor_komputer}")
            break

# Percabangan ketiga mekanismenya samadengan percabagan kedua yaitu kondisi apabila bot menang
    else:
        skor_komputer += 1
        if skor_komputer != 3:
            print(
                f"Yah kamu belum beruntung, skor kamu {skor_player} dan skor komputer {skor_komputer}")
        else:
            print(
                f"Yah kamu kalah mekanik dari komputer, coba lagi ya! skor kamu {skor_player} dan skor komputer {skor_komputer}")
            break
