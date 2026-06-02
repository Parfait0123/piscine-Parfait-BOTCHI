echo ">>> Exercice 1"

## Partie A : Navigation et création

# Affichage du chemin absolu du dossier
echo "[INFO] Chemin absolu actuel "
pwd

# Affichage du contenu
echo "[INFO] Contenu du dossier actuel"
ls -al

echo "[INFO] Creation du dossier ama_piscine "

if [-d "ama_piscine"]; then
    echo "[AVERTISSEMENT] Le dossier ama_piscine existe déjà"
else
    mkdir ama_piscine
    echo "[INFO] Dossier créé avec succès"
fi

echo "[INFO] Deplacement vers ama_piscine"
cd ama_piscine && pwd

echo "[INFO] Creation des dossiers jour1, jour2, jour3 dans le dossier courant"
mkdir jour1 jour2 jour3

echo "[INFO] Deplacement vers jour1 et creation des fichiers notes.txt donnees.csv rapport.md"
cd jour1 && touch script.sh notes.txt donnees.csv rapport.md

echo "[INFO] Contenu du dossier actuel"
ls -

## Partie B: Manipulation de contenu 

echo "[INFO] Ecriture dans le fichier notes.txt"
echo "AMA - Piscine Cahorte 2 - Jour 1" > notes.txt

echo "[INFO] Ecriture dans notes.txt ; la date est generee automatiquement"
echo "Etudiant : Parfait
$(date +%d/%m/%Y)
: En cours" >> notes.txt

echo "[INFO] Visualisation du contenu de notes.txt"
cat notes.txt

echo "[INFO] La premiere ligne de notes.txt"
head -n 1 notes.txt

echo "[INFO] La derniere ligne de notes.txt"
tail -n 1 notes.txt

echo "[INFO] Le nombre de ligne de notes.txt"
wc -l notes.txt

echo "[INFO] Recherche du mot Status dans le fichier notes.txt"
grep "Statut" notes.txt

## PARTIE C : Copie ; deplacement , suppression

echo "[INFO] Copie du fichier notes.txt courant dans les dossiers jour2 et jour3"
cp notes.txt ../jour2/
cp notes.txt ../jour3/

echo "[INFO] Deplacement vers ama_piscine"
cd ..

echo "[INFO] Aboressance complete de tous les dossiers et fichiers"
find . -print | sort

mv ./jour1/donnees.csv ./jour1/resultats_jour1.csv
echo "[INFO] Fichier donnees.csv du dossier jour1 renomme en esultats_jour1.scv"

mv ./jour1/rapport.md ./jour2/rapport.md
echo "[INFO] Fichier rapport.md du dossier jour1 deplace dans le dossier jour2"

rm ./jour1/script.sh
echo "[INFO] ./jour1/script.sh supprime avec succes."

echo "[INFO] Contenu final des dossiers jour1 jour2 et jour3"
find . -print | sort

## Partie D : Recherche et information systeme

echo "[INFO] Liste des fichiers .txt de l'aboressence"
find . -name "*.txt"

echo "[INFO] Liste des fichiers dont le nom contient 'notes'"
find . -name "*notes*"

if command -v python3; then
    echo "[OK] Python installé. Version : $(python3 --version)"
else 
    echo "[FIN] Python non installé. Arret du script...."
    exit 1
fi

echo "[INFO] Chemin complet de l'executable"
which python3

echo "[INFO] Scrapping de la liste complete des libraries python installees"
pip list > ./jour1/librairies.txt
echo "[INFO] Liste enregistree dans ./jour1/librairies.txt "

touch bib_verify.txt

# Verification des libraries
for lib in numpy scipy sympy; do 
    if grep lib "./jour1/librairies.txt";then
        echo "[OK] $lib est installé"
        echo "$lib" >> bib_verify.txt
    else
        echo "[MANQUANTE] $lib n'est pas installé"
    fi
done

echo "==================================================================="
echo "=============================RECAPITULATIF========================="
echo "==================================================================="
 
echo "[INFO] Aboressence cree "
find . | sort
echo "[INFO] Contenu de notes.txt"
cat ./jour1/notes.txt
echo "[INFO] Liste des librairies verifiees"
cat bib_verify.txt

echo "==================================================================="
echo "=============================END========================="
echo "==================================================================="
 