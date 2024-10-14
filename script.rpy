
define e = Character("Narrator")
define c = Character("Player")


label start:

    $ bad_ending = False
    $ good_ending = False
  
    scene ranges_keep_out

  
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