
# Personnages :
define me = Character('Moi', color='#ffffff')
define unknown = Character('...', color='#ffffff')
define IA = Character('Mia', color='#ffffff')

# stocke le Nom du player
init:
    $ povname = " "

    $ pov = DynamicCharacter(" povname ", color=(192, 64, 64, 255),show_two_window=True )

# %(povname)s pour le nom du perso

# BG
image sc_white = "bg/sc_white.jpg"


# scène 1
label start:
    

    unknown "Comment t'appelles-tu ?"

        #demande le nom du player

    if not renpy.variant('touch'):

        $ povname = renpy.input("Mon nom est : ")

    scene sc_white #dehors
    with dissolve

    unknown "Je marchais dans la rue en route vers mon appartement..."

    scene sc_black
    with dissolve

    play sound "audio/bruitage/bruit_de_pas_gravier_1.ogg"
    
    pause 3.0

    unknown "ah"

return