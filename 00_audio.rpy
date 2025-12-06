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
    MUSIC_BEDROOM = "audio/music/story/bedroom_soft_loop.ogg"
    MUSIC_BEDROOM_STORM = "audio/music/story/bedroom_storm.ogg"
    MUSIC_PROLOGUE = "audio/music/story/prologue_mysterious.ogg"

    # Main Theme
    MUSIC_MAIN_THEME = "audio/music/story/main_theme.ogg"
    MUSIC_HOME_RETURN = "audio/music/story/home_warm.ogg"

    # ===========================================
    # REGION MUSIC
    # ===========================================

    # Region 1 - Library (Ryan's domain)
    MUSIC_LIBRARY = "audio/music/regions/library_mystical.ogg"
    MUSIC_LIBRARY_PUZZLE = "audio/music/regions/library_puzzle.ogg"
    MUSIC_LIBRARY_DISCOVERY = "audio/music/regions/library_discovery.ogg"

    # Region 2 - Valley (Uncle Logan's domain)
    MUSIC_VALLEY = "audio/music/regions/valley_adventure.ogg"
    MUSIC_VALLEY_CLIMB = "audio/music/regions/valley_climb_action.ogg"
    MUSIC_VALLEY_PEACEFUL = "audio/music/regions/valley_peaceful.ogg"

    # Region 3 - Crystal Conservatory (Mom Lauren's domain)
    MUSIC_CONSERVATORY = "audio/music/regions/conservatory_magical.ogg"
    MUSIC_CONSERVATORY_CRYSTALS = "audio/music/regions/conservatory_crystals.ogg"
    MUSIC_CONSERVATORY_RHYTHM = "audio/music/regions/conservatory_rhythm_base.ogg"

    # Region 4 - Clocktower (Dad Jeff's domain)
    MUSIC_CLOCKTOWER = "audio/music/regions/clocktower_mechanical.ogg"
    MUSIC_CLOCKTOWER_TENSE = "audio/music/regions/clocktower_tense.ogg"
    MUSIC_CLOCKTOWER_TETRIS = "audio/music/regions/clocktower_tetris.ogg"  # Korobeiniki variant?

    # Region 5 - Skybridge (G-mom's domain)
    MUSIC_SKYBRIDGE = "audio/music/regions/skybridge_ethereal.ogg"
    MUSIC_SKYBRIDGE_EPIC = "audio/music/regions/skybridge_epic.ogg"
    MUSIC_BOSS_INTRO = "audio/music/regions/boss_intro.ogg"
    MUSIC_BOSS_BATTLE = "audio/music/regions/boss_battle_intense.ogg"
    MUSIC_BOSS_PHASE2 = "audio/music/regions/boss_battle_phase2.ogg"
    MUSIC_BOSS_PHASE3 = "audio/music/regions/boss_battle_finale.ogg"

    # ===========================================
    # MINIGAME MUSIC - Unique tracks for each minigame
    # ===========================================

    # Library Minigames
    MUSIC_MINIGAME_RUNE_DECODER = "audio/music/minigames/library_rune_decoder.ogg"  # Mysterious, puzzle-solving
    MUSIC_MINIGAME_WORD_PUZZLE = "audio/music/minigames/library_word_puzzle.ogg"    # Thoughtful, scholarly

    # Valley Minigames
    MUSIC_MINIGAME_VINE_BLASTER = "audio/music/minigames/valley_vine_blaster.ogg"   # Action, intense defense
    MUSIC_MINIGAME_VALLEY_CLIMB = "audio/music/minigames/valley_climb.ogg"          # Upbeat, adventurous climbing

    # Crystal Conservatory Minigames
    MUSIC_MINIGAME_CRYSTAL_MATCH = "audio/music/minigames/crystal_match3.ogg"       # Sparkling, puzzle casual
    MUSIC_MINIGAME_CRYSTAL_RHYTHM = "audio/music/minigames/crystal_rhythm.ogg"      # Melodic, rhythm-focused (this IS the rhythm game music)

    # Clocktower Minigames
    MUSIC_MINIGAME_CLOCKWORK_TETRIS = "audio/music/minigames/clocktower_tetris.ogg" # Mechanical, building tension
    MUSIC_MINIGAME_GEAR_RUSH = "audio/music/minigames/clocktower_gear_rush.ogg"     # Fast-paced, time pressure

    # Skybridge Minigames
    MUSIC_MINIGAME_BEACON_QUEST = "audio/music/minigames/skybridge_beacon_quest.ogg"  # Heroic, exploration
    MUSIC_MINIGAME_BOSS_INTRO = "audio/music/minigames/skybridge_boss_intro.ogg"      # Ominous, buildup
    MUSIC_MINIGAME_BOSS_PHASE1 = "audio/music/minigames/skybridge_boss_phase1.ogg"    # Battle, determined
    MUSIC_MINIGAME_BOSS_PHASE2 = "audio/music/minigames/skybridge_boss_phase2.ogg"    # Battle, intensifying
    MUSIC_MINIGAME_BOSS_PHASE3 = "audio/music/minigames/skybridge_boss_phase3.ogg"    # Battle, epic finale

    # ===========================================
    # EMOTIONAL/CUTSCENE MUSIC
    # ===========================================

    MUSIC_VICTORY = "audio/music/story/victory_triumphant.ogg"
    MUSIC_SAD = "audio/music/story/sad_moment.ogg"
    MUSIC_TENSION = "audio/music/story/tension_building.ogg"
    MUSIC_HEARTFELT = "audio/music/story/heartfelt_family.ogg"
    MUSIC_EPILOGUE = "audio/music/story/epilogue_peaceful.ogg"
    MUSIC_CREDITS = "audio/music/story/credits_roll.ogg"

