﻿
# Personnages :
define me = Character('Moi', color='#ffffff')
define unknown = Character('...', color='#ffffff')
define IA = Character('Mia', color='#ffffff')

# stocke le Nom du player
init:
    $ povname = " "

    $ pov = DynamicCharacter(" povname ", color=(192, 64, 64, 255),show_two_window=True )


# BG
image sc_white = "bg/sc_white.jpg"


# scène 1
label start:
    
    play music "audio/music/p1.mp3"

    unknown "Bonsoir"

    scene sc_white
    with dissolve

    unknown "Comment t'appelles-tu ?"

        #demande le nom du player

    if not renpy.variant('touch'):

        $ povname = renpy.input("Mon nom est : ")

    unknown "Salut ! %(povname)s "
    IA "Je me présente je m'appelle Mia, je suis une intelligence artificielle chargée de t'accompagner pendant toutes la durée du jeu."
    IA ""




return