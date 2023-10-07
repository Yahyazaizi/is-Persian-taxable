age=int(input("svp done un age"))
sexe=input("svp done la nature de labitant")
R1 = sexe =="H" and age >= 20
R2 = sexe =="F" and age >= 18 and age <=35
if R1 or R2:
     print("L'habitant est imposable")
else:
     print("L'habitant est non imposable")