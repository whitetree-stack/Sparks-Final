# crystal_rhythm.rpy - Crystal Conservatory Rhythm Minigame
# A Guitar Hero / Dance Dance Revolution style rhythm game

####################################################################################################################
# CRYSTAL RHYTHM MINIGAME
####################################################################################################################

init python in crystal_rhythm:
    import pygame
    import random
    import math
    from pygame.locals import *

    # Game constants
    WIDTH, HEIGHT = 1920, 1080
    NUM_LANES = 4
    LANE_WIDTH = 120
    LANE_SPACING = 20
    TOTAL_LANES_WIDTH = NUM_LANES * LANE_WIDTH + (NUM_LANES - 1) * LANE_SPACING
    LANES_START_X = (WIDTH - TOTAL_LANES_WIDTH) // 2

    # Hit zone
    HIT_ZONE_Y = HEIGHT - 150
    HIT_ZONE_HEIGHT = 30
    PERFECT_RANGE = 25
    GOOD_RANGE = 50
    OK_RANGE = 80

    # Note settings
    NOTE_HEIGHT = 40
    NOTE_SPEED = 400  # pixels per second (adjustable for difficulty)

    # Lane colors and keys
    LANE_CONFIGS = [
        {"color": (220, 50, 100), "glow": (255, 100, 150), "key": K_d, "key_name": "D"},
        {"color": (50, 200, 100), "glow": (100, 255, 150), "key": K_f, "key_name": "F"},
        {"color": (50, 150, 255), "glow": (100, 200, 255), "key": K_j, "key_name": "J"},
        {"color": (255, 200, 50), "glow": (255, 230, 100), "key": K_k, "key_name": "K"},
    ]

    # Game states
    STATE_COUNTDOWN = "countdown"
    STATE_PLAYING = "playing"
    STATE_VICTORY = "victory"
    STATE_GAMEOVER = "gameover"

    # Song generator functions (must be defined before SONGS dict)
    def generate_easy_song():
        """Generate an easy song pattern."""
        notes = []
        beat_time = 600  # ms per beat
        time = 2000  # start after 2 seconds

        # Simple pattern - one note at a time, slower
        pattern = [0, 1, 2, 3, 3, 2, 1, 0, 0, 2, 1, 3, 2, 0, 3, 1]
        for i, lane in enumerate(pattern):
            notes.append((time + i * beat_time, lane))

        # Second section
        time = notes[-1][0] + beat_time * 2
        pattern2 = [0, 0, 1, 1, 2, 2, 3, 3, 2, 2, 1, 1, 0, 0]
        for i, lane in enumerate(pattern2):
            notes.append((time + i * beat_time, lane))

        # Final section
        time = notes[-1][0] + beat_time * 2
        pattern3 = [0, 1, 2, 3, 2, 1, 0, 1, 2, 3]
        for i, lane in enumerate(pattern3):
            notes.append((time + i * beat_time, lane))

        return notes

    def generate_medium_song():
        """Generate a medium difficulty song."""
        notes = []
        beat_time = 500
        time = 2000

        # More complex patterns with some doubles
        patterns = [
            # Section 1 - alternating
            [(0, 0), (1, 1), (2, 2), (3, 3), (4, 2), (5, 1), (6, 0), (7, 1)],
            # Section 2 - faster
            [(0, 0), (0.5, 2), (1, 1), (1.5, 3), (2, 0), (2.5, 2), (3, 3), (3.5, 1)],
            # Section 3 - doubles
            [(0, 0), (0, 3), (2, 1), (2, 2), (4, 0), (4, 3), (6, 1), (6, 2)],
            # Section 4 - run
            [(0, 0), (0.5, 1), (1, 2), (1.5, 3), (2, 3), (2.5, 2), (3, 1), (3.5, 0)],
        ]

        for section in patterns:
            for beat_offset, lane in section:
                notes.append((int(time + beat_offset * beat_time), lane))
            time = notes[-1][0] + beat_time * 3

        return notes

    def generate_hard_song():
        """Generate a hard difficulty song."""
        notes = []
        beat_time = 400
        time = 2000

        # Complex patterns
        patterns = [
            # Fast alternating
            [(i * 0.5, i % 4) for i in range(16)],
            # Doubles and triples
            [(0, 0), (0, 1), (1, 2), (1, 3), (2, 0), (2, 2), (3, 1), (3, 3)],
            # Streams
            [(i * 0.25, (i * 2) % 4) for i in range(20)],
            # Chord section
            [(0, 0), (0, 3), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (2, 3)],
        ]

        for section in patterns:
            for beat_offset, lane in section:
                notes.append((int(time + beat_offset * beat_time), lane))
            time = notes[-1][0] + beat_time * 4

        return notes

    # Pre-defined songs (patterns of notes)
    # Each note is (time_ms, lane) - time when note should be hit
    SONGS = {
        "easy": {
            "name": "Crystal Waltz",
            "bpm": 100,
            "speed": 350,
            "notes": generate_easy_song()
        },
        "medium": {
            "name": "Gem Symphony",
            "bpm": 120,
            "speed": 450,
            "notes": generate_medium_song()
        },
        "hard": {
            "name": "Diamond Storm",
            "bpm": 140,
            "speed": 550,
            "notes": generate_hard_song()
        }
    }

    class Note:
        """A falling note that the player must hit."""
        def __init__(self, hit_time, lane, speed):
            self.hit_time = hit_time
            self.lane = lane
            self.speed = speed

            # Calculate starting position (above screen)
            travel_time = (HIT_ZONE_Y - 0) / speed * 1000  # ms to reach hit zone
            self.spawn_time = hit_time - travel_time

            self.y = -NOTE_HEIGHT
            self.active = False
            self.hit = False
            self.missed = False
            self.hit_result = None  # "perfect", "good", "ok", "miss"
            self.alpha = 255

            # Visual properties
            self.glow_phase = random.random() * math.pi * 2

        def update(self, current_time, dt):
            if current_time < self.spawn_time:
                return

            self.active = True

            # Calculate y position based on time
            elapsed = current_time - self.spawn_time
            self.y = (elapsed / 1000) * self.speed

            # Update glow
            self.glow_phase += dt * 0.005

            # Check if missed (past hit zone)
            if not self.hit and self.y > HIT_ZONE_Y + OK_RANGE:
                self.missed = True
                self.hit_result = "miss"

            # Fade out after being hit or missed
            if self.hit or self.missed:
                self.alpha = max(0, self.alpha - 15)

        def get_lane_x(self):
            return LANES_START_X + self.lane * (LANE_WIDTH + LANE_SPACING)

        def draw(self, surf, time_ms):
            if not self.active or self.alpha <= 0:
                return

            config = LANE_CONFIGS[self.lane]
            color = config["color"]
            glow_color = config["glow"]

            x = self.get_lane_x()
            y = int(self.y)

            # Note surface with alpha
            note_surf = pygame.Surface((LANE_WIDTH, NOTE_HEIGHT), pygame.SRCALPHA)

            # Glow effect
            glow_alpha = int(60 + 30 * math.sin(self.glow_phase))
            glow_rect = pygame.Rect(-10, -10, LANE_WIDTH + 20, NOTE_HEIGHT + 20)
            glow_surf = pygame.Surface((LANE_WIDTH + 20, NOTE_HEIGHT + 20), pygame.SRCALPHA)
            pygame.draw.rect(glow_surf, (*glow_color, glow_alpha), glow_surf.get_rect(), border_radius=12)
            surf.blit(glow_surf, (x - 10, y - 10))

            # Main note body
            note_alpha = int(self.alpha)
            pygame.draw.rect(note_surf, (*color, note_alpha), note_surf.get_rect(), border_radius=10)

            # Highlight
            highlight_rect = pygame.Rect(5, 5, LANE_WIDTH - 10, NOTE_HEIGHT // 3)
            highlight_color = tuple(min(255, c + 50) for c in color)
            pygame.draw.rect(note_surf, (*highlight_color, note_alpha), highlight_rect, border_radius=5)

            surf.blit(note_surf, (x, y))

            # Hit result feedback
            if self.hit_result and self.hit_result != "miss":
                result_colors = {
                    "perfect": (255, 255, 100),
                    "good": (100, 255, 100),
                    "ok": (100, 200, 255)
                }
                result_color = result_colors.get(self.hit_result, (255, 255, 255))
                font = pygame.font.Font(None, 36)
                result_text = font.render(self.hit_result.upper(), True, result_color)
                text_alpha = int(self.alpha)
                result_text.set_alpha(text_alpha)
                surf.blit(result_text, (x + LANE_WIDTH // 2 - result_text.get_width() // 2, y - 30))

    class HitEffect:
        """Visual effect when a note is hit."""
        def __init__(self, lane, result):
            self.lane = lane
            self.result = result
            self.lifetime = 300
            self.max_lifetime = 300

            config = LANE_CONFIGS[lane]
            self.color = config["glow"]

        def update(self, dt):
            self.lifetime -= dt
            return self.lifetime > 0

        def draw(self, surf):
            if self.lifetime <= 0:
                return

            progress = 1 - (self.lifetime / self.max_lifetime)
            x = LANES_START_X + self.lane * (LANE_WIDTH + LANE_SPACING)
            y = HIT_ZONE_Y

            # Expanding ring
            radius = int(30 + progress * 50)
            alpha = int(200 * (1 - progress))

            effect_surf = pygame.Surface((radius * 2 + 20, radius * 2 + 20), pygame.SRCALPHA)
            pygame.draw.circle(effect_surf, (*self.color, alpha),
                             (radius + 10, radius + 10), radius, width=4)
            surf.blit(effect_surf, (x + LANE_WIDTH // 2 - radius - 10, y - radius - 10))

    class RhythmGame:
        """Main game controller for Crystal Rhythm."""
        def __init__(self, difficulty="easy"):
            self.difficulty = difficulty
            song_data = SONGS.get(difficulty, SONGS["easy"])

            self.song_name = song_data["name"]
            self.speed = song_data["speed"]

            # Create notes from song data
            self.notes = [Note(hit_time, lane, self.speed) for hit_time, lane in song_data["notes"]]

            # Game state
            self.state = STATE_COUNTDOWN
            self.countdown = 3
            self.countdown_timer = 0

            # Timing
            self.game_time = 0
            self.start_time = None

            # Score
            self.score = 0
            self.combo = 0
            self.max_combo = 0
            self.perfect_count = 0
            self.good_count = 0
            self.ok_count = 0
            self.miss_count = 0

            # Visual effects
            self.hit_effects = []
            self.lane_pressed = [False] * NUM_LANES

            # Calculate passing threshold
            self.total_notes = len(self.notes)
            self.pass_threshold = 0.6  # 60% accuracy to pass

        def update(self, dt):
            if self.state == STATE_COUNTDOWN:
                self.countdown_timer += dt
                if self.countdown_timer >= 1000:
                    self.countdown_timer = 0
                    self.countdown -= 1
                    if self.countdown <= 0:
                        self.state = STATE_PLAYING
                        self.game_time = 0
                return

            if self.state != STATE_PLAYING:
                return

            # Update game time
            self.game_time += dt

            # Update notes
            all_done = True
            for note in self.notes:
                note.update(self.game_time, dt)
                if note.active and not note.hit and not note.missed:
                    all_done = False
                elif not note.active:
                    all_done = False

                # Count misses
                if note.missed and note.hit_result == "miss" and not hasattr(note, 'counted'):
                    note.counted = True
                    self.miss_count += 1
                    self.combo = 0

            # Update effects
            self.hit_effects = [e for e in self.hit_effects if e.update(dt)]

            # Check if song is complete
            if all_done:
                self.check_end_game()

        def check_end_game(self):
            """Determine victory or game over."""
            total_hit = self.perfect_count + self.good_count + self.ok_count
            accuracy = total_hit / self.total_notes if self.total_notes > 0 else 0

            if accuracy >= self.pass_threshold:
                self.state = STATE_VICTORY
            else:
                self.state = STATE_GAMEOVER

        def handle_key_down(self, key):
            """Handle key press."""
            if self.state != STATE_PLAYING:
                return

            # Find which lane was pressed
            lane = None
            for i, config in enumerate(LANE_CONFIGS):
                if key == config["key"]:
                    lane = i
                    break

            if lane is None:
                return

            self.lane_pressed[lane] = True

            # Find the closest unhit note in this lane
            closest_note = None
            closest_distance = float('inf')

            for note in self.notes:
                if note.lane == lane and note.active and not note.hit and not note.missed:
                    distance = abs(note.y - HIT_ZONE_Y)
                    if distance < closest_distance:
                        closest_distance = distance
                        closest_note = note

            if closest_note and closest_distance <= OK_RANGE:
                # Hit the note!
                closest_note.hit = True

                # Determine accuracy
                if closest_distance <= PERFECT_RANGE:
                    closest_note.hit_result = "perfect"
                    self.perfect_count += 1
                    self.score += 100
                elif closest_distance <= GOOD_RANGE:
                    closest_note.hit_result = "good"
                    self.good_count += 1
                    self.score += 50
                else:
                    closest_note.hit_result = "ok"
                    self.ok_count += 1
                    self.score += 25

                # Combo
                self.combo += 1
                self.max_combo = max(self.max_combo, self.combo)
                self.score += self.combo * 5  # Combo bonus

                # Visual effect
                self.hit_effects.append(HitEffect(lane, closest_note.hit_result))

        def handle_key_up(self, key):
            """Handle key release."""
            for i, config in enumerate(LANE_CONFIGS):
                if key == config["key"]:
                    self.lane_pressed[i] = False
                    break

        def draw(self, surf):
            time_ms = pygame.time.get_ticks()

            # Draw lanes
            self.draw_lanes(surf, time_ms)

            # Draw notes
            for note in self.notes:
                note.draw(surf, time_ms)

            # Draw hit effects
            for effect in self.hit_effects:
                effect.draw(surf)

            # Draw UI
            self.draw_ui(surf)

            # Draw countdown
            if self.state == STATE_COUNTDOWN:
                self.draw_countdown(surf)

            # Draw end screen
            if self.state in (STATE_VICTORY, STATE_GAMEOVER):
                self.draw_end_screen(surf)

        def draw_lanes(self, surf, time_ms):
            """Draw the lane backgrounds and hit zone."""
            for i in range(NUM_LANES):
                config = LANE_CONFIGS[i]
                x = LANES_START_X + i * (LANE_WIDTH + LANE_SPACING)

                # Lane background
                lane_surf = pygame.Surface((LANE_WIDTH, HEIGHT), pygame.SRCALPHA)
                lane_color = (30, 20, 50, 150) if not self.lane_pressed[i] else (50, 40, 80, 200)
                pygame.draw.rect(lane_surf, lane_color, lane_surf.get_rect())
                surf.blit(lane_surf, (x, 0))

                # Lane borders
                pygame.draw.line(surf, (60, 40, 90), (x, 0), (x, HEIGHT), 2)
                pygame.draw.line(surf, (60, 40, 90), (x + LANE_WIDTH, 0), (x + LANE_WIDTH, HEIGHT), 2)

            # Hit zone
            hz_surf = pygame.Surface((TOTAL_LANES_WIDTH, HIT_ZONE_HEIGHT), pygame.SRCALPHA)
            pygame.draw.rect(hz_surf, (80, 60, 120, 180), hz_surf.get_rect(), border_radius=5)
            surf.blit(hz_surf, (LANES_START_X, HIT_ZONE_Y - HIT_ZONE_HEIGHT // 2))

            # Hit zone line
            pygame.draw.line(surf, (200, 150, 255),
                           (LANES_START_X, HIT_ZONE_Y),
                           (LANES_START_X + TOTAL_LANES_WIDTH, HIT_ZONE_Y), 3)

            # Key indicators
            for i in range(NUM_LANES):
                config = LANE_CONFIGS[i]
                x = LANES_START_X + i * (LANE_WIDTH + LANE_SPACING)

                # Key box
                key_y = HEIGHT - 80
                key_size = 60
                key_x = x + LANE_WIDTH // 2 - key_size // 2

                key_color = config["glow"] if self.lane_pressed[i] else config["color"]
                key_alpha = 255 if self.lane_pressed[i] else 180

                key_surf = pygame.Surface((key_size, key_size), pygame.SRCALPHA)
                pygame.draw.rect(key_surf, (*key_color, key_alpha), key_surf.get_rect(), border_radius=10)
                if self.lane_pressed[i]:
                    pygame.draw.rect(key_surf, (255, 255, 255, 100), key_surf.get_rect(), border_radius=10)
                surf.blit(key_surf, (key_x, key_y))

                # Key label
                font = pygame.font.Font(None, 48)
                key_text = font.render(config["key_name"], True, (255, 255, 255))
                surf.blit(key_text, (key_x + key_size // 2 - key_text.get_width() // 2,
                                    key_y + key_size // 2 - key_text.get_height() // 2))

        def draw_ui(self, surf):
            """Draw score and combo display."""
            font_large = pygame.font.Font(None, 64)
            font_medium = pygame.font.Font(None, 48)
            font_small = pygame.font.Font(None, 32)

            # Score (top left)
            score_text = font_large.render(f"{self.score}", True, (255, 255, 255))
            surf.blit(score_text, (50, 50))

            score_label = font_small.render("SCORE", True, (180, 160, 220))
            surf.blit(score_label, (50, 30))

            # Combo (top right)
            if self.combo > 0:
                combo_color = (255, 220, 100) if self.combo >= 10 else (200, 180, 255)
                combo_text = font_large.render(f"{self.combo}x", True, combo_color)
                surf.blit(combo_text, (WIDTH - 150, 50))

                combo_label = font_small.render("COMBO", True, (180, 160, 220))
                surf.blit(combo_label, (WIDTH - 150, 30))

            # Song name (top center)
            song_text = font_medium.render(self.song_name, True, (200, 180, 255))
            surf.blit(song_text, (WIDTH // 2 - song_text.get_width() // 2, 30))

            # Progress
            notes_done = sum(1 for n in self.notes if n.hit or n.missed)
            progress = notes_done / self.total_notes if self.total_notes > 0 else 0

            bar_width = 300
            bar_height = 10
            bar_x = WIDTH // 2 - bar_width // 2
            bar_y = 80

            pygame.draw.rect(surf, (40, 30, 60), (bar_x, bar_y, bar_width, bar_height), border_radius=5)
            fill_width = int(bar_width * progress)
            if fill_width > 0:
                pygame.draw.rect(surf, (150, 100, 200), (bar_x, bar_y, fill_width, bar_height), border_radius=5)

        def draw_countdown(self, surf):
            """Draw countdown before song starts."""
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 150))
            surf.blit(overlay, (0, 0))

            font = pygame.font.Font(None, 200)

            if self.countdown > 0:
                count_text = font.render(str(self.countdown), True, (255, 255, 255))
            else:
                count_text = font.render("GO!", True, (100, 255, 150))

            surf.blit(count_text, (WIDTH // 2 - count_text.get_width() // 2,
                                  HEIGHT // 2 - count_text.get_height() // 2))

        def draw_end_screen(self, surf):
            """Draw victory or game over screen."""
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 200))
            surf.blit(overlay, (0, 0))

            font_title = pygame.font.Font(None, 96)
            font_large = pygame.font.Font(None, 64)
            font_medium = pygame.font.Font(None, 48)

            # Title
            if self.state == STATE_VICTORY:
                title = font_title.render("SONG COMPLETE!", True, (100, 255, 150))
            else:
                title = font_title.render("TRY AGAIN", True, (255, 100, 100))

            surf.blit(title, (WIDTH // 2 - title.get_width() // 2, 150))

            # Stats
            y = 280
            spacing = 50

            # Score
            score_text = font_large.render(f"Score: {self.score}", True, (255, 255, 255))
            surf.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, y))
            y += spacing + 20

            # Max combo
            combo_text = font_medium.render(f"Max Combo: {self.max_combo}x", True, (255, 220, 100))
            surf.blit(combo_text, (WIDTH // 2 - combo_text.get_width() // 2, y))
            y += spacing

            # Accuracy breakdown
            perfect_text = font_medium.render(f"Perfect: {self.perfect_count}", True, (255, 255, 100))
            surf.blit(perfect_text, (WIDTH // 2 - perfect_text.get_width() // 2, y))
            y += spacing

            good_text = font_medium.render(f"Good: {self.good_count}", True, (100, 255, 100))
            surf.blit(good_text, (WIDTH // 2 - good_text.get_width() // 2, y))
            y += spacing

            ok_text = font_medium.render(f"OK: {self.ok_count}", True, (100, 200, 255))
            surf.blit(ok_text, (WIDTH // 2 - ok_text.get_width() // 2, y))
            y += spacing

            miss_text = font_medium.render(f"Miss: {self.miss_count}", True, (255, 100, 100))
            surf.blit(miss_text, (WIDTH // 2 - miss_text.get_width() // 2, y))
            y += spacing + 20

            # Accuracy percentage
            total_hit = self.perfect_count + self.good_count + self.ok_count
            accuracy = (total_hit / self.total_notes * 100) if self.total_notes > 0 else 0
            acc_color = (100, 255, 150) if accuracy >= 80 else (255, 220, 100) if accuracy >= 60 else (255, 100, 100)
            acc_text = font_large.render(f"Accuracy: {accuracy:.1f}%", True, acc_color)
            surf.blit(acc_text, (WIDTH // 2 - acc_text.get_width() // 2, y))

            # Continue prompt
            prompt = font_medium.render("Press ENTER to continue", True, (180, 160, 220))
            surf.blit(prompt, (WIDTH // 2 - prompt.get_width() // 2, HEIGHT - 100))


# Regenerate songs on init (they use random, so generate them properly)
init python in crystal_rhythm:
    # Regenerate songs with proper functions now defined
    SONGS["easy"]["notes"] = generate_easy_song()
    SONGS["medium"]["notes"] = generate_medium_song()
    SONGS["hard"]["notes"] = generate_hard_song()


# Ren'Py Displayable wrapper
init python:
    class CrystalRhythmDisplayable(renpy.Displayable):
        """Ren'Py displayable wrapper for Crystal Rhythm game."""

        def __init__(self, difficulty="easy", **kwargs):
            super(CrystalRhythmDisplayable, self).__init__(**kwargs)
            self.difficulty = difficulty
            self.game = None
            self.last_time = None

        def render(self, width, height, st, at):
            import pygame

            # Initialize game on first render
            if self.game is None:
                self.game = crystal_rhythm.RhythmGame(self.difficulty)
                self.last_time = pygame.time.get_ticks()

            # Calculate delta time
            current_time = pygame.time.get_ticks()
            dt = current_time - self.last_time
            self.last_time = current_time

            # Update game
            self.game.update(dt)

            # Create render surface
            render = renpy.Render(crystal_rhythm.WIDTH, crystal_rhythm.HEIGHT)
            canvas = render.canvas()

            # Clear with background color
            canvas.rect((25, 15, 45), (0, 0, crystal_rhythm.WIDTH, crystal_rhythm.HEIGHT))

            # Draw game
            self.game.draw(canvas.get_surface())

            # Request redraw
            renpy.redraw(self, 0)

            return render

        def event(self, ev, x, y, st):
            import pygame

            if self.game is None:
                return None

            # Handle key events
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    return "quit"
                if ev.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    if self.game.state == crystal_rhythm.STATE_VICTORY:
                        return "victory"
                    elif self.game.state == crystal_rhythm.STATE_GAMEOVER:
                        return "retry"
                else:
                    self.game.handle_key_down(ev.key)

            elif ev.type == pygame.KEYUP:
                self.game.handle_key_up(ev.key)

            return None

        def visit(self):
            return []


# Screen for the minigame
screen crystal_rhythm_screen(difficulty="easy"):
    default game_display = CrystalRhythmDisplayable(difficulty)

    add Solid("#190f2d")
    add game_display

    key "K_ESCAPE" action Return("quit")


# Entry label for the minigame
label crystal_rhythm_start(difficulty="easy"):
    $ quick_menu = False

    call screen crystal_rhythm_screen(difficulty)

    $ quick_menu = True
    $ result = _return

    if result == "victory":
        return True
    else:
        return False


# Test label
label test_crystal_rhythm:
    menu:
        "Select difficulty:"

        "Easy":
            $ rhythm_difficulty = "easy"
        "Medium":
            $ rhythm_difficulty = "medium"
        "Hard":
            $ rhythm_difficulty = "hard"

    "Starting Crystal Rhythm - [rhythm_difficulty] mode..."

    call crystal_rhythm_start(difficulty=rhythm_difficulty)

    if _return:
        "Great performance!"
    else:
        "Keep practicing!"

    return
