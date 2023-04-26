from time import sleep

# !Note!
# run file with sudo for permission to be granted


HOSTS_PATH = "/etc/hosts"
REDIRECT = "127.0.0.1"

blocked_websites = []
while True:
    website = input(
        "Enter Site To Be Blocked [www.example.com || Enter Nothing To Stop]: "
    )
    if website.strip() == "":
        break
    blocked_websites.append(website)
    new_website = website.replace("www.", "")
    blocked_websites.append(new_website)
while True:
    with open(HOSTS_PATH, "r+", encoding="utf-8") as file:
        content = file.read()
        for website in blocked_websites:
            if website not in content:
                file.write(REDIRECT + " " + website + "\n")
    sleep(5)
