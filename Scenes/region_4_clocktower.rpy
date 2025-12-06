# =======================================================
# REGION 4: THE CELESTIAL CLOCKTOWER (Dad - Timekeeper)
# =======================================================

label region_4_clocktower:
    scene image "#ffffff" with dissolve

    scene bg_clocktower:
        zoom 0.85
        yalign 1.0
        xalign 0.5
    with fade

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

    play music "audio/music/clocktower_theme.ogg" fadein 2.0

    "The light faded, and the brothers found themselves surrounded by the rhythmic ticking of countless clocks."
    "Enormous gears turned overhead, brass and bronze spinning in an intricate dance of precision."
    "But something was wrong—the gears stuttered and jerked, their movements erratic and unpredictable."

    show t a_surprised:
        xzoom 1
    show h a_surprised_looking_down:
        xzoom -1

    t "Whoa..."

    show t a_pointing_confused_talking
    t "It's like being inside a giant watch!"

    show t a_pointing_confused
    show h a_skeptical_talking
    h "A broken giant watch. Listen—the ticking is all messed up."

    show h a_skeptical

    "TICK... tick-tick... TOCK... tick... TICK-TICK-TICK..."

    show p happy_talking:
        xzoom 1
        zoom 0.30

    p "Welcome to the Celestial Clocktower, Twin Sparks!"

    show p worried
    p "Though I must warn you... time here has become quite unstable."

    show t a_hands_on_hips_expressionless_talking:
        xzoom -1
    t "Unstable how? Like, time-travel unstable?"

    show t a_hands_on_hips_expressionless
    show p nervous_laugh
    p "Not quite that dramatic, but..."

    show p offended
    p "The Clockwork Beacon has fallen out of sync. Without it, time itself is becoming jumbled."

    show h a_unsure_looking_right_talking:
        xzoom -1
    h "Jumbled? What does that mean?"

    show h a_unsure_looking_right
    show p frustrated
    p "It means moments are happening out of order. Seconds stretch into minutes, hours collapse into heartbeats."

    show p worried
    p "If the Beacon isn't restored soon, the entire realm could become trapped in a loop—"
    p "—reliving the same broken moment forever."

    show t a_hands_on_hips_expressionless_talking
    t "That sounds like a bad dream I had once."

    show t a_hands_on_hips_expressionless
    show h a_skeptical_talking
    h "I hate time stuff. It always gives me a headache."

    show h a_skeptical
    show p happy_talking
    p "Fear not! The Guardian of Time should be here somewhere."

    show p proud
    p "And from what I've heard, he's quite... enthusiastic about challenges."

    show t a_pointing_confused_talking:
        xzoom 1
    t "Wait—Mom mentioned something about that..."

    show t a_pointing_confused
    show h a_unsure_looking_right_talking
    h "She said Dad's idea of team building was 'intense.'"

    show h a_unsure_looking_right
    show p nervous_laugh
    p "Yes, well... perhaps 'intense' is putting it mildly."

    "Before Pipwick could say more, a booming voice echoed through the clocktower."

    j "READY OR NOT, HERE COMES ROUND THREE!"

    show t a_surprised
    show h a_surprised_looking_down
    with vpunch

    "A massive gear came swinging down from above—and standing on top of it was a familiar figure."

    hide t
    hide h
    hide p
    with dissolve

    pause 0.5

    # --- MEETING DAD ---

    scene bg_clocktower:
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

    "The gear lowered slowly, revealing a man in work clothes covered in oil stains and gear dust."
    "He was furiously tightening bolts on a smaller mechanism, muttering to himself."

    show j back:
        xalign 0.3
        yalign 0.75
        zoom 0.45
    with dissolve

    j "Come on, come on... just need to get this calibrated..."

    show h a_surprised_looking_down:
        xzoom 1
    show t a_pointing_confused:
        xzoom -1

    h "Wait... is that...?"

    show h a_cheer_eyes_closed:
        xzoom -1
    h "DAD!"

    show j surprised:
        xzoom 1
    with vpunch

    "The man dropped his wrench with a loud CLANG."

    j "What the—?!"

    show j anchor
    j "HENRY?! TRISTAN?!"

    show j hands_on_hips_talking
    j "What in the WORLD are you doing here?!"

    show j anchor
    j "Wait—don't tell me."

    show j hands_on_hips_talking
    j "Pipwick finally found the Twin Sparks, didn't he?"

    show j hands_on_hips
    show p happy_talking:
        zoom 0.30
        xzoom 1
    p "Indeed I did, Guardian Jeff! Your sons are the heroes we've been waiting for!"

    show p proud
    p "They've already restored THREE beacons!"

    show j laughing
    j "HA! That's my boys!"

    show j hands_on_hips_talking
    j "I knew you two had it in you! How many monsters did you fight? How many puzzles did you solve?"

    show j hands_on_hips
    show t a_hands_on_hips_smile_talking:
        xzoom 1
    t "Giant metal spiders, dark vines, a whole library full of scrambled books..."

    show t a_hands_on_hips_smile
    show h a_thumbs_up_determined_talking:
        xzoom 1
    h "Plus we did a rhythm game with singing crystals!"

    show h a_thumbs_up_determined
    show j laughing
    j "A RHYTHM GAME! That's awesome!"

    show j hands_on_hips_talking
    j "Man, I've been stuck up here fixing gears while you two have been having all the fun!"

    show j hands_on_hips
    show t a_pointing_confused_talking
    t "This doesn't seem like fun, Dad. You're covered in grease."

    show t a_pointing_confused
    show j anchor
    j "Are you kidding? This is GREAT!"

    show j hands_on_hips_talking
    j "Giant machines! Impossible puzzles! A whole tower that needs fixing!"

    show j laughing
    j "This is basically my dream vacation!"

    show h a_skeptical_talking
    h "Mom said you'd say something like that."

    show h a_skeptical
    show j surprised_talking
    j "Wait—you saw your mom? She's here too?"

    show j surprised
    show t a_hands_on_hips_smile_talking
    t "Yeah! She was the Guardian of the Crystal Conservatory."

    show t a_hands_on_hips_smile
    show h a_smile_looking_right_talking
    h "She told us to tell you NOT to go fight the giant spiders."

    show h a_smile_looking_right
    show j hands_on_hips_talking
    j "..."

    show j laughing
    j "She knows me too well."

    show j anchor
    j "Alright, alright. Business first, spider-fighting later."

    show j frustrated_talking
    j "We've got a serious problem here. See those gears?"

    "Dad pointed upward at the enormous mechanism that filled the tower."
    "Gears of all sizes spun and clicked, but their movements were chaotic and disjointed."

    show j frustrated
    j "The Clockwork Beacon keeps time for the whole realm. But the gears that drive it have fallen out of alignment."

    show j hands_on_hips_talking
    j "When the gears don't mesh right, time gets... glitchy."

    show j hands_on_hips
    show t a_unsure_looking_left_talking:
        xzoom -1
    t "How do we fix it?"

    show t a_unsure_looking_left
    show j anchor
    j "That's where it gets fun."

    show j presenting_talking
    j "The main mechanism is controlled by these gear slots."

    show j presenting
    j "We need to fit the right pieces into the right places—like a giant puzzle."

    show h a_pointing_confused_talking
    h "That doesn't sound too hard."

    show h a_pointing_confused
    show j laughing
    j "Oh, did I mention the pieces fall from the ceiling?"

    show j hands_on_hips_talking
    j "And you have to rotate them mid-air to fit them into the mechanism?"

    show j hands_on_hips
    show j anchor
    j "And if you stack them wrong, the whole thing jams?"

    show t a_hands_on_hips_expressionless
    t "So it's basically Tetris."

    show j hands_on_hips_talking
    j "It's EXACTLY like Tetris! But with REAL CONSEQUENCES!"

    show j laughing
    j "Isn't that EXCITING?!"

    show h a_skeptical_talking
    h "Dad, your definition of 'exciting' is different from most people's."

    show h a_skeptical
    show j hands_on_hips_talking
    j "That's what makes me fun at parties!"

    show j anchor
    j "Now here's the deal—I've been trying to fix this thing for three days."

    show j frustrated_talking
    j "But my hands are too big for the precision work. I keep knocking pieces out of place."

    show j frustrated
    show t a_pointing_smile_talking:
        xzoom 1
    t "And our hands are smaller!"

    show t a_pointing_smile
    show j hands_on_hips_talking
    j "EXACTLY! You two are perfect for this!"

    show j anchor
    j "I'll operate the main lever to send down the pieces. You guide them into place."

    show j hands_on_hips_talking
    j "Work fast, stack smart, and don't let the pieces pile up too high."

    show j hands_on_hips
    show h a_thumbs_up_determined_talking:
        xzoom -1
    h "We can do this! I'm actually pretty good at Tetris!"

    show h a_thumbs_up_determined
    show t a_determined_looking_left_talking:
        xzoom -1
    t "Let's get these gears turning!"

    show t a_determined_looking_left
    show j laughing
    j "THAT'S THE SPIRIT!"

    show j hands_on_hips_talking
    j "Remember—this is a RACE AGAINST TIME!"

    show j anchor
    j "Literally! The longer we take, the more unstable time becomes!"

    show p nervous_laugh
    p "No pressure, Twin Sparks!"

    hide t
    hide h
    hide j
    hide p
    with dissolve

    "The brothers took their positions at the gear mechanism, ready for the challenge."

    jump clocktower_tetris_intro

