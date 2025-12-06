# --------------------------------------------------------
# Character Definitions
# --------------------------------------------------------

# Main heroes - Tristan (red/crimson) and Henry (blue/azure)
define t = Character("Tristan", color="#ff6b6b", who_outlines=[(2, "#4a1a1a", 0, 0)])
define h = Character("Henry", color="#6bb5ff", who_outlines=[(2, "#1a3a4a", 0, 0)])

# Family members - warm earth tones
define r = Character("Uncle Ryan", color="#e8a87c")
define k = Character("Aunt Kayla", color="#95d5b2")
define l = Character("Mom", color="#f4acb7")
define j = Character("Dad", color="#8ecae6")
define g = Character("G-Mom", color="#ddb892")

# Magical companion - golden sparkle
define p = Character("Pipwick", color="#ffd700", who_outlines=[(2, "#5a4500", 0, 0)])



# --------------------------------------------------------
# Character Images - Global variables
# --------------------------------------------------------

# Tristan
layeredimage t:
    group expression:
        attribute bd_facing_side default:
            "images/characters/Tristan/rmbg/facing_side.png"
        attribute bd_facing_side_talking:
            "images/characters/Tristan/rmbg/facing_side_talking.png"
        attribute bd_laying_back:
            "images/characters/Tristan/rmbg/laying_back.png"
        attribute bd_laying_back_talking:
            "images/characters/Tristan/rmbg/laying_back_talking.png"
        attribute bd_laying_back_laughing:
            "images/characters/Tristan/rmbg/laying_back_laughing.png"
        attribute bd_sitting_back:
            "images/characters/Tristan/rmbg/sitting_back.png"
        attribute bd_sitting_back_talking:
            "images/characters/Tristan/rmbg/sitting_back_talking.png"
        attribute bd_on_knees:
            "images/characters/Tristan/rmbg/on_knees.png"
        attribute bd_on_knees_talking:
            "images/characters/Tristan/rmbg/on_knees_talking.png"
        attribute a_unsure_looking_left:
            "images/characters/Tristan/rmbg/red_armor/unsure_looking_left.png"
        attribute a_unsure_looking_left_talking:
            "images/characters/Tristan/rmbg/red_armor/unsure_looking_left_talking.png"
        attribute a_surprised:
            "images/characters/Tristan/rmbg/red_armor/surprised.png"
        attribute a_determined_looking_left:
            "images/characters/Tristan/rmbg/red_armor/determined_looking_left.png"
        attribute a_looking_down_confused:
            "images/characters/Tristan/rmbg/red_armor/looking_down_confused.png"
        attribute a_surprised_talking:
            "images/characters/Tristan/rmbg/red_armor/surprised_talking.png"
        attribute a_determined_looking_left_talking:
            "images/characters/Tristan/rmbg/red_armor/determined_looking_left_talking.png"
        attribute a_looking_down_confused_talking:
            "images/characters/Tristan/rmbg/red_armor/looking_down_confused_talking.png"
        attribute a_back:
            "images/characters/Tristan/rmbg/red_armor/back.png"
        attribute a_pointing_smile:
            "images/characters/Tristan/rmbg/red_armor/pointing_smile.png"
        attribute a_pointing_confused:
            "images/characters/Tristan/rmbg/red_armor/pointing_confused.png"
        attribute a_pointing:
            "images/characters/Tristan/rmbg/red_armor/pointing.png"
        attribute a_cheering2:
            "images/characters/Tristan/rmbg/red_armor/cheering2.png"
        attribute a_cheering:
            "images/characters/Tristan/rmbg/red_armor/cheering.png"
        attribute a_cheering_mouth_open:
            "images/characters/Tristan/rmbg/red_armor/cheering_mouth_open.png"
        attribute a_hands_on_hips_smile:
            "images/characters/Tristan/rmbg/red_armor/hands_on_hips_smile.png"
        attribute a_hands_on_head_frustrated:
            "images/characters/Tristan/rmbg/red_armor/hands_on_head_frustrated.png"
        attribute a_hand_raised_from_behind:
            "images/characters/Tristan/rmbg/red_armor/hand_raised_from_behind.png"
        attribute a_hands_on_hips_expressionless:
            "images/characters/Tristan/rmbg/red_armor/hands_on_hips_expressionless.png"
        attribute a_hands_on_hips_expressionless_talking:
            "images/characters/Tristan/rmbg/red_armor/hands_on_hips_expressionless_talking.png"
        attribute a_hands_on_hips_talking:
            "images/characters/Tristan/rmbg/red_armor/hands_on_hips_talking.png"
        attribute a_hands_to_head_frustrated:
            "images/characters/Tristan/rmbg/red_armor/hands_to_head_frustrated.png"
        attribute a_pointing_confused_talking:
            "images/characters/Tristan/rmbg/red_armor/pointing_confused_talking.png"
        attribute a_pointing_smile_talking:
            "images/characters/Tristan/rmbg/red_armor/pointing_smile_talking.png"
        attribute a_hands_on_hips_smile_talking:
            "images/characters/Tristan/rmbg/red_armor/hands_on_hips_smile_talking.png"


