# This is a simple ATM application.
# we will not use a Database in this project 
# we will use the "Dictionary" instead.

account1={
    "accountno":"1122334455",
    "name":"customer1",    
    "balance":"2500",
    "additional_account":"2000",
    "additional_account_limit":"2000",
    "date":"20.06.2020",
}
print("BANKAMIZA HOŞ GELDİNİZ..")
print("Lütfen yapmak istediğiniz işlemi seçiniz\n"+
        "1.Bakiye görüntüle\n"+
        "2.Para çek\n"+
        "3.Para yatır\n"+
        "4.Çıkış için q basınız\n")



while True:
    islem = input("seçim: ")

    if str(islem) =="q":
        print("Çıkış yapılıyor.. İyi günler diliyoruz..")
        break
    
    elif str(islem)=="1":
        print(f"Hesabınızda {account1['balance']} bulunuyor..")

    elif str(islem)=="2":
        cekilen=input("Çekmek istediğiniz miktar: ")
        if int(cekilen)<int(account1["balance"]):
            account1["balance"]=int(account1["balance"])-int(cekilen)
            print(f"Hesabınızda kalan miktar: {account1['balance']}")
        else:
            print("Hesabınızda yeterli miktar bulunmuyor...")
            if (int(account1["balance"])+int(account1["additional_account"])>int(cekilen)):
                addaccountkarar=input("Ek hesabınızdan kullanmak istermisiniz? e/h: ")
                if addaccountkarar.lower()=="e":
                    int(account1["additional_account"])-(int(cekilen) - int(account1["balance"]))
                    print(f"Ek hesabınızda kalan miktar: {account1['additional_account']}")
                else:
                    print("Lütfen miktarı değiştiriniz..")

            else:
                print("Lütfen miktarı değiştiriniz..")
    elif str(islem)=="3":
        yatan=input("Yatırmak istediğiniz miktar: ")
        borc=int(account1["additional_account_limit"])-int(account1["additional_account"])
        if borc==0:
            balance=int(account1["balance"])+int(yatan)
            print(f"Hesabınızda ki miktar: {balance}")
        else:
            if yatan>borc:
                balance=int(account1["balance"])+(yatan-borc)
                account1["additional_account"]=account1["additional_account_limit"]
                print(f"Hesabınızda ki miktar: {balance}")
            else:
                account1["additional_account"]=int(account1["additional_account"])+(borc-yatan)

    else:
        print("Yanlış seçim. Lütfen geçerli bir işlem numarası giriniz..")
        
    