# --- TETRIS INTRO ---

label clocktower_tetris_intro:
    scene bg_clocktower:
        zoom 0.9
        yalign 0.3
        xalign 0.5
    with dissolve

    "The mechanism hummed to life as Dad pulled the main lever."
    "Above, a chute opened and the first gear piece began to descend."

    show t a_hands_on_hips_smile:
        zoom 0.35
        xalign 0.4
        yalign 0.7
    show h a_determined_looking_left:
        zoom 0.32
        xalign 0.6
        yalign 0.75
    with dissolve

    t "Here it comes! Get ready!"

    show h a_thumbs_up_determined_talking
    h "Left, right to move! Up to rotate! Down to drop faster!"

    show h a_thumbs_up_determined
    show j laughing:
        zoom 0.35
        xalign 0.85
        yalign 0.6
    with dissolve

    j "Clear complete rows to make room for more pieces!"

    show j hands_on_hips_talking
    j "I believe in you, boys! Make me proud!"

    hide t
    hide h
    hide j
    with dissolve

    "Arrow keys to move and rotate. Clear 20 lines to align the gears!"

    call clockwork_tetris_start(target_lines=20, time_limit=None)

    jump clocktower_tetris_complete

# --- TETRIS COMPLETE ---

label clocktower_tetris_complete:
    scene bg_clocktower:
        zoom 0.85
        yalign 0.3
        xalign 0.5
    with fade

    if clockwork_tetris_victory:
        jump clocktower_tetris_victory
    else:
        jump clocktower_tetris_retry

