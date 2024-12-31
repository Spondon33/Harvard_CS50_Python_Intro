# 1
url = input("URL: ").strip()
print(url)


# 2
url = input("URL: ").strip()
username = url.replace("https://x.com/", "")
print(f"Username: {username}")


# 3
url = input("URL: ").strip()
username = url.replace("https://x.com/", "")
print(f"Username: {username}")


# 4
url = input("URL: ").strip()
username = url.removeprefix("https://x.com/")
print(f"Username: {username}")


# 5
import re

url = input("URL: ").strip()

username = re.sub(r"^(https?://)?(www\.)?x\.com/", "", url)
print(f"Username: {username}")


# 6
import re

url = input("URL: ").strip()

matches = re.search(r"^(https?://)?(www\.)?x\.com/(.+)$", url, re.IGNORECASE)
if matches:
    print(f"Username: ", matches.group(3))


# 7
import re

url = input("URL: ").strip()

if matches := re.search(r"^(?:https?://)?(?:www\.)?x\.com/([a-zA-Z0-9_]+)$", url, re.IGNORECASE):
    print(f"Username: ", matches.group(1))
