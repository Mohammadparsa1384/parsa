while True :
    name = input("name:")

    vazn = input("vazn (kg) :")
    vazn_float = float(vazn)

    ghad = input("ghad (M) :")
    ghad_float = float(ghad)

    bmi = vazn_float / (ghad_float**2)
    if 16.5 > bmi :
        print("kambood vazn shadid")

    elif 16.5< bmi < 18.5 :
        print("kambood vazn")

    elif 18.5< bmi <25 :
        print("adi")

    elif 25< bmi <30 :
        print("ezafe vazn")

    elif 30< bmi <35 :
        print("chaghi class -e 1")

    elif 35< bmi <40 :
        print("chaghi class -e 2")

    elif 40< bmi :
        print("chaghi class -e 3")



    print(name, "aziz", "bmi shoma", bmi)

