# ── rune_decode_minigame.rpy (font-only version) ──────────────
# Uses your Khuzdulerebor-Rjno.ttf + a simple translation table

####################################################################################################################
# SPRITE CONFIGURATION - Set USE_SPRITES = True and provide sprite paths to use custom graphics
####################################################################################################################

init python:
    LIBRARY_USE_SPRITES = False  # Set to True when sprites are ready

    # Background sprites for library minigames
    LIBRARY_BACKGROUND_SPRITES = {
        "book_open": "images/minigames/library/backgrounds/book_open.png",
        "parchment": "images/minigames/library/backgrounds/parchment.png",
        "desk_surface": "images/minigames/library/backgrounds/desk_surface.png",
        "library_shelves": "images/minigames/library/backgrounds/library_shelves.png",
        "candlelight": "images/minigames/library/backgrounds/candlelight.png",
    }

    # Rune tile sprites (alternative to font rendering)
    RUNE_TILE_SPRITES = {
        "tile_empty": "images/minigames/library/runes/tile_empty.png",
        "tile_filled": "images/minigames/library/runes/tile_filled.png",
        "tile_correct": "images/minigames/library/runes/tile_correct.png",
        "tile_wrong": "images/minigames/library/runes/tile_wrong.png",
        "tile_partial": "images/minigames/library/runes/tile_partial.png",
        "tile_glow": "images/minigames/library/runes/tile_glow.png",
    }

    # Individual rune letter images (optional - can use font instead)
    RUNE_LETTER_SPRITES = {
        "A": "images/minigames/library/runes/letters/rune_a.png",
        "B": "images/minigames/library/runes/letters/rune_b.png",
        "C": "images/minigames/library/runes/letters/rune_c.png",
        "D": "images/minigames/library/runes/letters/rune_d.png",
        "E": "images/minigames/library/runes/letters/rune_e.png",
        "F": "images/minigames/library/runes/letters/rune_f.png",
        "G": "images/minigames/library/runes/letters/rune_g.png",
        "H": "images/minigames/library/runes/letters/rune_h.png",
        "I": "images/minigames/library/runes/letters/rune_i.png",
        "K": "images/minigames/library/runes/letters/rune_k.png",
        "L": "images/minigames/library/runes/letters/rune_l.png",
        "N": "images/minigames/library/runes/letters/rune_n.png",
        "O": "images/minigames/library/runes/letters/rune_o.png",
        "P": "images/minigames/library/runes/letters/rune_p.png",
        "R": "images/minigames/library/runes/letters/rune_r.png",
        "S": "images/minigames/library/runes/letters/rune_s.png",
        "T": "images/minigames/library/runes/letters/rune_t.png",
        "U": "images/minigames/library/runes/letters/rune_u.png",
        "W": "images/minigames/library/runes/letters/rune_w.png",
        "Y": "images/minigames/library/runes/letters/rune_y.png",
    }

    # UI element sprites for library minigames
    LIBRARY_UI_SPRITES = {
        "frame_ornate": "images/minigames/library/ui/frame_ornate.png",
        "frame_simple": "images/minigames/library/ui/frame_simple.png",
        "button_default": "images/minigames/library/ui/button_default.png",
        "button_hover": "images/minigames/library/ui/button_hover.png",
        "button_pressed": "images/minigames/library/ui/button_pressed.png",
        "hint_scroll": "images/minigames/library/ui/hint_scroll.png",
        "progress_bar_bg": "images/minigames/library/ui/progress_bar_bg.png",
        "progress_bar_fill": "images/minigames/library/ui/progress_bar_fill.png",
        "keyboard_bg": "images/minigames/library/ui/keyboard_bg.png",
        "key_normal": "images/minigames/library/ui/key_normal.png",
        "key_used": "images/minigames/library/ui/key_used.png",
        "key_correct": "images/minigames/library/ui/key_correct.png",
        "key_wrong": "images/minigames/library/ui/key_wrong.png",
    }

    # Effect sprites for library minigames
    LIBRARY_EFFECT_SPRITES = {
        "sparkle_success": "images/minigames/library/effects/sparkle_success.png",
        "dust_puff": "images/minigames/library/effects/dust_puff.png",
        "page_turn": "images/minigames/library/effects/page_turn.png",
        "ink_splatter": "images/minigames/library/effects/ink_splatter.png",
        "light_ray": "images/minigames/library/effects/light_ray.png",
        "magic_glow": "images/minigames/library/effects/magic_glow.png",
    }

    # Overlay sprites
    LIBRARY_OVERLAY_SPRITES = {
        "victory_scroll": "images/minigames/library/overlays/victory_scroll.png",
        "failure_scroll": "images/minigames/library/overlays/failure_scroll.png",
        "correct_stamp": "images/minigames/library/overlays/correct_stamp.png",
        "hint_reveal": "images/minigames/library/overlays/hint_reveal.png",
    }

    # Decorative sprites
    LIBRARY_DECOR_SPRITES = {
        "quill": "images/minigames/library/decor/quill.png",
        "inkwell": "images/minigames/library/decor/inkwell.png",
        "candle": "images/minigames/library/decor/candle.png",
        "bookmark": "images/minigames/library/decor/bookmark.png",
        "floating_book": "images/minigames/library/decor/floating_book.png",
        "magic_symbol": "images/minigames/library/decor/magic_symbol.png",
    }

