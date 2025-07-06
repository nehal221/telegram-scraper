import os
import time
import webbrowser
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch

def play_sound():
    try:
        os.system("mpv sound.mp3 --no-video > /dev/null 2>&1 &")
    except:
        pass

def animate_start():
    play_sound()
    for i in range(3):
        print("\033[1;32m[+] Loading Tool" + "." * (i + 1) + "\033[0m")
        time.sleep(1)
    os.system("clear")

def banner():
    os.system("clear")
    print("\033[1;31m=============================")
    print("     TELEGRAM SCRAPER PRO")
    print("=============================")
    print("TOLL OWNER: NEHAL DARK TRAP")
    print("YT: NEHAL DARK TRAP")
    print("INSTA: nehal_dark_trap")
    print("=============================\033[0m")

def open_link(link):
    try:
        os.system(f"xdg-open '{link}'")  # Forcefully open browser
    except:
        webbrowser.open(link)

def subscription_lock():
    while True:
        banner()
        print("\033[1;32m1. Subscribe Channel")
        print("2. Already Subscribed\033[0m")
        print("\033[1;31m", end="")
        choice = input("Enter your choice (1/2): ")
        print("\033[0m", end="")

        if choice == "1":
            print("🔁 Opening YouTube...")
            open_link("https://youtube.com/@nehal_dark_trap?si=CGE96-qu0BhVGHvi")
        elif choice == "2":
            break
        else:
            print("❌ Invalid input. Try again.")
            time.sleep(1)

def main_menu():
    while True:
        banner()
        print("\033[1;36m1. Join Telegram Group")
        print("2. Follow on Instagram")
        print("3. Scrape Group Users\033[0m")
        print("\033[1;31m", end="")
        choice = input("Enter your choice (1/2/3): ")
        print("\033[0m", end="")

        if choice == "1":
            open_link("https://t.me/NEHAL_DARK_TRAP")
        elif choice == "2":
            open_link("https://www.instagram.com/nehal_dark_trap?igsh=b2YxMDJnbjlzcm5r")
        elif choice == "3":
            scrape_users()
        else:
            print("❌ Invalid input!")
            time.sleep(1)

def scrape_users():
    api_id = int(input("Enter Telegram API ID: "))
    api_hash = input("Enter Telegram API HASH: ")
    phone = input("Enter your Telegram Phone Number: ")

    client = TelegramClient("session", api_id, api_hash)
    client.connect()
    if not client.is_user_authorized():
        client.send_code_request(phone)
        client.sign_in(phone, input("Enter the code you received: "))

    group_username = input("Enter public group username (without @): ")
    users = []

    try:
        group = client.get_entity(group_username)
        all_participants = client(GetParticipantsRequest(
            group, ChannelParticipantsSearch(''), 0, 10000, hash=0
        ))

        for user in all_participants.users:
            if user.username:
                users.append("@" + user.username)
                print(f"[✓] Found: @{user.username}")
                time.sleep(0.3)

        with open("users.txt", "w") as f:
            for u in users:
                f.write(u + "\n")

        print(f"\n✅ Done! {len(users)} usernames saved to users.txt")

    except Exception as e:
        print(f"❌ Error: {e}")

    client.disconnect()

# 🟢 Run Tool
animate_start()
subscription_lock()
main_menu()
