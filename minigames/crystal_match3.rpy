# crystal_match3.rpy - Crystal Conservatory Match-3 Minigame
# A Candy Crush style gem-matching game themed around crystals

####################################################################################################################
# CRYSTAL MATCH-3 MINIGAME
####################################################################################################################

init python in crystal_match:
    import pygame
    import random
    import math
    from pygame.locals import *

    # ==================================================================================
    # SPRITE CONFIGURATION - Replace these paths with actual sprite images
    # ==================================================================================

    # Set to True when you have real sprites to use instead of procedural graphics
    USE_SPRITES = False

    # Gem/Crystal sprites - one for each crystal type
    # Recommended size: 80x80 pixels with transparency
    GEM_SPRITES = {
        "ruby": "images/minigames/match3/gems/ruby.png",
        "sapphire": "images/minigames/match3/gems/sapphire.png",
        "emerald": "images/minigames/match3/gems/emerald.png",
        "topaz": "images/minigames/match3/gems/topaz.png",
        "amethyst": "images/minigames/match3/gems/amethyst.png",
        "diamond": "images/minigames/match3/gems/diamond.png",
    }

    # Selected/highlighted gem overlay
    GEM_SELECTED_SPRITE = "images/minigames/match3/gems/selected_overlay.png"

    # Match effect sprites (optional animated sequence)
    MATCH_EFFECT_SPRITES = [
        "images/minigames/match3/effects/match_01.png",
        "images/minigames/match3/effects/match_02.png",
        "images/minigames/match3/effects/match_03.png",
        "images/minigames/match3/effects/match_04.png",
    ]

    # Particle sprites for match explosions
    PARTICLE_SPRITES = {
        "ruby": "images/minigames/match3/particles/ruby_particle.png",
        "sapphire": "images/minigames/match3/particles/sapphire_particle.png",
        "emerald": "images/minigames/match3/particles/emerald_particle.png",
        "topaz": "images/minigames/match3/particles/topaz_particle.png",
        "amethyst": "images/minigames/match3/particles/amethyst_particle.png",
        "diamond": "images/minigames/match3/particles/diamond_particle.png",
    }

    # Background and UI sprites
    BACKGROUND_SPRITE = "images/minigames/match3/background.png"
    GRID_FRAME_SPRITE = "images/minigames/match3/grid_frame.png"
    SCORE_PANEL_SPRITE = "images/minigames/match3/score_panel.png"

    # Combo/chain effect sprites
    COMBO_SPRITES = {
        3: "images/minigames/match3/combo/combo_3.png",
        4: "images/minigames/match3/combo/combo_4.png",
        5: "images/minigames/match3/combo/combo_5.png",
    }

    # ==================================================================================
    # SPRITE CACHE - Loaded sprites are cached here
    # ==================================================================================
    _sprite_cache = {}

    def load_sprite(path, scale=None):
        """Load a sprite from path, with optional scaling. Returns None if not found."""
        if path in _sprite_cache:
            return _sprite_cache[path]
        try:
            sprite = pygame.image.load(path).convert_alpha()
            if scale:
                sprite = pygame.transform.scale(sprite, scale)
            _sprite_cache[path] = sprite
            return sprite
        except:
            return None

    def get_gem_sprite(gem_name, size=None):
        """Get the sprite for a gem type. Returns None if USE_SPRITES is False or sprite not found."""
        if not USE_SPRITES:
            return None
        path = GEM_SPRITES.get(gem_name)
        if path:
            return load_sprite(path, size)
        return None

    def get_particle_sprite(gem_name):
        """Get particle sprite for a gem type."""
        if not USE_SPRITES:
            return None
        path = PARTICLE_SPRITES.get(gem_name)
        if path:
            return load_sprite(path)
        return None

    # ==================================================================================
    # END SPRITE CONFIGURATION
    # ==================================================================================

    # ==================================================================================
    # AUDIO CONFIGURATION - Sound effects for the match-3 game
    # ==================================================================================

    USE_AUDIO = True  # Set to False to disable all minigame audio

    # Sound effect paths - replace with your actual audio files
    AUDIO_PATHS = {
        "gem_select": "audio/sfx/minigames/match3/gem_select.ogg",
        "gem_swap": "audio/sfx/minigames/match3/gem_swap.ogg",
        "gem_swap_fail": "audio/sfx/minigames/match3/gem_swap_fail.ogg",
        "match_3": "audio/sfx/minigames/match3/match_3.ogg",
        "match_4": "audio/sfx/minigames/match3/match_4.ogg",
        "match_5": "audio/sfx/minigames/match3/match_5.ogg",
        "cascade": "audio/sfx/minigames/match3/cascade.ogg",
        "gems_falling": "audio/sfx/minigames/match3/gems_falling.ogg",
        "combo_1": "audio/sfx/minigames/match3/combo_1.ogg",
        "combo_2": "audio/sfx/minigames/match3/combo_2.ogg",
        "combo_3": "audio/sfx/minigames/match3/combo_3.ogg",
        "combo_mega": "audio/sfx/minigames/match3/combo_mega.ogg",
        "victory": "audio/sfx/minigames/common/victory.ogg",
        "defeat": "audio/sfx/minigames/common/defeat.ogg",
        "game_start": "audio/sfx/minigames/common/game_start.ogg",
    }

    # Music track for this minigame - sparkling, puzzle casual vibe
    MUSIC_PATH = "audio/music/minigames/crystal_match3.ogg"
    _music_channel = None

    # Audio cache for loaded sounds
    _audio_cache = {}
    _audio_initialized = False

    def init_audio():
        """Initialize pygame mixer for audio playback."""
        global _audio_initialized
        if not _audio_initialized:
            try:
                pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
                _audio_initialized = True
            except:
                pass

    def load_sound(sound_key):
        """Load a sound effect by key. Returns None if not found."""
        if not USE_AUDIO or not _audio_initialized:
            return None
        if sound_key in _audio_cache:
            return _audio_cache[sound_key]
        path = AUDIO_PATHS.get(sound_key)
        if path:
            try:
                sound = pygame.mixer.Sound(path)
                _audio_cache[sound_key] = sound
                return sound
            except:
                return None
        return None

    def play_sound(sound_key, volume=1.0):
        """Play a sound effect by key with optional volume (0.0 to 1.0)."""
        if not USE_AUDIO:
            return
        init_audio()
        sound = load_sound(sound_key)
        if sound:
            sound.set_volume(volume)
            sound.play()

    def play_match_sound(match_count):
        """Play appropriate sound based on match size."""
        if match_count >= 5:
            play_sound("match_5")
        elif match_count >= 4:
            play_sound("match_4")
        else:
            play_sound("match_3")

    def play_combo_sound(combo_level):
        """Play combo sound based on combo level."""
        if combo_level >= 4:
            play_sound("combo_mega")
        elif combo_level >= 3:
            play_sound("combo_3")
        elif combo_level >= 2:
            play_sound("combo_2")
        elif combo_level >= 1:
            play_sound("combo_1")

    def start_music(volume=0.6):
        """Start playing the minigame music."""
        global _music_channel
        if not USE_AUDIO:
            return
        init_audio()
        try:
            pygame.mixer.music.load(MUSIC_PATH)
            pygame.mixer.music.set_volume(volume)
            pygame.mixer.music.play(-1)  # Loop indefinitely
        except:
            pass  # Silently fail if music file not found

    def stop_music(fadeout_ms=500):
        """Stop the minigame music with optional fadeout."""
        if not USE_AUDIO:
            return
        try:
            pygame.mixer.music.fadeout(fadeout_ms)
        except:
            pass

    # ==================================================================================
    # END AUDIO CONFIGURATION
    # ==================================================================================

    # Game constants
    WIDTH, HEIGHT = 1920, 1080
    GRID_COLS = 8
    GRID_ROWS = 8
    CELL_SIZE = 80
    GRID_OFFSET_X = (WIDTH - GRID_COLS * CELL_SIZE) // 2
    GRID_OFFSET_Y = (HEIGHT - GRID_ROWS * CELL_SIZE) // 2 + 30

    # Crystal types (colors for procedural fallback)
    CRYSTAL_TYPES = [
        {"name": "ruby", "color": (220, 50, 70), "glow": (255, 100, 120)},
        {"name": "sapphire", "color": (50, 100, 220), "glow": (100, 150, 255)},
        {"name": "emerald", "color": (50, 200, 80), "glow": (100, 255, 130)},
        {"name": "topaz", "color": (255, 200, 50), "glow": (255, 230, 100)},
        {"name": "amethyst", "color": (180, 80, 220), "glow": (220, 140, 255)},
        {"name": "diamond", "color": (200, 230, 255), "glow": (255, 255, 255)},
    ]

    # Game states
    STATE_PLAYING = "playing"
    STATE_SWAPPING = "swapping"
    STATE_MATCHING = "matching"
    STATE_FALLING = "falling"
    STATE_VICTORY = "victory"
    STATE_GAMEOVER = "gameover"

    class Crystal:
        """A single crystal gem on the board."""
        def __init__(self, crystal_type, row, col):
            self.type = crystal_type
            self.row = row
            self.col = col
            # Visual position (for animations)
            self.x = col * CELL_SIZE + GRID_OFFSET_X
            self.y = row * CELL_SIZE + GRID_OFFSET_Y
            self.target_x = self.x
            self.target_y = self.y
            # Animation state
            self.scale = 1.0
            self.alpha = 255
            self.matched = False
            self.falling = False
            self.glow_phase = random.random() * math.pi * 2
            # Cache sprite reference
            self._sprite = None
            self._sprite_loaded = False

        def update(self, dt):
            # Smooth movement towards target position
            speed = 0.15
            self.x += (self.target_x - self.x) * speed
            self.y += (self.target_y - self.y) * speed

            # Glow animation
            self.glow_phase += dt * 0.003

            # Match animation (shrink and fade)
            if self.matched:
                self.scale = max(0, self.scale - 0.08)
                self.alpha = max(0, self.alpha - 20)

        def set_grid_position(self, row, col):
            self.row = row
            self.col = col
            self.target_x = col * CELL_SIZE + GRID_OFFSET_X
            self.target_y = row * CELL_SIZE + GRID_OFFSET_Y

        def is_at_target(self):
            return abs(self.x - self.target_x) < 2 and abs(self.y - self.target_y) < 2

        def draw(self, surf, time_ms):
            if self.alpha <= 0:
                return

            crystal_info = CRYSTAL_TYPES[self.type]
            gem_name = crystal_info["name"]

            # Try to use sprite if available
            if not self._sprite_loaded:
                self._sprite = get_gem_sprite(gem_name, (CELL_SIZE, CELL_SIZE))
                self._sprite_loaded = True

            if self._sprite:
                # === SPRITE RENDERING PATH ===
                self._draw_with_sprite(surf, time_ms)
            else:
                # === PROCEDURAL FALLBACK ===
                self._draw_procedural(surf, time_ms)

        def _draw_with_sprite(self, surf, time_ms):
            """Draw crystal using loaded sprite."""
            # Apply scale and alpha transformations
            scaled_size = int(CELL_SIZE * self.scale)
            if scaled_size <= 0:
                return

            # Scale sprite
            scaled_sprite = pygame.transform.scale(self._sprite, (scaled_size, scaled_size))

            # Apply alpha
            if self.alpha < 255:
                scaled_sprite.set_alpha(self.alpha)

            # Center the scaled sprite
            offset = (CELL_SIZE - scaled_size) // 2
            surf.blit(scaled_sprite, (int(self.x) + offset, int(self.y) + offset))

        def _draw_procedural(self, surf, time_ms):
            """Draw crystal using procedural graphics (fallback)."""
            crystal_info = CRYSTAL_TYPES[self.type]
            color = crystal_info["color"]
            glow_color = crystal_info["glow"]

            # Calculate center position
            cx = int(self.x + CELL_SIZE // 2)
            cy = int(self.y + CELL_SIZE // 2)

            # Base size with scale
            base_size = int((CELL_SIZE // 2 - 8) * self.scale)
            if base_size <= 0:
                return

            # Glow effect (pulsing)
            glow_intensity = 0.3 + 0.2 * math.sin(self.glow_phase)
            glow_size = int(base_size * (1.3 + glow_intensity * 0.2))

            # Create surface for alpha blending
            gem_surf = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
            gem_cx, gem_cy = CELL_SIZE // 2, CELL_SIZE // 2

            # Outer glow
            glow_alpha = int(80 * glow_intensity * (self.alpha / 255))
            pygame.draw.circle(gem_surf, (*glow_color, glow_alpha), (gem_cx, gem_cy), glow_size)

            # Main crystal body (hexagonal shape)
            points = []
            for i in range(6):
                angle = math.pi / 6 + i * math.pi / 3
                px = gem_cx + math.cos(angle) * base_size
                py = gem_cy + math.sin(angle) * base_size
                points.append((px, py))

            # Draw with alpha
            crystal_alpha = int(self.alpha)
            pygame.draw.polygon(gem_surf, (*color, crystal_alpha), points)

            # Inner highlight (smaller hexagon)
            inner_size = base_size * 0.6
            inner_points = []
            for i in range(6):
                angle = math.pi / 6 + i * math.pi / 3
                px = gem_cx + math.cos(angle) * inner_size - 3
                py = gem_cy + math.sin(angle) * inner_size - 3
                inner_points.append((px, py))

            highlight_color = tuple(min(255, c + 60) for c in color)
            pygame.draw.polygon(gem_surf, (*highlight_color, crystal_alpha), inner_points)

            # Sparkle effect
            sparkle_alpha = int(150 + 100 * math.sin(self.glow_phase * 2))
            sparkle_size = 3 + int(2 * math.sin(self.glow_phase * 3))
            pygame.draw.circle(gem_surf, (255, 255, 255, min(255, sparkle_alpha)),
                            (gem_cx - base_size // 3, gem_cy - base_size // 3), sparkle_size)

            surf.blit(gem_surf, (int(self.x), int(self.y)))

    class MatchParticle:
        """Particle effect for matched crystals."""
        def __init__(self, x, y, color):
            self.x = x
            self.y = y
            angle = random.random() * math.pi * 2
            speed = random.uniform(3, 8)
            self.vx = math.cos(angle) * speed
            self.vy = math.sin(angle) * speed
            self.color = color
            self.size = random.uniform(4, 10)
            self.lifetime = random.randint(300, 600)
            self.max_lifetime = self.lifetime
            self.alive = True

        def update(self, dt):
            self.x += self.vx
            self.y += self.vy
            self.vy += 0.15  # Gravity
            self.lifetime -= dt
            if self.lifetime <= 0:
                self.alive = False

        def draw(self, surf):
            if not self.alive:
                return
            alpha = int(255 * (self.lifetime / self.max_lifetime))
            size = self.size * (self.lifetime / self.max_lifetime)
            if size < 1:
                return
            particle_surf = pygame.Surface((int(size * 2 + 4), int(size * 2 + 4)), pygame.SRCALPHA)
            pygame.draw.circle(particle_surf, (*self.color[:3], alpha),
                            (int(size + 2), int(size + 2)), int(size))
            surf.blit(particle_surf, (int(self.x - size), int(self.y - size)))

    class CrystalMatchGame:
        """Main game controller for Crystal Match-3."""
        def __init__(self, target_score=10000, moves_limit=30):
            self.grid = [[None for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]
            self.state = STATE_PLAYING
            self.score = 0
            self.target_score = target_score
            self.moves_left = moves_limit
            self.combo = 0

            # Selection state
            self.selected = None  # (row, col) of selected crystal
            self.swap_from = None
            self.swap_to = None

            # Animation
            self.particles = []
            self.match_delay = 0
            self.cascade_bonus = 0

            # Initialize board
            self.fill_board()
            # Remove any initial matches
            while self.find_matches():
                self.remove_matches_instant()
                self.fill_board()

        def fill_board(self):
            """Fill empty spaces with new crystals."""
            for col in range(GRID_COLS):
                # Count empty spaces in this column
                empty_count = 0
                for row in range(GRID_ROWS):
                    if self.grid[row][col] is None:
                        empty_count += 1

                # Drop existing crystals down
                write_row = GRID_ROWS - 1
                for read_row in range(GRID_ROWS - 1, -1, -1):
                    if self.grid[read_row][col] is not None:
                        if write_row != read_row:
                            self.grid[write_row][col] = self.grid[read_row][col]
                            self.grid[write_row][col].set_grid_position(write_row, col)
                            self.grid[write_row][col].falling = True
                            self.grid[read_row][col] = None
                        write_row -= 1

                # Fill empty spaces at top with new crystals
                for row in range(empty_count):
                    crystal_type = random.randint(0, len(CRYSTAL_TYPES) - 1)
                    crystal = Crystal(crystal_type, row, col)
                    # Start above the grid for drop animation
                    crystal.y = (row - empty_count) * CELL_SIZE + GRID_OFFSET_Y
                    crystal.falling = True
                    self.grid[row][col] = crystal

        def find_matches(self):
            """Find all matching groups of 3+ crystals."""
            matches = set()

            # Check horizontal matches
            for row in range(GRID_ROWS):
                for col in range(GRID_COLS - 2):
                    if self.grid[row][col] and self.grid[row][col + 1] and self.grid[row][col + 2]:
                        t = self.grid[row][col].type
                        if self.grid[row][col + 1].type == t and self.grid[row][col + 2].type == t:
                            matches.add((row, col))
                            matches.add((row, col + 1))
                            matches.add((row, col + 2))
                            # Check for 4 or 5 in a row
                            if col + 3 < GRID_COLS and self.grid[row][col + 3] and self.grid[row][col + 3].type == t:
                                matches.add((row, col + 3))
                                if col + 4 < GRID_COLS and self.grid[row][col + 4] and self.grid[row][col + 4].type == t:
                                    matches.add((row, col + 4))

            # Check vertical matches
            for col in range(GRID_COLS):
                for row in range(GRID_ROWS - 2):
                    if self.grid[row][col] and self.grid[row + 1][col] and self.grid[row + 2][col]:
                        t = self.grid[row][col].type
                        if self.grid[row + 1][col].type == t and self.grid[row + 2][col].type == t:
                            matches.add((row, col))
                            matches.add((row + 1, col))
                            matches.add((row + 2, col))
                            # Check for 4 or 5 in a column
                            if row + 3 < GRID_ROWS and self.grid[row + 3][col] and self.grid[row + 3][col].type == t:
                                matches.add((row + 3, col))
                                if row + 4 < GRID_ROWS and self.grid[row + 4][col] and self.grid[row + 4][col].type == t:
                                    matches.add((row + 4, col))

            return matches

        def remove_matches_instant(self):
            """Remove matches without animation (for initial setup)."""
            matches = self.find_matches()
            for row, col in matches:
                self.grid[row][col] = None

        def process_matches(self):
            """Process matches with scoring and particles."""
            matches = self.find_matches()
            if not matches:
                self.combo = 0
                self.cascade_bonus = 0
                return False

            self.combo += 1
            self.cascade_bonus += 1

            # Calculate score
            base_points = len(matches) * 10
            combo_multiplier = 1 + (self.combo - 1) * 0.5
            cascade_multiplier = 1 + (self.cascade_bonus - 1) * 0.25
            points = int(base_points * combo_multiplier * cascade_multiplier)
            self.score += points

            # Mark crystals as matched and spawn particles
            for row, col in matches:
                crystal = self.grid[row][col]
                if crystal and not crystal.matched:
                    crystal.matched = True
                    # Spawn particles
                    cx = crystal.x + CELL_SIZE // 2
                    cy = crystal.y + CELL_SIZE // 2
                    color = CRYSTAL_TYPES[crystal.type]["glow"]
                    for _ in range(6):
                        self.particles.append(MatchParticle(cx, cy, color))

            return True

        def remove_matched_crystals(self):
            """Remove crystals that have finished their match animation."""
            removed = False
            for row in range(GRID_ROWS):
                for col in range(GRID_COLS):
                    crystal = self.grid[row][col]
                    if crystal and crystal.matched and crystal.alpha <= 0:
                        self.grid[row][col] = None
                        removed = True
            return removed

        def is_board_stable(self):
            """Check if all crystals are at their target positions."""
            for row in range(GRID_ROWS):
                for col in range(GRID_COLS):
                    crystal = self.grid[row][col]
                    if crystal:
                        if not crystal.is_at_target():
                            return False
                        if crystal.matched and crystal.alpha > 0:
                            return False
            return True

        def has_empty_spaces(self):
            """Check if there are empty spaces on the board."""
            for row in range(GRID_ROWS):
                for col in range(GRID_COLS):
                    if self.grid[row][col] is None:
                        return True
            return False

        def get_crystal_at_pos(self, mx, my):
            """Get grid coordinates from mouse position."""
            col = (mx - GRID_OFFSET_X) // CELL_SIZE
            row = (my - GRID_OFFSET_Y) // CELL_SIZE
            if 0 <= row < GRID_ROWS and 0 <= col < GRID_COLS:
                return (row, col)
            return None

        def is_adjacent(self, pos1, pos2):
            """Check if two grid positions are adjacent."""
            r1, c1 = pos1
            r2, c2 = pos2
            return abs(r1 - r2) + abs(c1 - c2) == 1

        def swap_crystals(self, pos1, pos2):
            """Swap two crystals on the grid."""
            r1, c1 = pos1
            r2, c2 = pos2
            self.grid[r1][c1], self.grid[r2][c2] = self.grid[r2][c2], self.grid[r1][c1]
            if self.grid[r1][c1]:
                self.grid[r1][c1].set_grid_position(r1, c1)
            if self.grid[r2][c2]:
                self.grid[r2][c2].set_grid_position(r2, c2)

        def handle_click(self, mx, my):
            """Handle mouse click on the grid."""
            if self.state != STATE_PLAYING:
                return

            pos = self.get_crystal_at_pos(mx, my)
            if pos is None:
                return

            if self.selected is None:
                # First selection
                self.selected = pos
            elif pos == self.selected:
                # Deselect
                self.selected = None
            elif self.is_adjacent(self.selected, pos):
                # Attempt swap
                self.swap_from = self.selected
                self.swap_to = pos
                self.swap_crystals(self.swap_from, self.swap_to)
                self.state = STATE_SWAPPING
                self.selected = None
            else:
                # Select new crystal
                self.selected = pos

        def update(self, dt):
            """Update game state."""
            time_ms = pygame.time.get_ticks()

            # Update all crystals
            for row in range(GRID_ROWS):
                for col in range(GRID_COLS):
                    crystal = self.grid[row][col]
                    if crystal:
                        crystal.update(dt)

            # Update particles
            for particle in self.particles:
                particle.update(dt)
            self.particles = [p for p in self.particles if p.alive]

            # State machine
            if self.state == STATE_SWAPPING:
                if self.is_board_stable():
                    # Check if swap created a match
                    if self.find_matches():
                        self.moves_left -= 1
                        self.state = STATE_MATCHING
                    else:
                        # Swap back - invalid move
                        self.swap_crystals(self.swap_from, self.swap_to)
                        self.state = STATE_PLAYING
                    self.swap_from = None
                    self.swap_to = None

            elif self.state == STATE_MATCHING:
                if self.process_matches():
                    self.match_delay = 300  # Wait for match animation
                self.state = STATE_FALLING

            elif self.state == STATE_FALLING:
                # Wait for match animation
                if self.match_delay > 0:
                    self.match_delay -= dt
                    return

                # Remove finished match animations
                self.remove_matched_crystals()

                # Fill empty spaces
                if self.has_empty_spaces():
                    self.fill_board()

                # Wait for board to stabilize
                if self.is_board_stable():
                    # Check for cascade matches
                    if self.find_matches():
                        self.state = STATE_MATCHING
                    else:
                        # Check win/lose conditions
                        if self.score >= self.target_score:
                            self.state = STATE_VICTORY
                        elif self.moves_left <= 0:
                            self.state = STATE_GAMEOVER
                        else:
                            self.state = STATE_PLAYING

            elif self.state == STATE_PLAYING:
                # Check for valid moves (future: detect no moves left)
                pass

        def draw(self, surf):
            """Draw the game."""
            time_ms = pygame.time.get_ticks()

            # Draw grid background
            grid_bg = pygame.Surface((GRID_COLS * CELL_SIZE + 20, GRID_ROWS * CELL_SIZE + 20), pygame.SRCALPHA)
            draw_rounded_rect(grid_bg, (20, 10, 40, 200), grid_bg.get_rect(), radius=15)
            draw_rounded_rect(grid_bg, (100, 80, 150, 150), grid_bg.get_rect(), radius=15, width=3)
            surf.blit(grid_bg, (GRID_OFFSET_X - 10, GRID_OFFSET_Y - 10))

            # Draw grid cells
            for row in range(GRID_ROWS):
                for col in range(GRID_COLS):
                    x = col * CELL_SIZE + GRID_OFFSET_X
                    y = row * CELL_SIZE + GRID_OFFSET_Y
                    # Cell background
                    cell_color = (40, 25, 60, 100) if (row + col) % 2 == 0 else (50, 35, 70, 100)
                    cell_surf = pygame.Surface((CELL_SIZE - 4, CELL_SIZE - 4), pygame.SRCALPHA)
                    draw_rounded_rect(cell_surf, cell_color, cell_surf.get_rect(), radius=8)
                    surf.blit(cell_surf, (x + 2, y + 2))

            # Draw selection highlight
            if self.selected and self.state == STATE_PLAYING:
                sel_row, sel_col = self.selected
                sel_x = sel_col * CELL_SIZE + GRID_OFFSET_X
                sel_y = sel_row * CELL_SIZE + GRID_OFFSET_Y
                pulse = math.sin(time_ms * 0.008) * 5
                sel_surf = pygame.Surface((int(CELL_SIZE + pulse * 2), int(CELL_SIZE + pulse * 2)), pygame.SRCALPHA)
                draw_rounded_rect(sel_surf, (255, 255, 200, 150), sel_surf.get_rect(), radius=10, width=4)
                surf.blit(sel_surf, (sel_x - pulse, sel_y - pulse))

            # Draw crystals
            for row in range(GRID_ROWS):
                for col in range(GRID_COLS):
                    crystal = self.grid[row][col]
                    if crystal:
                        crystal.draw(surf, time_ms)

            # Draw particles
            for particle in self.particles:
                particle.draw(surf)

            # Draw UI
            self.draw_ui(surf)

        def draw_ui(self, surf):
            """Draw score, moves, and other UI elements."""
            # Score panel (left)
            panel_surf = pygame.Surface((280, 120), pygame.SRCALPHA)
            draw_rounded_rect(panel_surf, (20, 10, 40, 220), panel_surf.get_rect(), radius=15)
            draw_rounded_rect(panel_surf, (150, 100, 200), panel_surf.get_rect(), radius=15, width=2)
            surf.blit(panel_surf, (50, 50))

            # Score text
            font_large = pygame.font.Font(None, 48)
            font_small = pygame.font.Font(None, 32)

            score_label = font_small.render("SCORE", True, (200, 180, 255))
            surf.blit(score_label, (100, 65))

            score_text = font_large.render(f"{self.score}", True, (255, 255, 255))
            surf.blit(score_text, (100, 95))

            target_text = font_small.render(f"Target: {self.target_score}", True, (180, 160, 220))
            surf.blit(target_text, (100, 140))

            # Moves panel (right)
            surf.blit(panel_surf, (WIDTH - 330, 50))

            moves_label = font_small.render("MOVES", True, (200, 180, 255))
            surf.blit(moves_label, (WIDTH - 280, 65))

            moves_color = (255, 255, 255) if self.moves_left > 5 else (255, 100, 100)
            moves_text = font_large.render(f"{self.moves_left}", True, moves_color)
            surf.blit(moves_text, (WIDTH - 280, 95))

            # Combo indicator
            if self.combo > 1:
                combo_text = font_large.render(f"COMBO x{self.combo}!", True, (255, 220, 100))
                combo_x = WIDTH // 2 - combo_text.get_width() // 2
                surf.blit(combo_text, (combo_x, 60))

            # Progress bar
            bar_width = 400
            bar_height = 20
            bar_x = WIDTH // 2 - bar_width // 2
            bar_y = HEIGHT - 60

            # Background
            draw_rounded_rect(surf, (40, 20, 60), (bar_x, bar_y, bar_width, bar_height), radius=10)

            # Fill
            progress = min(1.0, self.score / self.target_score)
            fill_width = int(bar_width * progress)
            if fill_width > 0:
                # Gradient effect
                fill_color = (100, 200, 100) if progress < 1.0 else (255, 220, 100)
                draw_rounded_rect(surf, fill_color, (bar_x, bar_y, fill_width, bar_height), radius=10)

            # Border
            draw_rounded_rect(surf, (150, 100, 200), (bar_x, bar_y, bar_width, bar_height), radius=10, width=2)

            # State overlays
            if self.state == STATE_VICTORY:
                self.draw_overlay(surf, "VICTORY!", (100, 255, 150), "Crystal power restored!")
            elif self.state == STATE_GAMEOVER:
                self.draw_overlay(surf, "OUT OF MOVES", (255, 100, 100), "Try again!")

        def draw_overlay(self, surf, title, color, subtitle):
            """Draw victory/gameover overlay."""
            # Darken background
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))
            surf.blit(overlay, (0, 0))

            # Title
            font_title = pygame.font.Font(None, 96)
            font_sub = pygame.font.Font(None, 48)

            title_text = font_title.render(title, True, color)
            title_x = WIDTH // 2 - title_text.get_width() // 2
            surf.blit(title_text, (title_x, HEIGHT // 2 - 80))

            sub_text = font_sub.render(subtitle, True, (255, 255, 255))
            sub_x = WIDTH // 2 - sub_text.get_width() // 2
            surf.blit(sub_text, (sub_x, HEIGHT // 2))

            # Score display
            score_text = font_sub.render(f"Final Score: {self.score}", True, (200, 180, 255))
            score_x = WIDTH // 2 - score_text.get_width() // 2
            surf.blit(score_text, (score_x, HEIGHT // 2 + 60))


# Ren'Py Displayable wrapper
init python:
    class CrystalMatchDisplayable(renpy.Displayable):
        """Ren'Py displayable wrapper for Crystal Match-3 game."""

        def __init__(self, target_score=1000, moves_limit=30, **kwargs):
            super(CrystalMatchDisplayable, self).__init__(**kwargs)
            self.target_score = target_score
            self.moves_limit = moves_limit
            self.game = None
            self.last_time = None

        def render(self, width, height, st, at):
            import pygame

            # Initialize game on first render
            if self.game is None:
                self.game = crystal_match.CrystalMatchGame(self.target_score, self.moves_limit)
                self.last_time = pygame.time.get_ticks()

            # Calculate delta time
            current_time = pygame.time.get_ticks()
            dt = current_time - self.last_time
            self.last_time = current_time

            # Update game
            self.game.update(dt)

            # Create render surface
            render = renpy.Render(crystal_match.WIDTH, crystal_match.HEIGHT)
            canvas = render.canvas()

            # Clear with background color
            canvas.rect((30, 15, 50), (0, 0, crystal_match.WIDTH, crystal_match.HEIGHT))

            # Draw game
            self.game.draw(canvas.get_surface())

            # Request redraw
            renpy.redraw(self, 0)

            return render

        def event(self, ev, x, y, st):
            import pygame

            if self.game is None:
                return None

            # Handle mouse click
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                self.game.handle_click(x, y)

            # Handle escape to quit
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    return "quit"
                if ev.key == pygame.K_RETURN or ev.key == pygame.K_KP_ENTER:
                    if self.game.state == crystal_match.STATE_VICTORY:
                        return "victory"
                    elif self.game.state == crystal_match.STATE_GAMEOVER:
                        return "retry"

            return None

        def visit(self):
            return []


# Screen for the minigame
screen crystal_match_screen(target_score=1000, moves_limit=30):
    default game_display = CrystalMatchDisplayable(target_score, moves_limit)

    add Solid("#1e0f32")
    add game_display

    # Instructions (fade out after a few seconds)
    timer 5.0 action Hide("crystal_match_instructions")

    if crystal_match.STATE_VICTORY:
        key "K_RETURN" action Return("victory")
        key "K_KP_ENTER" action Return("victory")

    key "K_ESCAPE" action Return("quit")


screen crystal_match_instructions():
    frame:
        xalign 0.5 yalign 0.85
        background "#000000aa"
        padding (30, 20)

        vbox:
            spacing 10
            text "Click to select a crystal, then click an adjacent crystal to swap!" size 28 color "#ffffff" xalign 0.5
            text "Match 3 or more of the same type to score points!" size 24 color "#cccccc" xalign 0.5


# Entry label for the minigame
label crystal_match_start(target_score=1000, moves_limit=30):
    $ quick_menu = False

    # Start minigame music
    $ crystal_match.start_music()

    show screen crystal_match_instructions
    call screen crystal_match_screen(target_score, moves_limit)

    # Stop minigame music
    $ crystal_match.stop_music()

    $ quick_menu = True
    $ result = _return

    if result == "victory":
        return True
    else:
        return False


# Test label (can be removed in production)
label test_crystal_match:
    "Starting Crystal Match minigame..."

    call crystal_match_start(target_score=500, moves_limit=25)

    if _return:
        "Congratulations! You won!"
    else:
        "Better luck next time!"

    return