label clocktower_tetris_retry:
    show t a_hands_to_head_frustrated:
        zoom 0.35
        xalign 0.4
        yalign 0.7
    show h a_looking_down_confused:
        zoom 0.32
        xalign 0.6
        yalign 0.75
    with dissolve

    "The pieces stacked too high and the mechanism jammed."

    show j frustrated:
        zoom 0.4
        xalign 0.8
        yalign 0.6
    with dissolve

    j "No worries! That's just attempt number... let's not count!"
    j "Reset the mechanism and let's go again! You've got this!"

    show p nervous_laugh:
        zoom 0.25
        xalign 0.15
        yalign 0.7
    with dissolve

    p "Remember—don't let the pieces stack too high! Clear rows to make room!"

    menu:
        "Try again!":
            jump clocktower_tetris_intro
        "Take a break first":
            "The brothers studied the mechanism more carefully, planning their strategy."
            jump clocktower_tetris_intro

label clocktower_tetris_victory:
    "The final row cleared and the mechanism clicked into place!"

    show light_burst at light_burst_grow_2:
        alpha 0.0
        ease 0.3 alpha 1.0
        ease 0.5 alpha 0.0
    with vpunch

    "The gears above began to turn in perfect synchronization!"
    "The erratic ticking smoothed into a steady, rhythmic beat."

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

    t "YES! The gears are turning!"
    h "Listen—the ticking is normal now!"

    show j laughing:
        zoom 0.45
        xalign 0.75
        yalign 0.6
    with dissolve

    j "THAT'S MY BOYS! INCREDIBLE!"

    show p happy_talking:
        zoom 0.25
        xalign 0.15
        yalign 0.7
    with dissolve

    p "Wonderful! The primary mechanism is restored!"

    show p worried
    p "But... the Beacon itself is still out of sync."

    show t a_hands_on_hips_expressionless:
        xzoom 1
    show h a_skeptical:
        xzoom 1

    t "There's more?"
    h "Of course there's more."

    show j hands_on_hips_talking
    j "The main gears are fixed, but the timing crystals need calibration."

    show j anchor
    j "They're scattered around the tower, and they need to be activated in the right order."

    show j presenting_talking
    j "Think of it like... synchronized swimming, but with glowing rocks!"

    show h a_unsure_looking_right_talking
    h "That's a weird way to describe it."

    show h a_unsure_looking_right
    show j hands_on_hips_talking
    j "Here's the thing—the crystals only stay active for a few seconds."

    show j frustrated_talking
    j "You need to touch them in sequence, as fast as possible, before they reset."

    show j hands_on_hips
    show t a_pointing_confused_talking
    t "So it's a speed challenge?"

    show t a_pointing_confused
    show j laughing
    j "It's a RACE! Against TIME! In a CLOCKTOWER!"

    show j hands_on_hips_talking
    j "Get it? Because time... clocktower... timing..."

    show j hands_on_hips
    show h a_skeptical_talking
    h "We get it, Dad."

    show h a_skeptical
    show j anchor
    j "I've been practicing this for days, but I'm too slow."

    show j hands_on_hips_talking
    j "You two are younger, faster, more nimble."

    show j laughing
    j "Plus you've got that TWIN TELEPATHY thing going on!"

    show t a_hands_on_hips_smile_talking
    t "We don't have twin telepathy, Dad. We're not even twins."

    show t a_hands_on_hips_smile
    show j hands_on_hips_talking
    j "Close enough! You finish each other's sentences!"

    show j hands_on_hips
    show h a_smile_looking_right_talking:
        xzoom -1
    h "That's just because we—"

    show t a_hands_on_hips_smile_talking
    t "—know each other really well."

    show j laughing
    j "SEE?! TWIN TELEPATHY!"

    show p proud
    p "Regardless of telepathy, I believe you can do this!"

    show p happy_talking
    p "The timing crystals are numbered. Activate them in order, as quickly as you can!"

    hide t
    hide h
    hide j
    hide p
    with dissolve

    jump clocktower_timeattack_intro