####################################################################################################################
# AMBIENT SOUNDS - Environmental audio loops
####################################################################################################################

init python:
    # Bedroom/Home
    AMBIENT_RAIN = "audio/ambient/rain_on_window.ogg"
    AMBIENT_RAIN_HEAVY = "audio/ambient/rain_heavy_storm.ogg"
    AMBIENT_NIGHT_CRICKETS = "audio/ambient/night_crickets.ogg"
    AMBIENT_HOME_COZY = "audio/ambient/home_fireplace.ogg"

    # Library
    AMBIENT_LIBRARY = "audio/ambient/library_quiet.ogg"
    AMBIENT_MAGICAL_HUM = "audio/ambient/magical_hum.ogg"
    AMBIENT_PAGES_RUSTLING = "audio/ambient/pages_rustling.ogg"

    # Valley
    AMBIENT_FOREST = "audio/ambient/forest_birds.ogg"
    AMBIENT_WIND_TREES = "audio/ambient/wind_through_trees.ogg"
    AMBIENT_STREAM = "audio/ambient/gentle_stream.ogg"

    # Conservatory
    AMBIENT_CRYSTALS = "audio/ambient/crystal_resonance.ogg"
    AMBIENT_GREENHOUSE = "audio/ambient/greenhouse_peaceful.ogg"
    AMBIENT_CHIMES = "audio/ambient/wind_chimes.ogg"

    # Clocktower
    AMBIENT_CLOCKWORK = "audio/ambient/clockwork_ticking.ogg"
    AMBIENT_GEARS = "audio/ambient/gears_turning.ogg"
    AMBIENT_STEAM = "audio/ambient/steam_hiss.ogg"

    # Skybridge
    AMBIENT_WIND_HIGH = "audio/ambient/high_altitude_wind.ogg"
    AMBIENT_ETHEREAL = "audio/ambient/ethereal_whispers.ogg"
    AMBIENT_CLOUDS = "audio/ambient/cloud_atmosphere.ogg"

####################################################################################################################
# SOUND EFFECTS - UI and General
####################################################################################################################

