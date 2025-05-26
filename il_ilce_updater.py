# il_ilce_updater.py
import requests
import json

def fetch_and_save_iller_ilceler():
    try:
        iller_url = "https://namazvakti.diyanet.gov.tr/tr-TR/namazvakti/il"
        iller_response = requests.get(iller_url)
        iller = iller_response.json()

        full_data = []

        for il in iller:
            il_id = il["IlID"]
            il_ad = il["IlAd"]
            ilceler_url = f"https://namazvakti.diyanet.gov.tr/tr-TR/namazvakti/il/{il_id}"
            ilceler_response = requests.get(ilceler_url)
            ilceler = ilceler_response.json()
            full_data.append({
                "il": il_ad,
                "il_id": il_id,
                "ilceler": ilceler
            })

        with open("iller_ilceler.json", "w", encoding="utf-8") as f:
            json.dump(full_data, f, ensure_ascii=False, indent=2)

        return {"status": "ok", "message": "İl ve ilçeler başarıyla güncellendi."}

    except Exception as e:
        return {"status": "error", "message": str(e)}