####################################################################################################################
# END SPRITE CONFIGURATION
####################################################################################################################

####################################################################################################################
# AUDIO CONFIGURATION - Sound effects for Library minigames
####################################################################################################################

init python:
    LIBRARY_USE_AUDIO = True  # Set to False to disable all minigame audio

    LIBRARY_AUDIO_PATHS = {
        "key_press": "audio/sfx/minigames/library/key_press.ogg",
        "key_correct": "audio/sfx/minigames/library/key_correct.ogg",
        "key_wrong": "audio/sfx/minigames/library/key_wrong.ogg",
        "letter_reveal": "audio/sfx/minigames/library/letter_reveal.ogg",
        "word_complete": "audio/sfx/minigames/library/word_complete.ogg",
        "puzzle_solve": "audio/sfx/minigames/library/puzzle_solve.ogg",
        "hint_use": "audio/sfx/minigames/library/hint_use.ogg",
        "rune_glow": "audio/sfx/minigames/library/rune_glow.ogg",
        "page_flip": "audio/sfx/minigames/library/page_flip.ogg",
        "quill_write": "audio/sfx/minigames/library/quill_write.ogg",
        "victory": "audio/sfx/minigames/common/victory.ogg",
        "defeat": "audio/sfx/minigames/common/defeat.ogg",
    }

    def play_library_sound(sound_key, volume=1.0):
        """Play a library minigame sound effect using Ren'Py's audio system."""
        if not LIBRARY_USE_AUDIO:
            return
        path = LIBRARY_AUDIO_PATHS.get(sound_key)
        if path and renpy.loadable(path):
            renpy.sound.play(path)

####################################################################################################################
# END AUDIO CONFIGURATION
####################################################################################################################

init python:
    # ── YOUR RUNE FONT TRANSLATION TABLE ───────────────────────
    # Left = normal English letter (what the player must type)
    # Right = the character that shows the correct rune in your font
    # Example: when the answer needs “E”, we display “a” because in Khuzdulerebor-Rjno.ttf
    # the glyph at position “a” is actually the rune for E.
    # → Change the right-hand letters to whatever your font actually uses!
    RUNE_DISPLAY = {
        'A': 'a',   # replace these with the correct letters for your font
        'B': 'b',
        'C': 'c',
        'D': 'd',
        'E': 'e',   # ← very common one
        'F': 'f',
        'G': 'g',
        'H': 'h',
        'I': 'i',
        'K': 'k',
        'L': 'l',
        'N': 'n',
        'O': 'o',
        'P': 'p',
        'R': 'r',
        'S': 's',   # ← another very common one
        'T': 't',
        'U': 'u',
        'W': 'w',
        'Y': 'y',
        # add more if your font has them (most custom rune fonts are 1:1 A-Z mapping)
    }

    # ── 5 EASY PHRASES (now using your font) ─────────────────────
    DECODE_PHRASES = [
        {"mixed": "SnOw FALLS IN wInTER", "answer": "NW", "hint": "The coldest season."},
        {"mixed": "TrEES GrOW TaLL",  "answer": "RA",  "hint": "Mighty wood and leaves."},
        {"mixed": "tWINKlING StARlIGHt",     "answer": "TL",     "hint": "Beauty in the night sky."},
        {"mixed": "CATs ARE ThE BEsT",      "answer": "SH",      "hint": "Meow!"},
        {"mixed": "KNoWLeDGE IS PoWeR",    "answer": "OE",    "hint": "Wisdom brings strength."},
    ]

