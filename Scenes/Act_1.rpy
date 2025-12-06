# =========================================
# SCENE 1: "The Messenger in the Night"
# Location: Tristan & Henry's Bedroom
# =========================================
init:
    transform moonwindow_zoom:
        zoom 0.15
        xalign 0.5
        yalign -0.1

    image tunnel_trans = Movie("images/videos/tunnel_trans.webm", loop=True)

label prologue:

    scene black
    with fade

    # Start bedroom music and rain ambience
    play music MUSIC_BEDROOM fadein 1.0 volume 0.5 loop
    play ambient AMBIENT_RAIN fadein 1.0 volume 0.3 loop
    pause 4.0

    "A soft rain pattered against the window."


    "The hum of a faraway thunderstorm filled the quiet little room."
    


    show moonwindow at moonwindow_zoom
    
    
    show rain:
        xalign 0.5
        yalign 0.08
        zoom 0.6
    

    show bg_bedroom_night
    show t bd_laying_back:
        xalign 0.11
        yalign 0.44
        zoom 0.3
        rotate 10
    show h bd_laying_side:
        xalign 0.82
        yalign 0.42
        zoom 0.25
        xzoom -1
    with dissolve

    "Two brothers lay in their beds, drifting off to sleep."
    "They listened to the wind blow through the trees outside."

    pause 1.0

    show t bd_laying_back_talking
    t "Hey, Henry... you asleep?"
    show h bd_laying_side_talking
    show t bd_laying_back
    h "I was... but not anymore."
    show t bd_laying_back_talking
    show h bd_laying_side
    t "What do you think lightning sounds like up close? Like, right next to your ear?"
    show h bd_laying_side_talking
    show t bd_laying_back
    h "How should I know? I've never been struck by lightning."
    show t bd_laying_back_talking
    show h bd_laying_side
    t "Me neither. But I bet it's loud."
    show h bd_laying_side_talking
    show t bd_laying_back
    h "Yeah, almost as loud as you snoring."
    show t bd_laying_back_talking
    show h bd_laying_side
    t "I do not snore. You snore."
    show h bd_laying_side_talking
    show t bd_laying_back
    h "You snore so loud, it shakes the whole house."
    show t bd_laying_back_talking
    show h bd_laying_side
    t "You snore so loud, you wake up the neighbors."
    show h bd_laying_side_talking
    show t bd_laying_back
    h "You snore so loud, the people in your dreams complain about the noise."
    show t bd_laying_back_talking
    show h bd_laying_side
    t "You snore so loud, people think there's an earthquake."
    show t bd_laying_back_laughing
    show h bd_laying_side_laughing
    "They laughed softly, the kind of sleepy laughter that only happens right before drifting off."

    # --- THUNDER STRIKES ---
    play sound SFX_THUNDER_CLOSE volume 0.8

    pause 0.45
    
    show image Solid("#ffffff") with vpunch:
        alpha 1.0
        pause 1.0
        easeout 0.5 alpha 0.0
    
    show t bd_facing_side:
        xalign 0.14
        yalign 0.35
        zoom 0.3
    show h bd_sitting_up_confused:
        xalign 0.82
        yalign 0.39
        zoom 0.25
        xzoom 1.0




    with dissolve
    pause 1.0

    h "Tristan...?"
    show t bd_facing_side_talking
    t "That sounded like it hit the house!"

    # --- PIPWICK ARRIVES ---
    play sound SFX_MAGIC_SHIMMER

    pause 1.0
    show 2_magic_orb_static:
        xalign 0.5
        yalign 0.2
        zoom 0.05
        rotate 0
        linear 2.0 rotate -360
        repeat
    
    show spiral_magic:
        xalign 0.5
        yalign 0.15
        zoom 0.5
        rotate 0
        linear 2.0 rotate 360
        repeat
    with dissolve

    "A swirling blue light materialized just inside their window."



    show t bd_on_knees:
        xalign 0.11
        yalign 0.44
        zoom 0.3
    show h bd_sitting_up_scared:
        rotate 10
        xalign 0.9
    with vpunch

    h "Tristan, what is that?!"
    show t bd_on_knees_talking
    t "I... I don’t know!"

    # --- FLASH ---
    play sound SFX_PORTAL_OPEN
    show p frustrated_night:
        alpha 0.0
    show image Solid("#ffffff") with vpunch:
        alpha 1.0
        pause 1.0
        easeout 1.5 alpha 0.0
    hide spiral_magic
    hide 2_magic_orb_static




    show p frustrated_night:
        alpha 1.0
        zoom 0.3
        xpos 0.45
        ypos 0.145
    show t bd_on_knees:
        xalign 0.11
        yalign 0.44
        zoom 0.3
    show h bd_sitting_up_worried:
        xalign 0.95
        yalign 0.39
        zoom 0.25
        rotate 20

    
    # --- SMOKE OVERLAY (after scene) ---
    play sound SFX_PIPWICK_FLUTTER
    show smoke_full onlayer master at center:

        easein 10 zoom 1.4 alpha 0.0


    "A burst of blue smoke and the smell of cinnamon filled the room — followed by a squeaky voice in distress."

    play sound SFX_PIPWICK_CHIRP_WORRIED
    p "Oh dear heavens and half-lit lanterns! Wrong coordinates again!"


    show p nervous_laugh_night:
        xzoom -1.0


    p "Terribly sorry, young citizens! I appear to have... ah... misfired my landing spell!"
    show t bd_on_knees_talking
    t "What the—"
    show h bd_sitting_up_worried_talking
    h "It’s a goblin!"

    show p offended_night:
        xzoom 1.0
    p "Goblin? GOBLIN!?"
    show p frustrated_night with vpunch:
        zoom 0.3
        xpos 0.45
        ypos 0.145
        ease 0.2 ypos 0.07 zoom 0.35 xpos 0.47
        ease 0.4 ypos 0.35 zoom 0.36 xpos 0.5

    p "I’ll have you know, I am {i}Pipwick Lanternfirth{/i}, certified Messenger of the Lantern Realm, eighth rank, silver class, and—"

    t "What are you TALKING about?!"

    show p excited_night:
        xzoom -1.0
    p "Ah, yes, there it is, your faces! The resemblance is undeniable."
    show p excited_night:
        xpos 0.5
        ease 0.3 xpos 0.3
    
    p "Two boys. One with red-blonde hair, the other brown. Each with courageous, intelligent eyes!" 
    p "Yes, yes, the {i}Twin Sparks!{/i}"
    show t bd_sitting_back_talking with dissolve
    t "The what now?"
    h "Did he just call me eyes smart?"

    show p proud_night:
        xzoom 1.0
    p "Indeed! You are prophesied saviors of my world. The Great Beacon has almost been extinguished, and our realm will perish if it’s not restored."



    show p sad_night
    p "You were meant to receive this message through the proper channels, but time, alas, is not on our side."

    # --- CHOICE MOMENT 1 ---

    $ choices = [
        ("Wait, this is a dream, right?", "dream"),
        ("What's a Great Beacon?", "beacon"),
        ("You sure you got the right kids?", "kids"),
    ]
    $ clicked = set()

    label choice_loop:
        $ available = [c for c in choices if c[1] not in clicked]
        if not available:
            jump after_choices
        menu:
            "Wait, this is a dream, right?" if "dream" not in clicked:
                $ clicked.add("dream")
                t "Wait, this is a dream, right? Henry, tell me I'm not talking to a goblin with manners."
                show p frustrated_night:
                    xzoom -1.0
                p "Gremlin."
                show p proud_night:
                    xzoom 1.0
                p "And absolutely not. You're perfectly conscious. Well, moderately."
                jump choice_loop
            "What's a Great Beacon?" if "beacon" not in clicked:
                $ clicked.add("beacon")
                t "What's a Great Beacon? Sounds important."
                show p proud_night:
                    xzoom 1.0
                p "The most important! It's the heart of our realm — a light that keeps shadows from devouring the skies!"
                jump choice_loop
            "You sure you got the right kids?" if "kids" not in clicked:
                $ clicked.add("kids")
                t "You sure you've got the right kids? We aren't even allowed to have matches."
                show p proud_night:
                    xzoom 1.0
                p "Quite sure! I triple-checked the constellation coordinates. And the freckles!"
                jump choice_loop

    label after_choices:

    show p worried_night:
        xpos 0.3
        ease 0.3 xpos 0.55
    p "Now, I mustn't waste any more time — darkness is already on my trail. I must—"




    show spiral_magic:
        xpos 0.56545
        ypos 0.385
        zoom 0.5
        rotate 0
        
        linear 4.0 rotate 360
        repeat
    show light_burst with dissolve:
        alpha 0.7
        zoom 0.05
        xpos 0.57745
        ypos 0.4
        rotate 0
        linear 4.0 rotate -360
        repeat
    pause 0.5

    "The lantern in Pipwick’s hand flickered, swelling with a warm gold light."

    h "Whoa... it’s glowing!"

    t "What’s it doing?"
    show p proud_night:
        xzoom -1.0

    p "Oh, it’s perfectly safe!"
    show h bd_crawling_reaching:
        rotate 0
        zoom 0.32
        ease 1.0 xpos 0.89 
    p "This is really a very harmless tool."
    show h bd_crawling_reaching:
        ease 1.0 xpos 0.83 yalign 0.46
    p "As long as nobody touches it—"
    show h bd_laying_reaching:
        zoom 0.37
        xpos 0.84
        yalign 0.5



    with hpunch
    "Henry reached out and grabbed the lantern."
    show light_burst at light_burst_grow
    show p worried_night:
            xzoom 1.0
    with vpunch
    
    "The glow brightened, spilling across the room like liquid sunlight."
    
    p "No! Wait! It’s not—!"

    "In an instant, the light engulfed them all."

    # --- TRANSITION TO REALM ---
    play sound SFX_PORTAL_ENTER
    stop ambient fadeout 1.0

    show image Solid("#ffffff") with vpunch:
        alpha 1.0
        pause 1.0
        easeout 1.5 alpha 0.0

    # Portal tunnel animation
    show screen video_player("images/videos/tunnel_animation.webm", loop=True)

    play sound SFX_MAGIC_WHOOSH

    "The world stretched, twisted, and turned inside out."

    "When the light faded, the boys were no longer in their room."

    # Arrive in the Lantern Realm
    play music MUSIC_MAIN_THEME fadein 2.0
    play ambient AMBIENT_ETHEREAL fadein 2.0 volume 0.3 loop

    scene bg_act_2_with_boys:
        zoom 1.4
        yalign 0.2
        xalign 0.5
        ease 16.0 yalign 1.0 zoom 1.0
    with dissolve

    play sound SFX_PORTAL_EXIT
    "They found themselves in a strange land beneath a violet sky. Mountains drifted like islands. A giant moon glowed above."
    p "There it is, my brave young companions — the Great Beacon. Heart of the Lantern Realm."
    p "Once, its light filled every corner of this world. It kept the stars bright, the dreams alive, and the shadows asleep."

    p "But now the Beacon weakens. Five guardian lanterns, each tied to a pillar of the realm’s harmony, have started to go dark."
    p "Without them, the Beacon cannot hold against the dark that creeps from the edges of unlit space."

    
    scene bg_act_2_closeup
    show h a_back:
        zoom 0.44
        xalign 0.37
        yalign 0.5
    show t a_back:
        zoom 0.5
        xalign 0.25
        yalign 0.5
    show p facing_away:
        zoom 0.3
        xalign 0.5
        yalign 0.6
    with dissolve
    pause 2.0
    show t a_looking_down_confused_talking with vpunch
    t "Quick question - why am I wearing armor?"
    show p excited:
        zoom 0.35
        xzoom -1.0
        xalign 0.53
    show t a_looking_down_confused
    p "Ah, yes! The outfits! A necessary precaution. You see, in this realm, danger lurks around every corner."



    $ attire_choices = [
        ("Where did these outfits come from?", "outfits"),
        ("Are you sure this isn't a dream?", "dream"),
        ("How do we get back home?", "home"),
        ("Do we really have to save the world?", "save"),
    ]
    $ attire_clicked = set()

    label attire_choice_loop:
        $ available = [c for c in attire_choices if c[1] not in attire_clicked]
        if not available:
            jump after_attire_choices
        menu:
            "Where did these outfits come from?" if "outfits" not in attire_clicked:
                $ attire_clicked.add("outfits")
                show h a_looking_down_talking
                h "But where did it come from?"
                show h a_looking_down
                show p proud
                p "This is the manifestation of your heroic destinies! The realm has... equipped you accordingly."
                show h a_unsure_looking_left
                jump attire_choice_loop
            "Are you sure this isn't a dream?" if "dream" not in attire_clicked:
                $ attire_clicked.add("dream")
                show t a_unsure_looking_left_talking
                t "You still promise this isn't a dream?"
                show t a_unsure_looking_left
                show p excited
                p "Not at all! Quite real, I assure you."
                jump attire_choice_loop
            "How do we get back home?" if "home" not in attire_clicked:
                $ attire_clicked.add("home")
                show h a_unsure_looking_right_talking
                h "How do we get back home?"
                show h a_unsure_looking_right
                show p nervous_laugh
                p "Oh, you can't. Not yet, at least."
                show t a_surprised_talking with hpunch
                t "You mean we’re {i}stuck here?!{/i}"
                show p worried
                show t a_surprised
                p "Temporarily. Until we save the world, yes."
                jump attire_choice_loop
            "Do we really have to save the world?" if "save" not in attire_clicked:
                $ attire_clicked.add("save")
                show h a_unsure_looking_left_talking
                h "You're saying we have to save the world...?"
                show h a_unsure_looking_left
                show p frustrated
                p "Yes, yes! No time to waste! The Great Beacon must be restored, and you two are the only ones who can do it!"
                
                show t a_unsure_looking_left_talking
                t "Oh boy."
                show t a_unsure_looking_left

                jump attire_choice_loop

    label after_attire_choices:

        pause 1.0
    t "So, what do we do?"
    show t a_unsure_looking_left
    show p proud
    p "You must find each lantern, mend what’s broken, and rekindle its flame."
    p "Only then will the Beacon’s heart burn bright enough to restore balance."
    show h a_unsure_looking_left_talking
    h "Five lanterns...? That’s a lot of walking."
    show h a_unsure_looking_left
    show t a_unsure_looking_left_talking
    t "Better than staying here till the world breaks apart."
    show t a_unsure_looking_left
    show h a_unsure_looking_right_talking
    h "If that's even really going to happen."
    show h a_unsure_looking_right
    show p nervous_laugh
    p "Oh, thankfully the walking will be kept to a minimum."
    p "Each lantern possesses the ability to teleport you to the next region!"
    show p happy_talking
    p "So you won’t have to trek across the entire realm."
    show t a_surprised_talking
    t "But... how will we know where to go?"
    show p proud
    show t a_surprised
    p "You will not be alone! Each lantern is watched over by a guardian spirit — echoes of those you love most."
    p "Their light endures here because love endures everywhere. You’ll recognize them, though they may not remember you at first."
    show t a_surprised_talking
    t "So our family’s out there too?"
    show p nervous_laugh
    show t a_surprised
    p "In a manner of speaking. Fragments of them, shaped by the Lantern Realm’s memory of your hearts."
    show h a_unsure_looking_left_talking
    h "That sounds… kinda creepy."
    show h a_unsure_looking_left
    show p excited
    p "Touching and ethereal, my boy, not creepy! Language matters!"
    "The group paused, taking in the gravity of the situation."


    pause 2.0
    show h a_thumbs_up_determined_talking
    h "I'm in."
    show p excited
    show h a_thumbs_up_determined
    show t a_determined_looking_left_talking
    t "Yeah, me too. Let's do this."
    show t a_determined_looking_left
    show p excited
    p "Splendid!" 
    show p facing_away:
        xzoom 1.0
        zoom 0.3
    p "Now, first things first—"
    show t a_surprised
    show h a_surprised_looking_down
    show spiral_magic:
        xpos 0.395
        ypos 0.5
        zoom 0.5
        rotate 0
        
        linear 4.0 rotate 360
        repeat
    show light_burst:
        alpha 0.7
        zoom 0.05

        xpos 0.407
        ypos 0.515
        rotate 0
        linear 4.0 rotate -360
        repeat
    with vpunch
    pause 0.5
    "The lantern flickered again, pulling them into the void." 
    show t a_unsure_looking_left_talking
    t "Oh great."
    show light_burst at light_burst_grow_2


    "And so, their adventure began."

    scene image "#ffffff" with dissolve
    pause 2.0

    jump region_1_library

