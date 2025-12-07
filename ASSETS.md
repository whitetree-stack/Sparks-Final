# Sparks of the Beacon - Media Asset List

This document lists all image and audio assets needed for the game.

## Placeholder System

The game includes a **procedural placeholder system** (`00_placeholders.rpy`) that automatically generates visual stand-ins for any missing assets. This allows you to playtest the entire game without having all media files.

**How it works:**
- Missing backgrounds display as colored gradients with thematic decorations
- Missing character sprites display as colored silhouettes with name labels
- Missing effects display as animated procedural graphics
- Each placeholder is color-coded to match the intended character/region

**To playtest:** Simply run the game. Any missing images will automatically show placeholders.

---

## TITLE SCREEN

**Location:** `images/title/`

| Filename | Description |
|----------|-------------|
| `title_background.png` | Dark starfield/beacon realm vista (1920x1080) |
| `title_beacon.png` | Central glowing beacon element (transparent) |
| `title_text.png` | Main title "Sparks of the Beacon" text (transparent) |
| `title_subtitle.png` | Subtitle "A Twin Sparks Adventure" (transparent) |
| `title_rays.png` | Light rays emanating from beacon center (transparent, for rotation) |
| `title_sparks.png` | Floating spark particles overlay (transparent) |

**Audio:** `audio/music/story/title_reveal.ogg` - Epic stinger/swell for title reveal

**Animation Notes:**
- `title_rays` rotates slowly (20 second full rotation)
- `title_beacon` pulses with gentle zoom
- `title_sparks` float gently up and down
- Elements fade in sequentially for dramatic effect

---

## BACKGROUND IMAGES

**Location:** `images/bg/`

| Filename | Description |
|----------|-------------|
| `bg_bedroom_night.png` | Bedroom scene (prologue) |
| `bg_library_ext.png` | Library exterior entrance |
| `bg_library_int.png` | Library interior |
| `bg_library_int_new.png` | Library interior (main) |
| `bg_valley_ext.png` | Ironwood Valley exterior |
| `bg_valley_int.png` | Ironwood Valley interior/clearing |
| `bg_conservatory_ext.png` | Crystal Conservatory exterior |
| `bg_crystal_conservatory.png` | Crystal Conservatory interior |
| `bg_clocktower_ext.png` | Celestial Clocktower exterior |
| `bg_clocktower.png` | Celestial Clocktower interior |
| `bg_skybridge_ext.png` | Skybridge exterior approach |
| `bg_skybridge.png` | Skybridge interior/platform |
| `bg_hub_crossroads.png` | Navigation hub (central crossroads) |
| `bg_living_room.png` | Living room (epilogue) |
| `bg_act_2_start.png` | Act 2 transition |
| `bg_act_2_with_boys.png` | Act 2 with boys visible |
| `bg_act_2_closeup.png` | Act 2 closeup shot |

---

## CHARACTER SPRITES

### Tristan (Red Armor)

**Bedroom poses:** `images/characters/Tristan/rmbg/`
- `facing_side.png`
- `facing_side_talking.png`
- `laying_back.png`
- `laying_back_talking.png`
- `laying_back_laughing.png`
- `sitting_back.png`
- `sitting_back_talking.png`
- `on_knees.png`
- `on_knees_talking.png`

**Red armor poses:** `images/characters/Tristan/rmbg/red_armor/`
- `unsure_looking_left.png`
- `unsure_looking_left_talking.png`
- `surprised.png`
- `surprised_talking.png`
- `determined_looking_left.png`
- `determined_looking_left_talking.png`
- `looking_down_confused.png`
- `looking_down_confused_talking.png`
- `back.png`
- `pointing.png`
- `pointing_smile.png`
- `pointing_smile_talking.png`
- `pointing_confused.png`
- `pointing_confused_talking.png`
- `cheering.png`
- `cheering2.png`
- `cheering_mouth_open.png`
- `hands_on_hips_smile.png`
- `hands_on_hips_smile_talking.png`
- `hands_on_hips_expressionless.png`
- `hands_on_hips_expressionless_talking.png`
- `hands_on_hips_talking.png`
- `hands_on_head_frustrated.png`
- `hands_to_head_frustrated.png`
- `hand_raised_from_behind.png`

