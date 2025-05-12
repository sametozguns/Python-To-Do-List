# Görevleri dosyadan okuma
def gorevleri_yukle():
    try:
        with open("gorevler.txt", "r", encoding="utf-8") as dosya:
            return [satir.strip() for satir in dosya.readlines()]
    except FileNotFoundError:
        return []

# Görevleri dosyaya kaydetme
def gorevleri_kaydet(gorevler):
    with open("gorevler.txt", "w", encoding="utf-8") as dosya:
        for gorev in gorevler:
            dosya.write(gorev + "\n")

# Görevleri göster
def gorevleri_goster(gorevler):
    if not gorevler:
        print("📭 Hiç görev yok.")
    else:
        print("\n📋 Görev Listesi:")
        for i, g in enumerate(gorevler, 1):
            print(f"{i}. {g}")

# Görev ekle
def gorev_ekle(gorevler):
    yeni_gorev = input("✍️ Yeni görev girin: ").strip()
    if yeni_gorev:
        gorevler.append(yeni_gorev)
        gorevleri_kaydet(gorevler)
        print(f"✅ Görev eklendi: {yeni_gorev}")
    else:
        print("⚠️ Boş görev eklenemez.")

# Görev sil
def gorev_sil(gorevler):
    gorevleri_goster(gorevler)
    try:
        index = int(input("Silinecek görev numarası: ")) - 1
        if 0 <= index < len(gorevler):
            silinen = gorevler.pop(index)
            gorevleri_kaydet(gorevler)
            print(f"🗑️ Silindi: {silinen}")
        else:
            print("❌ Geçersiz görev numarası.")
    except ValueError:
        print("❌ Lütfen geçerli bir sayı girin.")

# Görev düzenle
def gorev_duzenle(gorevler):
    gorevleri_goster(gorevler)
    try:
        index = int(input("Düzenlenecek görev numarası: ")) - 1
        if 0 <= index < len(gorevler):
            yeni_gorev = input("Yeni görev: ").strip()
            if yeni_gorev:
                eski = gorevler[index]
                gorevler[index] = yeni_gorev
                gorevleri_kaydet(gorevler)
                print(f"✏️ Güncellendi: {eski} ➡️ {yeni_gorev}")
            else:
                print("⚠️ Boş görev girilemez.")
        else:
            print("❌ Geçersiz görev numarası.")
    except ValueError:
        print("❌ Lütfen geçerli bir sayı girin.")

# Ana program döngüsü
def ana_menu():
    gorevler = gorevleri_yukle()
    while True:
        print("\n🔹 Ana Menü 🔹")
        print("1. Görevleri Göster")
        print("2. Görev Ekle")
        print("3. Görev Sil")
        print("4. Görev Düzenle")
        print("q. Çıkış")
        secim = input("Seçiminiz: ").strip()

        if secim == "1":
            gorevleri_goster(gorevler)
        elif secim == "2":
            gorev_ekle(gorevler)
        elif secim == "3":
            gorev_sil(gorevler)
        elif secim == "4":
            gorev_duzenle(gorevler)
        elif secim.lower() == "q":
            print("👋 Programdan çıkılıyor...")
            break
        else:
            print("❌ Geçersiz seçim. Lütfen menüdeki seçenekleri kullanın.")

# Programı başlat
ana_menu()
