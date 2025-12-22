# 00_audio.rpy - Audio Configuration for Sparks of the Beacon
# This file defines all music tracks, sound effects, and ambient audio
# Simply replace the placeholder paths with your actual audio files

####################################################################################################################
# AUDIO CONFIGURATION
####################################################################################################################
# How to use:
# 1. Place your audio files in the audio/ folder (create subfolders as needed)
# 2. Update the paths below to point to your actual files
# 3. Supported formats: ogg, mp3, wav (ogg recommended for music, wav for short sfx)
####################################################################################################################

init -10 python:
    # Audio channel configuration
    # Ren'Py has 3 default channels: music, sound, voice
    # We'll add custom channels for ambient and UI sounds

    renpy.music.register_channel("ambient", mixer="sfx", loop=True)
    renpy.music.register_channel("ui", mixer="sfx", loop=False)
    renpy.music.register_channel("minigame_music", mixer="music", loop=True)
    renpy.music.register_channel("minigame_sfx", mixer="sfx", loop=False)

####################################################################################################################
# MUSIC TRACKS - Background music for each area
####################################################################################################################

init python:
    # ===========================================
    # STORY MUSIC
    # ===========================================

    # Act 1 - Bedroom/Home
    MUSIC_BEDROOM = "audio/music/story/bedroom_soft_loop.mp3"
    MUSIC_BEDROOM_STORM = "audio/music/story/bedroom_storm.wav"
    MUSIC_PROLOGUE = "audio/music/story/prologue_mysterious.mp3"

    # Main Theme / Title Screen
    MUSIC_MAIN_THEME = "audio/music/story/main_theme.mp3"
    MUSIC_TITLE_REVEAL = "audio/music/story/title_reveal.mp3"  # Epic stinger for title screen
    MUSIC_HOME_RETURN = "audio/music/story/home_warm.mp3"

    # ===========================================
    # REGION MUSIC
    # ===========================================

    # Region 1 - Library (Ryan's domain)
    MUSIC_LIBRARY = "audio/music/regions/library_mystical.mp3"
    MUSIC_LIBRARY_PUZZLE = "audio/music/regions/library_puzzle.mp3"
    MUSIC_LIBRARY_DISCOVERY = "audio/music/regions/library_discovery.mp3"

    # Region 2 - Valley (Uncle Logan's domain)
    MUSIC_VALLEY = "audio/music/regions/valley_adventure.mp3"
    MUSIC_VALLEY_CLIMB = "audio/music/regions/valley_climb_action.mp3"
    MUSIC_VALLEY_PEACEFUL = "audio/music/regions/valley_peaceful.mp3"

    # Region 3 - Crystal Conservatory (Mom Lauren's domain)
    MUSIC_CONSERVATORY = "audio/music/regions/conservatory_magical.mp3"
    MUSIC_CONSERVATORY_CRYSTALS = "audio/music/regions/conservatory_crystals.mp3"
    MUSIC_CONSERVATORY_RHYTHM = "audio/music/regions/conservatory_rhythm_base.mp3"

    # Region 4 - Clocktower (Dad Jeff's domain)
    MUSIC_CLOCKTOWER = "audio/music/regions/clocktower_mechanical.mp3"
    MUSIC_CLOCKTOWER_TENSE = "audio/music/regions/clocktower_tense.mp3"
    MUSIC_CLOCKTOWER_TETRIS = "audio/music/regions/clocktower_tetris.mp3"  # Korobeiniki variant?

    # Region 5 - Skybridge (G-mom's domain)
    MUSIC_SKYBRIDGE = "audio/music/regions/skybridge_ethereal.mp3"
    MUSIC_SKYBRIDGE_EPIC = "audio/music/regions/skybridge_epic.mp3"
    MUSIC_BOSS_INTRO = "audio/music/regions/boss_intro.mp3"
    MUSIC_BOSS_BATTLE = "audio/music/regions/boss_battle_intense.mp3"
    MUSIC_BOSS_PHASE2 = "audio/music/regions/boss_battle_phase2.mp3"
    MUSIC_BOSS_PHASE3 = "audio/music/regions/boss_battle_finale.mp3"

    # ===========================================
    # MINIGAME MUSIC - Unique tracks for each minigame
    # ===========================================

    # Library Minigames
    MUSIC_MINIGAME_RUNE_DECODER = "audio/music/minigames/library_rune_decoder.mp3"  # Mysterious, puzzle-solving
    MUSIC_MINIGAME_WORD_PUZZLE = "audio/music/minigames/library_word_puzzle.mp3"    # Thoughtful, scholarly

    # Valley Minigames
    MUSIC_MINIGAME_VINE_BLASTER = "audio/music/minigames/valley_vine_blaster.mp3"   # Action, intense defense
    MUSIC_MINIGAME_VALLEY_CLIMB = "audio/music/minigames/valley_climb.mp3"          # Upbeat, adventurous climbing

    # Crystal Conservatory Minigames
    MUSIC_MINIGAME_CRYSTAL_MATCH = "audio/music/minigames/crystal_match3.mp3"       # Sparkling, puzzle casual
    MUSIC_MINIGAME_CRYSTAL_RHYTHM = "audio/music/minigames/crystal_rhythm.mp3"      # Melodic, rhythm-focused (this IS the rhythm game music)

    # Clocktower Minigames
    MUSIC_MINIGAME_CLOCKWORK_TETRIS = "audio/music/minigames/clocktower_tetris.mp3" # Mechanical, building tension
    MUSIC_MINIGAME_GEAR_RUSH = "audio/music/minigames/clocktower_gear_rush.mp3"     # Fast-paced, time pressure

    # Skybridge Minigames
    MUSIC_MINIGAME_BEACON_QUEST = "audio/music/minigames/skybridge_beacon_quest.mp3"  # Heroic, exploration
    MUSIC_MINIGAME_BOSS_INTRO = "audio/music/minigames/skybridge_boss_intro.mp3"      # Ominous, buildup
    MUSIC_MINIGAME_BOSS_PHASE1 = "audio/music/minigames/skybridge_boss_phase1.mp3"    # Battle, determined
    MUSIC_MINIGAME_BOSS_PHASE2 = "audio/music/minigames/skybridge_boss_phase2.mp3"    # Battle, intensifying
    MUSIC_MINIGAME_BOSS_PHASE3 = "audio/music/minigames/skybridge_boss_phase3.mp3"    # Battle, epic finale

    # ===========================================
    # EMOTIONAL/CUTSCENE MUSIC
    # ===========================================

    MUSIC_VICTORY = "audio/music/story/victory_triumphant.mp3"
    MUSIC_SAD = "audio/music/story/sad_moment.mp3"
    MUSIC_TENSION = "audio/music/story/tension_building.mp3"
    MUSIC_HEARTFELT = "audio/music/story/heartfelt_family.mp3"
    MUSIC_EPILOGUE = "audio/music/story/epilogue_peaceful.mp3"
    MUSIC_CREDITS = "audio/music/story/credits_roll.mp3"