### Henry (Blue Armor)

**Bedroom poses:** `images/characters/Henry/rmbg/`
- `laying_side.png`
- `laying_side_talking.png`
- `laying_side_laughing.png`
- `crawling_reaching.png`
- `laying_reaching.png`
- `sitting_up_confused.png`
- `sitting_up_worried.png`
- `sitting_up_worried_talking.png`
- `sitting_up_scared.png`
- `sitting_up_surprised.png`

**Blue armor poses:** `images/characters/Henry/rmbg/blue_armor/`
- `looking_down.png`
- `looking_down_talking.png`
- `looking_down_confused.png`
- `looking_down_confused_talking.png`
- `unsure_looking_right.png`
- `unsure_looking_right_talking.png`
- `unsure_looking_left.png`
- `unsure_looking_left_talking.png`
- `thumbs_up_determined.png`
- `thumbs_up_determined_talking.png`
- `thumbs_up_smile.png`
- `thumbs_up_smile_talking.png`
- `back.png`
- `hand_raised_from_behind.png`
- `surprised_looking_down.png`
- `surprised_looking_up.png`
- `surprised_talking.png`
- `cheering.png`
- `cheering2.png`
- `cheering_mouth_open.png`
- `cheer_eyes_closed.png`
- `determined_looking_left.png`
- `determined_looking_left_talking.png`
- `hands_on_hips.png`
- `hands_on_hips_talking.png`
- `hands_on_hips_smile.png`
- `hands_on_hips_smile_talking.png`
- `hands_on_hips_expressionless_talking.png`
- `hands_to_head_frustrated.png`
- `pointing.png`
- `pointing_confused.png`
- `pointing_confused_talking.png`
- `pointing_smile.png`
- `pointing_smile_talking.png`
- `eyes_closed_talking_smile.png`
- `skeptical.png`
- `skeptical_talking.png`
- `smile_looking_right.png`
- `smile_looking_right_talking.png`

### Pipwick (Companion)

**General poses:** `images/characters/Pipwick/rmbg/general/`
- `_0000_rmbg_pipwick_nervous_laugh.png`
- `_0001_rmbg_pipwick_happy_talking.png`
- `_0003_rmbg_pipwick_worried.png`
- `_0004_rmbg_pipwick_sad.png`
- `_0005_rmbg_pipwick_proud.png`
- `_0006_rmbg_pipwick_offended.png`
- `_0007_rmbg_pipwick_expressionless.png`
- `_0008_rmbg_pipwick_excited.png`
- `facing_away.png`
- `frustrated.png`

**Night variants:** `images/characters/Pipwick/rmbg/night/`
- All of the above with `night_` prefix

### Aunt Kayla

**Location:** `images/characters/Kayla/rmbg/`
- `anchor.png`
- `annoyed.png`
- `annoyed_talking.png`
- `celebrating_wink.png`
- `cheering.png`
- `hands_on_hips.png`
- `hands_on_hips_talking.png`
- `pointing_from_behind.png`
- `presenting.png`
- `presenting_talking.png`
- `sad_looking_down.png`
- `sad_looking_down_talking.png`
- `shrug.png`
- `shrug_talking.png`
- `smiling_facing_viewer.png`
- `talking_facing_viewer.png`
- `talking_hands_clasped.png`
- `waving.png`

### Uncle Ryan

**Location:** `images/characters/Ryan/rmbg/`
- `anchor.png`
- `back.png`
- `surprised.png`
- `surprised_talking.png`
- `hands_on_hips.png`
- `hands_on_hips_talking.png`
- `skeptical.png`
- `skeptical_talking.png`
- `laughing.png`
- `frustrated.png`
- `frustrated_talking.png`
- `waving.png`

