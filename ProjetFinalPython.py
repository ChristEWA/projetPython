import tkinter as tk
from tkinter import messagebox
import json

# Liste des tâches
tasks = []

taches_json = "taches.json"

# Lisez le contenu du fichier JSON
with open(taches_json, "r") as f:
    tasks = json.load(f)

# Modifiez la tâche
tasks[0]["nom"] = "Nouveau nom"

# Écrivez le contenu du fichier JSON
with open(taches_json, "w") as f:
    json.dump(tasks, f)

# Afficher le contenu du fichier JSON
print(json.dumps(tasks, indent=4))


# Fonction pour ajouter une tâche
def ajouter_tache():
    nom = entry_nom.get()
    description = entry_description.get()
    date_d_echeance = entry_date_d_echeance.get()
    etat = entry_etat.get()
    nouvelle_tache = {
        "nom": nom,
        "description": description,
        "date_d_echeance": date_d_echeance,
        "etat": etat
    }
    tasks.append(nouvelle_tache)
    afficher_taches()
    vider_champs_saisie()
    messagebox.showinfo("Confirmation", "Tâche ajoutée avec succès !")
    nom = entry_nom.get()
    description = entry_description.get()
    date_d_echeance = entry_date_d_echeance.get()
    etat = entry_etat.get()
    nouvelle_tache = {
        "nom": nom,
        "description": description,
        "date_d_echeance": date_d_echeance,
        "etat": etat
    }
    tasks.append(nouvelle_tache)
    afficher_taches()
    vider_champs_saisie()  # Ajoutez cette ligne pour vider les champs de saisie
    print("Tâche ajoutée avec succès !")

# Fonction pour mettre à jour une tâche
def mettre_a_jour_tache():
    index = listbox.curselection()
    if index:
        nom = entry_nom.get()
        description = entry_description.get()
        date_d_echeance = entry_date_d_echeance.get()
        etat = entry_etat.get()
        tasks[index[0]] = {
            "nom": nom,
            "description": description,
            "date_d_echeance": date_d_echeance,
            "etat": etat
        }
        afficher_taches()
        vider_champs_saisie()
        messagebox.showinfo("Confirmation", "Tâche mise à jour avec succès !")
    index = listbox.curselection()
    if index:
        nom = entry_nom.get()
        description = entry_description.get()
        date_d_echeance = entry_date_d_echeance.get()
        etat = entry_etat.get()
        tasks[index[0]] = {
            "nom": nom,
            "description": description,
            "date_d_echeance": date_d_echeance,
            "etat": etat
        }
        afficher_taches()
        vider_champs_saisie()  # Ajoutez cette ligne pour vider les champs de saisie
        print("Tâche mise à jour avec succès !")

# Fonction pour vider les champs de saisie
def vider_champs_saisie():
    entry_nom.delete(0, tk.END)
    entry_description.delete(0, tk.END)
    entry_date_d_echeance.delete(0, tk.END)
    entry_etat.delete(0, tk.END)

    index = listbox.curselection()
    if index:
        nom = entry_nom.get()
        description = entry_description.get()
        date_d_echeance = entry_date_d_echeance.get()
        etat = entry_etat.get()
        tasks[index[0]] = {
            "nom": nom,
            "description": description,
            "date_d_echeance": date_d_echeance,
            "etat": etat
        }
        afficher_taches()
        print("Tâche mise à jour avec succès !")

# Fonction pour supprimer une tâche
def supprimer_tache():
    index = listbox.curselection()
    if index:
        tasks.pop(index[0])
        afficher_taches()
        messagebox.showinfo("Confirmation", "Tâche supprimée avec succès !")
    index = listbox.curselection()
    if index:
        tasks.pop(index[0])
        afficher_taches()
        print("Tâche supprimée avec succès !")

# Fonction pour afficher les tâches dans la liste
def afficher_taches():
    listbox.delete(0, tk.END)
    for i, tache in enumerate(tasks):
        listbox.insert(i, tache["nom"])

def afficher_details_tache():
    index = listbox.curselection()
    if index:
        tache_selectionnee = tasks[index[0]]
        messagebox.showinfo("Détails de la tâche", f"Nom : {tache_selectionnee['nom']}\nDescription : {tache_selectionnee['description']}\nDate d'échéance : {tache_selectionnee['date_d_echeance']}\nÉtat : {tache_selectionnee['etat']}")


# Interface graphique
fenetre = tk.Tk()
fenetre.title("Gestionnaire de tâches")

# Liste des tâches
listbox = tk.Listbox(fenetre, font=("Arial", 12), selectbackground="#4286f4", selectforeground="white")
listbox.pack(padx=10, pady=10)

# Entrées pour les détails de la tâche
frame_saisie = tk.Frame(fenetre)
frame_saisie.pack(pady=10)

label_nom = tk.Label(frame_saisie, text="Nom de la tâche:")
label_description = tk.Label(frame_saisie, text="Description:")
label_date = tk.Label(frame_saisie, text="Date d'échéance:")
label_etat = tk.Label(frame_saisie, text="État:")

entry_nom = tk.Entry(frame_saisie, width=20)
entry_description = tk.Entry(frame_saisie, width=40)
entry_date_d_echeance = tk.Entry(frame_saisie, width=10)
entry_etat = tk.Entry(frame_saisie, width=10)

label_nom.grid(row=0, column=0, sticky="w")
label_description.grid(row=1, column=0, sticky="w")
label_date.grid(row=2, column=0, sticky="w")
label_etat.grid(row=3, column=0, sticky="w")

entry_nom.grid(row=0, column=1)
entry_description.grid(row=1, column=1)
entry_date_d_echeance.grid(row=2, column=1)
entry_etat.grid(row=3, column=1)

# Boutons d'action
btn_ajouter = tk.Button(fenetre, text="Ajouter", command=ajouter_tache, bg="green", fg="white")
btn_mettre_a_jour = tk.Button(fenetre, text="Mettre à jour", command=mettre_a_jour_tache, bg="orange", fg="white")
btn_supprimer = tk.Button(fenetre, text="Supprimer", command=supprimer_tache, bg="red", fg="white")
btn_details = tk.Button(fenetre, text="Afficher les détails", command=afficher_details_tache,)
btn_details.pack()
btn_ajouter.pack()
btn_mettre_a_jour.pack()
btn_supprimer.pack()

# Afficher les tâches initiales
afficher_taches()

# Lancer l'application
fenetre.mainloop()