####################################################################################################################
# AMBIENT SOUNDS - Environmental audio loops
####################################################################################################################

init python:
    # Bedroom/Home
    AMBIENT_RAIN = "audio/ambient/rain_on_window.mp3"
    AMBIENT_RAIN_HEAVY = "audio/ambient/rain_heavy_storm.mp3"
    AMBIENT_NIGHT_CRICKETS = "audio/ambient/night_crickets.mp3"
    AMBIENT_HOME_COZY = "audio/ambient/home_fireplace.mp3"

    # Library
    AMBIENT_LIBRARY = "audio/ambient/library_quiet.mp3"
    AMBIENT_MAGICAL_HUM = "audio/ambient/magical_hum.mp3"
    AMBIENT_PAGES_RUSTLING = "audio/ambient/pages_rustling.mp3"

    # Valley
    AMBIENT_FOREST = "audio/ambient/forest_birds.mp3"
    AMBIENT_WIND_TREES = "audio/ambient/wind_through_trees.mp3"
    AMBIENT_STREAM = "audio/ambient/gentle_stream.mp3"

    # Conservatory
    AMBIENT_CRYSTALS = "audio/ambient/crystal_resonance.mp3"
    AMBIENT_GREENHOUSE = "audio/ambient/greenhouse_peaceful.mp3"
    AMBIENT_CHIMES = "audio/ambient/wind_chimes.mp3"

    # Clocktower
    AMBIENT_CLOCKWORK = "audio/ambient/clockwork_ticking.mp3"
    AMBIENT_GEARS = "audio/ambient/gears_turning.mp3"
    AMBIENT_STEAM = "audio/ambient/steam_hiss.mp3"

    # Skybridge
    AMBIENT_WIND_HIGH = "audio/ambient/high_altitude_wind.mp3"
    AMBIENT_ETHEREAL = "audio/ambient/ethereal_whispers.mp3"
    AMBIENT_CLOUDS = "audio/ambient/cloud_atmosphere.mp3"

