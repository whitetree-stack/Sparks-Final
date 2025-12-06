# =======================================================
# REGION 2: THE IRONWOOD VALLEY (Uncle Ryan - Explorer)
# =======================================================

label region_2_valley:
    # Valley region music and ambient
    play music MUSIC_VALLEY fadein 2.0
    play ambient AMBIENT_FOREST fadein 2.0 volume 0.3 loop

    scene image "#ffffff" with dissolve

    scene bg_valley:
        zoom 0.85
        yalign 1.0
        xalign 0.5
    with fade

    play sound SFX_PORTAL_EXIT
    pause 0.8

    show t a_back:
        alpha 0.0
    show h a_back:
        alpha 0.0
    show p facing_away:
        alpha 0.0
    show light_burst at light_burst_grow_2:
        alpha 0.0
        ease 0.2 alpha 1.0
        ease 0.4 alpha 0.0
    pause 0.2

    show t a_back:
        alpha 1.0
        zoom 0.4
        xalign 0.42
        yalign 0.8
    show h a_back:
        alpha 1.0
        zoom 0.36
        xalign 0.52
        yalign 0.8
    show p facing_away:
        alpha 1.0
        zoom 0.25
        xalign 0.62
        yalign 0.85

    "The light faded, and the brothers found themselves standing in a forest unlike anything they'd ever seen."
    "Towering trees of gleaming metal stretched toward a dark sky, their branches humming with faint electrical pulses."

    show t a_surprised:
        xzoom 1
    show h a_surprised_looking_down:
        xzoom -1
    
    t "Whoa..."
    
    show t a_pointing_confused_talking
    t "Are those trees made of... metal?"
    
    show t a_pointing_confused
    show h a_skeptical_talking
    h "They're buzzing. Why are they buzzing?"
    
    show h a_skeptical
    show p happy_talking:
        xzoom 1
        zoom 0.30
    
    p "Welcome to the Ironwood Valley, Twin Sparks!"
    
    show p proud
    p "The trees here are infused with a special kind of energy. They conduct light from the Ironwood Beacon throughout the entire forest."
    
    show t a_hands_on_hips_expressionless_talking:
        xzoom -1
    t "Ironwood Valley... that's a cool name, at least."
    
    show t a_hands_on_hips_expressionless
    show h a_unsure_looking_right_talking:
        xzoom -1
    h "It's giving me the creeps. Everything here feels... alive."
    
    show h a_unsure_looking_right
    show p nervous_laugh
    p "Well, that's because it {i}is{/i} alive, in a manner of speaking."
    
    show p offended
    p "But we must press on! The Beacon here is in grave danger."
    
    show t a_pointing_confused_talking:
        xzoom 1
    t "Danger? What kind of danger?"
    
    show t a_pointing_confused
    show p frustrated
    p "The worst kind! But I think it's better if you see for yourselves."
    p "This way, quickly!"

    "Pipwick floated ahead, his lantern casting dancing shadows through the metallic branches."
    "The boys followed, stepping carefully over roots that sparked with each footfall."
    
    hide t
    hide h
    hide p
    with dissolve
    
    pause 0.5
    
    # --- MEETING UNCLE RYAN ---
    
    scene bg_valley:
        zoom 0.85
        yalign 1.0
        xalign 0.5
    
    show t a_back:
        zoom 0.35
        xalign 0.65
        yalign 0.8
    show h a_back:
        zoom 0.32
        xalign 0.75
        yalign 0.8
    show p facing_away:
        zoom 0.22
        xalign 0.55
        yalign 0.85
    with dissolve

    "As they ventured deeper into the valley, they came across a large figure standing with his back to them."
    "He was looking up at the canopy, scratching his head in frustration."

    show r back:
        xalign 0.3
        yalign 0.75
        zoom 0.45
    with dissolve

    show h a_surprised_looking_down:
        xzoom 1
    show t a_pointing_confused:
        xzoom -1
    
    h "Wait... is that...?"
    
    show h a_cheer_eyes_closed:
        xzoom -1
    h "UNCLE RYAN!"

    show r surprised:
        xzoom 1
    with vpunch
    
    "The man spun around, nearly losing his balance."

    r "WHOA—!"
    
    show r anchor
    r "Henry?! Tristan?!"
    
    show r hands_on_hips_talking
    r "What in the world are you two doing here?!"
    
    show r hands_on_hips
    show t a_hands_on_hips_smile_talking:
        xzoom 1
    t "We could ask you the same thing!"
    
    show t a_hands_on_hips_smile
    show h a_thumbs_up_determined_talking:
        xzoom 1
    h "We're on a quest! To save the realm!"
    
    show h a_thumbs_up_determined
    show r skeptical_talking
    r "A quest? You two? The same kids who got lost at the mall last summer?"
    
    show r skeptical
    show t a_hands_on_hips_expressionless_talking
    t "That was ONE time. And the map was confusing."
    
    show t a_hands_on_hips_expressionless
    show h a_skeptical_talking
    h "Also that security guard gave us wrong directions."
    
    show h a_skeptical
    show r laughing
    r "Ha! Sure, blame the security guard."
    
    show r hands_on_hips_talking
    r "But seriously, how did you get here? This place isn't exactly on any tourist maps."
    
    show r hands_on_hips
    show p happy_talking:
        zoom 0.30
        xzoom 1
    p "I brought them here, Guardian Ryan!"
    
    show p proud
    p "They are the Twin Sparks, chosen to restore light to this realm!"
    
    show r surprised_talking
    r "Guardian? Oh right, that's what they call me here."
    
    show r anchor
    r "I'm more of an explorer, really. I just... ended up staying."
    
    show t a_pointing_confused_talking
    t "You {i}live{/i} here?"
    
    show t a_pointing_confused
    show r hands_on_hips_talking
    r "Sometimes. It's complicated. Time works differently between realms."
    
    show r skeptical_talking
    r "But enough about me—we've got bigger problems."
    
    show r hands_on_hips
    show h a_unsure_looking_right_talking
    h "Pipwick mentioned the Beacon was in danger..."
    
    show h a_unsure_looking_right
    show r frustrated_talking
    r "Danger doesn't even begin to cover it. Look up."

    "Uncle Ryan pointed toward the sky. High above the metallic canopy, something glowed faintly—"
    "—and it was wrapped in massive, thorny vines as black as night."

    show t a_surprised:
        xzoom 1
    show h a_surprised_looking_down:
        xzoom -1
    with vpunch
    
    t "What IS that?!"
    
    show r frustrated_talking
    r "That's the Ironwood Beacon. Or what's left of it."
    
    show r frustrated
    r "Those vines showed up about a week ago. They've been squeezing the life out of it ever since."
    
    show h a_skeptical_talking:
        xzoom 1
    h "Can't you just... cut them down?"
    
    show h a_skeptical
    show r skeptical_talking
    r "You think I haven't tried? Those vines are made of some kind of super-dense metal."
    
    show r frustrated_talking
    r "I broke three axes, two saws, and my favorite machete trying to get through."
    
    show r frustrated
    show t a_hands_on_hips_expressionless_talking
    t "RIP machete."
    
    show t a_hands_on_hips_expressionless
    show r hands_on_hips_talking
    r "She was a good blade. Served me well for twenty years."
    
    show r hands_on_hips
    show p offended
    p "The vines are draining the Beacon's energy! If we don't act soon, the entire valley will go dark!"
    
    show p frustrated
    p "And when that happens, the creatures here will become... aggressive."
    
    show h a_unsure_looking_right_talking
    h "Creatures? What creatures?"
    
    show h a_unsure_looking_right
    
    "As if on cue, a metallic skittering sound echoed from somewhere in the darkness."
    
    show t a_surprised
    show h a_surprised_looking_down
    with vpunch
    
    show r frustrated_talking
    r "Spiders. Giant metal spiders."
    
    show r frustrated
    show h a_skeptical_talking
    h "Of course. Why wouldn't there be giant metal spiders."
    
    show h a_skeptical
    show t a_hands_on_hips_expressionless_talking
    t "Is there anything in this realm that ISN'T trying to kill us?"
    
    show t a_hands_on_hips_expressionless
    show p nervous_laugh
    p "The butterflies are quite friendly!"
    
    show p happy_talking
    p "When they're not on fire, anyway."
    
    show t a_hands_on_hips_expressionless
    show h a_skeptical
    "..."
    
    show r hands_on_hips_talking
    r "Look, here's the situation. The Beacon is way up there, tangled in those vines."
    
    show r anchor
    r "I'm too heavy to climb that high without breaking branches. But you two..."
    
    show t a_pointing_smile_talking:
        xzoom -1
    t "We're lighter! We could make it up there!"
    
    show t a_pointing_smile
    show h a_thumbs_up_determined_talking:
        xzoom -1
    h "Yeah! We climb stuff all the time!"
    
    show h a_thumbs_up_determined
    show r skeptical_talking
    r "Climbing metal trees isn't the same as climbing the tree in your backyard, boys."
    
    show r hands_on_hips_talking
    r "These branches are sharp. And slippery. And sometimes they shock you."
    
    show r hands_on_hips
    show t a_hands_on_hips_smile_talking
    t "We've got this, Uncle Ryan. Trust us."
    
    show t a_hands_on_hips_smile
    show h a_smile_looking_right_talking:
        xzoom 1
    h "Besides, what's the alternative? Let the whole valley die?"
    
    show h a_smile_looking_right
    show r anchor
    r "..."
    
    show r hands_on_hips_talking
    r "You've got guts, I'll give you that."
    
    show r anchor
    r "Alright, but even if you get up there—how are you going to cut through those vines?"

    $ choices = [
        ("Try karate-chopping the vines", "karate"),
        ("Suggest using a saw or tool", "saw"),
        ("Ask Pipwick for help", "pipwick"),
    ]
    $ clicked = set()

