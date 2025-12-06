# =======================================================
# REGION 5: THE ETERNAL SKYBRIDGE (G-Mom - Keeper of Light)
# =======================================================

label region_5_skybridge:
    scene image "#ffffff" with dissolve

    scene bg_skybridge:
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

    play music "audio/music/skybridge_theme.ogg" fadein 2.0

    "The light faded, and the brothers found themselves standing on a bridge that stretched into infinity."
    "Beneath them, clouds swirled in an endless ocean of white and gold."
    "Above, stars glittered despite the light—a sky that held both day and night at once."

    show t a_surprised:
        xzoom 1
    show h a_surprised_looking_down:
        xzoom -1

    t "Whoa..."

    show t a_pointing_confused_talking
    t "Are we... above the clouds?"

    show t a_pointing_confused
    show h a_skeptical_talking
    h "How high UP are we?! I can't even see the ground!"

    show h a_skeptical
    show p happy_talking:
        xzoom 1
        zoom 0.30

    p "Welcome to the Eternal Skybridge, Twin Sparks!"

    show p proud
    p "This is the heart of the realm—where all the beacons' light converges."

    show p worried
    p "Or at least... it should be."

    "The bridge ahead was dark. Where light should have blazed, only shadows lurked."
    "A cold wind swept across the bridge, carrying whispers of despair."

    show t a_hands_on_hips_expressionless_talking:
        xzoom -1
    t "Let me guess—the Shadow King?"

    show t a_hands_on_hips_expressionless
    show p frustrated
    p "Yes. He's been siphoning the beacons' energy to corrupt this place."

    show p offended
    p "If he succeeds in extinguishing the Skybridge Beacon, all the light in the realm will fade forever."

    show h a_unsure_looking_right_talking:
        xzoom -1
    h "But we fixed four beacons! Doesn't that help?"

    show h a_unsure_looking_right
    show p happy_talking
    p "It does! The restored beacons are fighting back against the darkness."

    show p worried
    p "But they're not strong enough alone. We need to restore the final beacon and defeat the Shadow King."

    show t a_determined_looking_left_talking:
        xzoom 1
    t "Then let's do it. We didn't come this far to give up now."

    show t a_determined_looking_left
    show h a_thumbs_up_determined_talking:
        xzoom 1
    h "Yeah! Let's finish this!"

    show h a_thumbs_up_determined
    show p proud
    p "That's the spirit! But first—there's someone who wants to see you."

    show t a_pointing_confused_talking
    t "Someone else? Who's left?"

    show t a_pointing_confused
    show p happy_talking
    p "The Keeper of Light. The guardian who protects the Skybridge itself."

    show p nervous_laugh
    p "She's been waiting for you. And she brought... company."

    "Pipwick floated ahead, leading the brothers toward a gentle glow in the distance."

    hide t
    hide h
    hide p
    with dissolve

    pause 0.5

    # --- MEETING G-MOM ---

    scene bg_skybridge:
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

    "As they approached the glow, they saw a familiar figure sitting peacefully on a floating platform."
    "She was humming a gentle lullaby, rocking something small in her arms."

    show g back:
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
    h "G-MOM!"

    show g surprised:
        xzoom 1

    "The woman looked up with a warm, knowing smile."

    g "There you are! I was wondering when you'd arrive."

    show g anchor
    g "Come here, both of you. Let me look at my brave grandchildren."

    show t a_hands_on_hips_smile_talking:
        xzoom 1
    t "G-Mom! What are you doing here?"

    show t a_hands_on_hips_smile
    show h a_thumbs_up_determined_talking:
        xzoom 1
    h "And is that... is that LOGAN?!"

    show h a_thumbs_up_determined
    show g hands_on_hips_talking
    g "Shh, shh! He just fell asleep."

    "G-Mom gently adjusted the bundle in her arms, revealing baby Logan, peacefully snoozing."

    show g anchor
    g "The little one insisted on coming. Well, as much as a one-year-old can insist on anything."

    show t a_pointing_confused_talking
    t "How did a baby get here?!"

    show t a_pointing_confused
    show g hands_on_hips_talking
    g "The same way anyone gets here, dear. The lantern chose him too."

    show g shrug_talking
    g "Apparently he has an important role to play. Though right now, his role seems to be napping."

    show g anchor
    "Logan made a soft cooing sound in his sleep, clutching a tiny stuffed toy."

    show p happy_talking:
        zoom 0.30
        xzoom 1
    p "Guardian Gloria! It's wonderful to see you!"

    show p proud
    p "Your grandsons have been extraordinary! They've restored four beacons!"

    show g hands_on_hips_talking
    g "Of course they have. I never had a doubt."

    show g anchor
    g "These are Thompson boys. We don't know the meaning of the word 'quit.'"

    show h a_smile_looking_right_talking
    h "That's what Mom always says!"

    show h a_smile_looking_right
    show g hands_on_hips_talking
    g "Where do you think she learned it?"

    show g wink
    g "I've been watching you both from up here. The Library, the Valley, the Conservatory, the Clocktower..."

    show g presenting_talking
    g "You faced every challenge with courage and kindness. I'm so proud."

    show t a_hands_on_hips_expressionless_talking
    t "Thanks, G-Mom. But we're not done yet."

    show t a_hands_on_hips_expressionless
    show h a_unsure_looking_right_talking
    h "The Shadow King is still out there. And this beacon is still dark."

    show h a_unsure_looking_right
    show g frustrated_talking
    g "Yes. The Shadow King."

    show g frustrated
    g "He's been gathering power at the far end of the bridge. Drawing in all the darkness of the realm."

    show g hands_on_hips_talking
    g "To reach him, you'll need to cross the bridge. But it's been shattered into pieces."

    show g anchor
    g "The fragments are scattered across the sky, held together only by threads of light."

    show t a_pointing_confused_talking
    t "So we have to... jump across floating pieces of bridge?"

    show t a_pointing_confused
    show g hands_on_hips_talking
    g "Not just jump. The bridge fragments are guarded by shadow creatures."

    show g frustrated_talking
    g "You'll need to fight your way through, collecting shards of light to rebuild the path."

    show g frustrated
    show h a_skeptical_talking
    h "That sounds really hard."

    show h a_skeptical
    show g anchor
    g "It is. But you've done hard things before."

    show g presenting_talking
    g "Remember when Tristan fell off his bike and scraped his knee, but still finished the race?"

    show g presenting
    show t a_hands_on_hips_smile_talking
    t "I did come in last place though."

    show t a_hands_on_hips_smile
    show g hands_on_hips_talking
    g "But you finished. That's what matters."

    show g presenting_talking
    g "And Henry—remember when you were scared of the dark, but you walked through the whole haunted house anyway?"

    show h a_thumbs_up_determined_talking
    h "I only screamed twice!"

    show h a_thumbs_up_determined
    show g anchor
    g "You faced your fear. That's courage."

    show g hands_on_hips_talking
    g "This is just another haunted house. Another race to finish."

    show g anchor
    g "And this time, you have each other."

    show t a_determined_looking_left_talking:
        xzoom -1
    t "She's right. We can do this."

    show t a_determined_looking_left
    show h a_thumbs_up_determined_talking:
        xzoom -1
    h "Together!"

    show h a_thumbs_up_determined
    show p proud
    p "Splendid! Here's the plan—"

    show p happy_talking
    p "Navigate through the bridge fragments, defeat the shadows, and collect three beacon shards."

    show p offended
    p "Once you have all three, the path to the Shadow King will be revealed."

    show g hands_on_hips_talking
    g "I'll stay here with Logan and keep the light burning as long as I can."

    show g frustrated_talking
    g "But hurry—I can feel the darkness growing stronger."

    "Logan stirred in G-Mom's arms, making a tiny yawn."

    show g anchor
    g "He believes in you too. Even if he can't say it yet."

    show t a_hands_on_hips_smile_talking
    t "We won't let you down, G-Mom."

    show t a_hands_on_hips_smile
    show h a_thumbs_up_determined_talking
    h "Or Logan!"

    show h a_thumbs_up_determined
    show g waving
    g "Go on, then. Save the realm. And when you're done..."

    show g hands_on_hips_talking
    g "I'll make you both your favorite cookies."

    show h a_smile_looking_right_talking:
        xzoom 1
    h "Chocolate chip?!"

    show h a_smile_looking_right
    show g anchor
    g "With extra chips. Now go!"

    hide t
    hide h
    hide g
    hide p
    with dissolve

    "The brothers stepped forward onto the first bridge fragment, ready for their greatest challenge."

    jump skybridge_quest_intro