# ── Game state ───────────────────────────────────────
default current_phrase_idx = 0

default player_input = []        # List of typed letters
default hints_used = 0
default decode_state = "playing" # "playing", "victory", "failure"

# ── Screen ───────────────────────────────────────────
screen rune_decode_gate():
    # Book BG (reuse Wordle style)
    add Solid("#222222cc")
    # add "images/assets/books/book_open5.png" xalign -1.42 ypos 0.1 zoom 1.7

    $ phrase = DECODE_PHRASES[current_phrase_idx]

    $ answer = list(phrase["answer"].upper())  # No spaces for input
    $ max_hints = 3

    # ── STATE MESSAGES ──────────────────────────────────
    if decode_state == "victory":
        frame:
            xalign 0.5 yalign 0.5 background "#00a10080" padding (40,30)
            vbox:
                text "RUNES DECODED!" color "#ffffff" size 72 bold True xalign 0.5
                text "You've figured out the missing letters!" color "#ffffff" size 36 xalign 0.5

                text "Your true skills will now be revealed..." color "#ffffff" size 36 xalign 0.5
                null height 20
                textbutton "Enter the Inscription Hall" action Jump("start_rune_wordle") xalign 0.5

    elif decode_state == "failure":
        frame:
            xalign 0.5 yalign 0.5 background "#ff444480" padding (40,30)
            vbox:
                text "Not quite..." color "#ffffff" size 72 bold True xalign 0.5
                text "Don't give up!" color "#ff8888" size 48 xalign 0.5
                null height 20
                textbutton "Retry Phrase" text_color "#ffffff" action Jump("restart_decode") xalign 0.5
    
    elif decode_state == "correct":
        frame:
            xalign 0.5 yalign 0.5 background "#00a10080" padding (40,30)
            vbox:
                text "Correct!" color "#ffffff" size 72 bold True xalign 0.5
                text "You cracked the code!" color "#ffffff" size 48 xalign 0.5
                null height 20
                textbutton "Next Phrase" text_color "#ffffff"action Jump("next_phrase") xalign 0.5



    # ── PLAYING ─────────────────────────────────────────
    if decode_state == "playing":
        # Title + Progress
        vbox xalign 0.5 yalign 0.08 spacing 10:
            text "Decode the ancient runes" color "#ffd700" size 52 bold True xalign 0.5
            text "Challenge [current_phrase_idx + 1]/5" color "#ffd700" size 36 xalign 0.5

        vbox xpos 0.225 ypos 0.45 spacing 10 xysize 550,350:
            text "Can you figure out which letters match the runes above?" color "#ffffff" size 32 xpos 0.1
            text "Use the keyboard to type your guesses." color "#ffffff" size 32 xpos 0.1
            text "Tap 'Hint' for a clue." color "#ffffff" size 32 xpos 0.1
            text "Once you decode all of the phrases, the real challenge begins!" color "#ffffff" size 32 xpos 0.1

        # MIXED PHRASE – lowercase = runes, uppercase = English
        frame:
            xalign 0.5 yalign 0.3 background "#000000db" padding (40,30) xsize 1000
            hbox xalign 0.5 spacing 0:
                for c in phrase["mixed"]:
                    if c.islower() and c.upper() in RUNE_DISPLAY:
                        # Lowercase letter -> show as rune
                        text "[RUNE_DISPLAY[c.upper()]]" font RUNE_FONT size 64 color "#ffffff" 
                    elif c.isupper():
                        # Uppercase letter -> show as English
                        text "[c]" font ENGLISH_FONT size 72 color "#ffffff"
                    else:
                        # Space or punctuation
                        text "[c]" font ENGLISH_FONT size 72 color "#ffffff"

        # BLANKS – player types normal English (shown in Aleo like Wordle right grid)
        $ answer_no_spaces = phrase["answer"].replace(" ", "")
        $ answer_list = list(answer_no_spaces)
        $ submitted = (len(player_input) == len(answer_list) and 
                        player_input != answer_list and decode_state == "victory") or decode_state == "failure"

        frame:
            xpos 0.5 ypos 0.42 background None padding (30,20) xysize 800,600
            vbox xalign 0.5 spacing 10:
                for i in range(len(answer_list)):
                    $ typed = player_input[i] if i < len(player_input) else None
                    $ bg_color = "#333333"
                    $ text_color = "#ffffff"
                    
                    # Color feedback after submission
                    if submitted and typed:
                        if typed == answer_list[i]:
                            $ bg_color = "#90EE90"  # Green - correct
                            $ text_color = "#007b00"
                        else:
                            $ bg_color = "#622121"  # Red - wrong
                            $ text_color = "#ffffff"
                    else:
                        $ bg_color = "#333333"
                        $ text_color = "#ffffff"
                    
                    fixed xysize(180,180):
                        add Solid(bg_color)
                        if typed:
                            text "[typed]" font ENGLISH_FONT size 104 color text_color xalign 0.5 yalign 0.5
        frame:
            xpos 0.4 ypos 0.42 background None padding (30,20) xysize 800,600
            vbox xalign 0.5 spacing 10:
                for i in range(len(answer_list)):
                    $ runes_to_guess = answer_list[i].lower() if answer_list else None
                    $ bg_color = "#333333"
                    $ text_color = "#ffffff"
                    
                    
                    
                    fixed xysize(180,180):
                        add Solid(bg_color)
                        if runes_to_guess:
                            text "[runes_to_guess]" font RUNE_FONT size 104 color text_color xalign 0.5 yalign 0.5

        frame: 
            xalign 0.5 ypos 0.8 background "#000000db" padding (30,20) xysize 800,150 
            hbox xalign 0.5 yalign 0.0 spacing 40:
                textbutton "Show Hint" action Function(show_hint, phrase["hint"]) text_color "#ffd700"
                textbutton "Clear" action SetVariable("player_input", []) text_color "#ffd700"  

            # SUBMIT 
            hbox xpos 0.35 ypos 0.5 spacing 20:
                if len(player_input) == len(answer):
                    textbutton "Submit Guess" action Function(submit_decode) text_color "#00bbff" xysize(500,60)
                else:
                    textbutton "Submit Guess" action Function(submit_too_soon) text_color "#6b6b6b" xysize(500,60)
    
        # ── REUSE WORDLE KEYBOARD (A-Z taps build player_input) ─
        for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
            key ch action If(
                decode_state == "playing" and len(player_input) < len(answer),
                [SetVariable("player_input", player_input + [ch.upper()]), Play("sound", "audio/sfx/type.ogg")]
            )

        key "K_BACKSPACE" action If(
            decode_state == "playing" and player_input,
            SetVariable("player_input", player_input[:-1])
        )

        key "K_RETURN" action [
            If(
            decode_state == "playing" and len(player_input) == len(answer),
            Function(submit_decode)
            ),
            If(
            decode_state == "correct",
            Jump("next_phrase")
            )
        ]
        key "K_KP_ENTER" action [
            If(
            decode_state == "playing" and len(player_input) == len(answer),
            Function(submit_decode)
            ),
            If(
            decode_state == "correct",
            Jump("next_phrase")
            )
        ]

