# [LLM + H ] idee formule par moi code écrit par Claude (Sonnet 5.5, chat web) : l'idée est de retrouver le décalage tout seul
from collections import Counter

def caesar(texte):
    # [LLM] on compte les lettres (minuscules) et on prend la plus fréquente : en français c'est probablement le "e"
    lettres = [c for c in texte.lower() if c.isalpha()]
    plus_frequente = Counter(lettres).most_common(1)[0][0]
    # [LLM] distance entre cette lettre et "e" = décalage utilisé pour chiffrer (ici 3)
    decalage = (ord(plus_frequente) - ord("e")) % 26
    resultat = ""
    for c in texte:
        if c.isalpha():
            # [LLM] on garde la casse : base = "A" pour une majuscule, "a" pour une minuscule
            base = ord("A") if c.isupper() else ord("a")
            # [LLM] on recule de "decalage" rangs, le % 26 fait boucler l'alphabet
            resultat += chr((ord(c) - base - decalage) % 26 + base)
        else:
            # [LLM] espaces, virgules, points, retours à la ligne : inchangés
            resultat += c
    # [LLM] strip() enlève le retour à la ligne du début de txt, pour que le résultat commence par "Le plus..."
    return resultat.strip()



# [LLM] decypher applique une table de substitution "dic" (lettre chiffrée -> lettre claire)
def decypher(texte, dic):
    # [LLM] lower() car le chiffré a des majuscules (E, S, B...) ; ce qui n'est pas dans dic (espace, ponctuation) reste tel quel
    return "".join(dic.get(c.lower(), c) for c in texte).lower()

# [LLM] table construite "à la main" : on part de mots devinables ("Bkb," = "ici,", "Cl Fbialybxbjz" = "La Disparition"),
# [LLM] on complète lettre par lettre en vérifiant que les mots obtenus sont du français
dic = {
    "a": "p", "b": "i", "c": "l", "d": "z", "e": "b", "f": "d", "g": "h", "i": "s",
    "j": "o", "k": "c", "l": "a", "m": "u", "n": "y", "o": "f", "p": "v", "q": "x",
    "r": "g", "s": "j", "u": "m", "v": "q", "x": "t", "y": "r", "z": "n",
}



# [H] code ecrit par moi, même fonction decypher, mais avec une nouvelle table : ici chaque symbole du message est une clé
# [LLM] attention : on redéfinit "dic", sinon la cellule d'appel utiliserait la table française
dic = {
    "5": "a", "2": "b", "—": "c", "+": "d", "8": "e", "1": "f", "3": "g", "4": "h",
    "6": "i", "0": "l", "9": "m", "*": "n", "‡": "o", ".": "p", "(": "r", ")": "s",
    ";": "t", "?": "u", "¶": "v", ":": "y",
}

