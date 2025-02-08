import requests
import re

def fetch_playlist_url():
    print("Fetching playlist URL...")
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
        print(f"URL: {url}")
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Failed to fetch URL for {channel_name}: {url}")
            continue
        info = response.text
        print(f"Full API Response for {channel_name}: {info}")
        match = re.search(r'"address":"(.*?)"', info)
        if not match:
            print(f"Failed to extract playlist URL for {channel_name} from response")
            continue
        playlist_url = match.group(1).replace('\\/', '/')
        print(f"Playlist URL for {channel_name}: {playlist_url}")
        output_lines.append(f"{channel_name},{playlist_url}")
    with open("大连地方台.txt", "w") as file:
        file.write("\n".join(output_lines))
    print("File written successfully")

if __name__ == "__main__":
    fetch_playlist_url()
