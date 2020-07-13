# This is a simple ATM application.
# we will not use a Database in this project 
# we will use the "Dictionary" instead.

account1={
    "accountno":"1122334455",
    "name":"customer1",    
    "bakiye":"2500",
    "ekbakiye":"2000",
    "limit":"2000"
    }
islemler= "Lütfen yapmak istediğiniz işlemi seçiniz\n\
        1.Bakiye görüntüle\n\
        2.Para çek\n\
        3.Para yatır\n\
        4.Çıkış için q basınız"


print("\n                BANKAMIZA HOŞ GELDİNİZ                \n")




while True:
    print("********************* İŞLEMLER **************************")
    print(islemler)
    print("*********************************************************\n")
    
    islem = input("seçim: ")
    bakiye=int(account1['bakiye'])
    ekbakiye=int(account1['ekbakiye'])
    limit=int(account1['limit'])

    if str(islem) =="q":
        print("Çıkış yapılıyor.. İyi günler diliyoruz..")
        break
    
    elif str(islem)=="1":
        print(f"\n########## Hesabınızda {bakiye} bulunuyor.. ############\n ")

    elif str(islem)=="2":
        cekilen=input("Çekmek istediğiniz miktar: ")
        if int(cekilen)<=int(bakiye):
            bakiye=bakiye-int(cekilen)
            account1['bakiye']=str(bakiye)
            print(f"Hesabınızda kalan miktar: {bakiye}")
        else:
            print("Hesabınızda yeterli miktar bulunmuyor...")
            if (bakiye+ekbakiye)>int(cekilen):
                while True:
                    ekbakiyetalep=input("Ek hesabınızdan kullanmak istermisiniz? e/h: ")
                    if ekbakiyetalep.lower()=="h":
                        break
                    elif ekbakiyetalep.lower()=="e":
                        ekbakiye=ekbakiye-(int(cekilen) - bakiye)
                        account1['ekbakiye']=str(ekbakiye)
                        account1['bakiye']="0"
                        print("\nİşlem gerçekleştirildi.. İşlem sonrası")
                        print("Bakiyenizde kalan miktar: 0")
                        print(f"Ek hesabınızda kalan miktar: {ekbakiye}\n")
                        
                        break
                    else:
                        print("Yanlış seçim..\n")
 
  
    elif str(islem)=="3":
        # print(ekbakiye)
        # print(bakiye)
        yatan=input("Yatırmak istediğiniz miktar: ")
        borc=limit-ekbakiye
        if int(yatan)>borc:
            yatandankalan=int(yatan)-borc
            ekbakiye=limit
            bakiye=bakiye+yatandankalan
            account1['bakiye']=str(bakiye)
            account1['ekbakiye']=str(ekbakiye)
            print(f"Bakiyeni: {bakiye}")
            print(f"Ek bakiyeniz: {ekbakiye}")
        elif int(yatan)<borc:
            ekbakiye=ekbakiye+int(yatan)
            account1['ekbakiye']=str(ekbakiye)
            account1['bakiye']="0"
            print(f"Bakiyeni: {bakiye}")
            print(f"Ek bakiyeniz: {ekbakiye}")
        else:
            bakiye=bakiye+int(yatan)
            account1['ekbakiye']=account1['limit']
            account1['bakiye']=str(bakiye)
            print(f"Bakiyeni: {bakiye}")
            print(f"Ek bakiyeniz: {ekbakiye}")
    else:
        print("Yanlış seçim.. Lütfen listeden seçim yapınız..\n")

       
  