init python:
    # ===========================================
    # UI SOUNDS
    # ===========================================

    SFX_UI_CLICK = "audio/sfx/ui/click.ogg"
    SFX_UI_HOVER = "audio/sfx/ui/hover.ogg"
    SFX_UI_CONFIRM = "audio/sfx/ui/confirm.ogg"
    SFX_UI_CANCEL = "audio/sfx/ui/cancel.ogg"
    SFX_UI_MENU_OPEN = "audio/sfx/ui/menu_open.ogg"
    SFX_UI_MENU_CLOSE = "audio/sfx/ui/menu_close.ogg"
    SFX_UI_ERROR = "audio/sfx/ui/error_buzz.ogg"
    SFX_UI_SUCCESS = "audio/sfx/ui/success_chime.ogg"
    SFX_UI_NOTIFICATION = "audio/sfx/ui/notification.ogg"

    # ===========================================
    # STORY/CUTSCENE SOUNDS
    # ===========================================

    # Weather
    SFX_THUNDER_DISTANT = "audio/sfx/weather/thunder_distant.ogg"
    SFX_THUNDER_CLOSE = "audio/sfx/weather/thunder_close.ogg"
    SFX_THUNDER_CRACK = "audio/sfx/weather/thunder_crack.ogg"
    SFX_RAIN_START = "audio/sfx/weather/rain_start.ogg"
    SFX_WIND_GUST = "audio/sfx/weather/wind_gust.ogg"

    # Magic/Portal
    SFX_PORTAL_OPEN = "audio/sfx/magic/portal_open.ogg"
    SFX_PORTAL_ENTER = "audio/sfx/magic/portal_enter.ogg"
    SFX_PORTAL_EXIT = "audio/sfx/magic/portal_exit.ogg"
    SFX_MAGIC_SHIMMER = "audio/sfx/magic/shimmer.ogg"
    SFX_MAGIC_WHOOSH = "audio/sfx/magic/whoosh.ogg"
    SFX_MAGIC_SPARKLE = "audio/sfx/magic/sparkle.ogg"
    SFX_MAGIC_CHARGE = "audio/sfx/magic/charge_up.ogg"
    SFX_MAGIC_RELEASE = "audio/sfx/magic/release.ogg"
    SFX_BEACON_ACTIVATE = "audio/sfx/magic/beacon_activate.ogg"
    SFX_BEACON_HUM = "audio/sfx/magic/beacon_hum.ogg"

    # Character
    SFX_FOOTSTEP_WOOD = "audio/sfx/character/footstep_wood.ogg"
    SFX_FOOTSTEP_STONE = "audio/sfx/character/footstep_stone.ogg"
    SFX_FOOTSTEP_GRASS = "audio/sfx/character/footstep_grass.ogg"
    SFX_GASP = "audio/sfx/character/gasp.ogg"
    SFX_LAUGH_CHILD = "audio/sfx/character/laugh_child.ogg"
    SFX_HUG = "audio/sfx/character/hug_fabric.ogg"

    # Environment
    SFX_DOOR_OPEN = "audio/sfx/environment/door_open.ogg"
    SFX_DOOR_CLOSE = "audio/sfx/environment/door_close.ogg"
    SFX_BOOK_OPEN = "audio/sfx/environment/book_open.ogg"
    SFX_BOOK_CLOSE = "audio/sfx/environment/book_close.ogg"
    SFX_PAGE_TURN = "audio/sfx/environment/page_turn.ogg"
    SFX_CHEST_OPEN = "audio/sfx/environment/chest_open.ogg"
    SFX_KEY_PICKUP = "audio/sfx/environment/key_pickup.ogg"
    SFX_ITEM_PICKUP = "audio/sfx/environment/item_pickup.ogg"
    SFX_ITEM_EQUIP = "audio/sfx/environment/item_equip.ogg"

####################################################################################################################
# SOUND EFFECTS - Minigame Specific
####################################################################################################################