# Henry
layeredimage h:
    group expression:
        attribute bd_laying_side default:
            "images/characters/Henry/rmbg/laying_side.png"
        attribute bd_laying_side_talking:
            "images/characters/Henry/rmbg/laying_side_talking.png"
        attribute bd_laying_side_laughing:
            "images/characters/Henry/rmbg/laying_side_laughing.png"
        attribute bd_crawling_reaching:
            "images/characters/Henry/rmbg/crawling_reaching.png"
        attribute bd_sitting_up_confused:
            "images/characters/Henry/rmbg/sitting_up_confused.png"
        attribute bd_sitting_up_worried_talking:
            "images/characters/Henry/rmbg/sitting_up_worried_talking.png"
        attribute bd_sitting_up_worried:
            "images/characters/Henry/rmbg/sitting_up_worried.png"
        attribute bd_sitting_up_scared:
            "images/characters/Henry/rmbg/sitting_up_scared.png"
        attribute bd_sitting_up_surprised:
            "images/characters/Henry/rmbg/sitting_up_surprised.png"
        attribute bd_laying_reaching:
            "images/characters/Henry/rmbg/laying_reaching.png"
        attribute a_looking_down:
            "images/characters/Henry/rmbg/blue_armor/looking_down.png"
        attribute a_looking_down_talking:
            "images/characters/Henry/rmbg/blue_armor/looking_down_talking.png"
        attribute a_unsure_looking_right:
            "images/characters/Henry/rmbg/blue_armor/unsure_looking_right.png"
        attribute a_unsure_looking_right_talking:
            "images/characters/Henry/rmbg/blue_armor/unsure_looking_right_talking.png"
        attribute a_thumbs_up_determined:
            "images/characters/Henry/rmbg/blue_armor/thumbs_up_determined.png"
        attribute a_thumbs_up_determined_talking:
            "images/characters/Henry/rmbg/blue_armor/thumbs_up_determined_talking.png"
        attribute a_thumbs_up_smile:
            "images/characters/Henry/rmbg/blue_armor/thumbs_up_smile.png"
        attribute a_unsure_looking_left:
            "images/characters/Henry/rmbg/blue_armor/unsure_looking_left.png"
        attribute a_unsure_looking_left_talking:
            "images/characters/Henry/rmbg/blue_armor/unsure_looking_left_talking.png"
        attribute a_back:
            "images/characters/Henry/rmbg/blue_armor/back.png"
        attribute a_surprised_looking_down:
            "images/characters/Henry/rmbg/blue_armor/surprised_looking_down.png"
        attribute a_cheering:
            "images/characters/Henry/rmbg/blue_armor/cheering.png"
        attribute a_cheering2:
            "images/characters/Henry/rmbg/blue_armor/cheering2.png"
        attribute a_cheering_mouth_open:
            "images/characters/Henry/rmbg/blue_armor/cheering_mouth_open.png"
        attribute a_determined_looking_left:
            "images/characters/Henry/rmbg/blue_armor/determined_looking_left.png"
        attribute a_determined_looking_left_talking:
            "images/characters/Henry/rmbg/blue_armor/determined_looking_left_talking.png"
        attribute a_hands_on_hips:
            "images/characters/Henry/rmbg/blue_armor/hands_on_hips.png"
        attribute a_hands_on_hips_expressionless_talking:
            "images/characters/Henry/rmbg/blue_armor/hands_on_hips_expressionless_talking.png"
        attribute a_hands_on_hips_smile:
            "images/characters/Henry/rmbg/blue_armor/hands_on_hips_smile.png"
        attribute a_hands_on_hips_smile_talking:
            "images/characters/Henry/rmbg/blue_armor/hands_on_hips_smile_talking.png"
        attribute a_hands_on_hips_talking:
            "images/characters/Henry/rmbg/blue_armor/hands_on_hips_talking.png"
        attribute a_hands_to_head_frustrated:
            "images/characters/Henry/rmbg/blue_armor/hands_to_head_frustrated.png"
        attribute a_hand_raised_from_behind:
            "images/characters/Henry/rmbg/blue_armor/hand_raised_from_behind.png"
        attribute a_looking_down_confused:
            "images/characters/Henry/rmbg/blue_armor/looking_down_confused.png"
        attribute a_looking_down_confused_talking:
            "images/characters/Henry/rmbg/blue_armor/looking_down_confused_talking.png"
        attribute a_pointing:
            "images/characters/Henry/rmbg/blue_armor/pointing.png"
        attribute a_pointing_confused:
            "images/characters/Henry/rmbg/blue_armor/pointing_confused.png"
        attribute a_eyes_closed_talking_smile:
            "images/characters/Henry/rmbg/blue_armor/eyes_closed_talking_smile.png"
        attribute a_pointing_smile:
            "images/characters/Henry/rmbg/blue_armor/pointing_smile.png"
        attribute a_pointing_smile_talking:
            "images/characters/Henry/rmbg/blue_armor/pointing_smile_talking.png"
        attribute a_surprised_looking_up:
            "images/characters/Henry/rmbg/blue_armor/surprised_looking_up.png"
        attribute a_surprised_talking:
            "images/characters/Henry/rmbg/blue_armor/surprised_talking.png"
        attribute a_skeptical:
            "images/characters/Henry/rmbg/blue_armor/skeptical.png"
        attribute a_skeptical_talking:
            "images/characters/Henry/rmbg/blue_armor/skeptical_talking.png"
        attribute a_smile_looking_right_talking:
            "images/characters/Henry/rmbg/blue_armor/smile_looking_right_talking.png"
        attribute a_smile_looking_right:
            "images/characters/Henry/rmbg/blue_armor/smile_looking_right.png"
        attribute a_cheer_eyes_closed:
            "images/characters/Henry/rmbg/blue_armor/cheer_eyes_closed.png"
        attribute a_thumbs_up_smile_talking:
            "images/characters/Henry/rmbg/blue_armor/thumbs_up_smile_talking.png"
        attribute a_pointing_confused_talking:
            "images/characters/Henry/rmbg/blue_armor/pointing_confused_talking.png"

