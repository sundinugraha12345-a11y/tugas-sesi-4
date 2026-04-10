word= "UNIVERSITAS NUSA PUTRA SUKABUMI"
#A buat jadi putra nusa jadi huruf kecil
print("-"*20)
split_word = word.split()
print(split_word[2].lower(),split_word[1].lower())
reversed = split_word

#B buat jadi universitas nusa putra sukabumi tanpa huruf U
print("-"*20)
split_word = word.split()
print((split_word[0]+" "+split_word[1]+" "+split_word[2]+" "+split_word[3]).replace("U",""))

#C buat jadi sukabumi putra nusa universitas
print("-"*20)
split_word = word.split()
print(split_word[3],split_word[2],split_word[1],split_word[0])

#D buat jadi versitas unps
print("-"*20)
split_word = word.split()
print(split_word[0].replace("IVERSITAS","")+split_word[2].replace("UTRA","")+split_word[3].replace("UKABUMI",""))


#E buat jadi tas sapu bumi
print("-"*20)
split_word = word.split()
print(split_word[0].replace("UNIVERSI",""),split_word[1].replace("NU","")+split_word[2].replace("TRA",""),split_word[3].replace("SUKA",""))
print("-"*20)


