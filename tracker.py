import requests
import sys

def track(ip):
    r = requests.get(f"http://ip-api.com/json/{ip}").json()
    if r["status"] == "success":
        print(f"""
IP       : {r['query']}
Location : {r['city']}, {r['regionName']}, {r['country']}
ISP      : {r['isp']}
Org      : {r['org']}
Lat/Lon  : {r['lat']}, {r['lon']}
Timezone : {r['timezone']}
        """)
    else:
        print("Lookup failed.")

track(sys.argv[1] if len(sys.argv) > 1 else "8.8.8.8")# <---IP goes here