### Mom (Lauren)

**Location:** `images/characters/Lauren/rmbg/`
- `anchor.png`
- `back.png`
- `surprised.png`
- `surprised_talking.png`
- `hands_on_hips.png`
- `hands_on_hips_talking.png`
- `skeptical.png`
- `skeptical_talking.png`
- `presenting.png`
- `presenting_talking.png`
- `frustrated.png`
- `frustrated_talking.png`
- `cheering.png`
- `waving.png`

### Dad (Jeff)

**Location:** `images/characters/Jeff/rmbg/`
- `anchor.png`
- `back.png`
- `surprised.png`
- `surprised_talking.png`
- `hands_on_hips.png`
- `hands_on_hips_talking.png`
- `laughing.png`
- `frustrated.png`
- `frustrated_talking.png`
- `presenting.png`
- `presenting_talking.png`
- `waving.png`

### G-Mom (Gloria)

**Location:** `images/characters/GMom/rmbg/`
- `anchor.png`
- `back.png`
- `surprised.png`
- `hands_on_hips.png`
- `hands_on_hips_talking.png`
- `presenting.png`
- `presenting_talking.png`
- `shrug_talking.png`
- `frustrated.png`
- `frustrated_talking.png`
- `cheering.png`
- `waving.png`
- `wink.png`
- `worried.png`

### Bedimurk (Villain - Raccoon)

**Location:** `images/characters/Bedimurk/rmbg/`
- `neutral.png` - Default pose
- `angry.png` - Angry expression
- `shielding.png` - Shielding eyes from light
- `defeated.png` - After losing
- `sad.png` - Sad/sympathetic
- `surprised.png` - Surprised expression
- `happy.png` - Redeemed/happy
- `silhouette.png` - Shadow foreshadowing

---

## VISUAL EFFECTS & ASSETS

### Rain Overlay
**Location:** `images/assets/rain/`
- `overlay.png`

### Floating Books (Library)
**Location:** `images/assets/books/`
- `book1.png`
- `book2.png`
- `book3.png`
- `book4.png`
- `book5.png`
- `book6.png`
- `book7.png`

### Light Burst Effect
**Location:** `images/`
- `light_burst.png`

### Video Assets
**Location:** `images/videos/`
- `rainmoon2.gif`
- `tunnel_animation.webm`
- `tunnel_trans.webm`

---

## BOSS RUSH MINIGAME SPRITES

### Heroes
**Location:** `images/minigames/bossrush/heroes/`
- `tristan_idle.png`
- `tristan_move_left.png`
- `tristan_move_right.png`
- `tristan_shoot.png`
- `tristan_hit.png`
- `tristan_glow.png`
- `henry_idle.png`
- `henry_move_left.png`
- `henry_move_right.png`
- `henry_shoot.png`
- `henry_hit.png`
- `henry_glow.png`

### Hero Projectiles
**Location:** `images/minigames/bossrush/projectiles/`
- `orb_green.png`
- `orb_green_glow.png`
- `orb_green_trail.png`
- `orb_blue.png`
- `orb_blue_glow.png`
- `orb_blue_trail.png`

### Boss (Bedimurk)
**Location:** `images/minigames/bossrush/boss/`

**Phase 1:**
- `phase1_idle.png`
- `phase1_attack.png`
- `phase1_hit.png`
- `phase1_aura.png`

**Phase 2:**
- `phase2_idle.png`
- `phase2_attack.png`
- `phase2_hit.png`
- `phase2_aura.png`

**Phase 3:**
- `phase3_idle.png`
- `phase3_attack.png`
- `phase3_hit.png`
- `phase3_aura.png`

**Common:**
- `crown.png`
- `crown_glow.png`
- `eyes.png`
- `eyes_glow.png`
- `shadow.png`
- `death_anim_0.png`
- `death_anim_1.png`
- `death_anim_2.png`