# Pipwick
layeredimage p:

    group expression:

        attribute expressionless default:
            "images/characters/Pipwick/rmbg/general/_0007_rmbg_pipwick_expressionless.png"
        attribute expressionless_night:
            "images/characters/Pipwick/rmbg/night/night__0007_rmbg_pipwick_expressionless.png"

        attribute nervous_laugh:
            "images/characters/Pipwick/rmbg/general/_0000_rmbg_pipwick_nervous_laugh.png"
        attribute nervous_laugh_night:
            "images/characters/Pipwick/rmbg/night/night__0000_rmbg_pipwick_nervous_laugh.png"

        attribute happy_talking:
            "images/characters/Pipwick/rmbg/general/_0001_rmbg_pipwick_happy_talking.png"
        attribute happy_talking_night:
            "images/characters/Pipwick/rmbg/night/night__0001_rmbg_pipwick_happy_talking.png"


        attribute frustrated_night:
            "images/characters/Pipwick/rmbg/night/night__0002_rmbg_pipwick_frustrated.png"

        attribute worried:
            "images/characters/Pipwick/rmbg/general/_0003_rmbg_pipwick_worried.png"
        attribute worried_night:
            "images/characters/Pipwick/rmbg/night/night__0003_rmbg_pipwick_worried.png"

        attribute sad:
            "images/characters/Pipwick/rmbg/general/_0004_rmbg_pipwick_sad.png"
        attribute sad_night:
            "images/characters/Pipwick/rmbg/night/night__0004_rmbg_pipwick_sad.png"

        attribute proud:
            "images/characters/Pipwick/rmbg/general/_0005_rmbg_pipwick_proud.png"
        attribute proud_night:
            "images/characters/Pipwick/rmbg/night/night__0005_rmbg_pipwick_proud.png"

        attribute offended:
            "images/characters/Pipwick/rmbg/general/_0006_rmbg_pipwick_offended.png"
        attribute offended_night:
            "images/characters/Pipwick/rmbg/night/night__0006_rmbg_pipwick_offended.png"

        attribute excited:
            "images/characters/Pipwick/rmbg/general/_0008_rmbg_pipwick_excited.png"
        attribute excited_night:
            "images/characters/Pipwick/rmbg/night/night__0008_rmbg_pipwick_excited.png"

        attribute facing_away:
            "images/characters/Pipwick/rmbg/general/facing_away.png"
        attribute frustrated:
            "images/characters/Pipwick/rmbg/general/frustrated.png"

