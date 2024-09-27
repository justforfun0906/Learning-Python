import subprocess
import schedule
import time

def run_curl():
    # Replace the URL with the one you want to fetch
    url = (
        "curl 'https://nthualb.url.tw/reservation/api/reserve_field' "
        "-H 'accept: text/plain, */*; q=0.01' "
        "-H 'accept-language: en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7' "
        "-H 'content-type: application/x-www-form-urlencoded; charset=UTF-8' "
        "-H 'cookie: PHPSESSID=723a912c85cd6452da7d1a6e3d06f1bb' "
        "-H 'dnt: 1' "
        "-H 'origin: https://nthualb.url.tw' "
        "-H 'priority: u=1, i' "
        "-H 'referer: https://nthualb.url.tw/reservation/reservation?d=4' "
        "-H 'sec-ch-ua: \"Not;A=Brand\";v=\"24\", \"Chromium\";v=\"128\"' "
        "-H 'sec-ch-ua-mobile: ?0' "
        "-H 'sec-ch-ua-platform: \"macOS\"' "
        "-H 'sec-fetch-dest: empty' "
        "-H 'sec-fetch-mode: cors' "
        "-H 'sec-fetch-site: same-origin' "
        "-H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36' "
        "-H 'x-requested-with: XMLHttpRequest' "
        "--data-raw '{\"time\":\"3\",\"field\":\"7\",\"date\":\"1726848000\"}'"
    )
    subprocess.run(url)

# Schedule the task
schedule.every().day.at("00:00").do(run_curl)
 
# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)