### Boss Projectiles
**Location:** `images/minigames/bossrush/projectiles/`
- `orb_dark.png`
- `orb_dark_glow.png`
- `spike.png`
- `spike_glow.png`
- `shadow_bolt.png`
- `void_sphere.png`

### Attack Effects
**Location:** `images/minigames/bossrush/effects/`
- `spread_warning.png`
- `rain_warning.png`
- `spiral_charge.png`
- `targeted_lock.png`

### Hit Effects
**Location:** `images/minigames/bossrush/effects/`
- `spark_green.png`
- `spark_blue.png`
- `spark_purple.png`
- `spark_red.png`
- `explosion_small.png`
- `explosion_large.png`
- `hit_flash.png`

### Background
**Location:** `images/minigames/bossrush/background/`
- `sky_gradient.png`
- `floating_particle.png`
- `lightning_flash.png`
- `arena_floor.png`
- `arena_edge.png`

### UI Elements
**Location:** `images/minigames/bossrush/ui/`
- `heart_full.png`
- `heart_empty.png`
- `boss_health_bar_bg.png`
- `boss_health_bar_fill.png`
- `boss_health_bar_frame.png`
- `phase_indicator.png`
- `controls_panel.png`

### Overlays
**Location:** `images/minigames/bossrush/overlays/`
- `intro_title.png`
- `intro_subtitle.png`
- `victory_banner.png`
- `defeat_banner.png`
- `vignette.png`

---

## AUDIO - MUSIC

### Story Music
**Location:** `audio/music/story/`
| Filename | Description |
|----------|-------------|
| `bedroom_soft_loop.ogg` | Bedroom ambient |
| `bedroom_storm.ogg` | Bedroom during storm |
| `prologue_mysterious.ogg` | Prologue introduction |
| `main_theme.ogg` | Main game theme |
| `home_warm.ogg` | Home/cozy theme |
| `victory_triumphant.ogg` | Victory fanfare |
| `sad_moment.ogg` | Emotional moments |
| `tension_building.ogg` | Tension scenes |
| `heartfelt_family.ogg` | Family moments |
| `epilogue_peaceful.ogg` | Ending theme |
| `credits_roll.ogg` | Credits music |

### Region Music
**Location:** `audio/music/regions/`
| Filename | Region |
|----------|--------|
| `library_mystical.ogg` | Library main |
| `library_puzzle.ogg` | Library puzzles |
| `library_discovery.ogg` | Library discoveries |
| `valley_adventure.ogg` | Valley main |
| `valley_climb_action.ogg` | Valley climbing |
| `valley_peaceful.ogg` | Valley calm |
| `conservatory_magical.ogg` | Conservatory main |
| `conservatory_crystals.ogg` | Crystal sections |
| `conservatory_rhythm_base.ogg` | Rhythm base |
| `clocktower_mechanical.ogg` | Clocktower main |
| `clocktower_tense.ogg` | Clocktower tense |
| `clocktower_tetris.ogg` | Tetris minigame |
| `skybridge_ethereal.ogg` | Skybridge main |
| `skybridge_epic.ogg` | Skybridge epic |
| `boss_intro.ogg` | Boss introduction |
| `boss_battle_intense.ogg` | Boss phase 1 |
| `boss_battle_phase2.ogg` | Boss phase 2 |
| `boss_battle_finale.ogg` | Boss phase 3 |

### Minigame Music
**Location:** `audio/music/minigames/`
| Filename | Minigame |
|----------|----------|
| `library_rune_decoder.ogg` | Rune decoder puzzle |
| `library_word_puzzle.ogg` | Word puzzle |
| `valley_vine_blaster.ogg` | Vine defense |
| `valley_climb.ogg` | Valley climbing |
| `crystal_match3.ogg` | Match-3 |
| `crystal_rhythm.ogg` | Rhythm game |
| `clocktower_tetris.ogg` | Tetris |
| `clocktower_gear_rush.ogg` | Gear rush |
| `skybridge_beacon_quest.ogg` | Beacon quest |
| `skybridge_boss_intro.ogg` | Boss intro |
| `skybridge_boss_phase1.ogg` | Boss phase 1 |
| `skybridge_boss_phase2.ogg` | Boss phase 2 |
| `skybridge_boss_phase3.ogg` | Boss finale |