# Aunt Kayla
layeredimage k:
    group expression:
        attribute anchor default:
            "images/characters/Kayla/rmbg/anchor.png"
        attribute annoyed:
            "images/characters/Kayla/rmbg/annoyed.png"
        attribute annoyed_talking:
            "images/characters/Kayla/rmbg/annoyed_talking.png"
        attribute celebrating_wink:
            "images/characters/Kayla/rmbg/celebrating_wink.png"
        attribute cheering:
            "images/characters/Kayla/rmbg/cheering.png"
        attribute hands_on_hips:
            "images/characters/Kayla/rmbg/hands_on_hips.png"
        attribute hands_on_hips_talking:
            "images/characters/Kayla/rmbg/hands_on_hips_talking.png"
        attribute pointing_from_behind:
            "images/characters/Kayla/rmbg/pointing_from_behind.png"
        attribute presenting:
            "images/characters/Kayla/rmbg/presenting.png"
        attribute presenting_talking:
            "images/characters/Kayla/rmbg/presenting_talking.png"
        attribute sad_looking_down:
            "images/characters/Kayla/rmbg/sad_looking_down.png"
        attribute sad_looking_down_talking:
            "images/characters/Kayla/rmbg/sad_looking_down_talking.png"
        attribute shrug:
            "images/characters/Kayla/rmbg/shrug.png"
        attribute shrug_talking:
            "images/characters/Kayla/rmbg/shrug_talking.png"
        attribute smiling_facing_viewer:
            "images/characters/Kayla/rmbg/smiling_facing_viewer.png"
        attribute talking_facing_viewer:
            "images/characters/Kayla/rmbg/talking_facing_viewer.png"
        attribute talking_hands_clasped:
            "images/characters/Kayla/rmbg/talking_hands_clasped.png"
        attribute waving:
            "images/characters/Kayla/rmbg/waving.png"

# Uncle Ryan
layeredimage r:
    group expression:
        attribute anchor default:
            "images/characters/Ryan/rmbg/anchor.png"
        attribute back:
            "images/characters/Ryan/rmbg/back.png"
        attribute surprised:
            "images/characters/Ryan/rmbg/surprised.png"
        attribute surprised_talking:
            "images/characters/Ryan/rmbg/surprised_talking.png"
        attribute hands_on_hips:
            "images/characters/Ryan/rmbg/hands_on_hips.png"
        attribute hands_on_hips_talking:
            "images/characters/Ryan/rmbg/hands_on_hips_talking.png"
        attribute skeptical:
            "images/characters/Ryan/rmbg/skeptical.png"
        attribute skeptical_talking:
            "images/characters/Ryan/rmbg/skeptical_talking.png"
        attribute laughing:
            "images/characters/Ryan/rmbg/laughing.png"
        attribute frustrated:
            "images/characters/Ryan/rmbg/frustrated.png"
        attribute frustrated_talking:
            "images/characters/Ryan/rmbg/frustrated_talking.png"
        attribute waving:
            "images/characters/Ryan/rmbg/waving.png"

