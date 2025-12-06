label crystal_conservatory_start:
    scene bg_crystal_conservatory
    with fade
    play music "conservatory_theme.ogg" fadein 2.0
    p "Ah, the Crystal Conservatory. A place of beauty and reflection."


    "Hunting Game"
    window hide
    $ my_game_config = GameConfig(target_nb=4, time_limit=15, life_max=5, round_nb=4, bullet_max=20)
    $ hunt = HuntingGame(my_game_config)
    $ hunt.run()
    scene black
    "Finish Hunting"
    
    "wow, that was awesome!"
    "but here come more!"

    call play_zombie_knight

    "After the intense game, Pipwick took a moment to catch his breath."
    p "Phew! That was quite the workout. I needed that."