# ── LOGIC (Mirror submit_guess) ──────────────────────
init python:
    def submit_decode():
        global current_phrase_idx, player_input, hints_used, decode_state

        phrase = DECODE_PHRASES[current_phrase_idx]
        answer_list = list(phrase["answer"].upper().replace(" ", ""))

        if player_input != answer_list:
            renpy.sound.play("audio/sfx/fail.ogg")  # Reuse Wordle fail
            decode_state = "failure"
            renpy.restart_interaction()
            return

        # Correct answer
        renpy.sound.play("audio/sfx/victory.ogg")  # Reuse Wordle victory
        
        # Check if this was the last phrase
        if current_phrase_idx + 1 >= len(DECODE_PHRASES):
            decode_state = "victory"
        else:
            decode_state = "correct"
        
        renpy.restart_interaction()

    def show_hint(hint_text):
        # Simple: Could add temp text popup, or renpy.notify(hint_text)
        renpy.notify(hint_text)

    def submit_too_soon():
        renpy.sound.play("audio/sfx/fail.ogg")
        renpy.notify("You must complete the phrase before submitting!")

# ── CALL FROM MAIN GAME ───────────────────────────────
label start_rune_decode:
    $ current_phrase_idx = 0
    $ current_pos = 0
    $ player_input = []
    $ hints_used = 0
    $ decode_state = "playing"
    scene bg_library with fade

    "The boys found articles and scrolls filled with peculiar symbols."
    "Some of the symbols looked as if they were recently written, while others had faded with age."
    "Some of the symbols appeared to be English letters, but others were unfamiliar."
    t "I think these are runes! I've read about them in books before."
    t "If we can decode the runes, we might be able to read these other symbols!"
    h "I'm in!"

    call screen rune_decode_gate

    
