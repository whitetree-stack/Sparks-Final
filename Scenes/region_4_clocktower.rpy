label clocktower_start:
    scene bg_clocktower
    with fade
    play music "clocktower_theme.ogg" fadein 2.0
    p "The old clocktower stands tall, its hands frozen in time."
    p "It's a reminder that some things are better left untouched."
    "Exploring the Clocktower"

    call tetris_start

    "After playing Tetris, Pipwick felt a surge of nostalgia."
    p "Ah, Tetris! That game never gets old. It's amazing how those falling blocks can still captivate me."
    p "I think I could play that for hours on end!"

    call clock_krich

    "Having completed the puzzle, Pipwick took a moment to reflect."
    p "That was quite the challenge! I love puzzles that make me think."

    jump region_5_skybridge_start