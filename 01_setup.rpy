init python:
    import os
    import random
    import math
    config.auto_voice = "voice/{id}.mp3"

    # --------------------------------------------------------
    # Minigame Keyboard Utilities
    # --------------------------------------------------------
    # Stores original keymap bindings to restore after minigames
    _saved_keymap = {}

    def disable_minigame_conflicts():
        """
        Disable Ren'Py developer/system keys that conflict with minigame controls.
        Call this at the START of every minigame.
        """
        global _saved_keymap

        # Keys that commonly conflict with minigame input
        conflicting_keys = [
            'developer',      # Shift+D - developer menu
            'director',       # D - director mode (conflicts with movement!)
            'reload_game',    # Shift+R - reload (R might conflict)
            'inspector',      # Shift+I - inspector
            'console',        # Shift+O - console
            'self_voicing',   # V - self voicing
            'toggle_skip',    # Tab - skip toggle (conflicts with character switch!)
            'fast_skip',      # Ctrl, > - fast skip
            'screenshot',     # S - screenshot (conflicts with movement!)
            'rollback',       # Mouse scroll, pageup
            'rollforward',    # Mouse scroll, pagedown
            'hide_windows',   # H - hide windows
            'game_menu',      # Escape handled separately per minigame
        ]

        # Save current bindings and clear them
        for key in conflicting_keys:
            if key in config.keymap:
                _saved_keymap[key] = list(config.keymap[key])
                config.keymap[key] = []

        # Also disable some other problematic bindings
        if 'dismiss' in config.keymap:
            _saved_keymap['dismiss'] = list(config.keymap['dismiss'])
            # Keep only mouse click for dismiss, remove keyboard keys
            config.keymap['dismiss'] = ['mouseup_1']

    def restore_minigame_conflicts():
        """
        Restore Ren'Py developer/system keys after minigame ends.
        Call this at the END of every minigame.
        """
        global _saved_keymap

        for key, bindings in _saved_keymap.items():
            config.keymap[key] = bindings

        _saved_keymap = {}
# --------------------------------------------------------
# Setup File - Global settings and variables
# --------------------------------------------------------

define config.developer = True


define config.name = "Morning Light"
define config.version = "1.0"

# --------------------------------------------------------
# Character Positions - Global variables
# --------------------------------------------------------
init:
    transform p_bedroom:
        zoom 0.3
        xpos 0.45
        ypos 0.145
    
    transform light_burst_grow:
        rotate 0
        anchor (0.5, 0.5)

        xpos 0.66
        ypos 0.555

        linear 2.0 zoom 0.5 rotate -360 alpha 0.9
        #linear 2.0 zoom 0.5 rotate -720
        repeat


    transform light_burst_grow_2:
        rotate 0
        anchor (0.5, 0.5)

        xpos 0.49
        ypos 0.665

        linear 2.0 zoom 0.5 rotate -360 alpha 0.9
        #linear 2.0 zoom 0.5 rotate -720
        repeat



# --------------------------------------------------------
# Images - Global variables
# --------------------------------------------------------

# Backgrounds

image bg bedroom_night = "images/bg/bg_bedroom_night.png"
image bg library = "images/bg/bg_library.png"
image bg crystal_conservatory = "images/bg/bg_crystal_conservatory.png"
image bg skybridge = "images/bg/bg_skybridge.png"
image bg act_2_start = "images/bg/bg_act_2_start.png"


# --------------------------------------------------------
# Video Helper Function and Screen
# --------------------------------------------------------

image rainmoon = Movie(
        play="images/videos/rainmoon2.gif",
        channel="test",
        loop=True,
        size=(400, 300),
        pos=(900, 350)
    )

screen video_player(video_file, loop=True):
    add Movie(video_file)


# --------------------------------------------------------
# Layered ATL Images - Global variables
# --------------------------------------------------------

