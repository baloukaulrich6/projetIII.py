# calculatrice d'amour
# lower permet de changer un texte qui a des lettres majiscule en lettres minuscules
# count permet de compter de nombre de lettres dans un mot
print("Calculatrice d'amour ")
Name1 = input("Entre votre nom : ")
Name2 = input("Entre le nom de Mr ou Mme :")
concat_namne = Name1 + Name2
love_score = concat_namne.lower()

t = love_score.count("t")
r = love_score.count("r")
u = love_score.count("u")
e = love_score.count("e")

true = t + r + u + e

l = love_score.count("l")
o = love_score.count("o")
v = love_score.count("v")
e = love_score.count("e")

love = l + o + v + e

love_score = int(str(love) + str(love))

if love_score < 10 and love_score > 90 :
    print(f"votre love score est de {love_score} donc votre couple est explosif")
elif love_score >= 40 or love_score <=50:
    print(f"votre love score est de {love_score} donc votre couple est solide ")
else:
    print(f"votre love score est de {love_score} vous n'ête pas fais pour etre ensemblre")