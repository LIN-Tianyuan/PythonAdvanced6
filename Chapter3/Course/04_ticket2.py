print("Bienvenue au Zoo!")
height = int(input("Veuillez indiquer votre taille (cm): "))
vip_level = int(input("Veuillez entrer votre niveau VIP(1~5): "))
day = int(input("Veuillez entrer la date du jour(1~30): "))
if height < 120:
    print("Height < 120. Vous pouvez jouer gratuitement!")
elif vip_level > 3:
    print("Niveau vip > 3. Vous pouvez jouer gratuitement!")
elif day == 1:
    print("Aujourd'hui est le 1er jour libre pour visiter.")
else:
    print("Désolé, Un billet est nécessaire pour 10 euro.")
print("Bonne visite!")