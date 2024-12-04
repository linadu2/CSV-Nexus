### Installation
1. Téléchargez l'executable ou clonez ce dépôt Git.
2. Le programme est prêt à être utilisé

### Commandes principales
1. **Fusionner plusieurs fichiers CSV et enregistrer le résultat** :
   ```bash
   csv_nexus file1.csv file2.csv -o output.csv
   ```
2. **Trier les données par colonne** :
   ```bash
   csv_nexus file1.csv file2.csv --sort prix -o sorted_output.csv
   ```
3. **Afficher les données consolidées en console** :
   ```bash
   csv_nexus file1.csv file2.csv
   ```
4. **Forcer l'écrasement du fichier de sortie** :
   ```bash
   csv_nexus file1.csv file2.csv -o output.csv --force-overwrite
   ```