label next_phrase:
    if current_phrase_idx + 1 >= len(DECODE_PHRASES):
        $ decode_state = "victory"

    else:
        $ current_phrase_idx += 1
        $ current_pos = 0
        $ player_input = []
        $ hints_used = 0
        $ decode_state = "playing"
        scene bg_library with dissolve
        call screen rune_decode_gate


label restart_decode:
    $ player_input = []
    $ hints_used = 0
    jump start_rune_decode





########################################################################################################################################
########################################################################################################################################
######################################################## RUNE WORDLE MINIGAME ##########################################################
########################################################################################################################################
########################################################################################################################################



init python:
    # ── 15 MYSTIC 5-LETTER WORDS ───────────────────────
    CODEX = [
        {"book": 1,  "clue": "The knight's trusted weapon, long and sharp.", "target": list("SWORD")},
        {"book": 2,  "clue": "Four legs and a mane, a noble steed.", "target": list("HORSE")},
        {"book": 3,  "clue": "The sun sets, shadows fall.", "target": list("NIGHT")},
        {"book": 4,  "clue": "A pile of treasure guarded by dragons.", "target": list("HOARD")},
        {"book": 5,  "clue": "It beats with courage.", "target": list("HEART")},
        {"book": 6,  "clue": "It chases the darkness and illuminates the path ahead.", "target": list("LIGHT")},
        {"book": 7,  "clue": "The place we visit in sleep.", "target": list("DREAM")},
        {"book": 8,  "clue": "The heaviest part of a king's attire.", "target": list("CROWN")},
        {"book": 9,  "clue": "The student crafts a word, the wizard casts magic.", "target": list("SPELL")},
        {"book": 10, "clue": "Symbols carved in stone with magical power.", "target": list("RUNES")},
        {"book": 11, "clue": "Ice crystals form in the cold.", "target": list("FROST")},
        {"book": 12, "clue": "Used to light the beacon in the darkness.", "target": list("SPARK")},
        {"book": 13, "clue": "A piece of a broken whole.", "target": list("SHARD")},
        {"book": 14, "clue": "Unspeakable anger and fury.", "target": list("WRATH")},
        {"book": 15, "clue": "Brightest of all, infallible and eternal.", "target": list("TRUTH")},
    ]

    RUNE_FONT = "fonts/Erebcap1.ttf"
    ENGLISH_FONT = "fonts/Aleo-SemiBold.ttf"

# ── Game state ───────────────────────────────────────
default library_shelves = 0
default current_book = 0
default current_row   = 0
default current_guess = []          # list of 5 letters (or fewer)
default past_rows     = []          # list of completed guesses
default corrupted_slots = set()
default game_state = "playing"      # "playing", "victory", "failure"

default show_instructions = True

transform slide_book_in:
    xoffset -800
    alpha 0.0
    ease 0.5 xoffset 0 alpha 1.0

transform letter_fade_in:
    alpha 0.0
    ease 0.4 alpha 1.0
