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


#question 02 
recettes_tout_ingredients = []
liste_categories = set(categories.values())
for recette, ingredients in recettes.items():
   cat_temporaire = set()
   for ingredient in ingredients: 
      cat_temporaire.add(categories[ingredient])
   if cat_temporaire == liste_categories:
      recettes_tout_ingredients.append(recette)

print (" les recettes avec tous les ingredients sont :" , recettes_tout_ingredients)

 