label valley_choice_loop:
    $ available = [c for c in choices if c[1] not in clicked]
    if not available:
        jump valley_after_choices
    menu:
        "We could try karate-chopping them!" if "karate" not in clicked:
            $ clicked.add("karate")
            show t a_cheering_mouth_open:
                xzoom 1
            t "We could try karate-chopping them! HI-YA!"
            show t a_cheering
            show r laughing
            r "Ha! I love the enthusiasm, but those vines would break your hands before you'd make a dent."
            show r hands_on_hips
            jump valley_choice_loop
            
        "What if we used some tools? Like a laser saw?" if "saw" not in clicked:
            $ clicked.add("saw")
            show h a_unsure_looking_right_talking
            h "What if we used some kind of super-powered tool? Like a laser saw?"
            show h a_unsure_looking_right
            show r skeptical_talking
            r "A laser saw? Kid, this isn't a sci-fi movie."
            show r skeptical
            show p proud
            p "Actually..."
            show r surprised
            jump valley_choice_loop
            
        "Pipwick, do you have anything that could help?" if "pipwick" not in clicked:
            $ clicked.add("pipwick")
            show t a_pointing_confused_talking
            t "Hey Pipwick, you've got all kinds of gadgets. Got anything that could cut through metal vines?"
            show t a_pointing_confused
            show p happy_talking
            p "I thought you'd never ask!"
            show p proud
            p "I happen to have a portable energy cutter! It can slice through almost any material."
            show r surprised_talking
            r "You've had that this WHOLE TIME?!"
            show r surprised
            show p nervous_laugh
            p "Well, yes, but you never asked!"
            show p offended
            p "Besides, it requires two operators to function properly. One to aim, one to fire."
            show p happy_talking
            p "Perfect for a pair of Twin Sparks, wouldn't you say?"
            show t a_hands_on_hips_smile
            show h a_smile_looking_right
            jump valley_choice_loop

