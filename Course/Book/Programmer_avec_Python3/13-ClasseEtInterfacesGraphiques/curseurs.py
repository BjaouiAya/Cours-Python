#! /usr/bin/env python
# -*- coding:Utf8 -*-


"""CONSTRUCTION D'UN PANNEAU DE CONTRÔLE À 3 CURSEURS"""
"COURS 13 ET EXERCICE 13.13 À 13.16"

###########################################
#### Importation fonction et modules : ####
###########################################


from tkinter import *
from math import pi


###############################################################################
#### Gestion d'évènements : définition de différentes Fonctions/Classes : #####
###############################################################################


############# Création des Classes #############


class ChoixVibratoire(Frame):
    """Curseur pour choisir amplitude, fréquence, et phase d'une vibration"""
    def __init__(self, boss=None, coul='red'):
        Frame.__init__(self)
        self.freq, self.phase, self.ampl = 0, 0, 0
        self.coul = coul
        # Création de la case à cocher
        self.chk = IntVar()  # Instanciation d'un Objet variable tkinter
        Checkbutton(self, text='Afficher', variable=self.chk, fg=self.coul,
                    command=self.setCurve).pack(side=LEFT)
        # Création des 3 widgets curseurs
        Scale(self, length=150, orient=HORIZONTAL, label='Fréquence : ',
              troughcolor=coul, sliderlength=20, showvalue=0, from_=1.,
              to=9., tickinterval=2, resolution=0.25,
              command=self.setFrequence).pack(side=LEFT, padx=10, pady=10)
        # Exercice 13.14 : modification de showvalue
        Scale(self, length=150, orient=HORIZONTAL, label='Phase (degrés) : ',
              troughcolor=coul, sliderlength=20, showvalue=1,
              from_=-180, to=180, tickinterval=90,
              command=self.setPhase).pack(side=LEFT, padx=10, pady=10)
        Scale(self, length=150, orient=HORIZONTAL, label='Amplitude : ',
              troughcolor=coul, sliderlength=20, showvalue=0, from_=1.,
              to=10., tickinterval=2,
              command=self.setAmplitude).pack(side=LEFT, padx=10, pady=10)

    def setCurve(self):
        self.event_generate('<Control-Z>')

    def setFrequence(self, f):
        """Modification d'un paramètre :Fréquence"""
        self.freq = float(f)
        self.event_generate('<Control-Z>')

    def setPhase(self, p):
        """Modification d'un paramètre : Phase"""
        # TypeError: can't multiply sequence by non-int of type 'float'
        # ---> On doit créer une variable intermédiaire
        pp = float(p)
        self.phase = pp*2*pi/360  # Conversion en radians
        self.event_generate('<Control-Z>')

    def setAmplitude(self, a):
        """Modification d'un paramètre : Amplitude"""
        self.ampl = float(a)
        self.event_generate('<Control-Z>')

    def valeurs(self):
        """Tuple des paramètres d'une courbe"""
        return (self.freq, self.phase, self.ampl)

############# Création des Fonctions #############


def afficherTout(event=None):
    # On récupère les informations des divers éléments
    # On utilise get pour extraire le contenu de la variable objet chk
    lab.configure(text='{0} - {1} - {2} - {3}'.format(fra.chk.get(), fra.freq, fra.phase, fra.ampl))


###############################
#### Programme principal : ####
###############################


if __name__ == '__main__':
    root = Tk()
    fra = ChoixVibratoire(root, 'navy')
    fra.configure(bd=4, relief=GROOVE, padx=5, pady=5)  # Exercice 13.13
    fra.pack(side=TOP)
    lab = Label(root, text='test')
    lab.pack()
    root.bind('<Control-Z>', afficherTout)
    root.mainloop()
    print(fra.valeurs())
