# =======================================================
# REGION 1: THE LUMINOUS LIBRARY (Kayla - Linguist)
# =======================================================

label region_1_library:
    # Library region music and ambient
    play music MUSIC_LIBRARY fadein 2.0
    play ambient AMBIENT_LIBRARY fadein 2.0 volume 0.3 loop

    scene bg_library_ext:
        zoom 0.8
        yalign 1.0
        xalign 0.55

    with fade

    play sound SFX_PORTAL_EXIT
    pause 1.0
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
        xalign 0.45
        yalign 0.8
    show h a_back:
        alpha 1.0
        zoom 0.36
        xalign 0.55
        yalign 0.8
    show p facing_away:
        alpha 1.0
        zoom 0.25
        xalign 0.45
        yalign 0.85    


    "The brothers arrived at the grand entrance of the Luminous Library."

    t "Wow... This place is gigantic."
    h "Yeah, for real."
    p "Welcome to the Luminous Library, home of the Lantern of Knowledge."
    p "This is as good a place to start as any."
    p "Let's go inside and see if the Guardian of Knowledge is available."

    show h a_surprised_looking_down:
        xzoom -1
    h "Guardian of Knowledge?"
    p "Yes, every region has a guardian who watches over it."
    show h a_unsure_looking_right
    show t a_looking_down_confused_talking:
        xzoom -1
    t "Like a librarian?"
    show h a_surprised_looking_down
    show t a_looking_down_confused
    p "More or less. In this region, they help maintain order and ensure the knowledge is preserved."
    show h a_unsure_looking_right_talking
    h "I hope they are nice."
    show h a_back:
        xzoom 1
    p "Oh, I'm sure you'll get along just fine."

    show t a_back:
        xzoom 1
    "The boys took a deep breath and approached the colossal structure, stepping through the grand doors."

    show t a_back:
        xoffset 175
        yoffset -50
        zoom 0.24
    show h a_back:
        xoffset 250
        yoffset -50
        zoom 0.24
    show p facing_away:
        xoffset 280
        yoffset -85
        zoom 0.14
    with dissolve
    pause 1.0
    show t a_back:
        xoffset 360
        yoffset -105
        zoom 0.10
    show h a_back:
        xoffset 260
        yoffset -105
        zoom 0.10
    show p facing_away:
        xoffset 390
        yoffset -135
        zoom 0.05
    with dissolve
    pause 1.0

    hide t
    hide h 
    hide p
    with dissolve

    scene bg_library_int_new:
        zoom 0.8
        yalign 1.0
        xalign 0.5
    show screen floating_books_group
    
    show h a_back:
        zoom 0.36
        xalign 0.79
        yalign 0.8
        xzoom -1
    show t a_back:
        zoom 0.4
        xalign 0.69
        yalign 0.8
        xzoom -1
    show p facing_away:
        zoom 0.25
        xalign 0.59
        yalign 0.85
        xzoom -1
    with fade


    "The library was stacked to the ceiling with rows and rows of books."
    "Every sound echoed softly, and the air smelled like old paper and leather."
    show h a_surprised_looking_up
    h "It’s so quiet…"
    show h a_hands_on_hips:
        xzoom 1
        zoom 0.37
    show t a_unsure_looking_left_talking

    t "Feels like the whole place is holding its breath."
    show t a_unsure_looking_left:
        xzoom -1
    show p nervous_laugh:
        zoom 0.30
        xzoom 1
    p "Perhaps I should try and call the Guardian to-"
    show light_burst at light_burst_grow_2:
        alpha 0.0
        xoffset -100
        ease 0.2 alpha 1.0
        ease 0.4 alpha 0.0
    pause 0.2
    show k waving:
        xalign 0.45
        yalign 0.65
        zoom 0.35
    with dissolve

    show h a_back:
        xzoom -1
    show t a_back:
        xzoom -1
    show p facing_away:
        zoom 0.25
        xzoom -1

    k "You made it! I was beginning to think you were lost."
    show k anchor:
        xalign 0.3
        yalign 0.8
        zoom 0.5
    show h a_skeptical:
        xzoom -1
    show t a_pointing_confused_talking:
        xzoom 1
    show p happy_talking:
        zoom 0.30
    t "Aunt Kayla?!"
    show t a_pointing_confused
    show k hands_on_hips_talking
    k "Yes! Well... something like her, anyway. I'm a memory made of light. I only exist in this moment."
    show k hands_on_hips
    show h a_skeptical_talking
    h "Wait, time-out. For real?"
    show h a_skeptical
    show k hands_on_hips_talking
    k "For real."
    show k hands_on_hips


    show p nervous_laugh
    p "I think it's about time I take my leave..."
    show p happy_talking
    p "Good luck, Twin Sparks!"
    show light_burst at light_burst_grow_2:
        alpha 0.0
        xoffset -100
        ease 0.2 alpha 1.0
        ease 0.4 alpha 0.0
    pause 0.2
    hide p with dissolve


    show h a_skeptical_talking
    h "This is... weird."
    show h a_skeptical
    show t a_pointing_confused_talking
    t "Yeah, a little creepy too."
    show k annoyed_talking
    k "Well that is a bit rude."
    show k annoyed
    
    show t a_hands_on_hips_talking:
        xzoom -1
    t "Sorry. I didn't mean it like that."
    show t a_hands_on_hips_expressionless
    show k hands_on_hips_talking
    k "It's quite alright."
    show k anchor
    show t a_hands_on_hips_smile
    show h a_eyes_closed_talking_smile:
        xzoom 1
    h "I don't mean to interrupt but..."
    show h a_unsure_looking_right_talking:
        xzoom -1
        xoffset 60
    h "What happened to the library?"
    show h a_unsure_looking_right
    show k presenting_talking:
        xzoom -1
    k "Oh, the books? I thought you might notice."
    k "Welcome to the Luminous Library, home of the Lantern of Knowledge."
    show k annoyed_talking:
        xzoom 1

    k "I wish it looked a bit more welcoming, but..."
    k "The Lantern of Knowledge has gone dark. Its darkness has invited chaos."

    show k annoyed
    show h a_unsure_looking_right_talking
    h "Pipwick told us about Bedimurk. Did he do this?"

    show h a_unsure_looking_right
    show k hands_on_hips_talking
    k "That grumpy old mole? Yes, I'm afraid so."
    k "He tunneled up from below and drained the lantern's light while I was shelving books."

    show k annoyed_talking
    k "Left behind nothing but claw marks and the smell of damp earth."

    show t a_pointing_confused_talking:
        xzoom 1
    t "Why doesn't someone just... stop him?"

    show t a_pointing_confused
    show k hands_on_hips_talking:
        xzoom -1
    k "He's slippery. And he knows these tunnels better than anyone."
    k "By the time you spot his shadow, he's already three burrows away."

    show k annoyed
    show t a_hands_on_hips_expressionless_talking
    t "Looks pretty chaotic to me."
    show t a_hands_on_hips_expressionless
    show k annoyed_talking
    k "Yes, and without the light of knowledge, the language of this realm has begun to fade."
    show k annoyed_talking
    k "Books in this realm are not the same as books of your realm."
    show k annoyed
    show h a_unsure_looking_right_talking
    h "What do you mean?"
    show h a_unsure_looking_right
    show k presenting_talking:
        xzoom -1
    k "These books are the actual {i}knowledge itself{/i}, encoded in symbols of light."
    show k presenting
    show t a_pointing_confused_talking:
        xzoom 1

    t "So you're saying the books are... alive?"
    show t a_hands_on_hips_expressionless:
        xzoom -1
    show k shrug_talking
    k "In a manner of speaking, yes."
    show k annoyed_talking:
        xzoom 1
    k "And all of the knowledge has become... well, disorganized."
    show k hands_on_hips_talking
    k "Have you ever tried to say something but had trouble finding the words to say it?"
    show k hands_on_hips
    show h a_skeptical_talking:
        xoffset 0
    h "Yeah, like when my brain is full of ideas but I can't get them out."
    show h a_skeptical
    show t a_hands_on_hips_expressionless_talking
    t "Or when I'm so excited to tell someone something that I put the words in the wrong order."
    show t a_hands_on_hips_expressionless
    show k presenting_talking:
        xzoom -1
    k "Exactly!"
    k "Can you imagine what will happen when the entire realm's thoughts look like this?"
    show h a_skeptical_talking
    h "That sounds... bad."
    show h a_skeptical
    show k annoyed_talking:
        xzoom 1
    k "Very bad. If the Lantern of Knowledge remains dark, the entire realm could fall into chaos."
    show k annoyed
    show t a_hands_on_hips_talking
    t "So what do we do?"
    show t a_hands_on_hips_smile
    show k hands_on_hips_talking
    k "We need to restore the language of light. And to do that, we must put things in order."
    show k hands_on_hips
    show h a_skeptical_talking
    h "So we just… fix the books?"
    show h a_skeptical
    show k presenting_talking:
        xzoom -1
    k "Yes, we will sort the books by helping to rewrite their contents."
    show k hands_on_hips:
        xzoom 1
    show t a_pointing_confused_talking:
        xzoom 1
    t "But we have no idea how to read these languages! These letters look like someone spilled spaghetti!"
    show k hands_on_hips_talking
    show t a_pointing_confused
    k "Oh, you thought we needed your help with {i}easy problems{/i}?"
    show k annoyed_talking
    k "I know you can do it. Pipwick found you both for a reason."
    show k anchor
    show t a_hands_on_hips_expressionless_talking
    t "Alright, I guess there's no harm trying..."
    show t a_hands_on_hips_expressionless
    show h a_smile_looking_right_talking
    h "As long as we don't have to read anything out loud."
    show t a_hands_on_hips_smile
    show h a_smile_looking_right
    show k presenting_talking:
        xzoom -1
    k "Reading out loud helps us all understand better. I recommend it!"
    

    "The Guardian waved her hand, and the boys were presented with their first challenge."

    jump start_rune_decode

