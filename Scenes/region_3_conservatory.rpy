# =======================================================
# REGION 3: THE CRYSTAL CONSERVATORY (Mom - Harmonist)
# =======================================================

label region_3_conservatory:
    # Conservatory region music and ambient
    play music MUSIC_CONSERVATORY fadein 2.0
    play ambient AMBIENT_CRYSTALS fadein 2.0 volume 0.3 loop

    scene image "#ffffff" with dissolve

    scene bg_crystal_conservatory:

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
        zoom 0.15
        xalign 0.42
        yalign 0.9
    show h a_back:
        alpha 1.0
        zoom 0.12
        xalign 0.45
        yalign 0.89
    show p facing_away:
        alpha 1.0
        zoom 0.08
        xalign 0.49
        yalign 0.92

    "The light faded, and the brothers found themselves in a place of breathtaking beauty."
    "A towering crystalline structure rose before them, catching and refracting what little light remained."
    "But something was wrong. The crystals, which should have been gleaming with radiant color, were dull and gray."


    t "Whoa..."


    t "It's like a giant chandelier..."

    h "A broken chandelier. These crystals look... sick."

    p "Welcome to the Crystal Conservatory, Twin Sparks!"


    p "Though I must say... it looked much more impressive the last time I was here."

    show t a_hands_on_hips_expressionless_talking:
        xzoom -1
    t "Let me guess—another beacon problem?"

    show t a_hands_on_hips_expressionless
    show p offended
    p "I'm afraid so. The Crystal Beacon has been corrupted."

    show p frustrated
    p "This place was once filled with beautiful music. The crystals would sing in perfect harmony."

    show h a_unsure_looking_right_talking:
        xzoom -1
    h "The crystals... sing?"

    show h a_unsure_looking_right
    show p sad
    p "They used to. Now they're completely silent. The conservatory has lost its voice."

    "A faint, discordant hum echoed through the chamber—like an instrument badly out of tune."

    show t a_surprised:
        xzoom 1
    show h a_surprised_looking_down:
        xzoom -1

    t "What was THAT?"

    show p worried
    p "The last remnants of the crystal's song. It's trying to heal itself, but..."

    show p frustrated
    p "Without help, the conservatory will fall completely silent. And when that happens..."

    show h a_skeptical_talking
    h "Something bad, right? It's always something bad."

    show h a_skeptical
    show p nervous_laugh
    p "Well... yes. The realm's emotional balance is tied to the crystal's harmony."

    show p offended
    p "If the song dies, so does hope itself."

    show t a_hands_on_hips_expressionless_talking
    t "No pressure or anything."

    show t a_hands_on_hips_expressionless
    show p happy_talking
    p "But fear not! The Guardian of Harmony should be nearby. She can help!"

    "Pipwick floated ahead, leading the brothers deeper into the silent conservatory."

    hide t
    hide h
    hide p
    with dissolve

    pause 0.5

    # --- MEETING MOM ---

    scene bg_crystal_conservatory:
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

    "As they ventured deeper into the conservatory, they heard a familiar voice."
    "Someone was humming a gentle melody, trying to coax life from a cluster of gray crystals."

    show l back:
        xalign 0.3
        yalign 0.75
        zoom 0.45
    with dissolve

    show h a_surprised_looking_down:
        xzoom 1
    show t a_pointing_confused:
        xzoom -1

    h "Wait... that sounds like..."

    show h a_cheer_eyes_closed:
        xzoom -1
    h "MOM!"

    show l surprised:
        xzoom 1
    with vpunch

    "The woman turned around, her eyes widening in disbelief."

    l "Henry?! Tristan?!"

    show l anchor
    l "My babies! What are you doing here?!"

    show l hands_on_hips_talking
    l "This is no place for children! It's dangerous!"

    show l hands_on_hips
    show t a_hands_on_hips_smile_talking:
        xzoom 1
    t "Hi Mom! We're on a quest!"

    show t a_hands_on_hips_smile
    show h a_thumbs_up_determined_talking:
        xzoom 1
    $ beacon_count_text = get_beacon_text()
    h "We're the Twin Sparks! We've already restored [beacon_count_text]!"

    show h a_thumbs_up_determined
    show l skeptical_talking
    l "Twin Sparks? Beacons? What on earth are you talking about?"

    show l skeptical
    show p happy_talking:
        zoom 0.30
        xzoom 1
    p "Guardian Lauren! It's wonderful to see you!"

    show p proud
    p "Your sons are the chosen heroes of the realm. They've been doing magnificently!"

    show l surprised_talking
    l "Pipwick? You brought my children into this mess?"

    show l frustrated_talking
    l "I told you to find warriors, not... not my boys!"

    show l frustrated
    show p nervous_laugh
    p "With all due respect, Guardian, your boys ARE warriors."

    show p offended
    if valley_complete:
        p "They've faced giant spiders, dark vines, and puzzles that would stump most adults!"
    else:
        p "They've already proven themselves with puzzles that would stump most adults!"

    show l anchor
    l "..."

    if valley_complete:
        show l hands_on_hips_talking
        l "You faced giant spiders?"

        show l hands_on_hips
        show t a_hands_on_hips_expressionless_talking
        t "Metal ones. They were pretty gross."

        show t a_hands_on_hips_expressionless
        show h a_skeptical_talking
        h "I still have nightmares about the clicking sounds."

        show h a_skeptical
        show l frustrated
        l "..."

        show l hands_on_hips_talking
        l "I am going to have WORDS with your uncle about letting you climb into spider territory."

        show l hands_on_hips

    show t a_pointing_confused_talking
    t "We met Aunt Kayla! Well, sort of."

    show t a_pointing_confused
    show h a_smile_looking_right_talking
    h "She was a light memory version. It was weird but cool."

    show h a_smile_looking_right
    show l anchor
    l "..."

    "Mom took a deep breath, then slowly walked over and pulled both boys into a tight hug."

    show l anchor
    l "I'm so proud of you both. And also terrified. And also still proud."

    show l hands_on_hips_talking
    l "But we can talk about my complicated feelings later. Right now, we have a problem."

    show l hands_on_hips
    show t a_unsure_looking_left_talking:
        xzoom -1
    t "The crystals, right? Pipwick said they used to sing."

    show t a_unsure_looking_left
    show l presenting_talking
    l "That's right. The Crystal Conservatory was once the most beautiful place in all the realm."

    show l presenting
    l "Every crystal held a note, and together they created a perfect harmony."

    show l frustrated_talking
    l "But the darkness came and scattered the harmony. Now the crystals are jumbled and confused."

    show l frustrated
    show t a_hands_on_hips_expressionless_talking
    t "Let me guess—Bedimurk?"

    show t a_hands_on_hips_expressionless
    show l frustrated_talking
    l "That wretched raccoon, yes. He came through here with earplugs stuffed in his ears."
    l "Said the singing gave him headaches. Can you believe that?"

    show l annoyed_talking
    l "He scratched the crystals with his claws until they couldn't hold a tune anymore."
    l "Knocked things over everywhere. I'm still finding muddy pawprints in the corners."

    show l frustrated
    show h a_unsure_looking_right_talking
    h "Scattered how?"

    show h a_unsure_looking_right
    show l hands_on_hips_talking
    l "Think of it like... a puzzle that's been dumped on the floor."

    show l anchor
    l "All the pieces are still here, but they're in the wrong places."

    show l frustrated_talking
    l "The crystals need to be realigned—matched with others of their kind to restore the pattern."

    show l frustrated
    show t a_pointing_smile_talking:
        xzoom 1
    t "So we need to match them? Like a matching game?"

    show t a_pointing_smile
    show l hands_on_hips_talking
    l "Exactly! I've been trying to do it myself, but..."

    show l frustrated_talking
    l "There are too many crystals and they keep drifting apart. I need more hands."

    show l frustrated
    show h a_thumbs_up_determined_talking:
        xzoom -1
    h "We've got hands! Four of them!"

    show h a_thumbs_up_determined
    show t a_hands_on_hips_smile_talking
    t "We're great at matching games. Henry beats me at Memory all the time."

    show t a_hands_on_hips_smile
    show h a_smile_looking_right_talking:
        xzoom 1
    h "It's because you flip the cards too fast and don't pay attention."

    show h a_smile_looking_right
    show t a_hands_on_hips_expressionless_talking
    t "...That's probably true."

    show t a_hands_on_hips_expressionless
    show l anchor
    l "Alright, here's what we need to do."

    show l presenting_talking
    l "The crystal formations are controlled by these pedestals."

    show l presenting
    l "When you swap two crystals and create a match of three or more, they'll lock into place."

    show l hands_on_hips_talking
    l "Clear enough crystals and we'll restore the first layer of harmony."

    show l hands_on_hips
    show p proud
    p "Remember, Twin Sparks—look for chain reactions!"

    show p happy_talking
    p "When crystals match and disappear, others will fall into place. Sometimes they create new matches!"

    show t a_determined_looking_left_talking
    t "Got it. Let's do this!"

    show t a_determined_looking_left
    show l hands_on_hips_talking
    l "I'll be right here cheering you on. And please, PLEASE be careful."

    show l hands_on_hips
    show h a_eyes_closed_talking_smile:
        xzoom -1
    h "We're always careful, Mom!"

    show h a_eyes_closed_talking_smile
    show l skeptical_talking
    l "Henry, last week you tried to slide down the banister and broke a lamp."

    show l skeptical
    show h a_skeptical_talking:
        xzoom 1
    h "...We're SOMETIMES careful."

    hide t
    hide h
    hide l
    hide p
    with dissolve

    "The brothers approached the crystal pedestal, ready for their first challenge."

    jump conservatory_match_intro