init python:
    # ===========================================
    # CRYSTAL MATCH-3 (Conservatory)
    # ===========================================

    SFX_GEM_SELECT = "audio/sfx/minigames/match3/gem_select.ogg"
    SFX_GEM_SWAP = "audio/sfx/minigames/match3/gem_swap.ogg"
    SFX_GEM_SWAP_FAIL = "audio/sfx/minigames/match3/gem_swap_fail.ogg"
    SFX_GEM_MATCH_3 = "audio/sfx/minigames/match3/match_3.ogg"
    SFX_GEM_MATCH_4 = "audio/sfx/minigames/match3/match_4.ogg"
    SFX_GEM_MATCH_5 = "audio/sfx/minigames/match3/match_5.ogg"
    SFX_GEM_CASCADE = "audio/sfx/minigames/match3/cascade.ogg"
    SFX_GEM_FALL = "audio/sfx/minigames/match3/gems_falling.ogg"
    SFX_COMBO_1 = "audio/sfx/minigames/match3/combo_1.ogg"
    SFX_COMBO_2 = "audio/sfx/minigames/match3/combo_2.ogg"
    SFX_COMBO_3 = "audio/sfx/minigames/match3/combo_3.ogg"
    SFX_COMBO_MEGA = "audio/sfx/minigames/match3/combo_mega.ogg"

    # ===========================================
    # CRYSTAL RHYTHM (Conservatory)
    # ===========================================

    SFX_RHYTHM_PERFECT = "audio/sfx/minigames/rhythm/hit_perfect.ogg"
    SFX_RHYTHM_GOOD = "audio/sfx/minigames/rhythm/hit_good.ogg"
    SFX_RHYTHM_OK = "audio/sfx/minigames/rhythm/hit_ok.ogg"
    SFX_RHYTHM_MISS = "audio/sfx/minigames/rhythm/miss.ogg"
    SFX_RHYTHM_NOTE_SPAWN = "audio/sfx/minigames/rhythm/note_spawn.ogg"
    SFX_RHYTHM_HOLD_START = "audio/sfx/minigames/rhythm/hold_start.ogg"
    SFX_RHYTHM_HOLD_END = "audio/sfx/minigames/rhythm/hold_end.ogg"
    SFX_RHYTHM_STREAK_5 = "audio/sfx/minigames/rhythm/streak_5.ogg"
    SFX_RHYTHM_STREAK_10 = "audio/sfx/minigames/rhythm/streak_10.ogg"
    SFX_RHYTHM_STREAK_LOST = "audio/sfx/minigames/rhythm/streak_lost.ogg"

    # ===========================================
    # CLOCKWORK TETRIS (Clocktower)
    # ===========================================

    SFX_TETRIS_MOVE = "audio/sfx/minigames/tetris/piece_move.ogg"
    SFX_TETRIS_ROTATE = "audio/sfx/minigames/tetris/piece_rotate.ogg"
    SFX_TETRIS_DROP = "audio/sfx/minigames/tetris/piece_drop.ogg"
    SFX_TETRIS_HARD_DROP = "audio/sfx/minigames/tetris/hard_drop.ogg"
    SFX_TETRIS_LOCK = "audio/sfx/minigames/tetris/piece_lock.ogg"
    SFX_TETRIS_LINE_CLEAR = "audio/sfx/minigames/tetris/line_clear.ogg"
    SFX_TETRIS_LINE_CLEAR_2 = "audio/sfx/minigames/tetris/line_clear_double.ogg"
    SFX_TETRIS_LINE_CLEAR_3 = "audio/sfx/minigames/tetris/line_clear_triple.ogg"
    SFX_TETRIS_LINE_CLEAR_4 = "audio/sfx/minigames/tetris/line_clear_tetris.ogg"
    SFX_TETRIS_HOLD = "audio/sfx/minigames/tetris/hold_piece.ogg"
    SFX_TETRIS_LEVEL_UP = "audio/sfx/minigames/tetris/level_up.ogg"
    SFX_TETRIS_DANGER = "audio/sfx/minigames/tetris/danger_warning.ogg"

    # ===========================================
    # GEAR RUSH (Clocktower)
    # ===========================================

    SFX_GEAR_CLICK = "audio/sfx/minigames/gearrush/gear_click.ogg"
    SFX_GEAR_CORRECT = "audio/sfx/minigames/gearrush/gear_correct.ogg"
    SFX_GEAR_WRONG = "audio/sfx/minigames/gearrush/gear_wrong.ogg"
    SFX_GEAR_SPIN = "audio/sfx/minigames/gearrush/gear_spin.ogg"
    SFX_GEAR_CHAIN = "audio/sfx/minigames/gearrush/gear_chain.ogg"
    SFX_GEAR_WAVE_COMPLETE = "audio/sfx/minigames/gearrush/wave_complete.ogg"
    SFX_COUNTDOWN_TICK = "audio/sfx/minigames/gearrush/countdown_tick.ogg"
    SFX_COUNTDOWN_GO = "audio/sfx/minigames/gearrush/countdown_go.ogg"
    SFX_TIME_LOW = "audio/sfx/minigames/gearrush/time_low.ogg"
    SFX_TIME_BONUS = "audio/sfx/minigames/gearrush/time_bonus.ogg"

    # ===========================================
    # BEACON QUEST (Skybridge Adventure)
    # ===========================================

    SFX_PLAYER_WALK = "audio/sfx/minigames/adventure/player_walk.ogg"
    SFX_PLAYER_ATTACK = "audio/sfx/minigames/adventure/sword_swing.ogg"
    SFX_PLAYER_HIT = "audio/sfx/minigames/adventure/player_hurt.ogg"
    SFX_PLAYER_HEAL = "audio/sfx/minigames/adventure/heal.ogg"
    SFX_ENEMY_HIT = "audio/sfx/minigames/adventure/enemy_hit.ogg"
    SFX_ENEMY_DEATH = "audio/sfx/minigames/adventure/enemy_death.ogg"
    SFX_ENEMY_SPAWN = "audio/sfx/minigames/adventure/enemy_spawn.ogg"
    SFX_SHARD_COLLECT = "audio/sfx/minigames/adventure/shard_collect.ogg"
    SFX_SHARD_GLOW = "audio/sfx/minigames/adventure/shard_glow.ogg"
    SFX_BEACON_RESTORE = "audio/sfx/minigames/adventure/beacon_restore.ogg"

    # ===========================================
    # BOSS RUSH (Skybridge)
    # ===========================================

    SFX_BOSS_ROAR = "audio/sfx/minigames/bossrush/boss_roar.ogg"
    SFX_BOSS_ATTACK = "audio/sfx/minigames/bossrush/boss_attack.ogg"
    SFX_BOSS_HIT = "audio/sfx/minigames/bossrush/boss_hit.ogg"
    SFX_BOSS_PHASE_CHANGE = "audio/sfx/minigames/bossrush/phase_change.ogg"
    SFX_BOSS_DEATH = "audio/sfx/minigames/bossrush/boss_death.ogg"
    SFX_HERO_SHOOT = "audio/sfx/minigames/bossrush/hero_shoot.ogg"
    SFX_HERO_HIT = "audio/sfx/minigames/bossrush/hero_hit.ogg"
    SFX_PROJECTILE_FIRE = "audio/sfx/minigames/bossrush/projectile_fire.ogg"
    SFX_PROJECTILE_HIT = "audio/sfx/minigames/bossrush/projectile_hit.ogg"
    SFX_SPREAD_ATTACK = "audio/sfx/minigames/bossrush/spread_attack.ogg"
    SFX_RAIN_ATTACK = "audio/sfx/minigames/bossrush/rain_attack.ogg"
    SFX_SPIRAL_ATTACK = "audio/sfx/minigames/bossrush/spiral_attack.ogg"

    # ===========================================
    # VALLEY MINIGAMES (Vine Blaster / Valley Climb)
    # ===========================================

    SFX_FIREBALL_SHOOT = "audio/sfx/minigames/valley/fireball_shoot.ogg"
    SFX_FIREBALL_HIT = "audio/sfx/minigames/valley/fireball_hit.ogg"
    SFX_VINE_GROW = "audio/sfx/minigames/valley/vine_grow.ogg"
    SFX_VINE_DESTROY = "audio/sfx/minigames/valley/vine_destroy.ogg"
    SFX_SPIDER_CRAWL = "audio/sfx/minigames/valley/spider_crawl.ogg"
    SFX_SPIDER_DEATH = "audio/sfx/minigames/valley/spider_death.ogg"
    SFX_BEACON_DANGER = "audio/sfx/minigames/valley/beacon_danger.ogg"
    SFX_SECOND_WIND = "audio/sfx/minigames/valley/second_wind.ogg"
    SFX_WAVE_START = "audio/sfx/minigames/valley/wave_start.ogg"
    SFX_WAVE_COMPLETE = "audio/sfx/minigames/valley/wave_complete.ogg"

    # Valley Climb specific
    SFX_JUMP = "audio/sfx/minigames/valley/jump.ogg"
    SFX_LAND = "audio/sfx/minigames/valley/land.ogg"
    SFX_CLIMB = "audio/sfx/minigames/valley/climb.ogg"
    SFX_ACORN_COLLECT = "audio/sfx/minigames/valley/acorn_collect.ogg"
    SFX_BRANCH_GRAB = "audio/sfx/minigames/valley/branch_grab.ogg"
    SFX_FALL = "audio/sfx/minigames/valley/fall.ogg"

    # ===========================================
    # LIBRARY MINIGAMES (Rune Decode / Word Game)
    # ===========================================

    SFX_KEY_PRESS = "audio/sfx/minigames/library/key_press.ogg"
    SFX_KEY_CORRECT = "audio/sfx/minigames/library/key_correct.ogg"
    SFX_KEY_WRONG = "audio/sfx/minigames/library/key_wrong.ogg"
    SFX_LETTER_REVEAL = "audio/sfx/minigames/library/letter_reveal.ogg"
    SFX_WORD_COMPLETE = "audio/sfx/minigames/library/word_complete.ogg"
    SFX_PUZZLE_SOLVE = "audio/sfx/minigames/library/puzzle_solve.ogg"
    SFX_HINT_USE = "audio/sfx/minigames/library/hint_use.ogg"
    SFX_RUNE_GLOW = "audio/sfx/minigames/library/rune_glow.ogg"
    SFX_PAGE_FLIP = "audio/sfx/minigames/library/page_flip.ogg"
    SFX_QUILL_WRITE = "audio/sfx/minigames/library/quill_write.ogg"

