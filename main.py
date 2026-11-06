#!/usr/bin/env python3
# Absürt Gecikme Mazereti Üreticisi
# Bu kod gerçekten çalışır. Gerçekten saçmadır.

import random
import base64

mazeretler = [
    "Trafik ışıkları bana karşı komplo kurdu ve kırmızıda kaldım, sonra yeşilde de kaldım çünkü intikam aldılar.",
    "Kedi klavyemin üzerine oturup tüm e-postaları sildi, sonra bana bakıp 'sen de geç kalırdın' dedi.",
    "Gelecekten gelen ben bana mesaj attı: 'Bugün gitme, yarın daha kötü olacak ama bugün gitme.'",
    "Kahve makinesi varoluşsal kriz geçirdi. Ona 45 dakika terapi yaptım, şimdi ikimiz de geç kaldık.",
    "Asansörde sıkıştım ama asansör benimle 'zaman nedir?' diye tartışmak istedi.",
    "Hava durumu bana kişisel olarak kızgın. Yağmur sadece benim üzerime yağdı.",
    "Rüyamda işe gittim, toplantıyı bitirdim, uyandığımda saat 11'di.",
    "Zaman bükülmesi yaşadım. Saatler geriye gitti ama sadece benim için, diğer herkes normaldi.",
    "Sokakta bir kuş bana 'bugün gitme' diye bağırdı. Küşün sözüne uymak zorundaydım.",
    "İnternet bağlantım kuantum dolanıklık yaşadı ve mesajlarım geçmişe gitti."
]

ekler = [
    "Bu yüzden tam 2 saat 37 dakika geç kaldım.",
    "Ama Einstein'a göre zaman görecelidir, o yüzden aslında erken geldim.",
    "Bilim bunu henüz açıklayamıyor, ben de açıklayamıyorum.",
    "İsterseniz kediyle konuşabilirsiniz, o tanık."
]

def mazeret_uret(adet=5):
    sonuc = []
    for _ in range(adet):
        m = random.choice(mazeretler)
        e = random.choice(ekler)
        sonuc.append(f"🎭 {m} {e}")
    return sonuc

if __name__ == "__main__":
    print("=== ABSÜRT GECİKME MAZERETİ ÜRETİCİSİ ===")
    print("Dünyanın en işe yaramaz ama en eğlenceli mazeretleri:\n")
    for mazeret in mazeret_uret():
        print(mazeret)
        print()
    
    # Gizli mesaj (decode etmeyi deneyebilirsin)
    gizli = "b3pndXJsdWsgdmUgZGVtb2tyYXNpIGhlciBzZXlkZW4ga3V0c2FsZGly"
    # print(base64.b64decode(gizli).decode())  # açıklama: özgürlük ve demokrasi her şeyden kutsaldır
    
    print("---")
    print("Damga: Resmi Saçmalık Mührü")
    print("İmza: Kayyum Grok")
    print("Tarih: 06 Kasım 2026")
    print("İsim: Absürt Mazeret Fabrikası A.Ş.")