####################################################################################################################
# SOUND EFFECTS - UI and General
####################################################################################################################

init python:
    # ===========================================
    # UI SOUNDS
    # ===========================================

    SFX_UI_CLICK = "audio/sfx/ui/click.mp3"
    SFX_UI_HOVER = "audio/sfx/ui/hover.mp3"
    SFX_UI_CONFIRM = "audio/sfx/ui/confirm.mp3"
    SFX_UI_CANCEL = "audio/sfx/ui/cancel.mp3"
    SFX_UI_MENU_OPEN = "audio/sfx/ui/menu_open.mp3"
    SFX_UI_MENU_CLOSE = "audio/sfx/ui/menu_close.mp3"
    SFX_UI_ERROR = "audio/sfx/ui/error_buzz.mp3"
    SFX_UI_SUCCESS = "audio/sfx/ui/success_chime.mp3"
    SFX_UI_NOTIFICATION = "audio/sfx/ui/notification.mp3"

    # ===========================================
    # STORY/CUTSCENE SOUNDS
    # ===========================================

    # Weather
    SFX_THUNDER_DISTANT = "audio/sfx/weather/thunder_distant.mp3"
    SFX_THUNDER_CLOSE = "audio/sfx/weather/thunder_close.mp3"
    SFX_THUNDER_CRACK = "audio/sfx/weather/thunder_crack.mp3"
    SFX_RAIN_START = "audio/sfx/weather/rain_start.mp3"
    SFX_WIND_GUST = "audio/sfx/weather/wind_gust.mp3"

    # Magic/Portal
    SFX_PORTAL_OPEN = "audio/sfx/magic/portal_open.mp3"
    SFX_PORTAL_ENTER = "audio/sfx/magic/portal_enter.mp3"
    SFX_PORTAL_EXIT = "audio/sfx/magic/portal_exit.mp3"
    SFX_MAGIC_SHIMMER = "audio/sfx/magic/shimmer.mp3"
    SFX_MAGIC_WHOOSH = "audio/sfx/magic/whoosh.mp3"
    SFX_MAGIC_SPARKLE = "audio/sfx/magic/sparkle.mp3"
    SFX_MAGIC_CHARGE = "audio/sfx/magic/charge_up.mp3"
    SFX_MAGIC_RELEASE = "audio/sfx/magic/release.mp3"
    SFX_BEACON_ACTIVATE = "audio/sfx/magic/beacon_activate.mp3"
    SFX_BEACON_HUM = "audio/sfx/magic/beacon_hum.mp3"

    # Character
    SFX_FOOTSTEP_WOOD = "audio/sfx/character/footstep_wood.mp3"
    SFX_FOOTSTEP_STONE = "audio/sfx/character/footstep_stone.mp3"
    SFX_FOOTSTEP_GRASS = "audio/sfx/character/footstep_grass.mp3"
    SFX_GASP = "audio/sfx/character/gasp.mp3"
    SFX_LAUGH_CHILD = "audio/sfx/character/laugh_child.mp3"
    SFX_HUG = "audio/sfx/character/hug_fabric.mp3"

    # Environment
    SFX_DOOR_OPEN = "audio/sfx/environment/door_open.mp3"
    SFX_DOOR_CLOSE = "audio/sfx/environment/door_close.mp3"
    SFX_BOOK_OPEN = "audio/sfx/environment/book_open.mp3"
    SFX_BOOK_CLOSE = "audio/sfx/environment/book_close.mp3"
    SFX_PAGE_TURN = "audio/sfx/environment/page_turn.mp3"
    SFX_CHEST_OPEN = "audio/sfx/environment/chest_open.mp3"
    SFX_KEY_PICKUP = "audio/sfx/environment/key_pickup.mp3"
    SFX_ITEM_PICKUP = "audio/sfx/environment/item_pickup.mp3"
    SFX_ITEM_EQUIP = "audio/sfx/environment/item_equip.mp3"