# --- BEACON QUEST INTRO ---

label skybridge_quest_intro:
    scene bg_skybridge:
        zoom 0.9
        yalign 0.3
        xalign 0.5
    with dissolve

    "The bridge fragment floated in an ocean of clouds and stars."
    "Shadow creatures lurked at the edges, their eyes glowing with malevolent light."

    show t a_determined_looking_left:
        zoom 0.35
        xalign 0.4
        yalign 0.7
    show h a_thumbs_up_determined:
        zoom 0.32
        xalign 0.6
        yalign 0.75
    with dissolve

    t "I see shadow creatures everywhere..."

    show h a_pointing_smile_talking
    h "And those glowing things must be the beacon shards!"

    show h a_pointing_smile
    show p happy_talking:
        zoom 0.25
        xalign 0.85
        yalign 0.6
    with dissolve

    p "WASD to move, SPACE to attack! Collect all three beacon shards!"

    show p worried
    p "Be careful—the shadow creatures will try to stop you!"

    hide t
    hide h
    hide p
    with dissolve

    "WASD to move, SPACE to attack. Collect 3 beacon shards to open the path forward!"

    call beacon_quest_start()

    jump skybridge_quest_complete

# --- QUEST COMPLETE ---

label skybridge_quest_complete:
    scene bg_skybridge:
        zoom 0.85
        yalign 0.3
        xalign 0.5
    with fade

    if beacon_quest_victory:
        jump skybridge_quest_victory
    else:
        jump skybridge_quest_retry

