# clocktower_tetris.rpy - Clocktower Tetris Minigame
# A classic Tetris game with a clockwork/gear theme

####################################################################################################################
# CLOCKWORK TETRIS MINIGAME
####################################################################################################################

init python in clockwork_tetris:
    import pygame
    import random
    import math
    from pygame.locals import *

    ####################################################################################################################
    # SPRITE CONFIGURATION - Set USE_SPRITES = True and provide sprite paths to use custom graphics
    ####################################################################################################################

    USE_SPRITES = False  # Set to True when sprites are ready

    # Block/Tetromino sprites - one for each piece type
    # Each sprite should be a single block tile that tiles together
    BLOCK_SPRITES = {
        'I': "images/minigames/tetris/blocks/gear_shaft.png",      # Cyan - Gear Shaft piece
        'O': "images/minigames/tetris/blocks/cog.png",             # Yellow - Cog piece
        'T': "images/minigames/tetris/blocks/pivot.png",           # Purple - Pivot piece
        'S': "images/minigames/tetris/blocks/spring.png",          # Green - Spring piece
        'Z': "images/minigames/tetris/blocks/lever.png",           # Red - Lever piece
        'J': "images/minigames/tetris/blocks/hook.png",            # Blue - Hook piece
        'L': "images/minigames/tetris/blocks/bracket.png",         # Orange - Bracket piece
    }

    # Ghost piece sprites (semi-transparent versions shown where piece will land)
    GHOST_SPRITES = {
        'I': "images/minigames/tetris/ghosts/gear_shaft_ghost.png",
        'O': "images/minigames/tetris/ghosts/cog_ghost.png",
        'T': "images/minigames/tetris/ghosts/pivot_ghost.png",
        'S': "images/minigames/tetris/ghosts/spring_ghost.png",
        'Z': "images/minigames/tetris/ghosts/lever_ghost.png",
        'J': "images/minigames/tetris/ghosts/hook_ghost.png",
        'L': "images/minigames/tetris/ghosts/bracket_ghost.png",
    }

    # Block glow effect sprites (rendered behind blocks when active piece glows)
    BLOCK_GLOW_SPRITES = {
        'I': "images/minigames/tetris/glows/gear_shaft_glow.png",
        'O': "images/minigames/tetris/glows/cog_glow.png",
        'T': "images/minigames/tetris/glows/pivot_glow.png",
        'S': "images/minigames/tetris/glows/spring_glow.png",
        'Z': "images/minigames/tetris/glows/lever_glow.png",
        'J': "images/minigames/tetris/glows/hook_glow.png",
        'L': "images/minigames/tetris/glows/bracket_glow.png",
    }

    # Decorative gear sprites (background decoration)
    GEAR_SPRITES = {
        "small": "images/minigames/tetris/gears/gear_small.png",       # ~60px diameter
        "medium": "images/minigames/tetris/gears/gear_medium.png",     # ~90px diameter
        "large": "images/minigames/tetris/gears/gear_large.png",       # ~120px diameter
    }

    # Line clear effect sprites
    LINE_CLEAR_SPRITES = {
        "flash": "images/minigames/tetris/effects/line_flash.png",          # Full row flash effect
        "particle_gold": "images/minigames/tetris/effects/particle_gold.png",
        "particle_purple": "images/minigames/tetris/effects/particle_purple.png",
        "particle_white": "images/minigames/tetris/effects/particle_white.png",
    }

    # UI panel sprites
    UI_SPRITES = {
        "grid_frame": "images/minigames/tetris/ui/grid_frame.png",         # Frame around playfield
        "grid_bg": "images/minigames/tetris/ui/grid_background.png",       # Grid background
        "panel_next": "images/minigames/tetris/ui/panel_next.png",         # "NEXT" piece panel
        "panel_hold": "images/minigames/tetris/ui/panel_hold.png",         # "HOLD" piece panel
        "panel_score": "images/minigames/tetris/ui/panel_score.png",       # Score/stats panel
        "panel_controls": "images/minigames/tetris/ui/panel_controls.png", # Controls hint panel
    }

    # Overlay sprites
    OVERLAY_SPRITES = {
        "victory": "images/minigames/tetris/overlays/victory_banner.png",
        "gameover": "images/minigames/tetris/overlays/gameover_banner.png",
    }

    # Background sprite
    BACKGROUND_SPRITE = "images/minigames/tetris/background.png"

    # Sprite cache
    _sprite_cache = {}

    def load_sprite(path, scale=None):
        """Load a sprite from path with optional scaling.

        Args:
            path: Path to the sprite image
            scale: Optional (width, height) tuple to scale to

        Returns:
            pygame.Surface or None if loading fails
        """
        cache_key = (path, scale)
        if cache_key in _sprite_cache:
            return _sprite_cache[cache_key]

        try:
            sprite = pygame.image.load(path).convert_alpha()
            if scale:
                sprite = pygame.transform.scale(sprite, scale)
            _sprite_cache[cache_key] = sprite
            return sprite
        except (pygame.error, FileNotFoundError):
            return None

    def get_block_sprite(piece_type, size=None):
        """Get sprite for a tetromino block type.

        Args:
            piece_type: 'I', 'O', 'T', 'S', 'Z', 'J', or 'L'
            size: Optional (width, height) tuple

        Returns:
            pygame.Surface or None
        """
        if not USE_SPRITES:
            return None
        path = BLOCK_SPRITES.get(piece_type)
        if not path:
            return None
        return load_sprite(path, size)

    def get_ghost_sprite(piece_type, size=None):
        """Get ghost sprite for a tetromino block type."""
        if not USE_SPRITES:
            return None
        path = GHOST_SPRITES.get(piece_type)
        if not path:
            return None
        return load_sprite(path, size)

    def get_glow_sprite(piece_type, size=None):
        """Get glow sprite for a tetromino block type."""
        if not USE_SPRITES:
            return None
        path = BLOCK_GLOW_SPRITES.get(piece_type)
        if not path:
            return None
        return load_sprite(path, size)

    def get_gear_sprite(gear_size, dimensions=None):
        """Get a decorative gear sprite.

        Args:
            gear_size: 'small', 'medium', or 'large'
            dimensions: Optional (width, height) tuple
        """
        if not USE_SPRITES:
            return None
        path = GEAR_SPRITES.get(gear_size)
        if not path:
            return None
        return load_sprite(path, dimensions)

    def get_particle_sprite(particle_type, size=None):
        """Get a line clear particle sprite."""
        if not USE_SPRITES:
            return None
        path = LINE_CLEAR_SPRITES.get(particle_type)
        if not path:
            return None
        return load_sprite(path, size)

    def get_ui_sprite(element, size=None):
        """Get a UI element sprite."""
        if not USE_SPRITES:
            return None
        path = UI_SPRITES.get(element)
        if not path:
            return None
        return load_sprite(path, size)

    def clear_sprite_cache():
        """Clear the sprite cache to free memory."""
        _sprite_cache.clear()

    ####################################################################################################################
    # END SPRITE CONFIGURATION
    ####################################################################################################################

    ####################################################################################################################
    # AUDIO CONFIGURATION - Sound effects for Tetris
    ####################################################################################################################

    USE_AUDIO = True  # Set to False to disable all minigame audio

    AUDIO_PATHS = {
        "piece_move": "audio/sfx/minigames/tetris/piece_move.ogg",
        "piece_rotate": "audio/sfx/minigames/tetris/piece_rotate.ogg",
        "piece_drop": "audio/sfx/minigames/tetris/piece_drop.ogg",
        "hard_drop": "audio/sfx/minigames/tetris/hard_drop.ogg",
        "piece_lock": "audio/sfx/minigames/tetris/piece_lock.ogg",
        "line_clear": "audio/sfx/minigames/tetris/line_clear.ogg",
        "line_clear_double": "audio/sfx/minigames/tetris/line_clear_double.ogg",
        "line_clear_triple": "audio/sfx/minigames/tetris/line_clear_triple.ogg",
        "line_clear_tetris": "audio/sfx/minigames/tetris/line_clear_tetris.ogg",
        "hold_piece": "audio/sfx/minigames/tetris/hold_piece.ogg",
        "level_up": "audio/sfx/minigames/tetris/level_up.ogg",
        "danger_warning": "audio/sfx/minigames/tetris/danger_warning.ogg",
        "victory": "audio/sfx/minigames/common/victory.ogg",
        "defeat": "audio/sfx/minigames/common/defeat.ogg",
        "game_start": "audio/sfx/minigames/common/game_start.ogg",
    }

    # Background music - mechanical, building tension theme
    MUSIC_PATH = "audio/music/minigames/clocktower_tetris.ogg"

    _audio_cache = {}
    _audio_initialized = False
    _music_playing = False

    def init_audio():
        global _audio_initialized
        if not _audio_initialized:
            try:
                pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
                _audio_initialized = True
            except:
                pass

    def load_sound(sound_key):
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
        if not USE_AUDIO:
            return
        init_audio()
        sound = load_sound(sound_key)
        if sound:
            sound.set_volume(volume)
            sound.play()

    def play_line_clear_sound(lines_cleared):
        """Play appropriate sound based on lines cleared."""
        if lines_cleared >= 4:
            play_sound("line_clear_tetris")
        elif lines_cleared == 3:
            play_sound("line_clear_triple")
        elif lines_cleared == 2:
            play_sound("line_clear_double")
        elif lines_cleared == 1:
            play_sound("line_clear")

    def start_music(volume=0.6):
        """Start playing the Tetris music."""
        global _music_playing
        if not USE_AUDIO:
            return
        init_audio()
        try:
            pygame.mixer.music.load(MUSIC_PATH)
            pygame.mixer.music.set_volume(volume)
            pygame.mixer.music.play(-1)  # Loop indefinitely
            _music_playing = True
        except:
            pass

    def stop_music(fadeout_ms=500):
        """Stop the Tetris music with optional fadeout."""
        global _music_playing
        if not USE_AUDIO:
            return
        try:
            pygame.mixer.music.fadeout(fadeout_ms)
            _music_playing = False
        except:
            pass

    ####################################################################################################################
    # END AUDIO CONFIGURATION
    ####################################################################################################################

    # Game constants
    WIDTH, HEIGHT = 1920, 1080
    GRID_COLS = 10
    GRID_ROWS = 20
    CELL_SIZE = 38
    GRID_OFFSET_X = (WIDTH - GRID_COLS * CELL_SIZE) // 2
    GRID_OFFSET_Y = (HEIGHT - GRID_ROWS * CELL_SIZE) // 2 + 20

    # Tetromino definitions (each as a list of rotations, each rotation as relative coords)
    TETROMINOES = {
        'I': {
            'rotations': [
                [(0, 0), (1, 0), (2, 0), (3, 0)],
                [(0, 0), (0, 1), (0, 2), (0, 3)],
            ],
            'color': (100, 200, 255),
            'glow': (150, 230, 255),
            'name': 'Gear Shaft'
        },
        'O': {
            'rotations': [
                [(0, 0), (1, 0), (0, 1), (1, 1)],
            ],
            'color': (255, 220, 100),
            'glow': (255, 240, 150),
            'name': 'Cog'
        },
        'T': {
            'rotations': [
                [(0, 0), (1, 0), (2, 0), (1, 1)],
                [(0, 0), (0, 1), (0, 2), (1, 1)],
                [(1, 0), (0, 1), (1, 1), (2, 1)],
                [(1, 0), (1, 1), (1, 2), (0, 1)],
            ],
            'color': (180, 100, 220),
            'glow': (220, 150, 255),
            'name': 'Pivot'
        },
        'S': {
            'rotations': [
                [(1, 0), (2, 0), (0, 1), (1, 1)],
                [(0, 0), (0, 1), (1, 1), (1, 2)],
            ],
            'color': (100, 220, 100),
            'glow': (150, 255, 150),
            'name': 'Spring'
        },
        'Z': {
            'rotations': [
                [(0, 0), (1, 0), (1, 1), (2, 1)],
                [(1, 0), (0, 1), (1, 1), (0, 2)],
            ],
            'color': (220, 80, 80),
            'glow': (255, 130, 130),
            'name': 'Lever'
        },
        'J': {
            'rotations': [
                [(0, 0), (0, 1), (1, 1), (2, 1)],
                [(0, 0), (1, 0), (0, 1), (0, 2)],
                [(0, 0), (1, 0), (2, 0), (2, 1)],
                [(1, 0), (1, 1), (0, 2), (1, 2)],
            ],
            'color': (80, 100, 220),
            'glow': (130, 150, 255),
            'name': 'Hook'
        },
        'L': {
            'rotations': [
                [(2, 0), (0, 1), (1, 1), (2, 1)],
                [(0, 0), (0, 1), (0, 2), (1, 2)],
                [(0, 0), (1, 0), (2, 0), (0, 1)],
                [(0, 0), (1, 0), (1, 1), (1, 2)],
            ],
            'color': (255, 150, 50),
            'glow': (255, 190, 100),
            'name': 'Bracket'
        },
    }

    # Game states
    STATE_PLAYING = "playing"
    STATE_PAUSED = "paused"
    STATE_GAMEOVER = "gameover"
    STATE_VICTORY = "victory"

    class Piece:
        """A falling tetromino piece."""
        def __init__(self, piece_type):
            self.type = piece_type
            self.data = TETROMINOES[piece_type]
            self.rotation = 0
            self.x = GRID_COLS // 2 - 2
            self.y = 0
            self.glow_phase = 0

        def get_blocks(self):
            """Get current block positions."""
            rotations = self.data['rotations']
            blocks = rotations[self.rotation % len(rotations)]
            return [(self.x + bx, self.y + by) for bx, by in blocks]

        def get_ghost_blocks(self, grid):
            """Get position where piece would land."""
            ghost_y = self.y
            while True:
                # Check if can move down
                can_move = True
                blocks = self.data['rotations'][self.rotation % len(self.data['rotations'])]
                for bx, by in blocks:
                    new_y = ghost_y + by + 1
                    new_x = self.x + bx
                    if new_y >= GRID_ROWS or (new_x >= 0 and new_y >= 0 and grid[new_y][new_x] is not None):
                        can_move = False
                        break
                if can_move:
                    ghost_y += 1
                else:
                    break
            return [(self.x + bx, ghost_y + by) for bx, by in blocks]

        def rotate(self, grid, direction=1):
            """Try to rotate the piece."""
            old_rotation = self.rotation
            self.rotation = (self.rotation + direction) % len(self.data['rotations'])

            # Check if rotation is valid
            if not self.is_valid_position(grid):
                # Try wall kicks
                kicks = [(-1, 0), (1, 0), (0, -1), (-2, 0), (2, 0)]
                for dx, dy in kicks:
                    self.x += dx
                    self.y += dy
                    if self.is_valid_position(grid):
                        return True
                    self.x -= dx
                    self.y -= dy
                # Revert rotation
                self.rotation = old_rotation
                return False
            return True

        def move(self, dx, dy, grid):
            """Try to move the piece."""
            self.x += dx
            self.y += dy
            if not self.is_valid_position(grid):
                self.x -= dx
                self.y -= dy
                return False
            return True

        def is_valid_position(self, grid):
            """Check if current position is valid."""
            for bx, by in self.get_blocks():
                if bx < 0 or bx >= GRID_COLS or by >= GRID_ROWS:
                    return False
                if by >= 0 and grid[by][bx] is not None:
                    return False
            return True

    class LineClearEffect:
        """Visual effect for cleared lines."""
        def __init__(self, row):
            self.row = row
            self.lifetime = 300
            self.max_lifetime = 300
            self.particles = []

            # Spawn particles
            for col in range(GRID_COLS):
                x = GRID_OFFSET_X + col * CELL_SIZE + CELL_SIZE // 2
                y = GRID_OFFSET_Y + row * CELL_SIZE + CELL_SIZE // 2
                for _ in range(3):
                    angle = random.random() * math.pi * 2
                    speed = random.uniform(2, 5)
                    self.particles.append({
                        'x': x,
                        'y': y,
                        'vx': math.cos(angle) * speed,
                        'vy': math.sin(angle) * speed - 2,
                        'size': random.uniform(3, 8),
                        'color': random.choice([(255, 220, 100), (200, 180, 255), (255, 255, 255)])
                    })

        def update(self, dt):
            self.lifetime -= dt
            for p in self.particles:
                p['x'] += p['vx']
                p['y'] += p['vy']
                p['vy'] += 0.1
            return self.lifetime > 0

        def draw(self, surf):
            alpha = int(255 * (self.lifetime / self.max_lifetime))
            for p in self.particles:
                size = p['size'] * (self.lifetime / self.max_lifetime)
                if size > 0:
                    particle_surf = pygame.Surface((int(size * 2 + 4), int(size * 2 + 4)), pygame.SRCALPHA)
                    color = (*p['color'], alpha)
                    pygame.draw.circle(particle_surf, color, (int(size + 2), int(size + 2)), int(size))
                    surf.blit(particle_surf, (int(p['x'] - size), int(p['y'] - size)))

    class TetrisGame:
        """Main Tetris game controller."""
        def __init__(self, target_lines=25, time_limit=None):
            # Grid (None = empty, otherwise color tuple)
            self.grid = [[None for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]

            # Current and next pieces
            self.current_piece = None
            self.next_piece = None
            self.held_piece = None
            self.can_hold = True

            # Game state
            self.state = STATE_PLAYING
            self.target_lines = target_lines
            self.time_limit = time_limit  # None = no limit
            self.time_elapsed = 0

            # Scoring
            self.score = 0
            self.lines_cleared = 0
            self.level = 1
            self.combo = 0

            # Timing
            self.fall_timer = 0
            self.fall_interval = 1000  # ms between falls
            self.lock_timer = 0
            self.lock_delay = 500
            self.das_timer = 0  # Delayed auto-shift
            self.das_delay = 150
            self.das_repeat = 50
            self.das_active = False
            self.das_direction = 0

            # Input state
            self.key_left = False
            self.key_right = False
            self.key_down = False

            # Effects
            self.effects = []
            self.gear_rotation = 0

            # Spawn first pieces
            self.spawn_piece()
            self.next_piece = self.random_piece()

        def random_piece(self):
            """Get a random tetromino type."""
            return Piece(random.choice(list(TETROMINOES.keys())))

        def spawn_piece(self):
            """Spawn a new piece at the top."""
            if self.next_piece:
                self.current_piece = self.next_piece
            else:
                self.current_piece = self.random_piece()
            self.next_piece = self.random_piece()
            self.can_hold = True
            self.lock_timer = 0

            # Check game over
            if not self.current_piece.is_valid_position(self.grid):
                self.state = STATE_GAMEOVER

        def hold_piece(self):
            """Swap current piece with held piece."""
            if not self.can_hold:
                return

            self.can_hold = False
            if self.held_piece:
                self.current_piece, self.held_piece = self.held_piece, self.current_piece
                self.current_piece.x = GRID_COLS // 2 - 2
                self.current_piece.y = 0
                self.current_piece.rotation = 0
            else:
                self.held_piece = self.current_piece
                self.spawn_piece()

        def lock_piece(self):
            """Lock the current piece into the grid."""
            piece = self.current_piece
            for bx, by in piece.get_blocks():
                if 0 <= by < GRID_ROWS and 0 <= bx < GRID_COLS:
                    self.grid[by][bx] = piece.data['color']

            # Check for line clears
            lines_to_clear = []
            for row in range(GRID_ROWS):
                if all(self.grid[row][col] is not None for col in range(GRID_COLS)):
                    lines_to_clear.append(row)

            if lines_to_clear:
                self.clear_lines(lines_to_clear)
            else:
                self.combo = 0

            self.spawn_piece()

        def clear_lines(self, rows):
            """Clear completed lines."""
            # Add effects
            for row in rows:
                self.effects.append(LineClearEffect(row))

            # Update score
            lines = len(rows)
            self.lines_cleared += lines
            self.combo += 1

            # Scoring: 100/300/500/800 for 1/2/3/4 lines
            base_points = {1: 100, 2: 300, 3: 500, 4: 800}.get(lines, 800)
            self.score += base_points * self.level * self.combo

            # Remove lines - delete all rows first, then add new empty rows at top
            for row in sorted(rows, reverse=True):
                del self.grid[row]
            
            # Add new empty rows at the top for each cleared line
            for _ in range(len(rows)):
                self.grid.insert(0, [None for _ in range(GRID_COLS)])

            # Level up
            new_level = self.lines_cleared // 10 + 1
            if new_level > self.level:
                self.level = new_level
                self.fall_interval = max(100, 1000 - (self.level - 1) * 100)

            # Check victory
            if self.target_lines and self.lines_cleared >= self.target_lines:
                self.state = STATE_VICTORY

        def hard_drop(self):
            """Instantly drop piece to bottom."""
            drop_distance = 0
            while self.current_piece.move(0, 1, self.grid):
                drop_distance += 1
            self.score += drop_distance * 2
            self.lock_piece()

        def update(self, dt):
            if self.state != STATE_PLAYING:
                return

            # Update time
            self.time_elapsed += dt
            if self.time_limit and self.time_elapsed >= self.time_limit * 1000:
                self.state = STATE_GAMEOVER

            # Update visual effects
            self.gear_rotation += dt * 0.02
            self.effects = [e for e in self.effects if e.update(dt)]

            # Update piece glow
            if self.current_piece:
                self.current_piece.glow_phase += dt * 0.005

            # Handle DAS (delayed auto-shift)
            if self.key_left or self.key_right:
                self.das_timer += dt
                direction = -1 if self.key_left else 1
                if self.das_direction != direction:
                    self.das_timer = 0
                    self.das_direction = direction
                    self.das_active = False
                    self.current_piece.move(direction, 0, self.grid)

                if not self.das_active and self.das_timer >= self.das_delay:
                    self.das_active = True
                    self.das_timer = 0
                elif self.das_active and self.das_timer >= self.das_repeat:
                    self.das_timer = 0
                    self.current_piece.move(direction, 0, self.grid)
            else:
                self.das_timer = 0
                self.das_active = False
                self.das_direction = 0

            # Soft drop
            fall_interval = self.fall_interval // 20 if self.key_down else self.fall_interval

            # Auto fall
            self.fall_timer += dt
            if self.fall_timer >= fall_interval:
                self.fall_timer = 0
                if not self.current_piece.move(0, 1, self.grid):
                    # Piece can't move down, start lock delay
                    self.lock_timer += fall_interval
                    if self.lock_timer >= self.lock_delay:
                        self.lock_piece()
                else:
                    self.lock_timer = 0
                    if self.key_down:
                        self.score += 1

        def handle_key_down(self, key):
            if self.state != STATE_PLAYING:
                return

            if key == K_LEFT:
                self.key_left = True
            elif key == K_RIGHT:
                self.key_right = True
            elif key == K_DOWN:
                self.key_down = True
            elif key == K_UP or key == K_x:
                self.current_piece.rotate(self.grid, 1)
            elif key == K_z:
                self.current_piece.rotate(self.grid, -1)
            elif key == K_SPACE:
                self.hard_drop()
            elif key == K_c or key == K_LSHIFT:
                self.hold_piece()

        def handle_key_up(self, key):
            if key == K_LEFT:
                self.key_left = False
            elif key == K_RIGHT:
                self.key_right = False
            elif key == K_DOWN:
                self.key_down = False

        def draw(self, surf):
            time_ms = pygame.time.get_ticks()

            # Draw decorative gears in background
            self.draw_gears(surf, time_ms)

            # Draw grid background
            self.draw_grid_bg(surf)

            # Draw ghost piece
            if self.current_piece and self.state == STATE_PLAYING:
                self.draw_ghost(surf)

            # Draw placed blocks
            self.draw_blocks(surf, time_ms)

            # Draw current piece
            if self.current_piece and self.state == STATE_PLAYING:
                self.draw_piece(surf, self.current_piece, GRID_OFFSET_X, GRID_OFFSET_Y, time_ms)

            # Draw effects
            for effect in self.effects:
                effect.draw(surf)

            # Draw UI panels
            self.draw_ui(surf, time_ms)

            # Draw overlays
            if self.state == STATE_GAMEOVER:
                self.draw_overlay(surf, "GAME OVER", (255, 100, 100), f"Lines: {self.lines_cleared}")
            elif self.state == STATE_VICTORY:
                self.draw_overlay(surf, "CLOCKWORK RESTORED!", (100, 255, 150), f"Score: {self.score}")

        def draw_gears(self, surf, time_ms):
            """Draw decorative spinning gears in background."""
            gear_positions = [
                (200, 200, 100, 12),
                (150, 500, 60, 8),
                (250, 750, 80, 10),
                (WIDTH - 200, 300, 90, 11),
                (WIDTH - 180, 600, 70, 9),
                (WIDTH - 250, 850, 110, 13),
            ]

            for gx, gy, radius, teeth in gear_positions:
                # Alternate rotation direction
                rotation = self.gear_rotation * (1 if teeth % 2 == 0 else -1)

                gear_surf = pygame.Surface((radius * 2 + 40, radius * 2 + 40), pygame.SRCALPHA)
                cx, cy = radius + 20, radius + 20

                # Draw gear teeth
                for i in range(teeth):
                    angle = rotation + i * (2 * math.pi / teeth)
                    inner_r = radius - 10
                    outer_r = radius + 10
                    tooth_width = math.pi / teeth * 0.6

                    points = [
                        (cx + math.cos(angle - tooth_width) * inner_r,
                        cy + math.sin(angle - tooth_width) * inner_r),
                        (cx + math.cos(angle - tooth_width * 0.5) * outer_r,
                        cy + math.sin(angle - tooth_width * 0.5) * outer_r),
                        (cx + math.cos(angle + tooth_width * 0.5) * outer_r,
                        cy + math.sin(angle + tooth_width * 0.5) * outer_r),
                        (cx + math.cos(angle + tooth_width) * inner_r,
                        cy + math.sin(angle + tooth_width) * inner_r),
                    ]
                    pygame.draw.polygon(gear_surf, (50, 40, 70, 100), points)

                # Gear body
                pygame.draw.circle(gear_surf, (40, 30, 60, 120), (cx, cy), radius - 10)
                pygame.draw.circle(gear_surf, (60, 50, 80, 100), (cx, cy), radius - 20, 3)

                # Center hole
                pygame.draw.circle(gear_surf, (30, 20, 45, 150), (cx, cy), radius // 4)

                surf.blit(gear_surf, (gx - radius - 20, gy - radius - 20))

        def draw_grid_bg(self, surf):
            """Draw the game grid background."""
            # Main grid area
            grid_width = GRID_COLS * CELL_SIZE
            grid_height = GRID_ROWS * CELL_SIZE

            grid_surf = pygame.Surface((grid_width + 20, grid_height + 20), pygame.SRCALPHA)
            draw_rounded_rect(grid_surf, (20, 15, 35, 220), grid_surf.get_rect(), radius=10)
            draw_rounded_rect(grid_surf, (100, 80, 140), grid_surf.get_rect(), radius=10, width=3)
            surf.blit(grid_surf, (GRID_OFFSET_X - 10, GRID_OFFSET_Y - 10))

            # Grid lines
            for row in range(GRID_ROWS + 1):
                y = GRID_OFFSET_Y + row * CELL_SIZE
                pygame.draw.line(surf, (50, 40, 70), (GRID_OFFSET_X, y), (GRID_OFFSET_X + grid_width, y), 1)
            for col in range(GRID_COLS + 1):
                x = GRID_OFFSET_X + col * CELL_SIZE
                pygame.draw.line(surf, (50, 40, 70), (x, GRID_OFFSET_Y), (x, GRID_OFFSET_Y + grid_height), 1)

        def draw_ghost(self, surf):
            """Draw ghost piece showing where current piece will land."""
            ghost_blocks = self.current_piece.get_ghost_blocks(self.grid)
            color = self.current_piece.data['color']

            for bx, by in ghost_blocks:
                if by >= 0:
                    x = GRID_OFFSET_X + bx * CELL_SIZE
                    y = GRID_OFFSET_Y + by * CELL_SIZE
                    ghost_surf = pygame.Surface((CELL_SIZE - 2, CELL_SIZE - 2), pygame.SRCALPHA)
                    draw_rounded_rect(ghost_surf, (*color, 50), ghost_surf.get_rect(), radius=4)
                    draw_rounded_rect(ghost_surf, (*color, 100), ghost_surf.get_rect(), radius=4, width=2)
                    surf.blit(ghost_surf, (x + 1, y + 1))

        def draw_blocks(self, surf, time_ms):
            """Draw placed blocks on the grid."""
            for row in range(GRID_ROWS):
                for col in range(GRID_COLS):
                    color = self.grid[row][col]
                    if color:
                        x = GRID_OFFSET_X + col * CELL_SIZE
                        y = GRID_OFFSET_Y + row * CELL_SIZE
                        self.draw_block(surf, x, y, color, time_ms)

        def draw_block(self, surf, x, y, color, time_ms, glow_phase=0):
            """Draw a single block."""
            block_surf = pygame.Surface((CELL_SIZE - 2, CELL_SIZE - 2), pygame.SRCALPHA)

            # Main block
            draw_rounded_rect(block_surf, color, block_surf.get_rect(), radius=4)

            # Highlight
            highlight = tuple(min(255, c + 40) for c in color)
            draw_rounded_rect(block_surf, highlight, (2, 2, CELL_SIZE - 10, CELL_SIZE // 3), radius=2)

            # Shadow
            shadow = tuple(max(0, c - 40) for c in color)
            draw_rounded_rect(block_surf, shadow, (2, CELL_SIZE - 12, CELL_SIZE - 10, 6), radius=2)

            surf.blit(block_surf, (x + 1, y + 1))

        def draw_piece(self, surf, piece, offset_x, offset_y, time_ms, scale=1.0):
            """Draw a tetromino piece."""
            color = piece.data['color']
            glow = piece.data['glow']

            # Glow effect
            glow_intensity = 0.5 + 0.3 * math.sin(piece.glow_phase)

            for bx, by in piece.get_blocks():
                if by >= 0:
                    x = offset_x + bx * CELL_SIZE * scale
                    y = offset_y + by * CELL_SIZE * scale

                    # Glow
                    glow_size = int(CELL_SIZE * scale * 0.3)
                    glow_surf = pygame.Surface((int(CELL_SIZE * scale) + glow_size * 2,
                                                int(CELL_SIZE * scale) + glow_size * 2), pygame.SRCALPHA)
                    glow_alpha = int(80 * glow_intensity)
                    draw_rounded_rect(glow_surf, (*glow, glow_alpha), glow_surf.get_rect(), radius=8)
                    surf.blit(glow_surf, (x - glow_size, y - glow_size))

                    self.draw_block(surf, x, y, color, time_ms, piece.glow_phase)

        def draw_ui(self, surf, time_ms):
            """Draw UI panels."""
            font_large = pygame.font.Font(None, 48)
            font_medium = pygame.font.Font(None, 36)
            font_small = pygame.font.Font(None, 28)

            # Next piece panel (right)
            panel_x = GRID_OFFSET_X + GRID_COLS * CELL_SIZE + 40
            panel_y = GRID_OFFSET_Y

            next_panel = pygame.Surface((180, 200), pygame.SRCALPHA)
            draw_rounded_rect(next_panel, (30, 20, 50, 200), next_panel.get_rect(), radius=10)
            draw_rounded_rect(next_panel, (100, 80, 140), next_panel.get_rect(), radius=10, width=2)
            surf.blit(next_panel, (panel_x, panel_y))

            next_label = font_medium.render("NEXT", True, (200, 180, 255))
            surf.blit(next_label, (panel_x + 60, panel_y + 15))

            # Draw next piece
            if self.next_piece:
                # Center the piece preview
                preview_x = panel_x + 30
                preview_y = panel_y + 60
                self.next_piece.glow_phase = self.current_piece.glow_phase if self.current_piece else 0
                for bx, by in self.next_piece.data['rotations'][0]:
                    x = preview_x + bx * 30
                    y = preview_y + by * 30
                    color = self.next_piece.data['color']
                    block_surf = pygame.Surface((28, 28), pygame.SRCALPHA)
                    draw_rounded_rect(block_surf, color, block_surf.get_rect(), radius=3)
                    surf.blit(block_surf, (x, y))

            # Hold piece panel (left)
            hold_x = GRID_OFFSET_X - 220
            hold_panel = pygame.Surface((180, 200), pygame.SRCALPHA)
            draw_rounded_rect(hold_panel, (30, 20, 50, 200), hold_panel.get_rect(), radius=10)
            draw_rounded_rect(hold_panel, (100, 80, 140), hold_panel.get_rect(), radius=10, width=2)
            surf.blit(hold_panel, (hold_x, panel_y))

            hold_label = font_medium.render("HOLD", True, (200, 180, 255))
            surf.blit(hold_label, (hold_x + 55, panel_y + 15))

            if self.held_piece:
                preview_x = hold_x + 30
                preview_y = panel_y + 60
                for bx, by in self.held_piece.data['rotations'][0]:
                    x = preview_x + bx * 30
                    y = preview_y + by * 30
                    color = self.held_piece.data['color']
                    alpha = 255 if self.can_hold else 100
                    block_surf = pygame.Surface((28, 28), pygame.SRCALPHA)
                    draw_rounded_rect(block_surf, (*color, alpha), block_surf.get_rect(), radius=3)
                    surf.blit(block_surf, (x, y))

            # Score panel
            score_y = panel_y + 220
            score_panel = pygame.Surface((180, 280), pygame.SRCALPHA)
            draw_rounded_rect(score_panel, (30, 20, 50, 200), score_panel.get_rect(), radius=10)
            draw_rounded_rect(score_panel, (100, 80, 140), score_panel.get_rect(), radius=10, width=2)
            surf.blit(score_panel, (panel_x, score_y))

            # Score
            score_label = font_small.render("SCORE", True, (180, 160, 220))
            surf.blit(score_label, (panel_x + 55, score_y + 15))
            score_text = font_large.render(f"{self.score}", True, (255, 255, 255))
            surf.blit(score_text, (panel_x + 90 - score_text.get_width() // 2, score_y + 40))

            # Lines
            lines_label = font_small.render("LINES", True, (180, 160, 220))
            surf.blit(lines_label, (panel_x + 60, score_y + 90))
            lines_text = font_large.render(f"{self.lines_cleared}", True, (255, 255, 255))
            surf.blit(lines_text, (panel_x + 90 - lines_text.get_width() // 2, score_y + 115))

            if self.target_lines:
                target_text = font_small.render(f"/ {self.target_lines}", True, (150, 130, 190))
                surf.blit(target_text, (panel_x + 90 + lines_text.get_width() // 2 + 5, score_y + 125))

            # Level
            level_label = font_small.render("LEVEL", True, (180, 160, 220))
            surf.blit(level_label, (panel_x + 58, score_y + 165))
            level_text = font_large.render(f"{self.level}", True, (255, 220, 100))
            surf.blit(level_text, (panel_x + 90 - level_text.get_width() // 2, score_y + 190))

            # Time (if time limit)
            if self.time_limit:
                remaining = max(0, self.time_limit - self.time_elapsed / 1000)
                time_label = font_small.render("TIME", True, (180, 160, 220))
                surf.blit(time_label, (panel_x + 65, score_y + 235))
                time_color = (255, 255, 255) if remaining > 30 else (255, 100, 100)
                time_text = font_large.render(f"{int(remaining)}", True, time_color)
                surf.blit(time_text, (panel_x + 90 - time_text.get_width() // 2, score_y + 255))

            # Controls hint (left panel)
            controls_y = panel_y + 220
            controls_panel = pygame.Surface((180, 280), pygame.SRCALPHA)
            draw_rounded_rect(controls_panel, (30, 20, 50, 200), controls_panel.get_rect(), radius=10)
            draw_rounded_rect(controls_panel, (100, 80, 140), controls_panel.get_rect(), radius=10, width=2)
            surf.blit(controls_panel, (hold_x, controls_y))

            controls_label = font_small.render("CONTROLS", True, (180, 160, 220))
            surf.blit(controls_label, (hold_x + 40, controls_y + 15))

            control_texts = [
                "← → Move",
                "↓ Soft Drop",
                "↑ Rotate",
                "SPACE Hard Drop",
                "C Hold",
            ]
            for i, text in enumerate(control_texts):
                ctrl_text = font_small.render(text, True, (150, 140, 180))
                surf.blit(ctrl_text, (hold_x + 20, controls_y + 50 + i * 35))

        def draw_overlay(self, surf, title, color, subtitle):
            """Draw end game overlay."""
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 200))
            surf.blit(overlay, (0, 0))

            font_title = pygame.font.Font(None, 96)
            font_sub = pygame.font.Font(None, 48)

            title_text = font_title.render(title, True, color)
            surf.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 2 - 80))

            sub_text = font_sub.render(subtitle, True, (255, 255, 255))
            surf.blit(sub_text, (WIDTH // 2 - sub_text.get_width() // 2, HEIGHT // 2))

            prompt = font_sub.render("Press ENTER to continue", True, (180, 160, 220))
            surf.blit(prompt, (WIDTH // 2 - prompt.get_width() // 2, HEIGHT // 2 + 80))


# Ren'Py Displayable wrapper
init python:
    class ClockworkTetrisDisplayable(renpy.Displayable):
        """Ren'Py displayable wrapper for Clockwork Tetris."""

        def __init__(self, target_lines=20, time_limit=None, **kwargs):
            super(ClockworkTetrisDisplayable, self).__init__(**kwargs)
            self.target_lines = target_lines
            self.time_limit = time_limit
            self.game = None
            self.last_time = None

        def render(self, width, height, st, at):
            import pygame

            if self.game is None:
                self.game = clockwork_tetris.TetrisGame(self.target_lines, self.time_limit)
                self.last_time = pygame.time.get_ticks()

            current_time = pygame.time.get_ticks()
            dt = current_time - self.last_time
            self.last_time = current_time

            self.game.update(dt)

            render = renpy.Render(clockwork_tetris.WIDTH, clockwork_tetris.HEIGHT)
            canvas = render.canvas()
            canvas.rect((25, 18, 40), (0, 0, clockwork_tetris.WIDTH, clockwork_tetris.HEIGHT))
            self.game.draw(canvas.get_surface())

            renpy.redraw(self, 0)
            return render

        def event(self, ev, x, y, st):
            import pygame

            if self.game is None:
                return None

            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    return "quit"
                if ev.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    if self.game.state == clockwork_tetris.STATE_VICTORY:
                        return "victory"
                    elif self.game.state == clockwork_tetris.STATE_GAMEOVER:
                        return "retry"
                else:
                    self.game.handle_key_down(ev.key)

            elif ev.type == pygame.KEYUP:
                self.game.handle_key_up(ev.key)

            return None

        def visit(self):
            return []


# Screen
screen clockwork_tetris_screen(target_lines=20, time_limit=None):
    default game_display = ClockworkTetrisDisplayable(target_lines, time_limit)

    add Solid("#19122d")
    add game_display

    key "K_ESCAPE" action Return("quit")


# Entry label
label clockwork_tetris_start(target_lines=20, time_limit=None):
    $ quick_menu = False

    # Start minigame music
    $ clockwork_tetris.start_music()

    call screen clockwork_tetris_screen(target_lines, time_limit)

    # Stop minigame music
    $ clockwork_tetris.stop_music()

    $ quick_menu = True
    $ result = _return

    if result == "victory":
        return True
    else:
        return False


# Test label
label test_clockwork_tetris:
    "Starting Clockwork Tetris..."
    "Clear 20 lines to restore the clockwork!"

    call clockwork_tetris_start(target_lines=20)

    if _return:
        "The gears are turning again!"
    else:
        "The clockwork remains broken..."

    return