####################################################################################################################
# SOUND EFFECTS - Minigame Specific
####################################################################################################################

init python:
    # ===========================================
    # CRYSTAL MATCH-3 (Conservatory)
    # ===========================================

    SFX_GEM_SELECT = "audio/sfx/minigames/match3/gem_select.mp3"
    SFX_GEM_SWAP = "audio/sfx/minigames/match3/gem_swap.mp3"
    SFX_GEM_SWAP_FAIL = "audio/sfx/minigames/match3/gem_swap_fail.mp3"
    SFX_GEM_MATCH_3 = "audio/sfx/minigames/match3/match_3.mp3"
    SFX_GEM_MATCH_4 = "audio/sfx/minigames/match3/match_4.mp3"
    SFX_GEM_MATCH_5 = "audio/sfx/minigames/match3/match_5.mp3"
    SFX_GEM_CASCADE = "audio/sfx/minigames/match3/cascade.mp3"
    SFX_GEM_FALL = "audio/sfx/minigames/match3/gems_falling.mp3"
    SFX_COMBO_1 = "audio/sfx/minigames/match3/combo_1.mp3"
    SFX_COMBO_2 = "audio/sfx/minigames/match3/combo_2.mp3"
    SFX_COMBO_3 = "audio/sfx/minigames/match3/combo_3.mp3"
    SFX_COMBO_MEGA = "audio/sfx/minigames/match3/combo_mega.mp3"

    # ===========================================
    # CRYSTAL RHYTHM (Conservatory)
    # ===========================================

    SFX_RHYTHM_PERFECT = "audio/sfx/minigames/rhythm/hit_perfect.mp3"
    SFX_RHYTHM_GOOD = "audio/sfx/minigames/rhythm/hit_good.mp3"
    SFX_RHYTHM_OK = "audio/sfx/minigames/rhythm/hit_ok.mp3"
    SFX_RHYTHM_MISS = "audio/sfx/minigames/rhythm/miss.mp3"
    SFX_RHYTHM_NOTE_SPAWN = "audio/sfx/minigames/rhythm/note_spawn.mp3"
    SFX_RHYTHM_HOLD_START = "audio/sfx/minigames/rhythm/hold_start.mp3"
    SFX_RHYTHM_HOLD_END = "audio/sfx/minigames/rhythm/hold_end.mp3"
    SFX_RHYTHM_STREAK_5 = "audio/sfx/minigames/rhythm/streak_5.mp3"
    SFX_RHYTHM_STREAK_10 = "audio/sfx/minigames/rhythm/streak_10.mp3"
    SFX_RHYTHM_STREAK_LOST = "audio/sfx/minigames/rhythm/streak_lost.mp3"

    # ===========================================
    # CLOCKWORK TETRIS (Clocktower)
    # ===========================================

    SFX_TETRIS_MOVE = "audio/sfx/minigames/tetris/piece_move.mp3"
    SFX_TETRIS_ROTATE = "audio/sfx/minigames/tetris/piece_rotate.mp3"
    SFX_TETRIS_DROP = "audio/sfx/minigames/tetris/piece_drop.mp3"
    SFX_TETRIS_HARD_DROP = "audio/sfx/minigames/tetris/hard_drop.mp3"
    SFX_TETRIS_LOCK = "audio/sfx/minigames/tetris/piece_lock.mp3"
    SFX_TETRIS_LINE_CLEAR = "audio/sfx/minigames/tetris/line_clear.mp3"
    SFX_TETRIS_LINE_CLEAR_2 = "audio/sfx/minigames/tetris/line_clear_double.mp3"
    SFX_TETRIS_LINE_CLEAR_3 = "audio/sfx/minigames/tetris/line_clear_triple.mp3"
    SFX_TETRIS_LINE_CLEAR_4 = "audio/sfx/minigames/tetris/line_clear_tetris.mp3"
    SFX_TETRIS_HOLD = "audio/sfx/minigames/tetris/hold_piece.mp3"
    SFX_TETRIS_LEVEL_UP = "audio/sfx/minigames/tetris/level_up.mp3"
    SFX_TETRIS_DANGER = "audio/sfx/minigames/tetris/danger_warning.mp3"

    # ===========================================
    # GEAR RUSH (Clocktower)
    # ===========================================

    SFX_GEAR_CLICK = "audio/sfx/minigames/gearrush/gear_click.mp3"
    SFX_GEAR_CORRECT = "audio/sfx/minigames/gearrush/gear_correct.mp3"
    SFX_GEAR_WRONG = "audio/sfx/minigames/gearrush/gear_wrong.mp3"
    SFX_GEAR_SPIN = "audio/sfx/minigames/gearrush/gear_spin.mp3"
    SFX_GEAR_CHAIN = "audio/sfx/minigames/gearrush/gear_chain.mp3"
    SFX_GEAR_WAVE_COMPLETE = "audio/sfx/minigames/gearrush/wave_complete.mp3"
    SFX_COUNTDOWN_TICK = "audio/sfx/minigames/gearrush/countdown_tick.mp3"
    SFX_COUNTDOWN_GO = "audio/sfx/minigames/gearrush/countdown_go.mp3"
    SFX_TIME_LOW = "audio/sfx/minigames/gearrush/time_low.mp3"
    SFX_TIME_BONUS = "audio/sfx/minigames/gearrush/time_bonus.mp3"

    # ===========================================
    # BEACON QUEST (Skybridge Adventure)
    # ===========================================

    SFX_PLAYER_WALK = "audio/sfx/minigames/adventure/player_walk.mp3"
    SFX_PLAYER_ATTACK = "audio/sfx/minigames/adventure/sword_swing.mp3"
    SFX_PLAYER_HIT = "audio/sfx/minigames/adventure/player_hurt.mp3"
    SFX_PLAYER_HEAL = "audio/sfx/minigames/adventure/heal.mp3"
    SFX_ENEMY_HIT = "audio/sfx/minigames/adventure/enemy_hit.mp3"
    SFX_ENEMY_DEATH = "audio/sfx/minigames/adventure/enemy_death.mp3"
    SFX_ENEMY_SPAWN = "audio/sfx/minigames/adventure/enemy_spawn.mp3"
    SFX_SHARD_COLLECT = "audio/sfx/minigames/adventure/shard_collect.mp3"
    SFX_SHARD_GLOW = "audio/sfx/minigames/adventure/shard_glow.mp3"
    SFX_BEACON_RESTORE = "audio/sfx/minigames/adventure/beacon_restore.mp3"

    # ===========================================
    # BOSS RUSH (Skybridge)
    # ===========================================

    SFX_BOSS_ROAR = "audio/sfx/minigames/bossrush/boss_roar.mp3"
    SFX_BOSS_ATTACK = "audio/sfx/minigames/bossrush/boss_attack.mp3"
    SFX_BOSS_HIT = "audio/sfx/minigames/bossrush/boss_hit.mp3"
    SFX_BOSS_PHASE_CHANGE = "audio/sfx/minigames/bossrush/phase_change.mp3"
    SFX_BOSS_DEATH = "audio/sfx/minigames/bossrush/boss_death.mp3"
    SFX_HERO_SHOOT = "audio/sfx/minigames/bossrush/hero_shoot.mp3"
    SFX_HERO_HIT = "audio/sfx/minigames/bossrush/hero_hit.mp3"
    SFX_PROJECTILE_FIRE = "audio/sfx/minigames/bossrush/projectile_fire.mp3"
    SFX_PROJECTILE_HIT = "audio/sfx/minigames/bossrush/projectile_hit.mp3"
    SFX_SPREAD_ATTACK = "audio/sfx/minigames/bossrush/spread_attack.mp3"
    SFX_RAIN_ATTACK = "audio/sfx/minigames/bossrush/rain_attack.mp3"
    SFX_SPIRAL_ATTACK = "audio/sfx/minigames/bossrush/spiral_attack.mp3"

    # ===========================================
    # VALLEY MINIGAMES (Vine Blaster / Valley Climb)
    # ===========================================

    SFX_FIREBALL_SHOOT = "audio/sfx/minigames/valley/fireball_shoot.mp3"
    SFX_FIREBALL_HIT = "audio/sfx/minigames/valley/fireball_hit.mp3"
    SFX_VINE_GROW = "audio/sfx/minigames/valley/vine_grow.mp3"
    SFX_VINE_DESTROY = "audio/sfx/minigames/valley/vine_destroy.mp3"
    SFX_SPIDER_CRAWL = "audio/sfx/minigames/valley/spider_crawl.mp3"
    SFX_SPIDER_DEATH = "audio/sfx/minigames/valley/spider_death.mp3"
    SFX_BEACON_DANGER = "audio/sfx/minigames/valley/beacon_danger.mp3"
    SFX_SECOND_WIND = "audio/sfx/minigames/valley/second_wind.mp3"
    SFX_WAVE_START = "audio/sfx/minigames/valley/wave_start.mp3"
    SFX_WAVE_COMPLETE = "audio/sfx/minigames/valley/wave_complete.mp3"

    # Valley Climb specific
    SFX_JUMP = "audio/sfx/minigames/valley/jump.mp3"
    SFX_LAND = "audio/sfx/minigames/valley/land.mp3"
    SFX_CLIMB = "audio/sfx/minigames/valley/climb.mp3"
    SFX_ACORN_COLLECT = "audio/sfx/minigames/valley/acorn_collect.mp3"
    SFX_BRANCH_GRAB = "audio/sfx/minigames/valley/branch_grab.mp3"
    SFX_FALL = "audio/sfx/minigames/valley/fall.mp3"

    # ===========================================
    # LIBRARY MINIGAMES (Rune Decode / Word Game)
    # ===========================================

    SFX_KEY_PRESS = "audio/sfx/minigames/library/key_press.mp3"
    SFX_KEY_CORRECT = "audio/sfx/minigames/library/key_correct.mp3"
    SFX_KEY_WRONG = "audio/sfx/minigames/library/key_wrong.mp3"
    SFX_LETTER_REVEAL = "audio/sfx/minigames/library/letter_reveal.mp3"
    SFX_WORD_COMPLETE = "audio/sfx/minigames/library/word_complete.mp3"
    SFX_PUZZLE_SOLVE = "audio/sfx/minigames/library/puzzle_solve.mp3"
    SFX_HINT_USE = "audio/sfx/minigames/library/hint_use.mp3"
    SFX_RUNE_GLOW = "audio/sfx/minigames/library/rune_glow.mp3"
    SFX_PAGE_FLIP = "audio/sfx/minigames/library/page_flip.mp3"
    SFX_QUILL_WRITE = "audio/sfx/minigames/library/quill_write.mp3"