####################################################################################################################
# MINIGAME VICTORY/DEFEAT SOUNDS
####################################################################################################################

init python:
    SFX_MINIGAME_START = "audio/sfx/minigames/common/game_start.ogg"
    SFX_MINIGAME_VICTORY = "audio/sfx/minigames/common/victory.ogg"
    SFX_MINIGAME_DEFEAT = "audio/sfx/minigames/common/defeat.ogg"
    SFX_MINIGAME_RETRY = "audio/sfx/minigames/common/retry.ogg"
    SFX_SCORE_TICK = "audio/sfx/minigames/common/score_tick.ogg"
    SFX_SCORE_BONUS = "audio/sfx/minigames/common/score_bonus.ogg"
    SFX_HIGH_SCORE = "audio/sfx/minigames/common/high_score.ogg"
    SFX_COUNTDOWN_3 = "audio/sfx/minigames/common/countdown_3.ogg"
    SFX_COUNTDOWN_2 = "audio/sfx/minigames/common/countdown_2.ogg"
    SFX_COUNTDOWN_1 = "audio/sfx/minigames/common/countdown_1.ogg"

####################################################################################################################
# PIPWICK (Companion Character) SOUNDS
####################################################################################################################

init python:
    SFX_PIPWICK_CHIRP = "audio/sfx/pipwick/chirp_happy.ogg"
    SFX_PIPWICK_CHIRP_SAD = "audio/sfx/pipwick/chirp_sad.ogg"
    SFX_PIPWICK_CHIRP_EXCITED = "audio/sfx/pipwick/chirp_excited.ogg"
    SFX_PIPWICK_CHIRP_WORRIED = "audio/sfx/pipwick/chirp_worried.ogg"
    SFX_PIPWICK_FLUTTER = "audio/sfx/pipwick/wing_flutter.ogg"
    SFX_PIPWICK_LAND = "audio/sfx/pipwick/land_perch.ogg"
    SFX_PIPWICK_ALERT = "audio/sfx/pipwick/alert.ogg"

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
define audio.thunder = "audio/sfx/weather/thunder_close.ogg"
define audio.thunder_distant = "audio/sfx/weather/thunder_distant.ogg"
define audio.wind_gust = "audio/sfx/weather/wind_gust.ogg"
define audio.whoosh = "audio/sfx/magic/whoosh.ogg"

