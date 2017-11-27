import sys
hurap_file = open(sys.argv[1],"r")
schuckscii_file = open(sys.argv[2], "r")
virus_codes_file = open(sys.argv[3], "r")

def hexadecimal(sayi):
    liste = []
    bolum = sayi
    string = ""
    while bolum != 0:
        kalan = int(bolum) % 16
        bolum = int(bolum / 16)
        if kalan == 10:
            liste.append('A')
        elif kalan == 11:
            liste.append('B')
        elif kalan == 12:
            liste.append('C')
        elif kalan == 13:
            liste.append('D')
        elif kalan == 14:
            liste.append('E')
        elif kalan == 15:
            liste.append('F')
        else:
            liste.append(str(kalan))
    if sayi == 0:
        liste.append(str(sayi))
    liste.reverse()
    string = ''.join(liste)
    return string

def onlaltitoon(sayi):
    sayi = sayi[::-1]
    liste = []
    liste.append(sayi)
    sayac = 0
    toplam = 0
    for harf in liste[0]:
        if harf == 'A':
            toplam += int(10)*(16**sayac)
        elif harf == 'B':
            toplam += int(11) * (16 ** sayac)
        elif harf == 'C':
            toplam += int(12) * (16 ** sayac)
        elif harf == 'D':
            toplam += int(13) * (16 ** sayac)
        elif harf == 'E':
             toplam += int(14) * (16 ** sayac)
        elif harf == 'F':
            toplam += int(15) * (16 ** sayac)
        else:
            toplam += int(harf)*(16**sayac)
        sayac+=1
    return toplam

def ontoiki(sayi):
    liste = []
    bolum = sayi
    string = ""
    while bolum != 0 :
        kalan = int(bolum%2)
        bolum = int(bolum / 2)
        liste.append(str(kalan))
    if len(liste) == 6:
        liste.append('0')
        liste.append('0')
    elif len(liste) == 7:
        liste.append('0')
    elif len(liste) == 5:
        liste.append('0')
        liste.append('0')
        liste.append('0')
    elif len(liste) == 4:
        liste.append('0')
        liste.append('0')
        liste.append('0')
        liste.append('0')
    elif len(liste) == 3:
        liste.append('0')
        liste.append('0')
        liste.append('0')
        liste.append('0')
        liste.append('0')
    elif len(liste) == 2:
        liste.append('0')
        liste.append('0')
        liste.append('0')
        liste.append('0')
        liste.append('0')
        liste.append('0')
    elif len(liste) == 1:
        liste.append('0')
        liste.append('0')
        liste.append('0')
        liste.append('0')
        liste.append('0')
        liste.append('0')
        liste.append('0')
    elif len(liste) == 0:
        liste.append('0')
        liste.append('0')
        liste.append('0')
        liste.append('0')
        liste.append('0')
        liste.append('0')
        liste.append('0')
        liste.append('0')
    liste.reverse()
    string = ''.join(liste)
    return string

print("""*********************
     Mission 00 
*********************""", end="\n\n")

print("""--- hex of encrypted code ---
-----------------------------""", end="\n\n")
liste2 = []
liste3 = []
liste=hurap_file.read().splitlines()
string = ""
string2 = ""
elemansayisi = 4
sonuc = 0
sayac = 0
complement = []
while sayac < len(liste):
 for numbers in liste[sayac]:
    if numbers != '0' and numbers != '1':
        complement.append(liste[sayac][1:])
        break
    liste2.append(numbers)
    if len(liste2) == 4:
        for sayilar in liste2:
            string+=sayilar
        for c in string:
            elemansayisi-=1
            sonuc = sonuc + (int(c)*(2**elemansayisi))
        sonuc = hexadecimal(sonuc)
        liste3.append(sonuc)
        sonuc = 0
        elemansayisi = 4
        liste2.clear()
        string = ""
 for rakam in liste3:
    string2 += rakam
 if string2 != "":
     print(string2.upper())
 string2 = ""
 liste3.clear()
 sayac+=1
print("""\n--- encrypted code ----
-----------------------""", end="\n\n")
hurap_file.seek(0)
liste2 = []
liste3 = []
listee = []
liste4 = []
string3 = ""
liste5 = []
liste=hurap_file.read().splitlines()
read = schuckscii_file.readline()
while read != "":
    listee.append(read.split("\t"))
    read = schuckscii_file.readline()
sayac = 0
strng = ""
while sayac < len(liste):
 for numbers in liste[sayac]:
    if numbers != '0' and numbers != '1':
        break
    liste2.append(numbers)
    if len(liste2) == 4:
        for sayilar in liste2:
            string+=sayilar
        for c in string:
            elemansayisi-=1
            sonuc = sonuc + (int(c)*(2**elemansayisi))
        sonuc = hexadecimal(sonuc)
        liste3.append(sonuc)
        if len(liste3) == 2:
            for harf in liste3:
                string2 += harf
            string3 = string2.upper()
            for sayi in range(0,len(listee)):
                if string3 == listee[sayi][1]:
                    liste4.append(listee[sayi][0])
            liste3.clear()
            string2 = ""
        sonuc = 0
        elemansayisi = 4
        liste2.clear()
        string = ""
 for harf in liste4:
     strng += harf
 liste4.clear()
 if strng != "":
     print(strng)
 strng = ""
 sayac+=1
print("""\n--- decrypted code ---
----------------------""", end="\n\n")
strr = ""
strr2 = ""
complement2 = []
for harf in complement:
    strr+=harf
if complement[0][0] == '0':
    shift_amound = (int(strr,2))