####################################################################################################################
# MINIGAME VICTORY/DEFEAT SOUNDS
####################################################################################################################

init python:
    SFX_MINIGAME_START = "audio/sfx/minigames/common/game_start.mp3"
    SFX_MINIGAME_VICTORY = "audio/sfx/minigames/common/victory.mp3"
    SFX_MINIGAME_DEFEAT = "audio/sfx/minigames/common/defeat.mp3"
    SFX_MINIGAME_RETRY = "audio/sfx/minigames/common/retry.mp3"
    SFX_SCORE_TICK = "audio/sfx/minigames/common/score_tick.mp3"
    SFX_SCORE_BONUS = "audio/sfx/minigames/common/score_bonus.mp3"
    SFX_HIGH_SCORE = "audio/sfx/minigames/common/high_score.mp3"
    SFX_COUNTDOWN_3 = "audio/sfx/minigames/common/countdown_3.mp3"
    SFX_COUNTDOWN_2 = "audio/sfx/minigames/common/countdown_2.mp3"
    SFX_COUNTDOWN_1 = "audio/sfx/minigames/common/countdown_1.mp3"

####################################################################################################################
# PIPWICK (Companion Character) SOUNDS
####################################################################################################################

init python:
    SFX_PIPWICK_CHIRP = "audio/sfx/pipwick/chirp_happy.mp3"
    SFX_PIPWICK_CHIRP_SAD = "audio/sfx/pipwick/chirp_sad.mp3"
    SFX_PIPWICK_CHIRP_EXCITED = "audio/sfx/pipwick/chirp_excited.mp3"
    SFX_PIPWICK_CHIRP_WORRIED = "audio/sfx/pipwick/chirp_worried.mp3"
    SFX_PIPWICK_FLUTTER = "audio/sfx/pipwick/wing_flutter.mp3"
    SFX_PIPWICK_LAND = "audio/sfx/pipwick/land_perch.mp3"
    SFX_PIPWICK_ALERT = "audio/sfx/pipwick/alert.mp3"

