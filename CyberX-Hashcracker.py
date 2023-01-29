#kütüphaneler
import hashlib

#banner
print('''

 _____       _             __   __      _   _           _                         _             
/  __ \     | |            \ \ / /     | | | |         | |                       | |            
| /  \/_   _| |__   ___ _ __\ V /      | |_| | __ _ ___| |__   ___ _ __ __ _  ___| | _____ _ __ 
| |   | | | | '_ \ / _ \ '__/   \      |  _  |/ _` / __| '_ \ / __| '__/ _` |/ __| |/ / _ \ '__|
| \__/\ |_| | |_) |  __/ | / /^\ \     | | | | (_| \__ \ | | | (__| | | (_| | (__|   <  __/ |   
 \____/\__, |_.__/ \___|_| \/   \/     \_| |_/\__,_|___/_| |_|\___|_|  \__,_|\___|_|\_\___|_|   
        __/ |                                                                                   
       |___/                                                                                    

''')

#girdiler
wlist = input("wordlist: ")
hash2crack = input("hash: ")

#dosya okuma işlemi
wlistlines = open(wlist, "r").readlines()

#döngü
for i in range(0, len(wlistlines)):
    hash2comp = hashlib.md5(wlistlines[i].replace("\n","").encode()).hexdigest()
    if hash2crack == hash2comp:
        print("Şifre Bulundu: "+wlistlines[i].replace("\n",""))
        exit()
print("Şifre bulunamadı")