label skybridge_quest_retry:
    show t a_hands_to_head_frustrated:
        zoom 0.35
        xalign 0.4
        yalign 0.7
    show h a_looking_down_confused:
        zoom 0.32
        xalign 0.6
        yalign 0.75
    with dissolve

    "The shadows overwhelmed them. They had to retreat."

    show g worried:
        zoom 0.35
        xalign 0.85
        yalign 0.6
    with dissolve

    g "It's alright, boys. Catch your breath and try again."
    g "The shadows are strong, but you're stronger together!"

    show p nervous_laugh:
        zoom 0.25
        xalign 0.15
        yalign 0.7
    with dissolve

    p "Remember—don't let them surround you! Keep moving!"

    menu:
        "Try again!":
            jump skybridge_quest_intro
        "Take a break first":
            "The brothers rested for a moment, planning their approach."
            jump skybridge_quest_intro

label skybridge_quest_victory:
    "The final beacon shard clicked into place!"

    show light_burst at light_burst_grow_2:
        alpha 0.0
        ease 0.3 alpha 1.0
        ease 0.5 alpha 0.0
    with vpunch

    "A bridge of pure light materialized before them, stretching toward a dark throne in the distance."
    "Upon it sat a massive figure wreathed in shadows—the Shadow King himself."

    show t a_surprised:
        zoom 0.35
        xalign 0.35
        yalign 0.6
    show h a_surprised_looking_down:
        zoom 0.32
        xalign 0.55
        yalign 0.65
        xzoom -1
    with dissolve

    t "There he is..."
    h "He's... huge."

    "The Shadow King rose from his throne, his voice echoing across the sky."

    "SHADOW KING" "So... the Twin Sparks finally arrive."

    "SHADOW KING" "You've restored my corrupted beacons. Impressive."

    "SHADOW KING" "But do you really think you can challenge ME?"

    show t a_determined_looking_left_talking:
        xzoom 1
    t "We've come this far! We're not backing down now!"

    show t a_determined_looking_left
    show h a_thumbs_up_determined_talking:
        xzoom 1
    h "Everyone's counting on us! We're going to stop you!"

    show h a_thumbs_up_determined

    "SHADOW KING" "HA HA HA! Such spirit!"

    "SHADOW KING" "Very well, little sparks. Let us see if your light can truly overcome my darkness."

    "SHADOW KING" "COME! FACE ME!"

    show p offended:
        zoom 0.28
        xalign 0.8
        yalign 0.65
    with dissolve

    p "This is it, Twin Sparks! The final battle!"

    show p happy_talking
    p "You must fight TOGETHER! Tristan, use the arrow keys! Henry, use WASD!"

    show p proud
    p "Combine your attacks! Only by working as one can you defeat him!"

    show g presenting_talking:
        zoom 0.3
        xalign 0.15
        yalign 0.7
    with dissolve

    g "Remember everything you've learned! Trust each other!"

    show g anchor
    g "You're not alone—everyone who loves you is cheering you on!"

    "Logan giggled in G-Mom's arms, as if he understood."

    hide t
    hide h
    hide p
    hide g
    with dissolve

    jump skybridge_boss_intro