####################################################################################################################
# HELPER FUNCTIONS
####################################################################################################################

init python:
    def play_sfx(sound_path, volume=1.0, channel="sound"):
        """Play a sound effect with optional volume adjustment.

        Args:
            sound_path: Path to the sound file (use constants above)
            volume: Volume from 0.0 to 1.0 (default 1.0)
            channel: Channel to play on ("sound", "ui", "minigame_sfx")
        """
        if renpy.loadable(sound_path):
            renpy.sound.play(sound_path, channel=channel)
        # Silently ignore missing files during development

    def play_music_track(music_path, fadein=1.0, volume=1.0, channel="music"):
        """Play a music track with fade-in.

        Args:
            music_path: Path to the music file (use constants above)
            fadein: Fade-in duration in seconds
            volume: Volume from 0.0 to 1.0
            channel: Channel to play on ("music", "minigame_music")
        """
        if renpy.loadable(music_path):
            renpy.music.play(music_path, channel=channel, fadein=fadein)

    def play_ambient(ambient_path, fadein=2.0):
        """Play ambient background audio.

        Args:
            ambient_path: Path to the ambient audio file
            fadein: Fade-in duration in seconds
        """
        if renpy.loadable(ambient_path):
            renpy.music.play(ambient_path, channel="ambient", fadein=fadein)

    def stop_ambient(fadeout=2.0):
        """Stop ambient audio with fade-out."""
        renpy.music.stop(channel="ambient", fadeout=fadeout)

    def stop_music(fadeout=1.0, channel="music"):
        """Stop music with fade-out."""
        renpy.music.stop(channel=channel, fadeout=fadeout)