label library_conclusion:
    # Stop minigame music when library games complete
    $ library_stop_music()

    scene bg_library_int
    show k cheering
    show h a_cheer_eyes_closed:
        xzoom -1
    show t a_cheering_mouth_open:
        xzoom 1
    with dissolve
    k "Well done! You've restored order to the library!"
    show t a_hands_on_hips_smile_talking
    show h a_smile_looking_right
    t "That was... actually kind of fun."
    show h a_smile_looking_right_talking
    h "Yeah, I didn't think I'd enjoy a word puzzle."
    show h a_smile_looking_right
    show k presenting_talking

    k "Thank you both for your help. This place feels brighter already."
    show light_burst at light_burst_grow_2:
        alpha 0.0
        xoffset -100
        ease 0.2 alpha 1.0
        ease 0.4 alpha 0.0
    show p happy_talking
    with dissolve
    p "Yay! You did it!"
    p "The knowledge is coming back!"
    show k hands_on_hips_talking
    k "Indeed it is, Pipwick."
    show k hands_on_hips
    show t a_pointing_confused_talking
    t "You two know each other?"
    show t a_pointing_confused
    show k presenting_talking
    k "Oh yes, Pipwick and I go way back."
    show k presenting
    show p proud
    p "Aunt Kayla is the best! She helped me pass my Elvish exams in high school!"
    show k hands_on_hips_talking
    k "I hope you are still practicing every day, Pipwick."
    show k hands_on_hips
    show t a_hands_on_hips_smile
    show p nervous_laugh
    p "Of course! Well... most days."
    show p offended
    p "But let's stay focused, here. We have more to do!"
    show h a_skeptical_talking
    h "More puzzles?"
    show h a_skeptical
    show p proud
    p "Not here, but yes! There are other regions in this realm that need our help."
    show k shrug_talking
    k "With each section you complete, the Lantern will shine brighter."
    show k anchor
    show t a_determined_looking_left_talking:
        xzoom 1
    t "Alright, let's do it!"
    show t a_determined_looking_left
    show h a_thumbs_up_determined_talking
    h "Yeah, let's go!"
    show h a_thumbs_up_determined
    show k hands_on_hips_talking:
        xzoom -1
    k "I'm so proud of you both. You are truly illuminating."
    show k presenting_talking
    k "Good luck on your next region!"
    show t a_hands_on_hips_talking
    t "Will we see you again?"
    show k hands_on_hips_talking
    k "Oh, perhaps. But if not me, then you will see the {i}real{/i} Aunt Kayla when you return home."
    show k hands_on_hips
    show h a_skeptical_talking
    h "You mean {i}if{/i} we return home."
    show h a_skeptical
    show k annoyed_talking
    k "Yes, Henry. If."
    show p nervous_laugh
    p "Oh, come now. Don't be so gloomy!"
    show p happy_talking
    p "We are off to an excellent start, and I just know you boys will keep up the great work."
    p "Onward to the next region!"
    show t a_hands_on_hips_smile_talking
    t "Bye, Aunt Kayla!"
    show t a_hands_on_hips_smile
    show h a_eyes_closed_talking_smile:
        xzoom 1
    h "Enjoy your books!"
    show h a_smile_looking_right
    show k waving
    k "Goodbye, boys! Be careful out there."
    hide k with dissolve

    "Pipwick held out his lantern, its light pulsing warmly."
    show h a_unsure_looking_right_talking:
        xzoom -1
    show t a_unsure_looking_left:
        xzoom 1
    show p proud
    p "Okay, Twin Sparks, time to move on."
    p "The next stop is the Ironwood Valley."
    show p offended
    p "And Henry, {i}now{/i} you can touch the lantern."
    show h a_skeptical_talking
    h "Are you sure?"
    show h a_skeptical
    show p nervous_laugh:
        xzoom 1
    p "Absolutely. Go ahead."
    show h a_skeptical_talking
    h "We aren't going to get lost again or something?"
    show h a_skeptical
    show p proud
    p "No, no. This time the lantern will take us to the correct place at the correct time."
    show h a_skeptical_talking
    h "Okay, because last time-"
    show p frustrated with vpunch
    p "{i}JUST TOUCH THE LANTERN!{/i}"
    show p nervous_laugh
    p "Please."
    show h a_eyes_closed_talking_smile:
        xzoom 1
    h "Okay, okay..."

    "Henry reached out and placed his hand on the lantern's frame. A soft glow enveloped them both."
    "Then all turned to white and silence. They felt themselves moving, floating through space and time."

    show light_burst at light_burst_grow_2:
        alpha 0.0
        ease 0.2 alpha 1.0


    jump region_2_valley