# Mom (Lauren)
layeredimage l:
    group expression:
        attribute anchor default:
            "images/characters/Lauren/rmbg/anchor.png"
        attribute back:
            "images/characters/Lauren/rmbg/back.png"
        attribute surprised:
            "images/characters/Lauren/rmbg/surprised.png"
        attribute surprised_talking:
            "images/characters/Lauren/rmbg/surprised_talking.png"
        attribute hands_on_hips:
            "images/characters/Lauren/rmbg/hands_on_hips.png"
        attribute hands_on_hips_talking:
            "images/characters/Lauren/rmbg/hands_on_hips_talking.png"
        attribute skeptical:
            "images/characters/Lauren/rmbg/skeptical.png"
        attribute skeptical_talking:
            "images/characters/Lauren/rmbg/skeptical_talking.png"
        attribute presenting:
            "images/characters/Lauren/rmbg/presenting.png"
        attribute presenting_talking:
            "images/characters/Lauren/rmbg/presenting_talking.png"
        attribute frustrated:
            "images/characters/Lauren/rmbg/frustrated.png"
        attribute frustrated_talking:
            "images/characters/Lauren/rmbg/frustrated_talking.png"
        attribute cheering:
            "images/characters/Lauren/rmbg/cheering.png"
        attribute waving:
            "images/characters/Lauren/rmbg/waving.png"

# Dad (Jeff)
layeredimage j:
    group expression:
        attribute anchor default:
            "images/characters/Jeff/rmbg/anchor.png"
        attribute back:
            "images/characters/Jeff/rmbg/back.png"
        attribute surprised:
            "images/characters/Jeff/rmbg/surprised.png"
        attribute surprised_talking:
            "images/characters/Jeff/rmbg/surprised_talking.png"
        attribute hands_on_hips:
            "images/characters/Jeff/rmbg/hands_on_hips.png"
        attribute hands_on_hips_talking:
            "images/characters/Jeff/rmbg/hands_on_hips_talking.png"
        attribute laughing:
            "images/characters/Jeff/rmbg/laughing.png"
        attribute frustrated:
            "images/characters/Jeff/rmbg/frustrated.png"
        attribute frustrated_talking:
            "images/characters/Jeff/rmbg/frustrated_talking.png"
        attribute presenting:
            "images/characters/Jeff/rmbg/presenting.png"
        attribute presenting_talking:
            "images/characters/Jeff/rmbg/presenting_talking.png"
        attribute waving:
            "images/characters/Jeff/rmbg/waving.png"

# G-Mom (Gloria)
layeredimage g:
    group expression:
        attribute anchor default:
            "images/characters/GMom/rmbg/anchor.png"
        attribute back:
            "images/characters/GMom/rmbg/back.png"
        attribute surprised:
            "images/characters/GMom/rmbg/surprised.png"
        attribute hands_on_hips:
            "images/characters/GMom/rmbg/hands_on_hips.png"
        attribute hands_on_hips_talking:
            "images/characters/GMom/rmbg/hands_on_hips_talking.png"
        attribute presenting:
            "images/characters/GMom/rmbg/presenting.png"
        attribute presenting_talking:
            "images/characters/GMom/rmbg/presenting_talking.png"
        attribute shrug_talking:
            "images/characters/GMom/rmbg/shrug_talking.png"
        attribute frustrated:
            "images/characters/GMom/rmbg/frustrated.png"
        attribute frustrated_talking:
            "images/characters/GMom/rmbg/frustrated_talking.png"
        attribute cheering:
            "images/characters/GMom/rmbg/cheering.png"
        attribute waving:
            "images/characters/GMom/rmbg/waving.png"
        attribute wink:
            "images/characters/GMom/rmbg/wink.png"
        attribute worried:
            "images/characters/GMom/rmbg/worried.png"

# --------------------------------------------------------
