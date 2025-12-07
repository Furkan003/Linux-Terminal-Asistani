import os
import sys
import time
import json
import random
import google.generativeai as genai

def get_api_key():
    # 1. Ortam değişkenine bakar
    api_key = os.getenv("DOKTOR_API_KEY")

    # 2. Yoksa kullanıcıdan ister
    if not api_key:
        print("\n" + "*"*60)
        print("UYARI: Bu programın çalışması için Google Gemini API Key gereklidir.")
        print("Lütfen sağlayıcıdan aldığınız anahtarı girin.")
        print("*"*60 + "\n")
        api_key = input("API Key'i yapıştır ve Enter'a bas: ").strip()
    
    if not api_key:
        print("Anahtar girilmedi, program kapatılıyor...")
        time.sleep(2)
        sys.exit()
        
    return api_key

def main():
    # Ekranı temizle
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # API Key'i al
    benim_anahtarim = get_api_key()
    
    print(f"\nAnahtar alındı, sisteme bağlanılıyor...\n")

    # --- KRİTİK EKLEME: API'Yİ YAPILANDIRMA ---
    try:
        genai.configure(api_key=benim_anahtarim)
        # Modeli seçiyoruz (Gemini Pro)
        model = genai.GenerativeModel('gemini-2.5-flash')
        print("Bağlantı Başarılı! Doktor şu an seni dinliyor. (Çıkmak için 'q' bas)")
    except Exception as e:
        print(f"Hata oluştu: {e}")
        input()
        sys.exit()

    # --- SOHBET DÖNGÜSÜ ---
    while True:
        soru = input("\nSen: ")
        
        if soru.lower() == 'q':
            print("Görüşürüz kral...")
            break
            
        if soru.strip() == "":
            continue
            
        print("Doktor düşünüyor...")
        
        try:
            # Soruyu Google'a gönderip cevap alıyoruz
            response = model.generate_content(soru)
            print(f"Doktor: {response.text}")
        except Exception as e:
            print(f"Bir hata oldu: {e}")

    input("\nKapatmak için Enter'a bas...")

if __name__ == "__main__":
    main()