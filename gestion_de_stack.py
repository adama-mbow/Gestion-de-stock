from  tkinter import *
import mysql.connector
import csv
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pc17svt15",
    database="boutique"
)


# Ajouter des données à la table
def ajouter_produit():
    cursor = conn.cursor()
    nom = entry_nom.get()
    description = entry_description.get()
    prix = entry_prix.get()
    id_categorie= entry_idcategorie.get()
    cursor.execute("""
        INSERT INTO produit (nom, description, prix,id_categorie )
        VALUES (%s, %s, %s, %s)
    """, (nom, description, prix,id_categorie))
    conn.commit()
    afficher_produits()
    
# Lire des données à partir de la table
def afficher_produits():
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM produit
    """)
    produits = cursor.fetchall()
    listbox_produits.delete(0,END)
    for produit in produits:
        listbox_produits.insert(END, produit)
        
# Mettre à jour des données dans la table
def modifier_produit():
    cursor = conn.cursor()
    produit = listbox_produits.get(ACTIVE)
    id = produit[0]
    nom = entry_nom.get()
    description = entry_description.get()
    prix = entry_prix.get()
    id_categorie = entry_idcategorie.get()
    cursor.execute("""
        UPDATE produit
        SET nom = %s, description = %s, prix = %s,id_categoorie= %s
        WHERE id = %s,description = %s, prix = %s,id_categoorie= %s
    """, (nom, description, prix, id_categorie))
    

"""def supprimer_produit():
    id_produit = listbox_produits.get(listbox_produits.curselection())[0]
    cursor = conn.cursor()
    cursor.execute("DELETE FROM produit WHERE id = %s, description = %s, prix = %s,id_categoorie= %s ", (id_produit,))
    conn.commit()
    refresh_liste_produits()"""
    
def supprimer_produit():
    id_produit = listbox_produits.get(listbox_produits.curselection())[0]
    cursor = conn.cursor()
    cursor.execute("DELETE FROM produit WHERE id = %s AND description = %s AND prix = %s AND id_categorie = %s", (id_produit))
    conn.commit()
    refresh_liste_produits()
    
def refresh_liste_produits():
    listbox_produits.delete(0, END)
    afficher_produits()
    
def exporter_produit():
    cursor = conn.cursor()
    cursor.execute("""SELECT *FROM produit""")
    produits = cursor.fetchall()
    
    with open ('produits.csv', 'w', newline= '') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['id', 'nom','description','prix','id_categorie'])
        for produit in produits:
            writer.writerow(produit)
    
exporter_produit()
fenetre = Tk()
fenetre.title("Gestion des produits")

#Creer les differents labels
label_nom = Label(fenetre, text="nom")
label_nom.grid(row=0, column=0)
entry_nom = Entry(fenetre)
entry_nom.grid(row=0, column=1)
label_description =Label(fenetre, text="description")
label_description.grid(row=1, column=0)
entry_description =Entry(fenetre)
entry_description.grid(row=1, column=1)
label_prix = Label(fenetre, text="Prix")
label_prix.grid(row=2, column=0)
entry_prix = Entry(fenetre)
entry_prix.grid(row=2, column=1)
label_idcategorie = Label(fenetre, text="id_categorie")
label_idcategorie.grid(row=3, column=0)
entry_idcategorie = Entry(fenetre)
entry_idcategorie.grid(row=3, column=1)

#creation de bouton CRUD
button_ajouter = Button(fenetre, text="Ajouter", command=ajouter_produit)
button_ajouter.grid(row=3, column=5)
button_modifier =Button(fenetre, text="Modifier", command=modifier_produit)
button_modifier.grid(row=3, column=6)
button_supprimer =Button(fenetre, text="Supprimer", command=supprimer_produit)
button_supprimer.grid(row=3, column=7)
button_reset =Button(fenetre, text="reset", command=afficher_produits)
button_reset.grid(row=3, column=8)
listbox_produits =Listbox(fenetre)
listbox_produits.grid(row=4, column=0, columnspan=3)


fenetre.mainloop()