# Animated rain overlay using ATL (Animation and Transformation Language)
image rain:
    "images/assets/rain/overlay.png"
    zoom 0.2
    alpha 0.7
    xoffset -150
    yoffset 0
    0.1
    "images/assets/rain/overlay.png"
    zoom 0.2
    alpha 0.7
    xoffset 0
    yoffset 10
    0.1
    "images/assets/rain/overlay.png"
    zoom 0.2
    alpha 0.7
    xoffset 150
    yoffset 1
    0.1
    "images/assets/rain/overlay.png"
    zoom 0.2
    alpha 0.7
    xoffset -50
    yoffset -10
    0.1
    "images/assets/rain/overlay.png"
    zoom 0.2
    alpha 0.7
    xoffset 0
    yoffset 0
    0.1
    "images/assets/rain/overlay.png"
    zoom 0.2
    alpha 0.7
    xoffset 50
    yoffset -5
    0.1
    "images/assets/rain/overlay.png"
    zoom 0.2
    alpha 0.7
    xoffset -10
    yoffset 0
    0.1
    "images/assets/rain/overlay.png"
    zoom 0.2
    alpha 0.7
    xoffset 80
    yoffset 20
    0.1
    "images/assets/rain/overlay.png"
    zoom 0.2
    alpha 0.7
    xoffset 130
    yoffset -20
    0.1
    "images/assets/rain/overlay.png"
    zoom 0.2
    alpha 0.7
    xoffset -90
    yoffset 7
    0.1
    "images/assets/rain/overlay.png"
    zoom 0.2
    alpha 0.7
    xoffset 10
    yoffset 3
    0.1
    "images/assets/rain/overlay.png"
    zoom 0.2
    alpha 0.7
    xoffset 50
    yoffset 0
    0.1
    repeat

# ─── Images (no animation here) ─────────────────────
define book1 = "images/assets/books/book1.png"
define book2 = "images/assets/books/book2.png"
define book3 = "images/assets/books/book3.png"
define book4 = "images/assets/books/book4.png"
define book5 = "images/assets/books/book5.png"
define book6 = "images/assets/books/book6.png"
define book7 = "images/assets/books/book7.png"

# ─── Transforms (the actual floating animation) ─────
transform float_book1:
    zoom 0.021
    xalign 0.2 yalign 0.3
    ease 2.0 xoffset 25 rotate 10
    ease 2.0 xoffset 30 rotate -10
    repeat

transform float_book2:
    zoom 0.008
    xalign 0.4 yalign 0.35
    ease 1.5 yoffset 0 rotate 15
    ease 1.5 yoffset 40 rotate -15
    repeat

transform float_book3:
    zoom 0.007
    xalign 0.6 yalign 0.4
    ease 2.2 xoffset 0 rotate 8
    ease 2.2 xoffset 40 rotate -8
    repeat

transform float_book4:
    zoom 0.014
    xalign 0.3 yalign 0.05
    ease 1.8 yoffset 0 rotate 0
    ease 3.8 yoffset -130 rotate 90
    repeat

transform float_book5:
    zoom 0.029
    xalign 0.7 yalign 0.2
    ease 2.5 xoffset 0 rotate 20
    ease 2.5 xoffset 20 rotate -20
    repeat

transform float_book6:
    zoom 0.022
    xalign 0.5 yalign 0.3
    ease 2.6 yoffset -80 rotate 0
    ease 1.6 yoffset 50 rotate 100
    repeat

transform float_book7:
    zoom 0.019
    xalign 0.8 yalign 0.4
    ease 2.3 xoffset 0 rotate 12
    ease 2.3 xoffset 40 rotate -12
    repeat

transform float_book8:
    zoom 0.025
    xalign 0.1 yalign 0.5
    ease 2.0 yoffset -30 rotate 10
    ease 2.0 yoffset 30 rotate -10
    repeat

transform float_book9:
    zoom 0.017
    xalign 0.8 yalign 0.1
    ease 1.5 xoffset 0 rotate 15
    ease 1.5 xoffset 40 rotate -15
    repeat

transform float_book10:
    zoom 0.023
    xalign 0.95 yalign 0.3
    ease 2.2 yoffset 0 rotate 8
    ease 2.2 yoffset 40 rotate -8
    repeat

transform float_book11:
    zoom 0.016
    xalign 0.4 yalign 0.7
    ease 1.8 xoffset 0 
    ease 1.8 xoffset 30 
    repeat

transform float_book12:
    zoom 0.028
    xalign 0.1 yalign 0.8
    ease 2.5 yoffset 0 xoffset 0 rotate 20
    ease 2.5 yoffset 40 xoffset 75 rotate -20
    repeat

transform float_book13:
    zoom 0.013
    xalign 0.4 yalign 0.1
    ease 2.6 xoffset 0 rotate 0
    ease 2.6 xoffset 50 rotate 100
    repeat

transform float_book14:
    zoom 0.024
    xalign 0.1 yalign 0.1
    ease 2.3 yoffset 0 rotate 12
    ease 2.3 yoffset 40 rotate -12
    repeat

# ─── Screen ───────────────────────────────────────
screen floating_books_group():
    tag floating_books_group

    add book1 at float_book1
    add book2 at float_book2
    add book3 at float_book3
    add book4 at float_book4
    add book5 at float_book5
    add book6 at float_book6
    add book7 at float_book7
    add book7 at float_book8
    add book6 at float_book9
    add book5 at float_book10
    add book3 at float_book11
    add book4 at float_book12
    add book3 at float_book13
    add book2 at float_book14
    