# --- BOSS BATTLE INTRO ---

label skybridge_boss_intro:
    scene bg_skybridge:
        zoom 0.9
        yalign 0.5
        xalign 0.5
    with dissolve

    "The brothers stepped onto the bridge of light, facing the Shadow King together."
    "Behind them, the restored beacons blazed with power, lending them strength."

    show t a_determined_looking_left:
        zoom 0.35
        xalign 0.35
        yalign 0.7
        xzoom 1
    show h a_thumbs_up_determined:
        zoom 0.32
        xalign 0.65
        yalign 0.75
        xzoom -1
    with dissolve

    t "Ready, Henry?"
    h "Ready, Tristan!"

    t "Let's do this—TOGETHER!"

    hide t
    hide h
    with dissolve

    "Tristan: Arrow Keys + Enter to attack | Henry: WASD + Space to attack"
    "Work together to defeat the Shadow King!"

    call boss_rush_start()

    jump skybridge_boss_complete

# --- BOSS BATTLE COMPLETE ---

label skybridge_boss_complete:
    scene bg_skybridge:
        zoom 0.85
        yalign 0.5
        xalign 0.5
    with fade

    if boss_rush_victory:
        jump skybridge_victory
    else:
        jump skybridge_boss_retry

label skybridge_boss_retry:
    show t a_hands_on_head_frustrated:
        zoom 0.35
        xalign 0.4
        yalign 0.6
    show h a_hands_to_head_frustrated:
        zoom 0.32
        xalign 0.6
        yalign 0.65
    with dissolve

    "The Shadow King's power was overwhelming. The brothers were forced back."

    "SHADOW KING" "Is that all you have? Pathetic!"

    show g frustrated:
        zoom 0.35
        xalign 0.85
        yalign 0.6
    with dissolve

    g "Don't give up! You're so close!"
    g "Remember—work TOGETHER! Time your attacks!"

    show p worried:
        zoom 0.25
        xalign 0.15
        yalign 0.7
    with dissolve

    p "The Shadow King has weak points between attacks! Strike when he's vulnerable!"

    menu:
        "Try again!":
            jump skybridge_boss_intro
        "Take a break first":
            "The brothers caught their breath, strengthening their resolve."
            jump skybridge_boss_intro

# --- FINAL VICTORY ---

label skybridge_victory:
    "With one final combined attack, light EXPLODED from the brothers!"

    show light_burst at light_burst_grow_2:
        alpha 0.0
        ease 0.5 alpha 1.0
        ease 1.0 alpha 0.0
    with vpunch

    "The Shadow King howled as pure radiance tore through his darkness."

    "SHADOW KING" "NO! IMPOSSIBLE! How can two children—"

    "SHADOW KING" "HOW CAN YOUR LIGHT BE SO STRONG?!"

    show t a_cheering_mouth_open:
        zoom 0.35
        xalign 0.35
        yalign 0.6
        xzoom 1
    show h a_cheer_eyes_closed:
        zoom 0.32
        xalign 0.55
        yalign 0.65
        xzoom -1
    with dissolve

    t "Because we're not just two kids!"

    h "We have our whole family behind us!"

    "SHADOW KING" "Family... such a simple thing..."

    "SHADOW KING" "And yet... it burns brighter than any beacon..."

    "The Shadow King's form began to dissolve, shadows streaming away into nothing."

    "SHADOW KING" "Perhaps... there is more to light than I understood..."

    "SHADOW KING" "Remember this, Twin Sparks... even the deepest darkness..."

    "SHADOW KING" "...fears the smallest light..."

    "With a final flash, the Shadow King vanished completely."
    "In his place, the Skybridge Beacon blazed to life—brighter than ever before."

    show light_burst at light_burst_grow_2:
        alpha 0.0
        ease 0.3 alpha 1.0
        ease 0.5 alpha 0.0
    with vpunch

    "All five beacons connected, their light streaming together across the sky."
    "The realm ERUPTED with color and warmth as darkness fled from every corner."

    jump skybridge_finale