---

## AUDIO - AMBIENT

**Location:** `audio/ambient/`
| Filename | Environment |
|----------|-------------|
| `rain_on_window.ogg` | Rain (light) |
| `rain_heavy_storm.ogg` | Rain (heavy) |
| `night_crickets.ogg` | Night sounds |
| `home_fireplace.ogg` | Home cozy |
| `library_quiet.ogg` | Library |
| `magical_hum.ogg` | Magic ambient |
| `pages_rustling.ogg` | Book pages |
| `forest_birds.ogg` | Forest |
| `wind_through_trees.ogg` | Wind |
| `gentle_stream.ogg` | Water |
| `crystal_resonance.ogg` | Crystals |
| `greenhouse_peaceful.ogg` | Greenhouse |
| `wind_chimes.ogg` | Chimes |
| `clockwork_ticking.ogg` | Clock ticking |
| `gears_turning.ogg` | Mechanical |
| `steam_hiss.ogg` | Steam |
| `high_altitude_wind.ogg` | High wind |
| `ethereal_whispers.ogg` | Mystical |
| `cloud_atmosphere.ogg` | Clouds |

---

## AUDIO - SOUND EFFECTS

### UI Sounds
**Location:** `audio/sfx/ui/`
- `click.ogg`
- `hover.ogg`
- `confirm.ogg`
- `cancel.ogg`
- `menu_open.ogg`
- `menu_close.ogg`
- `error_buzz.ogg`
- `success_chime.ogg`
- `notification.ogg`

### Weather SFX
**Location:** `audio/sfx/weather/`
- `thunder_distant.ogg`
- `thunder_close.ogg`
- `thunder_crack.ogg`
- `rain_start.ogg`
- `wind_gust.ogg`

### Magic SFX
**Location:** `audio/sfx/magic/`
- `portal_open.ogg`
- `portal_enter.ogg`
- `portal_exit.ogg`
- `shimmer.ogg`
- `whoosh.ogg`
- `sparkle.ogg`
- `charge_up.ogg`
- `release.ogg`
- `beacon_activate.ogg`
- `beacon_hum.ogg`

### Character SFX
**Location:** `audio/sfx/character/`
- `footstep_wood.ogg`
- `footstep_stone.ogg`
- `footstep_grass.ogg`
- `gasp.ogg`
- `laugh_child.ogg`
- `hug_fabric.ogg`

### Environment SFX
**Location:** `audio/sfx/environment/`
- `door_open.ogg`
- `door_close.ogg`
- `book_open.ogg`
- `book_close.ogg`
- `page_turn.ogg`
- `chest_open.ogg`
- `key_pickup.ogg`
- `item_pickup.ogg`
- `item_equip.ogg`

### Pipwick SFX
**Location:** `audio/sfx/pipwick/`
- `chirp_happy.ogg`
- `chirp_sad.ogg`
- `chirp_excited.ogg`
- `chirp_worried.ogg`
- `wing_flutter.ogg`
- `land_perch.ogg`
- `alert.ogg`

### Minigame Common SFX
**Location:** `audio/sfx/minigames/common/`
- `game_start.ogg`
- `victory.ogg`
- `defeat.ogg`
- `retry.ogg`
- `score_tick.ogg`
- `score_bonus.ogg`
- `high_score.ogg`
- `countdown_3.ogg`
- `countdown_2.ogg`
- `countdown_1.ogg`

### Match-3 SFX
**Location:** `audio/sfx/minigames/match3/`
- `gem_select.ogg`
- `gem_swap.ogg`
- `gem_swap_fail.ogg`
- `match_3.ogg`
- `match_4.ogg`
- `match_5.ogg`
- `cascade.ogg`
- `gems_falling.ogg`
- `combo_1.ogg`
- `combo_2.ogg`
- `combo_3.ogg`
- `combo_mega.ogg`