# --- TIME ATTACK INTRO ---

label clocktower_timeattack_intro:
    scene bg_clocktower:
        zoom 0.9
        yalign 0.5
        xalign 0.5
    with dissolve

    "The tower shifted around them, platforms rising and falling in a complex pattern."
    "Glowing crystals appeared throughout the chamber, each one marked with a number."

    show t a_determined_looking_left:
        zoom 0.35
        xalign 0.4
        yalign 0.7
    show h a_thumbs_up_determined:
        zoom 0.32
        xalign 0.6
        yalign 0.75
    with dissolve

    t "I see them! They're all over the place!"

    show h a_pointing_smile_talking
    h "Start with 1, then 2, then 3... got it!"

    show h a_pointing_smile
    show j hands_on_hips_talking:
        zoom 0.35
        xalign 0.85
        yalign 0.6
    with dissolve

    j "Click on the gears in the right order! Watch the numbers!"

    show j laughing
    j "AND GO FAST! Time's ticking! Literally!"

    hide t
    hide h
    hide j
    with dissolve

    "Click the numbered gears in order as fast as you can! Don't let time run out!"

    call gear_rush_start(target_waves=5, time_limit=60)

    jump clocktower_timeattack_complete

# --- TIME ATTACK COMPLETE ---

label clocktower_timeattack_complete:
    scene bg_clocktower:
        zoom 0.85
        yalign 0.5
        xalign 0.5
    with fade

    if gear_rush_victory:
        jump clocktower_victory
    else:
        jump clocktower_timeattack_retry

