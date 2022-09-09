import random

valg = ["1","2","3","4","5","6","7","8","9","10"]

forsøk = 3
score = 0

spillIgjen = True
while spillIgjen == True:

    maskinValg = random.choice (valg)
    
    spillerValg = input("Velg ett tall mellom 1 og 10: ")



    if spillerValg == maskinValg:
        print ("du gjettet riktig :)")
        score += 1
    
    
    
    
    elif (spillerValg) > (maskinValg):
            print ("feil, prøv lavere")
            forsøk -= 1

    elif (spillerValg) < (maskinValg):
        print ("feil, prøv høyere")
        forsøk -= 1



    if forsøk == 0:
        print ("du tapte, din score ble")
        print (score)
        spillIgjen = False
    
        