# --- CRYSTAL MATCH INTRO ---

label conservatory_match_intro:
    scene bg_crystal_conservatory:
        zoom 0.9
        yalign 0.3
        xalign 0.5
    with dissolve

    "The pedestal lit up, revealing a grid of dull crystals in various shapes and colors."
    "Even in their faded state, the crystals pulsed with potential energy."

    show t a_hands_on_hips_smile:
        zoom 0.35
        xalign 0.4
        yalign 0.7
    show h a_thumbs_up_determined:
        zoom 0.32
        xalign 0.6
        yalign 0.75
    with dissolve

    t "Okay, I see the pattern. Red ones here, blue ones there..."

    show h a_pointing_smile_talking
    h "Look! If we swap those two green ones, we'll get a match!"

    show h a_pointing_smile
    show t a_pointing_smile_talking
    t "Good eye! Let's start there!"

    hide t
    hide h
    with dissolve

    "Arrow keys to move, SPACE to select and swap crystals. Match 3 or more to clear them!"

    call crystal_match_start(target_score=1000, moves_limit=40)
    $ crystal_match_victory = _return

    jump conservatory_match_complete

# --- MATCH GAME COMPLETE ---

label conservatory_match_complete:
    scene bg_crystal_conservatory:
        zoom 0.85
        yalign 0.3
        xalign 0.5
    with fade

    if crystal_match_victory:
        jump conservatory_match_victory
    else:
        jump conservatory_match_retry