label valley_after_choices:
    
    show p proud
    p "Here you are! The Sparkfire Cutter!"
    
    "Pipwick produced a strange device that looked like a cross between a flashlight and a video game controller."
    
    show h a_skeptical_talking
    h "It's... kind of small."
    
    show h a_skeptical
    show p offended
    p "Size isn't everything, Henry! This little device packs quite a punch."
    
    show p happy_talking
    p "Simply point it at the target and press the button. It will fire concentrated energy orbs."
    
    show t a_pointing_confused_talking
    t "Energy orbs. Right. Totally normal."
    
    show t a_pointing_confused
    show p nervous_laugh
    p "Oh, and one more thing—try not to look directly at the beam. It's rather... bright."
    
    show h a_unsure_looking_right_talking
    h "Great safety instructions there, Pipwick."
    
    show h a_unsure_looking_right
    show r hands_on_hips_talking
    r "Alright, if you're really doing this, here's what you need to know."
    
    show r anchor
    r "The climb is dangerous. Those spiders I mentioned? They nest in the branches."
    
    show r frustrated_talking
    r "They're not aggressive unless threatened, but... you're going to be climbing through their home."
    
    show r frustrated
    show t a_hands_on_hips_expressionless_talking
    t "So they'll definitely be aggressive."
    
    show t a_hands_on_hips_expressionless
    show r hands_on_hips_talking
    r "Almost certainly, yes."
    
    show r anchor
    r "Stick together. Watch each other's backs. And for the love of all that's holy..."
    
    show r frustrated_talking
    r "Don't. Fall."
    
    show r frustrated
    show h a_thumbs_up_determined_talking
    h "We won't let you down, Uncle Ryan!"
    
    show h a_thumbs_up_determined
    show t a_determined_looking_left_talking:
        xzoom 1
    t "Let's do this!"
    
    show t a_determined_looking_left
    show r hands_on_hips_talking
    r "I'll be right here if you need me. I can't climb, but I can shout encouragement!"
    
    show r laughing
    r "GO TEAM! WOO!"
    
    show r hands_on_hips
    show t a_hands_on_hips_smile
    show h a_smile_looking_right
    
    "Tristan and Henry exchanged a look—a mix of excitement and terror."
    "Then they turned to face the towering metallic trees and began their ascent."

    jump valley_climb_intro