# Magic
define audio.portal_open = "audio/sfx/magic/portal_open.ogg"
define audio.magic_sparkle = "audio/sfx/magic/sparkle.ogg"
define audio.beacon_activate = "audio/sfx/magic/beacon_activate.ogg"

# UI
define audio.click = "audio/sfx/ui/click.ogg"
define audio.confirm = "audio/sfx/ui/confirm.ogg"

# Match-3
define audio.gem_match = "audio/sfx/minigames/match3/match_3.ogg"
define audio.gem_swap = "audio/sfx/minigames/match3/gem_swap.ogg"

# Rhythm
define audio.hit_perfect = "audio/sfx/minigames/rhythm/hit_perfect.ogg"
define audio.hit_miss = "audio/sfx/minigames/rhythm/miss.ogg"

# Tetris
define audio.line_clear = "audio/sfx/minigames/tetris/line_clear.ogg"
define audio.piece_drop = "audio/sfx/minigames/tetris/piece_drop.ogg"

# Combat
define audio.sword_swing = "audio/sfx/minigames/adventure/sword_swing.ogg"
define audio.enemy_death = "audio/sfx/minigames/adventure/enemy_death.ogg"

# Pipwick
define audio.pipwick_chirp = "audio/sfx/pipwick/chirp_happy.ogg"
