numversos = int(input("Numero de versos: "))

if numversos >= 2 and numversos <= 4:
    verso1 = input("- ")
    vocales = 0
    letrafinal = len(verso1) - 1
    asonante1 = ""
    consonante1 = "" 
    while vocales < 2:
        if verso1[letrafinal] == 'a' or verso1[letrafinal] == 'e' or verso1[letrafinal] == 'i' or verso1[letrafinal] == 'o' or verso1[letrafinal] or verso1[letrafinal] == 'u':
            vocales += 1
            asonante1 = verso1[letrafinal] + asonante1
        consonante1 = verso1[letrafinal] + consonante1
        letrafinal -= 1
    
    verso2 = input("- ")
    vocales = 0
    letrafinal = len(verso2) - 1
    asonante2 = ""
    consonante2 = ""
    while vocales < 2:
        if verso2[letrafinal] == 'a' or verso2[letrafinal] == 'e' or verso2[letrafinal] == 'i' or verso2[letrafinal] == 'o' or verso2[letrafinal] or verso2[letrafinal] == 'u':
            vocales += 1
            asonante2 = verso2[letrafinal] + asonante2
        consonante2 = verso2[letrafinal] + consonante2
        letrafinal -= 1
    
    if numversos == 3:
        verso3 = input("- ")
        vocales = 0
        letrafinal = len(verso3) - 1
        asonante3 = ""
        consonante3 = ""
        while vocales < 2:
            if verso3[letrafinal] == 'a' or verso3[letrafinal] == 'e' or verso3[letrafinal] == 'i' or verso3[letrafinal] == 'o' or verso3[letrafinal] or verso3[letrafinal] == 'u':
                vocales += 1
                asonante3 = verso3[letrafinal] + asonante3
            consonante3 = verso3[letrafinal] + consonante3
            letrafinal -= 1
    
    if numversos == 4:
        verso4 = input("- ")
        vocales = 0
        letrafinal = len(verso4) - 1
        asonante4 = ""
        consonante4 = ""
        while vocales < 2:
            if verso4[letrafinal] == 'a' or verso4[letrafinal] == 'e' or verso4[letrafinal] == 'i' or verso4[letrafinal] == 'o' or verso4[letrafinal] or verso4[letrafinal] == 'u':
                vocales += 1
                asonante4 = verso4[letrafinal] + asonante4
            consonante4 = verso4[letrafinal] + consonante4
            letrafinal -= 1
            
    if numversos == 2:
        if consonante1 == consonante2: print("PAREADO")
        else: print("DESCONOCIDO")
        
    elif numversos == 3:
        if consonante1 == consonante3 and consonante1 != consonante2: print("TERCETO")
        else: print("DESCONOCIDO")
        
    else:
        if consonante1 == consonante3 and consonante2 == consonante3 and consonante3 == consonante4:
            print ("CUADERNA VIA")
        elif consonante1 == consonante4 and consonante2 == consonante3:
            print("CUARTETO")