#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PROJET SPOTIFY
    PARTIE 3 : CREATION D'INTERFACE GRAPHIQUE
"""

##### import des modules d'interface graphique
import tkinter as tk
import webbrowser


##### Chargement et nettoyage des donnees a partir des modules
print("Loading data...")
import data_loading
df_artists, df_tracks, df_top200 = data_loading.load()

print("Cleaning data...")
import data_cleaning
df_artists, df_tracks, df_top200 = data_cleaning.clean(df_artists, df_tracks, df_top200)


##### import des modules de recherche
import search1
import search2
import search3





##### interface principale

# creation de la fenetre
window = tk.Tk()
window.title("Spotify") # ajout d'un titre
window.geometry("500x700+20+120")  # longueur * largeur + position x + position y
window.resizable(False, False) # bloquer la taille de la fenetre
window.config(background='#E6E0F8') # couleur du fond



# Ajout d'un titre principal
title = tk.Label(window,text="Bienvenue sur Spotify",background="#E6E0F8", font="arial, 30")
title.pack(pady=10) # pady = interligne



# insertion de l'image
photo = tk.PhotoImage(file="page.png").zoom(10).subsample(25)
canvas = tk.Canvas(window, background='#E6E0F8',bd=0, highlightthickness=0)
canvas.create_image(15, 15, anchor="nw", image=photo)
canvas.pack(pady=10)


# zone d'entree
entry = tk.Entry(window,font="arial, 20", bg='#E6E0F8',width=20)
entry.pack(pady=10)




### fonctions des 3 recherches

# par artiste
def search_one():
    
    research = entry.get().strip() # enlever les espaces avant et apres
    
    
    if search1.is_artist_valid(research):
    
        # on definit une deuxieme fenetre qui affiche la recherche
        window2 = tk.Tk()
        window2.title("Résultat artiste")
        window2.geometry("880x700+530+120")          
        window2.config(background='#E6E0F8') 
        
        # on ajoute un titre a la page
        title2 = tk.Label(window2,text=f"Informations sur {research} ",background="#E6E0F8",
                          foreground="black",font="arial, 30")   
        title2.pack(pady=10)
        
        
        infos = f"""Le nombre d'abonnés de {research} : {search1.nb_followers(research)}
        
        Le top 3 des chansons de {research} :
        {search1.get_artist_top3_popular_songs(research)}
        
        
        Les 3 chansons les plus récentes de {research} :
        {search1.get_artist_recent3_songs(research)}
        
        
        Nombre de chansons dans le top 200 global de {research} :
        {search1.get_artist_top200_songs(research)}
        
        
        """
        
        # bouton qui mene vers le spotify de l'artiste
        button_spotify = tk.Button(window2,text="ouvrir la page spotify",background="#F2E0F7",
                                foreground="black",font="arial, 10", command=lien_spotify)
        button_spotify.pack()
        
        # bouton qui mene vers le wikipedia de l'artiste
        button_wiki = tk.Button(window2,text="ouvrir la page wikipédia",background="#F2E0F7",
                                foreground="black",font="arial, 10", command=lien_wikipedia)
        button_wiki.pack()
        
        # on affiche les infos sur l'artiste
        results =  tk.Label(window2,text = infos, background='#F2E0F7',foreground="black",
                            font="arial, 14")
        results.pack()
        
        # on affiche la fenetre de recherche
        window2.mainloop()
        
    else:
        
        # message box warning si l'artiste saisi est invalide
        tk.messagebox.showerror("Erreur", "Saisie invalide. Veuillez vérifier vos entrées.")

        
      
# par chanson
def search_two():
    
    research = entry.get().strip() # enlever les espaces avant et apres
    
    if search2.is_title_valid(research):
        
        # on definit une deuxieme fenetre qui affiche la recherche
        window2 = tk.Tk()
        window2.title("Résultat chansons")
        window2.geometry("880x700+530+120")          
        window2.config(background='#E6E0F8') 
        
        # on ajoute un titre a la page
        title2 = tk.Label(window2,text=f"Chansons trouvées pour : {research} ",background="#E6E0F8",
                          foreground="black",font="arial, 30")   
        title2.pack(pady=10)
        
        # on affiche les chansons trouvees
        results = tk.Label(window2,text = str(search2.get_titles(research)),background='#F2E0F7',
                           foreground="black",font="arial, 14")
        results.pack()
        
        # on affiche la fenetre de recherche
        window2.mainloop()
        
    else:
        
        # message box warning si la chanson saisie est invalide
        tk.messagebox.showerror("Erreur", "Saisie invalide. Veuillez vérifier vos entrées.") 



# par annee et genre
def search_three():
    
    research = entry.get().strip() # enlever les espaces avant et apres
    
    # on separe la recherche en deux par la virgule : annee et genre -> stock dans une liste
    couple_yg = research.split(',')
    
    # s'il y'a deux elements dans la liste precedemment creee
    if len(couple_yg) == 2 :
        
        annee_saisie = couple_yg[0] # on recupere l'annee
        genre_saisi = couple_yg[1]# on recupere le genre
        
        # on enleve les espaces avant et apres
        annee_saisie = annee_saisie.strip()
        genre_saisi = genre_saisi.strip()
        
        # si les saisies sont valides
        if search3.is_year_valid(annee_saisie) and search3.is_genre_valid(genre_saisi) :
            
            # on definit une deuxieme fenetre qui affiche la recherche
            window2 = tk.Tk()
            window2.title("Résultat année & genre")
            window2.geometry("880x700+530+120")          
            window2.config(background='#E6E0F8') 
            
            # on ajoute un titre a la page
            title2 = tk.Label(window2,text=f"Informations sur {research} ",background="#E6E0F8",
                              foreground="black",font="arial, 30")   
            title2.pack(pady=10)
            
            
            # on ajoute une barre de defilement 
            scrollbar = tk.Scrollbar(window2)
            scrollbar.pack(side = "right", fill ="y") # barre verticale a droite
            
            # on ajoute un titre pour le nom des colonnes
            title3 = tk.Label(window2,text= "Nom de la chanson   -   Nom de(s) artiste(s) ",
                              background="#E6E0F8",foreground="black",font="arial, 18")
            title3.pack()    
            
            # on creer une zone pour afficher les resultats et on y ajoute la barre de recherche
            results = tk.Text(window2, width=150, height=150, background='#F2E0F7',foreground="black",
                              font="arial, 12",wrap="word",yscrollcommand = scrollbar.set)
            results.pack(pady=10)
            
            # on insere dans la zone les resultats
            results.insert(tk.END, search3.get_titles_year_genre(annee_saisie, genre_saisi))

            # lier la barre de recherche a la zone de resultats pour permettre le defilement
            scrollbar.config(command = results.yview)
            
            
            # on affiche la fenetre de recherche
            window2.mainloop()
        

        else :
            
            # message box warning si l'annee ou le genre est invalide
            tk.messagebox.showerror("Erreur", "Saisie invalide. Veuillez vérifier vos entrées.")   
            
    else :
        
        # message box warning si la saisie ne correspond pas a une annee et un genre
        tk.messagebox.showerror("Erreur", """Saisie invalide. Veuillez vérifier vos entrées.
                                format attendu : année, genre""")  



## def lien des sites

def lien_wikipedia():
    # seulement pour les 10 artistes les plus populaires
    
    wikipath = "https://fr.wikipedia.org/wiki/"
    
    # on cree un dictionnaire avec un lien pour chaque ariste
    site = {"justin bieber" : wikipath + "Justin_Bieber",
         "taylor swift" : wikipath + "Taylor_Swift",
         "drake" : wikipath + "Drake_(rappeur)",
         "bad bunny" : "wikipathBad_Bunny",
         "bts" : wikipath + "BTS_(groupe)",
         "the weeknd" : wikipath + "The_Weeknd",
         "juice wrld" : wikipath + "Juice_Wrld",
         "myke towers" : wikipath + "Myke_Towers",
         "dua lipa" : wikipath + "Dua_Lipa",
         "j balvin" : wikipath + "J_Balvin",}

    # on met en minuscule et on retire les espaces autour
    research = entry.get().lower().strip()
    
    # on recupere le lien de l'artiste dans le dictionnaire
    site_research = site.get(research)
    
    if site_research:
        
        webbrowser.open_new(site_research)
        
    else:
        
        tk.messagebox.showinfo("Désolée", f"Aucun lien pour {research}")
              

def lien_spotify():
    
    spotifypath = "https://open.spotify.com/intl-fr/artist/"
    
    research = entry.get().lower().strip()
    
    if search1.is_artist_valid(research) :
        
        # on utilise la variable globale creee dans search1 qui recupere l'id de l'artiste
        webbrowser.open_new(spotifypath + str(search1.id_spotify))
        
    else:
        
        tk.messagebox.showinfo("Erreur", f"Aucun lien pour {research}")
        


## fonction effacer la saisie
def clear():
    entry.delete(0,"end")

# afficher le bouton effacer la saisie
reset_button = tk.Button(window,text="Effacer la saisie",background="#E6E0F8",foreground="black",
                         font="arial, 15", command=clear, width=24) 
reset_button.pack(pady=10)


### On affiche les boutons qui executent la recherche et menent vers leurs fonctions respectifs


button_search1 = tk.Button(window,text="Rechercher un artiste",background="#E6E0F8",
                           foreground="black",font="arial, 15", command=search_one, width=24) 
button_search1.pack(pady=10)


button_search2 = tk.Button(window,text="Rechercher une chanson",background="#E6E0F8",
                           foreground="black",font="arial, 15", command=search_two, width=24) 
button_search2.pack(pady=10)


button_search3 = tk.Button(window,text="Rechercher par année et genre",background="#E6E0F8",
                           foreground="black",font="arial, 15", command=search_three, width=24) 
button_search3.pack(pady=10)


print("Interface ouverte")

# afficher la fenetre principale
window.mainloop()