label conservatory_match_retry:
    show t a_hands_to_head_frustrated:
        zoom 0.35
        xalign 0.4
        yalign 0.7
    show h a_skeptical:
        zoom 0.32
        xalign 0.6
        yalign 0.75
    with dissolve

    "The crystals drifted apart again. The pattern wasn't quite right."

    show l frustrated:
        zoom 0.4
        xalign 0.8
        yalign 0.7
    with dissolve

    l "So close! The crystals are stubborn, but don't give up!"
    l "Take a breath and try again. You can do this!"

    menu:
        "Try again!":
            jump conservatory_match_intro
        "Take a break first":
            "The brothers took a moment to study the crystal patterns more carefully."
            jump conservatory_match_intro

label conservatory_match_victory:
    "The final crystals clicked into place, and suddenly—"

    show light_burst at light_burst_grow_2:
        alpha 0.0
        ease 0.3 alpha 1.0
        ease 0.5 alpha 0.0
    with vpunch

    "A wave of color swept through the conservatory!"
    "The crystals blazed to life, each one glowing with its true vibrant hue."

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

    t "YEAH! Look at them shine!"
    h "They're so pretty now!"

    show l cheering:
        zoom 0.4
        xalign 0.75
        yalign 0.6
    with dissolve

    l "That's my boys! You did it!"

    show p happy_talking:
        zoom 0.25
        xalign 0.2
        yalign 0.7
    with dissolve

    p "Wonderful! The first layer of harmony is restored!"

    show p worried
    p "But... I'm afraid that's only half the battle."

    show t a_hands_on_hips_expressionless:
        xzoom 1
    show h a_skeptical:
        xzoom 1

    t "Of course there's more."
    h "There's always more."

    show l hands_on_hips_talking
    l "The crystals have their colors back, but they still can't sing."

    show l anchor
    l "The harmony needs to be... awakened. Reminded of its rhythm."

    show h a_unsure_looking_right_talking
    h "How do we do that?"

    show h a_unsure_looking_right
    show l presenting_talking
    l "We need to play along with them. Match their rhythm until they remember how to sing on their own."

    show l presenting
    show t a_pointing_confused_talking
    t "Play along? Like... making music?"

    show t a_pointing_confused
    show l hands_on_hips_talking
    l "Exactly. The crystals will play notes, and you need to echo them back at the right moment."

    show l anchor
    l "Think of it like a duet—they sing, you answer."

    show p proud
    p "It's quite fun, actually! Like a rhythm game!"

    show h a_thumbs_up_smile_talking:
        xzoom -1
    h "I love rhythm games!"

    show h a_thumbs_up_smile
    show t a_determined_looking_left_talking:
        xzoom -1
    t "Let's wake these crystals up!"

    hide t
    hide h
    hide l
    hide p
    with dissolve

    jump conservatory_rhythm_intro

