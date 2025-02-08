import requests
import re

def fetch_playlist_url():
    idn = {
        "大连新闻综合": "tcb3IB5",
        "大连生活": "JzcFkF4",
        "大连文体": "hxT7Fc3",
        "大连影视": "8cuL6wa",
        "大连少儿": "q6tZ6Ba",
        "大连购物": "N4S4uAj",
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    output_lines = []
    for channel_name, channel_id in idn.items():
        url = f"https://dlyapp.dltv.cn/apiv4.5/api/m3u8_notoken?channelid={channel_id}"
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            continue
        info = response.text
        match = re.search(r'"address":"(.*?)"', info)
        if not match:
            continue
        playlist_url = match.group(1).replace('\\/', '/')
        output_lines.append(f"{channel_name},{playlist_url}")
    with open("大连地方台.txt", "w") as file:
        file.write("\n".join(output_lines))

if __name__ == "__main__":
    fetch_playlist_url()