# ── Slot images (empty background) ─────────────────────
init python:
    import random
    slot_imgs = [
        "images/assets/slots/slot1.png","images/assets/slots/slot2.png",
        "images/assets/slots/slot3.png","images/assets/slots/slot4.png",
        "images/assets/slots/slot5.png","images/assets/slots/slot6.png"
    ]

    # -----------------------------------------------------------------
    # 1. Rune grid (original)
    # -----------------------------------------------------------------
    def build_letter_slot(letter, target, row_idx, col_idx):
        if letter is None:
            # 50 % transparent empty slot
            return Transform(random.choice(slot_imgs), alpha=0.0)
        

        # Current row – white normal letters with fade-in
        if row_idx >= len(past_rows):
            return At(
                Fixed(
                    Text(letter, font=RUNE_FONT, size=70, color="#000000", xalign=0.5, yalign=0.5,),
                    xysize=(90, 90),
                ),
                letter_fade_in
            )

        # Past rows – colour feedback with fade-in
        guess = past_rows[row_idx]

        if guess[col_idx] == target[col_idx]:                     # GREEN
            return At(
                Fixed(
                    Solid("#90EE90"), 
                    Text(letter, font=RUNE_FONT, size=70, color="#007b00", xalign=0.5, yalign=0.5),
                    xysize=(90,90)
                ),
                letter_fade_in
            )
        elif letter in target:                            # YELLOW
            return At(
                Fixed(
                    Solid("#FFD700"), 
                    Text(letter, font=RUNE_FONT, size=70, color="#535353", xalign=0.5, yalign=0.5),
                    xysize=(90,90)
                ),
                letter_fade_in
            )
        else:                                             # GRAY
            return At(
                Fixed(
                    Solid("#333"), 
                    Text(letter, font=RUNE_FONT, size=70, color="#c3c3c3", xalign=0.5, yalign=0.5),
                    xysize=(90,90),
                ),
                letter_fade_in
            )

    # -----------------------------------------------------------------
    # 2. English grid – identical logic, just a normal font
    # -----------------------------------------------------------------

    def build_letter_english(letter, target, row_idx, col_idx):
        if letter is None:
            return Transform(random.choice(slot_imgs), alpha=0.0)

        # Current row – white normal letters
        if row_idx >= len(past_rows):
            return Fixed(
                
                Text(letter, font=ENGLISH_FONT, size=80, color="#ffffff", xalign=0.5, yalign=0.5),
                xysize=(90, 90)
            )

        # Past rows – same colour rules
        guess = past_rows[row_idx]

        if guess[col_idx] == target[col_idx]:              # GREEN
            return Fixed(
                Solid("#90EE90"),
                Text(letter, font=ENGLISH_FONT, size=80, color="#007b00", xalign=0.5, yalign=0.5),
                xysize=(90, 90)
            )
        elif letter in target:                            # YELLOW
            return Fixed(
                Solid("#FFD700"),
                Text(letter, font=ENGLISH_FONT, size=80, color="#000", xalign=0.5, yalign=0.5),
                xysize=(90, 90)
            )
        else:                                             # GRAY
            return Fixed(
                Solid("#333"),
                Text(letter, font=ENGLISH_FONT, size=80, color="#ffffff", xalign=0.5, yalign=0.5),
                xysize=(90, 90)
            )
