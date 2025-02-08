import requests
import re

def fetch_playlist_url():
    print("Fetching playlist URL...")
    id = "dlxwzh"
    idn = {
        "dlxwzh": "tcb3IB5",
        "dlsh": "JzcFkF4",
        "dlwt": "hxT7Fc3",
        "dlys": "8cuL6wa",
        "dlse": "q6tZ6Ba",
        "dlgw": "N4S4uAj",
    }
    url = f"https://dlyapp.dltv.cn/apiv4.5/api/m3u8_notoken?channelid={idn[id]}"
    print(f"URL: {url}")
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch URL: {url}")
        return
    info = response.text
    print(f"API Response: {info}")
    match = re.search(r'"address":"(.*?)"', info)
    if not match:
        print("Failed to extract playlist URL from response")
        return
    playlist_url = match.group(1).replace('\\/', '/')
    print(f"Playlist URL: {playlist_url}")
    with open("大连地方台.txt", "w") as file:
        file.write(playlist_url)
    print("File written successfully")

if __name__ == "__main__":
    fetch_playlist_url()
