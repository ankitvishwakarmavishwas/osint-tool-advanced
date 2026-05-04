import requests

PLATFORMS = {
    "GitHub": "https://github.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "Twitter": "https://twitter.com/{}"
}

def check_username(username):
    results = []

    for platform, url in PLATFORMS.items():
        full_url = url.format(username)

        try:
            r = requests.get(full_url, timeout=5)
            status = "Found" if r.status_code == 200 else "Not Found"
        except:
            status = "Error"

        results.append({
            "platform": platform,
            "url": full_url,
            "status": status
        })

    return results