# ── SCREEN ─────────────────────────────────────────────
screen rune_wordle_builder():
    # Background
    add Solid("#222222cc")
    add "images/assets/books/book_open5.png" xalign -1.42 ypos 0.1 zoom 1.7 at slide_book_in

    $ book   = CODEX[current_book]
    $ target = book["target"]
    $ max_rows = 6

    # ── STATE MESSAGES ──────────────────────────────────
    if game_state == "victory":
        frame:
            xalign 0.5 yalign 0.5 background "#00a10080" padding (40,30)
            vbox:
                text "VICTORY!" color "#ffffff" size 72 bold True xalign 0.5
                text "The rune ignites!" color "#ffffff" size 48 xalign 0.5
                null height 20
                textbutton "Next Book" action Return(True) xalign 0.5

    elif game_state == "failure":
        frame:
            xalign 0.5 yalign 0.5 background "#ff444480" padding (40,30)
            vbox:
                text "FAILED!" color "#ffffff" size 72 bold True xalign 0.5
                text "The runes fade..." color "#ff8888" size 48 xalign 0.5
                null height 20
                hbox:
                    textbutton "Try Again" action Jump("restart_word") xalign 0.5
                    textbutton "Give Up" action Return(False) xalign 0.5

    # ── PLAYING STATE ───────────────────────────────────
    if game_state == "playing":
        # Clue
        frame:
            xalign 0.95 yalign 0.05 background "#000000db" padding (25,15) xsize 600 at clue_float
            vbox:
                text "Clue:" color "#ffd700" size 44 bold True
                text "[book['clue']]" color "#ffffff" size 36
        
        if len(current_guess) == 0 and len(past_rows) == 0:
            frame: 
                xalign 0.35 yalign 0.35 background "#000000db" padding (25,15)
                text "Start typing your guess!" color "#ffffff" size 32
        

        if show_instructions:
            frame:
                xalign 0.5 yalign 0.5 background "#000000db" padding (25,15) 
                vbox xalign 0.5 yalign 0.5 spacing 25 xysize 850,350:
                    text "Use clues to guess which words will restore order to the library." color "#ffffff" size 32 
                    text "Each guess must be a five-letter word."
                    text "The color of a tile will change to show you how close your guess was." color "#ffffff" size 32 
                    text "If the tile turns green, the letter is in the word, and it is in the correct spot." color "#ffffff" size 32 
                    text "If the tile turns yellow, the letter is in the word, but it is not in the correct spot." color "#ffffff" size 32 
                    text "If the tile turns gray, the letter is not in the word." color "#ffffff" size 32 
                    textbutton "Hide Instructions" action SetVariable("show_instructions", False) text_color "#ffd700" text_hover_color "#ffffff" xalign 0.5

        # ── RUNE GRID (left) ────────────────────────
        vbox xpos 0.27 ypos 0.22 spacing 10:
            for row_idx in range(max_rows):
                hbox spacing 10:
                    for col_idx in range(5):
                        $ letter = None
                        if row_idx < len(past_rows) and col_idx < len(past_rows[row_idx]):
                            $ letter = past_rows[row_idx][col_idx]
                        elif row_idx == current_row and col_idx < len(current_guess):
                            $ letter = current_guess[col_idx]

                        add build_letter_slot(letter, target, row_idx, col_idx)

        # ── ENGLISH GRID (right) ─────────────────────
        vbox xpos 0.63 ypos 0.22 spacing 10:
            for row_idx in range(max_rows):
                hbox spacing 10:
                    for col_idx in range(5):
                        $ letter = None
                        if row_idx < len(past_rows) and col_idx < len(past_rows[row_idx]):
                            $ letter = past_rows[row_idx][col_idx]
                        elif row_idx == current_row and col_idx < len(current_guess):
                            $ letter = current_guess[col_idx]

                        add build_letter_english(letter, target, row_idx, col_idx)
        vbox xpos 0.27 ypos 0.85 spacing 10:
            if show_instructions == False:
                textbutton "Show Instructions" action SetVariable("show_instructions", True) text_color "#000" text_hover_size 36
            if len(current_guess) == 5:
                textbutton "Submit" action Function(submit_guess) text_color "#000" text_hover_size 36
            textbutton "Clear Row" action SetVariable("current_guess", []) text_color "#000" text_hover_size 36
            if corrupted_slots:
                textbutton "Purify" action Function(purify_slot) text_color "#000" text_hover_size 36

        text "Book [current_book + 1]/15" xalign 0.35 yalign 0.05 color "#ffd700" bold True

        # ── KEYBOARD INPUT ───────────────────────────────
        for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
            key ch action If(
                game_state == "playing" and len(current_guess) < 5,
                [SetVariable("current_guess", current_guess + [ch.upper()]),
                Play("sound", "audio/sfx/type.ogg")]
            )

        key "K_BACKSPACE" action If(
            game_state == "playing" and current_guess,
            SetVariable("current_guess", current_guess[:-1])
        )

        key "K_RETURN" action [
            If(
                game_state == "playing" and len(current_guess) == 5,
                Function(submit_guess)
            ),
            If(
                game_state == "victory",
                Function(next_book)
            )
        ]
        key "K_KP_ENTER" action [
            If(
                game_state == "playing" and len(current_guess) == 5,
                Function(submit_guess)
            ),
            If(
                game_state == "victory",
                Function(next_book)
            )
        ]