### Rhythm SFX
**Location:** `audio/sfx/minigames/rhythm/`
- `hit_perfect.ogg`
- `hit_good.ogg`
- `hit_ok.ogg`
- `miss.ogg`
- `note_spawn.ogg`
- `hold_start.ogg`
- `hold_end.ogg`
- `streak_5.ogg`
- `streak_10.ogg`
- `streak_lost.ogg`

### Tetris SFX
**Location:** `audio/sfx/minigames/tetris/`
- `piece_move.ogg`
- `piece_rotate.ogg`
- `piece_drop.ogg`
- `hard_drop.ogg`
- `piece_lock.ogg`
- `line_clear.ogg`
- `line_clear_double.ogg`
- `line_clear_triple.ogg`
- `line_clear_tetris.ogg`
- `hold_piece.ogg`
- `level_up.ogg`
- `danger_warning.ogg`

### Gear Rush SFX
**Location:** `audio/sfx/minigames/gearrush/`
- `gear_click.ogg`
- `gear_correct.ogg`
- `gear_wrong.ogg`
- `gear_spin.ogg`
- `gear_chain.ogg`
- `wave_complete.ogg`
- `countdown_tick.ogg`
- `countdown_go.ogg`
- `time_low.ogg`
- `time_bonus.ogg`

### Adventure SFX
**Location:** `audio/sfx/minigames/adventure/`
- `player_walk.ogg`
- `sword_swing.ogg`
- `player_hurt.ogg`
- `heal.ogg`
- `enemy_hit.ogg`
- `enemy_death.ogg`
- `enemy_spawn.ogg`
- `shard_collect.ogg`
- `shard_glow.ogg`
- `beacon_restore.ogg`

### Boss Rush SFX
**Location:** `audio/sfx/minigames/bossrush/`
- `boss_roar.ogg`
- `boss_attack.ogg`
- `boss_hit.ogg`
- `phase_change.ogg`
- `boss_death.ogg`
- `hero_shoot.ogg`
- `hero_hit.ogg`
- `projectile_fire.ogg`
- `projectile_hit.ogg`
- `spread_attack.ogg`
- `rain_attack.ogg`
- `spiral_attack.ogg`

### Valley SFX
**Location:** `audio/sfx/minigames/valley/`
- `fireball_shoot.ogg`
- `fireball_hit.ogg`
- `vine_grow.ogg`
- `vine_destroy.ogg`
- `spider_crawl.ogg`
- `spider_death.ogg`
- `beacon_danger.ogg`
- `second_wind.ogg`
- `wave_start.ogg`
- `wave_complete.ogg`
- `jump.ogg`
- `land.ogg`
- `climb.ogg`
- `acorn_collect.ogg`
- `branch_grab.ogg`
- `fall.ogg`

### Library SFX
**Location:** `audio/sfx/minigames/library/`
- `key_press.ogg`
- `key_correct.ogg`
- `key_wrong.ogg`
- `letter_reveal.ogg`
- `word_complete.ogg`
- `puzzle_solve.ogg`
- `hint_use.ogg`
- `rune_glow.ogg`
- `page_flip.ogg`
- `quill_write.ogg`

---

## ASSET COUNTS

| Category | Count |
|----------|-------|
| Background images | 17 |
| Character sprites (Tristan) | 34 |
| Character sprites (Henry) | 48 |
| Character sprites (Pipwick) | 21 |
| Character sprites (Kayla) | 18 |
| Character sprites (Ryan) | 12 |
| Character sprites (Lauren) | 14 |
| Character sprites (Jeff) | 12 |
| Character sprites (G-Mom) | 14 |
| Character sprites (Bedimurk) | 8 |
| Boss Rush sprites | ~60 |
| Visual effects/assets | 13 |
| Music tracks | 42 |
| Ambient sounds | 19 |
| Sound effects | ~130 |
| **Total** | **~460** |