else:
    for harf in strr:
        if harf == '1':
            complement2.append('0')
        elif harf == '0':
            complement2.append('1')
    for harf in complement2:
        strr2 += harf
    shift_amound = -(int(strr2,2)+1)
schuckscii_file.seek(0)
hurap_file.seek(0)
liste2 = []
liste3 = []
listee = []
liste4 = []
string3 = ""
encrypted_list = []
encrypted_str = ""
encrypted_str2 = ""
liste=hurap_file.read().splitlines()
read = schuckscii_file.readline()
while read != "":
    listee.append(read.split("\t"))
    read = schuckscii_file.readline()
sayac = 0
num_in_memory = 0
encrypted_char = 0
while sayac < len(liste):
 for numbers in liste[sayac]:
    if numbers != '0' and numbers != '1':
        break
    liste2.append(numbers)
    if len(liste2) == 4:
        for sayilar in liste2:
            string+=sayilar
        for c in string:
            elemansayisi-=1
            sonuc = sonuc + (int(c)*(2**elemansayisi))
        sonuc = hexadecimal(sonuc)
        liste3.append(sonuc)
        if len(liste3) == 2:
            for harf in liste3:
                string2 += harf
            string3 = string2.upper()
            for sayi in range(0,len(listee)):
                if string3 == listee[sayi][1]:
                    liste4.append(listee[sayi][0])
            liste3.clear()
            string2 = ""
        sonuc = 0
        elemansayisi = 4
        liste2.clear()
        string = ""
 for harf in liste4:
     strng+=harf
 if strng != "":
     for harf in liste4:
         for sayi in range(0,len(listee)):
             if harf == listee[sayi][0]:
                 num_in_memory = sayi + 1
                 encrypted_char = (num_in_memory - shift_amound) % len(listee)
                 encrypted_list.append(listee[encrypted_char-1][0])
 for harf in encrypted_list:
     encrypted_str+=harf
 if encrypted_str != "":
     encrypted_str2 += encrypted_str + "\n"
     print(encrypted_str)
 encrypted_str = ""
 encrypted_list.clear()
 strng = ""
 liste4.clear()
 sayac+=1
print("""\n*********************
     Mission 01 
*********************""", end="\n\n")
sarkac = 0
stringg = ""
stringg2 = ""
read2 = virus_codes_file.readline()
virus_codes_list = []
virus_codes_list2 = []
while read2 != "":
    virus_codes_list.append(read2.split(":"))
    read2 = virus_codes_file.readline()
for sayi3 in range(len(virus_codes_list)):
    for harf in virus_codes_list[sayi3][1]:
        stringg2+=harf
    virus_codes_list2.append(stringg2.split("\n"))
    stringg2 = ""
encrypted_list2 = encrypted_str2.split("\n")
for sayi in range(0,len(virus_codes_list2)):
    harf = virus_codes_list[sayi][0]
    encrypted_str2=encrypted_str2.replace(harf,virus_codes_list2[sayi][0])
listey = encrypted_str2.split("\n")
while sarkac < len(listey):
    for harf in listey[sarkac]:
        stringg+=harf
    print(stringg)
    stringg = ""
    sarkac+=1
print("""\n*********************
     Mission 10 
*********************""", end="\n\n")


print("""--- encrypted code ---
----------------------""", end="\n\n")
sayim = 0
stringler = ""
encrypted_list3 = []
while sayim < len(listey):
    for harf in listey[sayim]:
        for sayi in range(len(listee)):
            if harf == listee[sayi][0]:
                num_in_memory2 = sayi + 1
                encrypted_char2 = (num_in_memory2 + shift_amound) % len(listee)
                encrypted_list3.append(listee[encrypted_char2-1][0])
    sayim +=1
    for harf in encrypted_list3:
        stringler += harf
    print(stringler)
    stringler = ""
    encrypted_list3.clear()
print("""\n--- hex of encrypted code ---
-----------------------------""", end="\n\n")
sayim = 0
encrypted_list3 = []
encrypted_list4 = []
stringleer = ""
while sayim < len(listey):
    for harf in listey[sayim]:
        for sayi in range(len(listee)):
            if harf == listee[sayi][0]:
                num_in_memory2 = sayi + 1
                encrypted_char2 = (num_in_memory2 + shift_amound) % len(listee)
                encrypted_list3.append(listee[encrypted_char2-1][0])
    sayim +=1
    for harf in encrypted_list3:
        for sayi in range(len(listee)):
            if harf == listee[sayi][0]:
                encrypted_list4.append(listee[sayi][1])
    for harf2 in encrypted_list4:
        stringleer += harf2
    print(stringleer)
    stringleer = ""
    encrypted_list4.clear()
    encrypted_list3.clear()
print("""\n--- bin of encrypted code ---
-----------------------------""", end="\n\n")
sayim = 0
encrypted_list3 = []
encrypted_list4 = []
stringgg = ""
while sayim < len(listey):
    for harf in listey[sayim]:
        for sayi in range(len(listee)):
            if harf == listee[sayi][0]:
                num_in_memory2 = sayi + 1
                encrypted_char2 = (num_in_memory2 + shift_amound) % len(listee)
                encrypted_list3.append(listee[encrypted_char2-1][0])
    sayim +=1
    for harf in encrypted_list3:
        for sayi in range(len(listee)):
            if harf == listee[sayi][0]:
                encrypted_list4.append(listee[sayi][1])
    for harf in encrypted_list4:
        harf = onlaltitoon(harf)
        harf = ontoiki(harf)
        stringgg += harf
    print(stringgg)
    stringgg = ""
    encrypted_list4.clear()
    encrypted_list3.clear()

hurap_file.close()
schuckscii_file.close()
virus_codes_file.close()