label clocktower_timeattack_retry:
    show t a_hands_on_head_frustrated:
        zoom 0.35
        xalign 0.4
        yalign 0.6
    show h a_hands_to_head_frustrated:
        zoom 0.32
        xalign 0.6
        yalign 0.65
    with dissolve

    "Time ran out. The crystals dimmed and reset."

    show j frustrated:
        zoom 0.4
        xalign 0.8
        yalign 0.6
    with dissolve

    j "SO CLOSE! You almost had it!"
    j "That's exactly what happened to me the first... twelve times."

    show p worried:
        zoom 0.25
        xalign 0.15
        yalign 0.7
    with dissolve

    p "The crystals will reset in a moment. Don't give up!"

    menu:
        "Try again!":
            jump clocktower_timeattack_intro
        "Take a break first":
            "The brothers caught their breath, mentally mapping out the crystal locations."
            jump clocktower_timeattack_intro

# --- REGION VICTORY ---

label clocktower_victory:
    "The final crystal blazed to life, completing the sequence!"

    show light_burst at light_burst_grow_2:
        alpha 0.0
        ease 0.3 alpha 1.0
        ease 0.5 alpha 0.0
    with vpunch

    "The entire clocktower CHIMED as the Clockwork Beacon roared back to life!"
    "Gears spun in perfect harmony, their ticking forming a beautiful, steady rhythm."
    "Time itself seemed to sigh with relief as the chaos settled into order."

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

    t "WE DID IT!"
    h "THE BEACON IS FIXED!"

    show j laughing:
        zoom 0.5
        xalign 0.7
        yalign 0.6
    with dissolve

    j "YEEEEAAAAH! THAT'S WHAT I'M TALKING ABOUT!"

    "Dad ran over and scooped both boys into a massive bear hug, lifting them off their feet."

    j "I KNEW you could do it! That was AMAZING!"

    show p happy_talking:
        zoom 0.28
        xalign 0.15
        yalign 0.7
    with dissolve

    p "SPLENDID! The Clockwork Beacon ticks true once more!"

    "High above, the great clock face blazed with golden light, its hands finally moving in perfect sync."

    jump clocktower_conclusion

# --- REGION CONCLUSION ---