# --- PRE-CLIMB CUTSCENE ---

label valley_climb_intro:
    scene bg_valley:
        zoom 0.9
        yalign 0.3
        xalign 0.5
    with dissolve
    
    "The first few branches were easy enough—sturdy and wide, with good handholds."
    "But as they climbed higher, the metal grew thinner, sharper, more treacherous."
    
    show t a_hands_on_hips_expressionless:
        zoom 0.35
        xalign 0.4
        yalign 0.7
    show h a_unsure_looking_right:
        zoom 0.32
        xalign 0.6
        yalign 0.75
    with dissolve
    
    t "You doing okay back there?"
    
    show h a_skeptical_talking
    h "Define 'okay.' Because I'm pretty sure I just saw something move."
    
    show h a_skeptical
    show t a_surprised
    t "Move? Move where?"
    
    "A metallic clicking sound echoed from above."
    
    show h a_surprised_looking_down
    with vpunch
    
    h "THERE!"
    
    "A spider the size of a dinner plate skittered across a nearby branch, its metal legs glinting in the dim light."
    
    show t a_hands_on_hips_expressionless_talking
    t "Okay. Okay. It's fine. It's just a spider. A big, metal, terrifying spider."
    
    show t a_hands_on_hips_expressionless
    show h a_skeptical_talking
    h "I hate this realm. I hate it so much."
    
    show h a_skeptical
    show t a_determined_looking_left_talking:
        xzoom 1
    t "Come on. We've got a beacon to save. Stay close and keep moving!"
    
    hide t
    hide h
    with dissolve
    
    "The brothers pressed onward, climbing higher and higher into the metallic canopy."
    "Above them, the trapped Beacon pulsed weakly, its light growing fainter by the minute."
    
    call play_valley_climb_game
    
    jump valley_climb_complete

# --- CLIMB MINIGAME WRAPPER ---

label play_valley_climb_game:
    scene bg_valley:
        zoom 0.9
        yalign 0.0
        xalign 0.5
    with dissolve
    
    "Arrow Keys to climb! SPACE to attack spiders! Watch your health!"
    
    show screen valley_climb_screen
    $ climb_score = ui.interact()
    hide screen valley_climb_screen
    
    return

# --- POST-CLIMB SCENE ---