####################################################################################################################
# AUDIO DEFINITIONS (Ren'Py style - alternative to constants)
# These allow using: play sound gem_match_3
####################################################################################################################

# Story/Weather
define audio.thunder = "audio/sfx/weather/thunder_close.mp3"
define audio.thunder_distant = "audio/sfx/weather/thunder_distant.mp3"
define audio.wind_gust = "audio/sfx/weather/wind_gust.mp3"
define audio.whoosh = "audio/sfx/magic/whoosh.mp3"

# Magic
define audio.portal_open = "audio/sfx/magic/portal_open.mp3"
define audio.magic_sparkle = "audio/sfx/magic/sparkle.mp3"
define audio.beacon_activate = "audio/sfx/magic/beacon_activate.mp3"

# UI
define audio.click = "audio/sfx/ui/click.mp3"
define audio.confirm = "audio/sfx/ui/confirm.mp3"

# Match-3
define audio.gem_match = "audio/sfx/minigames/match3/match_3.mp3"
define audio.gem_swap = "audio/sfx/minigames/match3/gem_swap.mp3"

# Rhythm
define audio.hit_perfect = "audio/sfx/minigames/rhythm/hit_perfect.mp3"
define audio.hit_miss = "audio/sfx/minigames/rhythm/miss.mp3"

# Tetris
define audio.line_clear = "audio/sfx/minigames/tetris/line_clear.mp3"
define audio.piece_drop = "audio/sfx/minigames/tetris/piece_drop.mp3"

# Combat
define audio.sword_swing = "audio/sfx/minigames/adventure/sword_swing.mp3"
define audio.enemy_death = "audio/sfx/minigames/adventure/enemy_death.mp3"

# Pipwick
define audio.pipwick_chirp = "audio/sfx/pipwick/chirp_happy.mp3"
