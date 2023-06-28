import random
import tkinter as tk

def kelime_sec():
    kelimeler = ["elma", "armut", "portakal", "muz", "çilek", "kiraz", "karpuz", "erik"]
    return random.choice(kelimeler)

def kelimeyi_goster(kelime, tahmin_edilen_harfler):
    kelime_str = ""
    for harf in kelime:
        if harf in tahmin_edilen_harfler:
            kelime_str += harf + " "
        else:
            kelime_str += "_ "
    return kelime_str.strip()

def tahmin_al():
    tahmin = tahmin_entry.get()
    tahmin_entry.delete(0, tk.END)
    return tahmin.lower()

def tahmin_yap():
    tahmin = tahmin_al()

    if len(tahmin) == 1:
        if tahmin in tahmin_edilen_harfler:
            mesaj.set("Bu harfi zaten tahmin ettiniz.")
        elif tahmin in kelime:
            tahmin_edilen_harfler.append(tahmin)
            kelime_str = kelimeyi_goster(kelime, tahmin_edilen_harfler)
            kelime_label.config(text=kelime_str)
            if "_" not in kelime_str:
                mesaj.set("Tebrikler! Kelimeyi doğru tahmin ettiniz.")
                tahmin_button.config(state=tk.DISABLED)
        else:
            hatali_tahmin()
    else:
        if tahmin == kelime:
            mesaj.set("Tebrikler! Kelimeyi doğru tahmin ettiniz.")
            tahmin_button.config(state=tk.DISABLED)
        else:
            hatali_tahmin()

    tahmin_entry.focus()

def hatali_tahmin():
    global haklar
    haklar -= 1
    mesaj.set("Yanlış tahmin! Kalan hakkınız: {}".format(haklar))
    if haklar == 0:
        mesaj.set("Maalesef hakkınız bitti. Doğru kelime: {}".format(kelime))
        tahmin_button.config(state=tk.DISABLED)

def oyunu_baslat():
    global kelime, tahmin_edilen_harfler, haklar
    kelime = kelime_sec()
    tahmin_edilen_harfler = []
    haklar = 6
    kelime_str = kelimeyi_goster(kelime, tahmin_edilen_harfler)
    kelime_label.config(text=kelime_str)
    tahmin_button.config(state=tk.NORMAL)
    mesaj.set("Kelime Tahmini Oyununa Hoş Geldiniz!")

# Ana pencereyi oluştur
pencere = tk.Tk()
pencere.title("Kelime Tahmini Oyunu")
pencere.geometry("400x200")

# Değişkenler
kelime = ""
tahmin_edilen_harfler = []
haklar = 6
mesaj = tk.StringVar()

# Arayüz elemanları
baslik_label = tk.Label(pencere, text="Kelime Tahmini Oyunu", font=("Helvetica", 16))
baslik_label.pack(pady=10)

kelime_label = tk.Label(pencere, text="", font=("Helvetica", 14))
kelime_label.pack(pady=10)

tahmin_entry = tk.Entry(pencere, font=("Helvetica", 12))
tahmin_entry.pack(pady=5)
tahmin_entry.focus()

tahmin_button = tk.Button(pencere, text="Tahmin Et", font=("Helvetica", 12), command=tahmin_yap)
tahmin_button.pack(pady=5)
tahmin_button.config(state=tk.DISABLED)

mesaj_label = tk.Label(pencere, textvariable=mesaj, font=("Helvetica", 12))
mesaj_label.pack(pady=5)

yeni_oyun_button = tk.Button(pencere, text="Yeni Oyun", font=("Helvetica", 12), command=oyunu_baslat)
yeni_oyun_button.pack(pady=5)

# Oyunu başlat
oyunu_baslat()

# Ana döngüyü çalıştır
pencere.mainloop()
