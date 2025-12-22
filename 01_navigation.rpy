# =======================================================
# NAVIGATION HUB SYSTEM
# Allows players to choose which regions to visit (after Library tutorial)
# =======================================================

# --- Progress Tracking ---
default beacons_restored = 0
default library_complete = False
default valley_complete = False
default conservatory_complete = False
default clocktower_complete = False
default skybridge_unlocked = False

# Track which guardians have been met (for dialogue variations)
default met_uncle_ryan = False
default met_mom = False
default met_dad = False

# --- Helper Functions ---
init python:
    def get_beacon_count():
        """Returns the number of beacons restored so far."""
        count = 0
        if store.library_complete:
            count += 1
        if store.valley_complete:
            count += 1
        if store.conservatory_complete:
            count += 1
        if store.clocktower_complete:
            count += 1
        return count

    def check_skybridge_unlock():
        """Check if all 4 beacons are restored to unlock Skybridge."""
        return (store.library_complete and store.valley_complete and
                store.conservatory_complete and store.clocktower_complete)

    def get_beacon_text():
        """Returns appropriate text for beacon count."""
        count = get_beacon_count()
        if count == 0:
            return "no beacons"
        elif count == 1:
            return "one beacon"
        elif count == 2:
            return "two beacons"
        elif count == 3:
            return "three beacons"
        elif count == 4:
            return "four beacons"
        return str(count) + " beacons"

# --- Navigation Hub Label ---
label navigation_hub:
    # Update beacon count and check for skybridge unlock
    $ beacons_restored = get_beacon_count()
    $ skybridge_unlocked = check_skybridge_unlock()

    # Different hub scenes based on progress
    if skybridge_unlocked:
        jump navigation_hub_finale
    else:
        jump navigation_hub_choose

# --- Hub: Choose Next Region ---
label navigation_hub_choose:
    scene bg_hub_crossroads with fade

    # Show Pipwick at the crossroads
    show p happy_talking:
        zoom 0.4
        xalign 0.5
        yalign 0.6
    with dissolve

    if beacons_restored == 1:
        p "Wonderful work restoring the Library's beacon, Twin Sparks!"
        p "Now, three more beacons await your help. Where would you like to go next?"
    elif beacons_restored == 2:
        p "Two beacons now shine bright! The realm grows stronger!"
        p "Two more regions need your help. Which shall we visit?"
    elif beacons_restored == 3:
        p "Three beacons restored! Just one more to go!"
        p "Only one region remains darkened. Shall we head there now?"

    show p proud

    # Build menu dynamically based on what's available
    menu:
        "Where should we go next?"

        "The Ironwood Valley (Uncle Ryan)" if not valley_complete:
            p "To the Valley we go! Hold tight!"
            jump navigation_transition_valley

        "The Crystal Conservatory (Mom)" if not conservatory_complete:
            p "The Conservatory awaits! Let's restore its song!"
            jump navigation_transition_conservatory

        "The Celestial Clocktower (Dad)" if not clocktower_complete:
            p "Time to fix time itself! To the Clocktower!"
            jump navigation_transition_clocktower

# --- Hub: All Beacons Ready, Finale Time ---
label navigation_hub_finale:
    scene bg_hub_crossroads with fade

    show p happy_talking:
        zoom 0.4
        xalign 0.5
        yalign 0.6
    with dissolve

    p "Twin Sparks! You've done it!"

    show p proud
    p "All four regional beacons have been restored!"

    show p worried
    p "But our work isn't finished. Bedimurk still lurks at the Eternal Skybridge."
    p "He's making his final stand, trying to extinguish the last beacon."

    show p offended
    p "Are you ready for the final challenge?"

    menu:
        "Are you ready to face Bedimurk?"

        "We're ready! Let's finish this!":
            show p proud
            p "That's the spirit! To the Eternal Skybridge!"
            jump navigation_transition_skybridge

        "Let us prepare a moment...":
            show p happy_talking
            p "Of course! Take your time. The fate of the realm can wait a moment."
            p "When you're ready, just say the word!"
            jump navigation_hub_finale

# --- Transition Scenes ---
label navigation_transition_valley:
    hide p
    with dissolve

    "Pipwick's lantern glowed bright, and the world dissolved into light..."

    show light_burst at light_burst_grow_2:
        alpha 0.0
        ease 0.2 alpha 1.0

    scene image "#ffffff" with dissolve
    pause 0.5

    jump region_2_valley

label navigation_transition_conservatory:
    hide p
    with dissolve

    "Pipwick's lantern glowed bright, and the world dissolved into light..."

    show light_burst at light_burst_grow_2:
        alpha 0.0
        ease 0.2 alpha 1.0

    scene image "#ffffff" with dissolve
    pause 0.5

    jump region_3_conservatory

label navigation_transition_clocktower:
    hide p
    with dissolve

    "Pipwick's lantern glowed bright, and the world dissolved into light..."

    show light_burst at light_burst_grow_2:
        alpha 0.0
        ease 0.2 alpha 1.0

    scene image "#ffffff" with dissolve
    pause 0.5

    jump region_4_clocktower

label navigation_transition_skybridge:
    hide p
    with dissolve

    "Pipwick's lantern blazed with the combined light of four restored beacons..."
    "This was it. The final journey."

    show light_burst at light_burst_grow_2:
        alpha 0.0
        ease 0.2 alpha 1.0

    scene image "#ffffff" with dissolve
    pause 0.5

    jump region_5_skybridge
