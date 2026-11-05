# [H] on decompresse les fichiers qui sont en .gz j'ai cherche comment le faire directement en python sur stackoverflow 
# [H] et sur stackabuse voici le lien qui ou j'ai trouve la partie du code utilise ici https://stackabuse.com/bytes/how-to-unzip-a-gz-file-using-python/
import gzip
with gzip.open("ingredients.txt.gz", "rt", encoding="utf-8") as f:
    lignes = f.read().splitlines()

# [H] on cree le dictionnaire pour mettre chaque ingredient avec sa categorie
categories = {}
# [H] on parcour toutes les lignes 
for ligne in lignes:
    # [H] a chaque fois on decoupe au niveau des deux points ":" une seule fois pour mettre chaque categorie a coter de sa liste d'ingredients
    categorie, liste_ingredients = ligne.split(": ", 1)
    # [H] on parcour maintenant chaque liste d'ingredients ingredient par ingredient un par un et a chaque fois on decoupe au niveau de la virgule 
    # [H] on decoupe au niveau de la virgule et on laisse l'espace apres la virgule pour suprimmer les espaces pour rechercher directement sans espaces
    # [H] on met chaque ingredients dans le dictionnaire a coter de sa categorie comme cle 
    for ingredient in liste_ingredients.split(", "):
        categories[ingredient] = categorie

# [H] on refait la meme chose on decompresse le fichier des recettes avec le mm module gzip et on decoupe chaque ligne 
with gzip.open("recipes.txt.gz", "rt", encoding="utf-8") as f:
    lignes = f.read().splitlines()

# [H] on cree un autre dictionnaire mais cette fois pour les recettes
recettes = {}
for ligne in lignes:
    # [H] comme fait avant on decoupe chaque recette avec sa liste d'ingredients une seule fois au niveau des deux points
    recette , liste = ligne.split(": ", 1)
    # [H] a chaque fois on met chaque recette dans le dictionnaire et on decoupe chaque ingredient pour que le dictionnaire contienne chaque recette et ses ingredients
    recettes[recette] = liste.split(", ")

# QUESTION 01 
# [H] on intialise le nombre de recettes trouve a 0 
NB_recettes = 0 
# [H] on parcour le dictionnaire recettes ligne par ligne on mettant pour chaqur recette ses ingredients
for recette , ingredients in recettes.items(): 
   # [H] on initialise la variable trouve a faux 
   trouve = False 
   # [H] on parcour chaque ingredients de la liste des ingredients de chaque recette un par un
   for ingredient in ingredients : 
     # [H] pour chaque ingredient on verifie a l'interieur du dictionnaire categories sa categorie et on compare avec Proteins ou Diary 
     # [H] si on trouve une correspondance alors on met trouve a vrai et on continue 
     if categories[ingredient] in ("Proteins", "Dairy"):
      trouve = True 
    #[H] si la variable trouve est encore a false donc on a pas trouve la categorie alors on incremente le nombre de recettes et on re boucle avec la prochaine recette
   if not trouve:
     NB_recettes += 1
# [H] on print le nombre de recettes qui n'ont pas d'ingredients      
print("le nombre de recettes est: " , NB_recettes)


#QUESTION 02 
# [H] on cree une liste vide pour mettre les recettes avec tout les ingredients 
recettes_tout_ingredients = []
# [H] cette liste contient toutes les categories grace a SET chaque categories est unique
liste_categories = set(categories.values())
# [H] on parcourt les recettes a chaque fois on prend la recette et ses igredients 
for recette, ingredients in recettes.items():
   #[H] cette ensemble est recree a chaque tour de la recette on y met les categories de la recette en cours d'execution
   cat_temporaire = set()
   #[H] on parcours chaque ingredient et on met a l'interieur de cat_temporaire sa categorie elle est unique grace au SET 
   for ingredient in ingredients: 
      cat_temporaire.add(categories[ingredient])
   # [H] on verifie si cette recette a toutes les categories 
   if cat_temporaire == liste_categories:
      # [H] si oui alors on ajoute cette recette a la liste qui contient tout les ingredients
      recettes_tout_ingredients.append(recette)
# [H] on affiche les resultats
print (" les recettes avec tous les ingredients sont :" , recettes_tout_ingredients)


 #QUESTION 03 

# QUESTION 03
# [H] mes poids : plus c'est haut plus j'aime l'ingrédient 
poids = {
    "chocolate chips": 4, "salmon": 4, "mango": 3, "avocado": 2,
    "garlic": 2, "olive oil": 1, "cheese": 4, "chicken": 5, "pasta": 4,
    "tomato": 2, "basil": 2, "honey": 4,
    "lemon": 1, "rice": 5, "butter": 1, "black pepper": 2, "salt": 2,
    "kale": -3, "cottage cheese": -3, "sour cream": -2, "mayonnaise": -2,
    "dill": -2, "kidney beans": -2, "barley": -1, "sage": -1,
}
#[H] on initialise les variables ou mettre la meilleure recette et le meilleur score a none
meilleure_recette = None
meilleur_score = None
# [H] on parcourt chaque recette
for recette, ingredients in recettes.items():
    # [H] on initialise le score provisoire a 0
    score = 0
    # [H] on parcour chaque ingredient un par un de la recette en cours
    for ingredient in ingredients:
        # [H] a chaque fois on ajoute le poid de l'ingredient a la variable score provisoire
        score += poids.get(ingredient, 0)
        # [H] on verfie maintenant si le score actuel est superieur a l'ancien meilleur score
    if meilleur_score is None or score > meilleur_score:
        # [H] si oui alors le score devient le nouveau meilleur score
        meilleur_score = score
        # [H] et la recette devient la nouvelle meilleure recette 
        meilleure_recette = recette
# [H] on affiche le resultat
print("ma recette preferee est :", meilleure_recette, "avec", meilleur_score,)