# --- FINALE ---

label skybridge_finale:
    scene bg_skybridge:
        zoom 0.85
        yalign 1.0
        xalign 0.5
    with dissolve

    "The bridge solidified beneath their feet as light returned to the realm."
    "G-Mom hurried over, Logan giggling and clapping in her arms."

    show g cheering:
        zoom 0.5
        xalign 0.25
        yalign 0.75
    show t a_cheering_mouth_open:
        zoom 0.38
        xalign 0.45
        yalign 0.78
    show h a_cheer_eyes_closed:
        zoom 0.35
        xalign 0.6
        yalign 0.8
        xzoom -1
    show p happy_talking:
        zoom 0.3
        xalign 0.78
        yalign 0.82
    with dissolve

    g "YOU DID IT! My wonderful, brave grandsons!"

    p "INCREDIBLE! ABSOLUTELY INCREDIBLE!"

    "G-Mom pulled both boys into a tight embrace, tears of joy in her eyes."

    show g anchor
    g "I knew you could do it. I always knew."

    show t a_hands_on_hips_smile_talking
    t "We couldn't have done it without everyone. Aunt Kayla, Uncle Ryan, Mom, Dad..."

    show t a_hands_on_hips_smile
    show h a_smile_looking_right_talking:
        xzoom 1
    h "And you, G-Mom! And even baby Logan!"

    show h a_smile_looking_right
    "Logan babbled happily and reached toward the glowing sky."

    show g hands_on_hips_talking
    g "He's proud of you too. Even if all he can say is 'ba ba.'"

    show g anchor
    show p proud
    p "Twin Sparks... there are no words to express my gratitude."

    show p happy_talking
    p "You've saved the realm! All five beacons burn bright once more!"

    show p offended
    p "The light will spread across the land, bringing hope and harmony back to everyone."

    show h a_unsure_looking_right_talking
    h "What happens now? Do we... go home?"

    show h a_unsure_looking_right
    show p sad
    p "I'm afraid so. Now that the darkness is defeated, the lantern will guide you back."

    show p nervous_laugh
    p "You'll wake up as if from a dream... though you'll remember everything."

    show t a_hands_on_hips_expressionless_talking
    t "Will we ever come back? Will we see everyone again?"

    show t a_hands_on_hips_expressionless
    show g presenting_talking
    g "That depends on whether the realm needs you again."

    show g anchor
    g "But even if you don't return here... you'll see all of us at home."

    show g hands_on_hips_talking
    g "Aunt Kayla, Uncle Ryan, your mom, your dad... they're all there, waiting."

    show g anchor
    g "They may not remember being guardians, but they'll always love you just the same."

    show p happy_talking
    p "It's time, Twin Sparks. Place your hands on the lantern one last time."

    "Pipwick held out his lantern, now blazing with the combined light of all five beacons."

    show h a_smile_looking_right_talking
    h "Bye, Pipwick. Thanks for choosing us."

    show h a_smile_looking_right
    show p sad
    p "Thank you for answering the call. I couldn't have asked for better heroes."

    show t a_hands_on_hips_smile_talking
    t "Bye, G-Mom. See you at the next family dinner."

    show t a_hands_on_hips_smile
    show g waving
    g "I'll be there. With cookies. Now go on—your adventure is complete."

    "Logan waved a tiny hand, babbling a cheerful goodbye."

    "The brothers looked at each other one last time, then placed their hands on the lantern together."

    show light_burst at light_burst_grow_2:
        alpha 0.0
        ease 0.3 alpha 1.0

    "Light surrounded them, warm and welcoming."
    "They felt themselves lifting, floating, rising through clouds and stars."

    hide t
    hide h
    hide g
    hide p
    with dissolve

    "The voices of everyone they'd met echoed around them..."

    k "Well done, boys!"
    r "That's my nephews!"
    l "I'm so proud of you!"
    j "Make the family proud!"
    g "We love you!"

    "And then... peace."

    scene image "#ffffff"
    with fade

    pause 1.0

    jump game_epilogue