label valley_climb_complete:
    scene bg_valley:
        zoom 0.85
        yalign 0.0
        xalign 0.5
    with dissolve
    
    show t a_hands_on_hips_smile:
        zoom 0.35
        xalign 0.35
        yalign 0.6
    show h a_thumbs_up_determined:
        zoom 0.32
        xalign 0.55
        yalign 0.65
    with dissolve
    
    "Breathing hard, the brothers pulled themselves onto the highest platform."
    "Before them, the Ironwood Beacon hung suspended in a cage of writhing black vines."
    
    show t a_surprised:
        xzoom 1
    show h a_surprised_looking_down:
        xzoom -1
    
    t "We made it!"
    
    h "I can't believe we actually made it!"
    
    show t a_pointing_confused_talking
    t "Look at those vines... they're even bigger up close."
    
    show t a_pointing_confused
    show h a_unsure_looking_right_talking:
        xzoom 1
    h "And they're moving. Why are they moving?!"
    
    show h a_unsure_looking_right
    
    "The vines pulsed with dark energy, tightening their grip on the fading Beacon."
    
    show p happy_talking:
        zoom 0.25
        xalign 0.75
        yalign 0.5
    with dissolve
    
    p "Quickly! Use the Sparkfire Cutter! The Beacon can't hold out much longer!"
    
    show p offended
    p "Those vines are feeding on its energy—if they drain it completely, the damage could be permanent!"
    
    show t a_determined_looking_left_talking:
        xzoom -1
    t "Henry, you aim! I'll handle the trigger!"
    
    show t a_determined_looking_left
    show h a_thumbs_up_determined_talking:
        xzoom -1
    h "Got it! Let's light these things up!"
    
    show h a_thumbs_up_determined
    
    "The brothers raised the Sparkfire Cutter together, its tip beginning to glow with brilliant golden light."
    "The vines seemed to sense the threat—they began to writhe and twist, spawning smaller tendrils to defend themselves."
    
    show p frustrated
    p "They're fighting back! Don't let them overwhelm the Beacon!"
    
    hide t
    hide h
    hide p
    with dissolve
    
    jump valley_vine_blaster_intro

# --- VINE BLASTER INTRO ---

label valley_vine_blaster_intro:
    scene bg_valley:
        zoom 0.9
        yalign 0.0
        xalign 0.5
    with dissolve
    
    "The vines attacked from all directions, their thorny tips reaching for the glowing Beacon."
    "Tristan and Henry stood back to back, the Sparkfire Cutter humming with power."
    
    t "Here they come!"
    h "I see them! Firing!"
    
    call play_vine_blaster_game
    
    jump valley_vine_blaster_complete

# --- VINE BLASTER WRAPPER ---

label play_vine_blaster_game:
    "Tristan: Arrow Keys + SPACE | Henry: WASD + E | Protect the Beacon!"
    
    show screen vine_blaster_screen
    $ vine_score = ui.interact()
    hide screen vine_blaster_screen
    
    # Check if they won
    $ vine_display = VineBlasterDisplayable()
    $ vine_victory = vine_display.victory
    
    return

# --- VINE BLASTER COMPLETE ---

label valley_vine_blaster_complete:
    scene bg_valley:
        zoom 0.85
        yalign 0.0
        xalign 0.5
    with fade
    
    if vine_victory:
        jump valley_victory
    else:
        jump valley_retry
        
label valley_retry:
    show t a_hands_on_head_frustrated:
        zoom 0.35
        xalign 0.4
        yalign 0.6
    show h a_skeptical:
        zoom 0.32
        xalign 0.6
        yalign 0.65
    with dissolve
    
    "The vines proved too strong. The Beacon's light flickered dangerously."
    
    show p frustrated:
        zoom 0.25
        xalign 0.8
        yalign 0.5
    with dissolve
    
    p "We were so close! But the Beacon still has some energy left..."
    p "We can try again if you're ready!"
    
    menu:
        "Try again!":
            jump valley_vine_blaster_intro
        "Take a break first":
            "The brothers caught their breath, preparing for another attempt."
            jump valley_vine_blaster_intro

label valley_victory:
    "With one final burst of energy, the Sparkfire Cutter sliced through the last of the vines."
    "The dark tendrils withered and fell away, dissolving into ash before they hit the ground."
    
    show light_burst at light_burst_grow_2:
        alpha 0.0
        ease 0.3 alpha 1.0
        ease 0.5 alpha 0.0
    with vpunch
    
    "The Ironwood Beacon blazed to life, its brilliant light flooding the valley below."
    
    show t a_cheering_mouth_open:
        zoom 0.35
        xalign 0.35
        yalign 0.6
    show h a_cheer_eyes_closed:
        zoom 0.32
        xalign 0.55
        yalign 0.65
        xzoom -1
    with dissolve
    
    t "YES! WE DID IT!"
    h "THE BEACON IS FREE!"
    
    show p happy_talking:
        zoom 0.28
        xalign 0.75
        yalign 0.5
    with dissolve
    
    p "MAGNIFICENT! ABSOLUTELY MAGNIFICENT!"
    
    show p proud
    p "The light is returning to the valley! The trees are already beginning to heal!"
    
    "Below, they could hear Uncle Ryan's voice echoing up through the canopy."
    
    r "YEAH! THAT'S MY NEPHEWS! WOOOOO!"
    
    show t a_hands_on_hips_smile
    show h a_smile_looking_right:
        xzoom 1
    
    "The brothers laughed, exhausted but triumphant."
    
    jump valley_conclusion

