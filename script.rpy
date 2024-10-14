# The script of the game goes in this file.
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Narrator")
define c = Character("Player")

# The game starts here.

label start:

    $ bad_ending = False
    $ good_ending = False
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene ranges_keep_out

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    # These display lines of dialogue.
    e "welcome to hythe ranges"
    e "you see a keep out sign alongside a red flag, do you wish to continue?"

menu:

     "What should I do?"
     "Ignore sign and continue onwards":
        $ bad_ending = True
        jump bad_ending
 
     "Turn around and explore where you can":
        $ good_ending = True
        jump good_ending
        
     
     
label bad_ending:

    scene ranges_bad_ending
    "you ignore the flag and continue onwards, you hear a loud bang and see the human figure next to you now has a hole in it"
    "You look up to see a bunch of people holding guns and pointing them in your direction, you try to shout but they've already shot"
    jump ending

label good_ending:

    scene ranges_no
    "you turn around and explore where you can you have a wonderful time before returning home"
    jump ending

label ending:

     if bad_ending:

         scene bad_end
         "you die. the end."

     else:

         scene the_end
         "The end"
 
    # This ends the game.

return