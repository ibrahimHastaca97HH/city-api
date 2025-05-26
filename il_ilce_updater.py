# il_ilce_updater.py
import requests
import json


def fetch_and_save_iller_ilceler():
    il_url = "https://ezanvakti.herokuapp.com/sehirler"
    iller = requests.get(il_url).json()

    data = []

    for il in iller:
        il_adi = il['sehirAdi']
        il_kodu = il['sehirID']

        ilce_url = f"https://ezanvakti.herokuapp.com/ilceler/{il_kodu}"
        try:
            ilceler = requests.get(ilce_url).json()
            ilce_listesi = [{'ilceAdi': ilce['ilceAdi'], 'ilceID': ilce['ilceID']} for ilce in ilceler]

            data.append({
                'ilAdi': il_adi,
                'ilID': il_kodu,
                'ilceler': ilce_listesi
            })
        except:
            continue

    with open("iller_ilceler.json", "w", encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return {"status": "ok", "message": "Veri başarıyla güncellendi"}