# --- REGION CONCLUSION ---

label valley_conclusion:
    scene bg_valley:
        zoom 0.85
        yalign 1.0
        xalign 0.5
    with dissolve
    
    show r hands_on_hips:
        zoom 0.5
        xalign 0.25
        yalign 0.75
    show t a_hands_on_hips_smile:
        zoom 0.38
        xalign 0.45
        yalign 0.78
    show h a_smile_looking_right:
        zoom 0.35
        xalign 0.6
        yalign 0.8
        xzoom -1
    show p proud:
        zoom 0.28
        xalign 0.78
        yalign 0.82
    with dissolve
    
    "Back on solid ground, Uncle Ryan swept both boys into a crushing bear hug."
    
    show r laughing
    r "That was INCREDIBLE! I've never seen anyone climb that fast!"
    
    show r hands_on_hips_talking
    r "And the way you handled those vines—like a couple of pros!"
    
    show r hands_on_hips
    show t a_hands_on_hips_expressionless_talking
    t "I thought we were gonna die at least three times."
    
    show t a_hands_on_hips_expressionless
    show h a_skeptical_talking
    h "Only three? I counted five."
    
    show h a_skeptical
    show r laughing
    r "Ha! That's the spirit! A healthy fear of death keeps you sharp!"
    
    show r hands_on_hips
    show p happy_talking
    p "You've done wonderfully, Twin Sparks! The Ironwood Beacon shines brighter than ever!"
    
    "The metallic trees around them hummed with renewed energy, their surfaces glowing with soft golden light."
    
    show p offended
    p "But I'm afraid our work is not yet done. There are still more regions in need of your help."
    
    show t a_surprised_talking
    t "More regions? How many are there?"
    
    show t a_surprised
    show p nervous_laugh
    p "Oh, just a few more. Nothing you can't handle!"
    
    show p proud
    p "The next stop is the Crystal Conservatory. It's quite beautiful... when it's not frozen solid."
    
    show h a_unsure_looking_right_talking
    h "Frozen solid. Perfect. My favorite."
    
    show h a_unsure_looking_right
    show r hands_on_hips_talking
    r "Hey, before you go—I want you to know I'm proud of you both."
    
    show r anchor
    r "You faced something scary and you didn't back down. That takes real courage."
    
    show t a_hands_on_hips_smile_talking
    t "Thanks, Uncle Ryan. Will we see you again?"
    
    show t a_hands_on_hips_smile
    show r hands_on_hips_talking
    r "In this realm? Maybe. But definitely back home."
    
    show r laughing
    r "I expect a full report at the next family dinner!"
    
    show r hands_on_hips
    show h a_thumbs_up_determined_talking
    h "You got it!"
    
    show h a_thumbs_up_determined
    show p happy_talking
    p "Time to move on, Twin Sparks! Touch the lantern when you're ready!"
    
    "Pipwick held out his lantern, its light now burning stronger than before."
    
    show t a_determined_looking_left_talking:
        xzoom 1
    t "Ready?"
    
    show t a_determined_looking_left
    show h a_thumbs_up_determined_talking:
        xzoom -1
    h "Ready."
    
    "Together, the brothers placed their hands on the lantern."
    "The light enveloped them, warm and welcoming, as the Ironwood Valley faded from view."
    
    show r waving with dissolve
    r "Good luck, boys! Make the family proud!"
    
    show light_burst at light_burst_grow_2:
        alpha 0.0
        ease 0.2 alpha 1.0
    
    hide r
    hide t
    hide h
    hide p
    with dissolve
    
    "And then they were gone, carried on beams of light toward their next adventure."
    
    jump region_3_conservatory