# ── LOGIC ─────────────────────────────────────────────
init python:
    def submit_guess():
        global current_row, past_rows, current_guess, corrupted_slots, current_book, game_state

        if len(current_guess) != 5:
            return

        book   = CODEX[current_book]
        target = book["target"]

        past_rows.append(current_guess[:])

        if current_guess == target:
            game_state = "victory"
            renpy.sound.play("audio/sfx/victory.ogg")
            renpy.restart_interaction()
            return

        current_guess = []
        current_row  += 1

        if current_row >= 6:
            game_state = "failure"
            corrupted_slots.add("fail")
            renpy.sound.play("audio/sfx/fail.ogg")
            renpy.restart_interaction()
            return

        renpy.sound.play("audio/sfx/feedback.ogg")
        renpy.restart_interaction()

    def purify_slot():
        global corrupted_slots, game_state
        if game_state == "playing":
            corrupted_slots.clear()
            renpy.restart_interaction()

    def next_book():
        global current_book, current_row, current_guess, past_rows, corrupted_slots, game_state
        current_book += 1
        current_row   = 0
        current_guess = []
        past_rows     = []
        corrupted_slots = set()
        game_state    = "playing"
        renpy.restart_interaction()

# ── RESTART LABEL ─────────────────────────────────────
label restart_word:
    $ current_row   = 0
    $ current_guess = []
    $ past_rows     = []
    $ corrupted_slots = set()
    $ game_state    = "playing"
    jump start_rune_wordle

# ── START LABEL ───────────────────────────────────────
label start_rune_wordle:
    $ current_book = library_shelves
    $ current_row   = 0
    $ current_guess = []
    $ past_rows     = []
    $ corrupted_slots = set()
    $ game_state    = "playing"
    scene bg_library 
    
    if current_book == 0:
        show k talking_facing_viewer:
            xalign 0.55 yalign 1.0 zoom 0.6
        k "Now the real fun begins."
        k "Since you've gotten the hang of the runes, we need to start unlocking actual words."
        show k pointing_from_behind
        k "Each of these floating books contains a mystic 5-letter word..."
        show k sad_looking_down_talking
        k "... or is supposed to, at least."
        show k talking_hands_clasped
        k "If we can get the words right, the books will begin to reorganize themselves."
        k "These are hard puzzles. Don't give up too easily."
        show k talking_facing_viewer
        k "Good luck!"
    call screen rune_wordle_builder with dissolve
    

    if _return:                     # victory → next book
        $ library_shelves += 1
        $ word = "".join(CODEX[current_book]["target"])
        scene bg_library 
        show k cheering:
                xalign 0.55 yalign 1.0 zoom 0.6
        with vpunch
        k "The rune ignites!"
        show k talking_facing_viewer
        k "The word is...{b}[word]{/b}"
        k "[k_responses[ library_shelves - 1 ]]"

        if library_shelves >= len(CODEX):
            jump library_conclusion
        else:
            jump start_rune_wordle

# ── FLOAT ANIMATION (optional) ───────────────────────
transform clue_float:
    alpha 1.0
    linear 1.8 yoffset -18 alpha 0.7
    linear 1.8 yoffset 0 alpha 1.0
    repeat

define k_responses = [
    "The runes are no match for you!",
    "You're unlocking the secrets of the library!",
    "Nice job! The ancient knowledge is within your grasp.",
    "You're mastering the art of decoding.",
    "The runes are revealing their mysteries to you!",
    "Your skills are sharpening with each word.",
    "The library's secrets are becoming clearer!",
    "This place will be organized in no time.",
    "Well done — that sigil hums with purpose now.",
    "I don't think I could have gotten that one.",
    "Another mystery eased from the page; that was sharp thinking.",
    "You are doing great! Keep going.",
    "I'm so glad Pipwick sent you two.",
    "Nicely done!",
    "I can feel the order being restored!",
    "The knowledge is flowing back into the realm!"
]