# --- EPILOGUE ---

label game_epilogue:
    scene bg_living_room:
        zoom 0.85
        yalign 1.0
        xalign 0.5
    with fade

    play music "audio/music/home_theme.ogg" fadein 2.0

    "..."

    "Tristan opened his eyes slowly."
    "He was lying on the couch in Grandma's living room, warm sunlight streaming through the windows."

    show t a_surprised:
        zoom 0.4
        xalign 0.5
        yalign 0.8
    with dissolve

    "Beside him, Henry was just waking up too."

    show h a_surprised_looking_down:
        zoom 0.36
        xalign 0.65
        yalign 0.82
        xzoom -1
    with dissolve

    t "Henry...? Was that... real?"

    h "I... I think so? I remember everything. The library, the valley, the crystals..."

    t "The giant metal spiders."

    h "The Shadow King."

    "They looked at each other, the same question in their eyes."

    show t a_hands_on_hips_smile
    show h a_thumbs_up_determined:
        xzoom 1

    t "We actually did it."

    h "We saved the realm!"

    "Before they could say more, the sound of footsteps approached."

    l "Oh good, you're awake! Dinner's almost ready."

    show l anchor:
        zoom 0.4
        xalign 0.2
        yalign 0.75
    with dissolve

    "Mom smiled at them from the doorway, looking completely normal."

    l "You two must have been exhausted—you've been napping for hours!"

    show t a_pointing_confused_talking
    t "Mom... do you remember anything? About the Crystal Conservatory?"

    show t a_pointing_confused
    show l surprised_talking
    l "The what now?"

    show l hands_on_hips_talking
    l "Did you have weird dreams? You shouldn't eat so much candy before naps."

    show l hands_on_hips
    show h a_unsure_looking_right_talking
    h "It wasn't a dream! We—"

    show h a_unsure_looking_right

    "Henry stopped as G-Mom appeared behind Mom, holding baby Logan."
    "She caught the boys' eyes and gave them a tiny, knowing wink."

    show g anchor:
        zoom 0.35
        xalign 0.35
        yalign 0.8
    with dissolve

    g "Let them rest, Lauren. They've had quite the adventure."

    show l skeptical_talking
    l "Adventure? They've been asleep on the couch."

    show l skeptical
    show g shrug_talking
    g "The best adventures happen in our dreams, dear."

    "G-Mom smiled at the boys, and for just a moment, they saw a flicker of light in her eyes."

    show g hands_on_hips_talking
    g "Now come on, both of you. Your father made his famous tacos."

    show g anchor
    g "And I believe I owe you some chocolate chip cookies."

    "The boys exchanged a glance, then grinned."

    show t a_hands_on_hips_smile_talking
    t "With extra chips?"

    show t a_hands_on_hips_smile
    show g wink
    g "With extra chips."

    "The family gathered in the dining room as the sun set outside."
    "Uncle Ryan told jokes that made everyone groan."
    "Aunt Kayla corrected his pronunciation of 'quinoa.'"
    "Dad challenged everyone to an arm-wrestling contest."
    "Mom reminded him that the table wasn't sturdy enough for that."
    "G-Mom smiled at everything, bouncing Logan on her knee."

    "And Tristan and Henry sat side by side, sharing secret smiles."

    "They had saved a realm."
    "They had faced darkness and won."
    "They had discovered that family—whether in magical kingdoms or around dinner tables—"
    "—is the brightest light of all."

    scene image "#000000" with fade

    pause 1.0

    centered "{size=+10}THE END{/size}"

    pause 2.0

    centered "{size=+5}Thank you for playing{/size}"
    centered "{size=+5}SPARKS OF THE BEACON{/size}"

    pause 2.0

    centered "Created with love for"
    centered "Tristan and Henry"

    pause 2.0

    centered "May your light always shine bright."

    pause 3.0

    return