label clocktower_conclusion:
    scene bg_clocktower:
        zoom 0.85
        yalign 1.0
        xalign 0.5
    with dissolve

    show j anchor:
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

    "Dad set the boys down, grinning from ear to ear."

    j "You know what? I've been in some tough spots before."

    show j hands_on_hips_talking
    j "Climbed mountains. Fixed machines that nobody else could fix."

    show j anchor
    j "But watching you two work together... that was something else."

    show t a_hands_on_hips_expressionless_talking
    t "It wasn't that impressive, Dad. We just played some games."

    show t a_hands_on_hips_expressionless
    show j hands_on_hips_talking
    j "Are you kidding? You saved TIME ITSELF!"

    show j laughing
    j "Do you know how many people can say they saved time itself? NOT MANY!"

    show h a_thumbs_up_determined_talking
    h "It was pretty cool, actually. Especially the racing part."

    show h a_thumbs_up_determined
    show j hands_on_hips_talking
    j "Right?! The racing part was AWESOME!"

    show j anchor
    j "You know, when all this is over, we should build a clocktower in the backyard."

    show t a_pointing_confused_talking
    t "Mom would never let us build a clocktower in the backyard."

    show t a_pointing_confused
    show j hands_on_hips_talking
    j "A SMALL clocktower. Like, six feet tall, tops."

    show j hands_on_hips
    show h a_skeptical_talking
    h "She still wouldn't let us."

    show h a_skeptical
    show j frustrated
    j "...Yeah, probably not."

    show j hands_on_hips_talking
    j "Speaking of your mom, she's going to be SO jealous that I got to see you in action."

    show j laughing
    j "I can't wait to tell her about the Tetris part!"

    show p happy_talking
    p "If I may interrupt—we still have one more region to visit!"

    show p offended
    p "The Eternal Skybridge awaits, and the Shadow King grows stronger by the minute!"

    show t a_surprised_talking
    t "The Shadow King?"

    show t a_surprised
    show p worried
    p "The one who has been corrupting the beacons. The source of all this darkness."

    show p frustrated
    p "He waits at the Skybridge, gathering power. We must stop him before it's too late!"

    show j anchor
    j "The big boss fight, huh?"

    show j hands_on_hips_talking
    j "Man, I wish I could come with you. But my place is here, keeping the clock running."

    show j hands_on_hips
    show h a_unsure_looking_right_talking
    h "Will you be okay by yourself?"

    show h a_unsure_looking_right
    show j laughing
    j "Are you kidding? I've got a whole tower full of gears to play with!"

    show j anchor
    j "Besides, someone has to keep time running while you save the world."

    show j hands_on_hips_talking
    j "Now listen—whoever you meet at the Skybridge, whatever challenge they throw at you..."

    show j anchor
    j "Remember what I always say."

    show t a_hands_on_hips_smile_talking
    t "Never give up?"

    show t a_hands_on_hips_smile
    show j hands_on_hips_talking
    j "Well, yes, but specifically—"

    show j laughing
    j "If it looks impossible, that just means you haven't found the RIGHT way yet!"

    show h a_thumbs_up_determined_talking:
        xzoom 1
    h "We won't let you down, Dad!"

    show h a_thumbs_up_determined
    show t a_determined_looking_left_talking:
        xzoom -1
    t "We're going to save the realm!"

    show t a_determined_looking_left
    show j anchor
    j "I know you will."

    "Dad pulled them into one more quick hug."

    show j waving
    j "Go get 'em, boys. Make your old man proud."

    show j hands_on_hips_talking
    j "And when you get back home, you're telling me EVERYTHING. Every single detail!"

    show j hands_on_hips
    show p happy_talking
    p "Time to move on, Twin Sparks! The final region awaits!"

    "Pipwick held out his lantern, now blazing with the combined light of four restored beacons."

    show t a_determined_looking_left_talking:
        xzoom 1
    t "Ready?"

    show t a_determined_looking_left
    show h a_thumbs_up_determined_talking:
        xzoom -1
    h "Ready!"

    "Together, the brothers placed their hands on the lantern."
    "The steady ticking of the restored clocktower accompanied them as light filled the chamber."

    j "GO TEAM THOMPSON!"

    show light_burst at light_burst_grow_2:
        alpha 0.0
        ease 0.2 alpha 1.0

    hide j
    hide t
    hide h
    hide p
    with dissolve

    "And then they were gone, carried on beams of light toward the final challenge."
    "The Eternal Skybridge—and the Shadow King—awaited."

    jump region_5_skybridge
