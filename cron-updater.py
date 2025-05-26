# cron-updater.py
from il_ilce_updater import fetch_and_save_iller_ilceler

if __name__ == "__main__":
    result = fetch_and_save_iller_ilceler()
    print(result)