# --- RHYTHM GAME INTRO ---

label conservatory_rhythm_intro:
    scene bg_crystal_conservatory:
        zoom 0.9
        yalign 0.5
        xalign 0.5
    with dissolve

    "The conservatory began to hum as the restored crystals pulsed with potential energy."
    "Four large crystal pillars rose from the ground, each one glowing a different color."

    show t a_surprised:
        zoom 0.35
        xalign 0.4
        yalign 0.7
    show h a_surprised_looking_up:
        zoom 0.32
        xalign 0.6
        yalign 0.75
    with dissolve

    t "Whoa... they're starting to glow!"

    show h a_hands_on_hips_smile_talking
    h "I can hear something... like music, but far away."

    show h a_hands_on_hips_smile
    show l presenting_talking:
        zoom 0.35
        xalign 0.8
        yalign 0.65
    with dissolve

    l "That's the crystal's memory of the old song. Help it remember!"

    show l anchor
    l "When a crystal lights up, press the matching key to echo it back!"

    show p happy_talking:
        zoom 0.25
        xalign 0.15
        yalign 0.7
    with dissolve

    p "D, F, J, and K keys for the four pillars! Press them when the notes reach the bottom!"

    show t a_determined_looking_left_talking:
        xzoom 1
    t "Got it. D, F, J, K. Like a keyboard pattern."

    show t a_determined_looking_left
    show h a_thumbs_up_determined_talking:
        xzoom -1
    h "Let's make some music!"

    hide t
    hide h
    hide l
    hide p
    with dissolve

    "Press D, F, J, K when notes reach the target line. Keep the rhythm!"

    call crystal_rhythm_start(difficulty="easy")
    $ crystal_rhythm_victory = _return

    jump conservatory_rhythm_complete

# --- RHYTHM GAME COMPLETE ---

label conservatory_rhythm_complete:
    scene bg_crystal_conservatory:
        zoom 0.85
        yalign 0.5
        xalign 0.5
    with fade

    if crystal_rhythm_victory:
        jump conservatory_victory
    else:
        jump conservatory_rhythm_retry

label conservatory_rhythm_retry:
    show t a_hands_on_head_frustrated:
        zoom 0.35
        xalign 0.4
        yalign 0.6
    show h a_looking_down_confused:
        zoom 0.32
        xalign 0.6
        yalign 0.65
    with dissolve

    "The rhythm faltered. The crystals flickered and fell silent again."

    show l frustrated:
        zoom 0.4
        xalign 0.8
        yalign 0.6
    with dissolve

    l "So close! The crystals almost remembered!"
    l "Don't worry—the song is still there, waiting. Try again!"

    show p nervous_laugh:
        zoom 0.25
        xalign 0.15
        yalign 0.7
    with dissolve

    p "Remember—timing is everything! Wait for the notes to hit the line!"

    menu:
        "Try again!":
            jump conservatory_rhythm_intro
        "Take a break first":
            "The brothers listened to the faint echoes of the crystal song, preparing for another attempt."
            jump conservatory_rhythm_intro

# --- REGION VICTORY ---

