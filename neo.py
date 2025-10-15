print("\n\n\n\n\n\nAssalam-o-alaikum and Welcome to HadiXYT STORE that is the store you are looking for\n\n")


demand = (input("\nhang bro kiya chaye or kiya kar sakta ho ma apky liye?\n\n"))



Banner = ("\n\nPUBG MOBILE UC RATE LIST FOR SPEACIAL DISCOUND USE HADI IS PRO\n\n")

not_avaiable = ("\n\nSorry you are at wrong store my boy")

list = ("\n \n1.60 UC\n 340RS\n \n2.300UC\n 1300RS \n\n3.600UC\n 2600RS \n\n4.1200UC\n 13000RS")

cheapBanner = ("\n\nPUBG MOBILE UC RATE LIST FOR C@rding SPEACIAL DISCOUND USE HADI IS PRO \n IF YOU GOT BAN WE WILL RETURN YOUR MONEY\n\n")

cheaplist = ("\n \n1. 60 UC\n \n2. 300UC\n \n3. 600UC\n \n4. 4000UC\n ")

notcheap = ("\nIf you got no CRYPTO then make a account on binanace or watch tutorial on youtube make the transaction\n")


if demand == "uc" or demand == "uc chaye" or demand == "uc" or demand == "uc chaye bro" or demand == "UC":
    print(Banner)
    print(list)
    discount = (input("\n\nSasti UC chaye ?\n"))
    discount == "ha" or discount == "yes" or discount == "yeah bro"
    print(cheapBanner)
    print(cheaplist)
    cheap = int (input("JUST TYPE NUMBER LIKE IF YOU WANT the first PACK type 60 or if you want the second one type 300\n\n"))
    budget = int (input ("\n\n OR Bro apka Budget kiya hai ?\n\n"))
    if cheap < 60 :
        print("easyPaisa ONLY")
    else:
        print("CRYPTO ONLY")

    if budget < 90 :
        print(" i got better offer\n")
    else:
        print("ok send me the payment and dont play with me like sending the fake screenshot is going to be BAN your PUBG MOBILE ID")

else:
    print(not_avaiable)
    exit()
