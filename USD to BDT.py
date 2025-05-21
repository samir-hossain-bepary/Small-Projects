def converter(usd_val):
    bdt_val =usd_val * 121.43
    print(usd_val, "USD=", bdt_val, "BDT")

converter(int(input("Enter Value :")))