label conservatory_victory:
    "The final note rang out, perfect and clear—"

    show light_burst at light_burst_grow_2:
        alpha 0.0
        ease 0.3 alpha 1.0
        ease 0.5 alpha 0.0
    with vpunch

    "And suddenly, the entire conservatory EXPLODED with sound!"
    "Every crystal sang in perfect harmony, their voices weaving together into a magnificent chorus."
    "Colors danced through the air as the music swelled and filled every corner of the chamber."

    show t a_cheering_mouth_open:
        zoom 0.35
        xalign 0.3
        yalign 0.6
    show h a_cheer_eyes_closed:
        zoom 0.32
        xalign 0.5
        yalign 0.65
        xzoom -1
    with dissolve

    t "LISTEN TO THAT!"
    h "IT'S SO BEAUTIFUL!"

    show l cheering:
        zoom 0.45
        xalign 0.7
        yalign 0.6
    with dissolve

    l "YOU DID IT! The harmony is restored!"

    show p happy_talking:
        zoom 0.28
        xalign 0.15
        yalign 0.7
    with dissolve

    p "MAGNIFICENT! The Crystal Beacon is singing again!"

    "High above, the Crystal Beacon blazed with brilliant light, its song echoing through the entire realm."

    jump conservatory_conclusion

# --- REGION CONCLUSION ---

label conservatory_conclusion:
    scene bg_crystal_conservatory:
        zoom 0.85
        yalign 1.0
        xalign 0.5
    with dissolve

    show l anchor:
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

    "Mom gathered both boys into a long, warm hug, her eyes glistening."

    l "I am so, SO proud of you both."

    show l hands_on_hips_talking
    l "When I was called to be a Guardian, I never imagined my own children would come to help."

    show l anchor
    l "You've grown so much. You're real heroes now."

    show t a_hands_on_hips_expressionless_talking
    t "We had a good teacher. You always told us to never give up."

    show t a_hands_on_hips_expressionless
    show h a_thumbs_up_determined_talking
    h "Yeah! 'Thompson boys don't quit!' Remember?"

    show h a_thumbs_up_determined
    show l hands_on_hips_talking
    l "I remember. And you've proven it today."

    if valley_complete:
        show l frustrated_talking
        l "But please, when you get home—don't tell your father about the giant spiders."

        show l frustrated
        show t a_pointing_confused_talking
        t "Why not?"

        show t a_pointing_confused
        show l skeptical_talking
        l "Because he'll want to come back here and FIGHT them, and I cannot deal with that right now."

        show l skeptical
        show h a_eyes_closed_talking_smile:
            xzoom 1
        h "Dad would totally try to fight the spiders."

        show h a_smile_looking_right
        show l anchor
        l "Your father would try to fight a dragon if it looked at him funny."
    else:
        show l frustrated_talking
        l "But please, be careful out there. I worry about you both."

        show l frustrated

    show p happy_talking
    p "Time to move on, Twin Sparks! More beacons need your help!"

    show l anchor
    l "Go save the rest of the realm, my brave boys."

    show l hands_on_hips_talking
    l "And whatever challenges you face... try to be careful, okay?"

    show l hands_on_hips
    show t a_hands_on_hips_smile_talking
    t "We can handle anything. We've got this, Mom!"

    show t a_hands_on_hips_smile
    show l anchor
    l "I know you do."

    "Mom hugged them one more time, then stepped back with a proud smile."

    show l waving
    l "Go save the realm, my brave boys. I'll be right here, listening to the crystals sing."

    show p happy_talking
    p "Time to move on, Twin Sparks! Touch the lantern when you're ready!"

    $ beacon_desc = get_beacon_text()
    "Pipwick held out his lantern, its light burning brighter with [beacon_desc] restored."

    show t a_determined_looking_left_talking:
        xzoom 1
    t "Ready?"

    show t a_determined_looking_left
    show h a_thumbs_up_determined_talking:
        xzoom -1
    h "Ready!"

    "Together, the brothers placed their hands on the lantern."
    "The beautiful crystal song swelled around them as light filled the conservatory."

    l "I love you both! Be safe!"

    show light_burst at light_burst_grow_2:
        alpha 0.0
        ease 0.2 alpha 1.0

    hide l
    hide t
    hide h
    hide p
    with dissolve

    # Mark Conservatory as complete
    $ conservatory_complete = True
    $ met_mom = True

    "And then they were gone, carried on beams of light toward their next adventure."
    "Behind them, the Crystal Conservatory sparkled with restored harmony—"
    "A testament to the power of the Twin Sparks."

    # Return to navigation hub
    jump navigation_hub
