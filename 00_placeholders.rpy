# 00_placeholders.rpy - Procedural Placeholder System
# Generates visual placeholders when image files are missing
# This allows playtesting without requiring all media assets

init -100 python:
    import math
    import hashlib

    # ============================================================================
    # PYGAME_SDL2 COMPATIBLE ROUNDED RECTANGLE
    # ============================================================================
    # pygame_sdl2 (used by Ren'Py) doesn't support border_radius parameter
    # This helper function draws rounded rectangles manually

    def draw_rounded_rect(surface, color, rect, radius=0, width=0):
        """
        Draw a rounded rectangle compatible with pygame_sdl2.

        Args:
            surface: pygame surface to draw on
            color: color tuple (R, G, B) or (R, G, B, A)
            rect: (x, y, width, height) or pygame.Rect
            radius: corner radius (default 0 = sharp corners)
            width: border width (0 = filled, >0 = outline only)
        """
        import pygame

        # Handle rect input
        if isinstance(rect, pygame.Rect):
            x, y, w, h = rect.x, rect.y, rect.width, rect.height
        else:
            x, y, w, h = rect

        # Clamp radius to half of smallest dimension
        radius = min(radius, w // 2, h // 2)

        if radius <= 0:
            # No rounding, just draw regular rect
            pygame.draw.rect(surface, color, (x, y, w, h), width)
            return

        if width == 0:
            # Filled rounded rectangle
            # Draw center rectangle
            pygame.draw.rect(surface, color, (x + radius, y, w - 2 * radius, h))
            # Draw side rectangles
            pygame.draw.rect(surface, color, (x, y + radius, w, h - 2 * radius))
            # Draw four corner circles
            pygame.draw.circle(surface, color, (x + radius, y + radius), radius)
            pygame.draw.circle(surface, color, (x + w - radius, y + radius), radius)
            pygame.draw.circle(surface, color, (x + radius, y + h - radius), radius)
            pygame.draw.circle(surface, color, (x + w - radius, y + h - radius), radius)
        else:
            # Outlined rounded rectangle
            # Draw four corner arcs (using circles with width)
            pygame.draw.circle(surface, color, (x + radius, y + radius), radius, width)
            pygame.draw.circle(surface, color, (x + w - radius, y + radius), radius, width)
            pygame.draw.circle(surface, color, (x + radius, y + h - radius), radius, width)
            pygame.draw.circle(surface, color, (x + w - radius, y + h - radius), radius, width)
            # Draw four straight lines
            pygame.draw.line(surface, color, (x + radius, y), (x + w - radius, y), width)
            pygame.draw.line(surface, color, (x + radius, y + h - 1), (x + w - radius, y + h - 1), width)
            pygame.draw.line(surface, color, (x, y + radius), (x, y + h - radius), width)
            pygame.draw.line(surface, color, (x + w - 1, y + radius), (x + w - 1, y + h - radius), width)

    # Register function globally so minigames can access it
    renpy.store.draw_rounded_rect = draw_rounded_rect
    # Also add to Python builtins for universal access
    import builtins
    builtins.draw_rounded_rect = draw_rounded_rect

    # ============================================================================
    # PYGAME_SDL2 COMPATIBLE ARC DRAWING
    # ============================================================================
    # pygame_sdl2 doesn't implement pygame.draw.arc
    # This helper function draws arcs using line segments

    def draw_arc(surface, color, rect, start_angle, stop_angle, width=1):
        """
        Draw an arc compatible with pygame_sdl2.

        Args:
            surface: pygame surface to draw on
            color: color tuple (R, G, B) or (R, G, B, A)
            rect: (x, y, width, height) or pygame.Rect - bounding box of the ellipse
            start_angle: start angle in radians
            stop_angle: stop angle in radians
            width: line width (default 1)
        """
        import pygame

        # Handle rect input
        if isinstance(rect, pygame.Rect):
            x, y, w, h = rect.x, rect.y, rect.width, rect.height
        else:
            x, y, w, h = rect

        # Calculate center and radii
        cx = x + w / 2
        cy = y + h / 2
        rx = w / 2
        ry = h / 2

        # Number of segments based on arc length
        angle_diff = abs(stop_angle - start_angle)
        num_segments = max(8, int(angle_diff * max(rx, ry) / 4))

        # Generate points along the arc
        points = []
        for i in range(num_segments + 1):
            angle = start_angle + (stop_angle - start_angle) * i / num_segments
            px = cx + rx * math.cos(angle)
            py = cy - ry * math.sin(angle)  # Negative because pygame Y is inverted
            points.append((int(px), int(py)))

        # Draw lines between consecutive points
        if len(points) >= 2:
            for i in range(len(points) - 1):
                pygame.draw.line(surface, color, points[i], points[i + 1], width)

    # Register arc function globally
    renpy.store.draw_arc = draw_arc
    builtins.draw_arc = draw_arc

    # ============================================================================
    # RENPY-COMPATIBLE FONT CLASS
    # ============================================================================
    # pygame_sdl2 doesn't include pygame.font module
    # This class mimics pygame.font.Font using Ren'Py's text rendering

    class RenpyFont:
        """A pygame.font.Font compatible class using Ren'Py's text rendering."""

        # Simple bitmap font data (5x7 pixel characters)
        CHAR_WIDTH = 6
        CHAR_HEIGHT = 9

        def __init__(self, font_name, size):
            """Initialize font with given size."""
            self.size = size
            self.scale = max(1, size // 12)  # Scale factor based on requested size

        def render(self, text, antialias, color, background=None):
            """
            Render text to a pygame surface.

            Args:
                text: The text to render
                antialias: Ignored (we use simple rendering)
                color: RGB or RGBA tuple
                background: Optional background color (ignored)

            Returns:
                pygame surface with rendered text
            """
            import pygame

            if not text:
                surf = pygame.Surface((1, self.size), pygame.SRCALPHA)
                return surf

            # Calculate dimensions
            char_w = self.CHAR_WIDTH * self.scale
            char_h = self.CHAR_HEIGHT * self.scale
            width = len(text) * char_w
            height = max(char_h, self.size)

            # Create surface
            surf = pygame.Surface((width, height), pygame.SRCALPHA)

            # Handle color with alpha
            if len(color) == 3:
                color = (color[0], color[1], color[2], 255)

            # Draw each character
            x = 0
            for char in text:
                self._draw_char(surf, char, x, (height - char_h) // 2, color)
                x += char_w

            return surf

        def _draw_char(self, surf, char, x, y, color):
            """Draw a single character using simple bitmap patterns."""
            import pygame

            s = self.scale  # Shorthand for scale
            c = char.upper()

            # Define simple 5x7 bitmap patterns for common characters
            patterns = {
                'A': [(1,1,3), (0,2,1), (4,2,1), (0,3,5), (0,4,1), (4,4,1), (0,5,1), (4,5,1), (0,6,1), (4,6,1)],
                'B': [(0,1,4), (0,2,1), (4,2,1), (0,3,4), (0,4,1), (4,4,1), (0,5,1), (4,5,1), (0,6,4)],
                'C': [(1,1,3), (0,2,1), (0,3,1), (0,4,1), (0,5,1), (1,6,3)],
                'D': [(0,1,3), (0,2,1), (3,2,1), (0,3,1), (4,3,1), (0,4,1), (4,4,1), (0,5,1), (3,5,1), (0,6,3)],
                'E': [(0,1,5), (0,2,1), (0,3,4), (0,4,1), (0,5,1), (0,6,5)],
                'F': [(0,1,5), (0,2,1), (0,3,4), (0,4,1), (0,5,1), (0,6,1)],
                'G': [(1,1,3), (0,2,1), (0,3,1), (0,4,1), (2,4,3), (0,5,1), (4,5,1), (1,6,3)],
                'H': [(0,1,1), (4,1,1), (0,2,1), (4,2,1), (0,3,5), (0,4,1), (4,4,1), (0,5,1), (4,5,1), (0,6,1), (4,6,1)],
                'I': [(1,1,3), (2,2,1), (2,3,1), (2,4,1), (2,5,1), (1,6,3)],
                'J': [(3,1,2), (4,2,1), (4,3,1), (4,4,1), (0,5,1), (4,5,1), (1,6,3)],
                'K': [(0,1,1), (4,1,1), (0,2,1), (3,2,1), (0,3,3), (0,4,1), (3,4,1), (0,5,1), (4,5,1), (0,6,1), (4,6,1)],
                'L': [(0,1,1), (0,2,1), (0,3,1), (0,4,1), (0,5,1), (0,6,5)],
                'M': [(0,1,1), (4,1,1), (0,2,2), (3,2,2), (0,3,1), (2,3,1), (4,3,1), (0,4,1), (4,4,1), (0,5,1), (4,5,1), (0,6,1), (4,6,1)],
                'N': [(0,1,1), (4,1,1), (0,2,2), (4,2,1), (0,3,1), (2,3,1), (4,3,1), (0,4,1), (3,4,2), (0,5,1), (4,5,1), (0,6,1), (4,6,1)],
                'O': [(1,1,3), (0,2,1), (4,2,1), (0,3,1), (4,3,1), (0,4,1), (4,4,1), (0,5,1), (4,5,1), (1,6,3)],
                'P': [(0,1,4), (0,2,1), (4,2,1), (0,3,4), (0,4,1), (0,5,1), (0,6,1)],
                'Q': [(1,1,3), (0,2,1), (4,2,1), (0,3,1), (4,3,1), (0,4,1), (4,4,1), (0,5,1), (3,5,1), (1,6,2), (4,6,1)],
                'R': [(0,1,4), (0,2,1), (4,2,1), (0,3,4), (0,4,1), (3,4,1), (0,5,1), (4,5,1), (0,6,1), (4,6,1)],
                'S': [(1,1,4), (0,2,1), (1,3,3), (4,4,1), (4,5,1), (0,6,4)],
                'T': [(0,1,5), (2,2,1), (2,3,1), (2,4,1), (2,5,1), (2,6,1)],
                'U': [(0,1,1), (4,1,1), (0,2,1), (4,2,1), (0,3,1), (4,3,1), (0,4,1), (4,4,1), (0,5,1), (4,5,1), (1,6,3)],
                'V': [(0,1,1), (4,1,1), (0,2,1), (4,2,1), (0,3,1), (4,3,1), (1,4,1), (3,4,1), (1,5,1), (3,5,1), (2,6,1)],
                'W': [(0,1,1), (4,1,1), (0,2,1), (4,2,1), (0,3,1), (2,3,1), (4,3,1), (0,4,1), (2,4,1), (4,4,1), (0,5,2), (3,5,2), (0,6,1), (4,6,1)],
                'X': [(0,1,1), (4,1,1), (1,2,1), (3,2,1), (2,3,1), (2,4,1), (1,5,1), (3,5,1), (0,6,1), (4,6,1)],
                'Y': [(0,1,1), (4,1,1), (1,2,1), (3,2,1), (2,3,1), (2,4,1), (2,5,1), (2,6,1)],
                'Z': [(0,1,5), (4,2,1), (3,3,1), (2,4,1), (1,5,1), (0,6,5)],
                '0': [(1,1,3), (0,2,1), (4,2,1), (0,3,1), (3,3,2), (0,4,2), (4,4,1), (0,5,1), (4,5,1), (1,6,3)],
                '1': [(2,1,1), (1,2,2), (2,3,1), (2,4,1), (2,5,1), (1,6,3)],
                '2': [(1,1,3), (0,2,1), (4,2,1), (3,3,1), (2,4,1), (1,5,1), (0,6,5)],
                '3': [(1,1,3), (4,2,1), (2,3,2), (4,4,1), (0,5,1), (4,5,1), (1,6,3)],
                '4': [(0,1,1), (3,1,1), (0,2,1), (3,2,1), (0,3,1), (3,3,1), (0,4,5), (3,5,1), (3,6,1)],
                '5': [(0,1,5), (0,2,1), (0,3,4), (4,4,1), (4,5,1), (0,6,4)],
                '6': [(1,1,3), (0,2,1), (0,3,4), (0,4,1), (4,4,1), (0,5,1), (4,5,1), (1,6,3)],
                '7': [(0,1,5), (4,2,1), (3,3,1), (2,4,1), (2,5,1), (2,6,1)],
                '8': [(1,1,3), (0,2,1), (4,2,1), (1,3,3), (0,4,1), (4,4,1), (0,5,1), (4,5,1), (1,6,3)],
                '9': [(1,1,3), (0,2,1), (4,2,1), (0,3,1), (4,3,1), (1,4,4), (4,5,1), (1,6,3)],
                ' ': [],
                '.': [(2,5,1), (2,6,1)],
                ',': [(2,5,1), (1,6,1)],
                ':': [(2,2,1), (2,5,1)],
                '!': [(2,1,1), (2,2,1), (2,3,1), (2,4,1), (2,6,1)],
                '?': [(1,1,3), (4,2,1), (3,3,1), (2,4,1), (2,6,1)],
                '-': [(1,3,3)],
                '+': [(2,2,1), (1,3,3), (2,4,1)],
                '/': [(4,1,1), (3,2,1), (2,3,1), (1,4,1), (0,5,1)],
                '(': [(3,1,1), (2,2,1), (2,3,1), (2,4,1), (2,5,1), (3,6,1)],
                ')': [(1,1,1), (2,2,1), (2,3,1), (2,4,1), (2,5,1), (1,6,1)],
                'x': [(0,2,1), (4,2,1), (1,3,1), (3,3,1), (2,4,1), (1,5,1), (3,5,1), (0,6,1), (4,6,1)],
            }

            # Default pattern for unknown characters
            default = [(0,1,5), (0,2,1), (4,2,1), (0,3,1), (4,3,1), (0,4,1), (4,4,1), (0,5,1), (4,5,1), (0,6,5)]

            pattern = patterns.get(c, default)
            for px, py, pw in pattern:
                pygame.draw.rect(surf, color, (x + px * s, y + py * s, pw * s, s))

        def get_height(self):
            """Return the font height."""
            return self.size

    # Create a mock pygame.font module
    class MockPygameFont:
        """Mock pygame.font module that uses RenpyFont."""
        Font = RenpyFont

        @staticmethod
        def init():
            pass

        @staticmethod
        def get_init():
            return True

    # Patch pygame.font with our mock
    import pygame
    pygame.font = MockPygameFont()

    # Register the font class globally
    renpy.store.RenpyFont = RenpyFont
    builtins.RenpyFont = RenpyFont

    # ============================================================================
    # PLACEHOLDER COLOR SCHEMES
    # ============================================================================

    # Background colors by region/type
    PLACEHOLDER_BG_COLORS = {
        "bedroom": ("#1a1a2e", "#16213e"),      # Dark blue night
        "library": ("#2d1b4e", "#4a2c6e"),      # Purple mystical
        "valley": ("#1a3d1a", "#2d5a2d"),       # Forest green
        "conservatory": ("#3d1a4a", "#5a2d6e"), # Crystal purple
        "clocktower": ("#3d2a1a", "#5a4a2d"),   # Bronze/brass
        "skybridge": ("#1a2a4a", "#2d4a6e"),    # Sky blue
        "hub": ("#2a1a3a", "#4a2d5a"),          # Crossroads purple
        "living": ("#3a2a1a", "#5a4a3a"),       # Warm brown
        "act_2": ("#1a1a3a", "#2a2a5a"),        # Transition blue
        "default": ("#2a2a2a", "#4a4a4a"),      # Gray default
    }

    # Character colors
    PLACEHOLDER_CHAR_COLORS = {
        "tristan": "#b20000",      # Red
        "t": "#b20000",
        "henry": "#6bb5ff",        # Blue
        "h": "#6bb5ff",
        "pipwick": "#ffd700",      # Gold
        "p": "#ffd700",
        "kayla": "#95d5b2",        # Green
        "k": "#95d5b2",
        "ryan": "#e8a87c",         # Orange
        "r": "#e8a87c",
        "lauren": "#f4acb7",       # Pink
        "l": "#f4acb7",
        "jeff": "#8ecae6",         # Light blue
        "j": "#8ecae6",
        "gmom": "#ddb892",         # Tan
        "g": "#ddb892",
        "bedimurk": "#6b4c8a",     # Purple
        "b": "#6b4c8a",
        "default": "#888888",      # Gray
    }

    def get_color_for_name(name):
        """Get a consistent color based on a name string."""
        name_lower = name.lower()

        # Check direct matches first
        for key, color in PLACEHOLDER_CHAR_COLORS.items():
            if key in name_lower:
                return color

        # Generate a consistent color from the name hash
        hash_val = int(hashlib.md5(name.encode()).hexdigest()[:6], 16)
        r = (hash_val >> 16) & 0xFF
        g = (hash_val >> 8) & 0xFF
        b = hash_val & 0xFF
        # Ensure it's not too dark
        r = max(100, r)
        g = max(100, g)
        b = max(100, b)
        return "#{:02x}{:02x}{:02x}".format(r, g, b)

    def get_bg_colors_for_name(name):
        """Get gradient colors for a background based on its name."""
        name_lower = name.lower()

        for key, colors in PLACEHOLDER_BG_COLORS.items():
            if key in name_lower:
                return colors

        return PLACEHOLDER_BG_COLORS["default"]


# ============================================================================
# PLACEHOLDER DISPLAYABLE CLASSES
# ============================================================================

init -100 python:

    class PlaceholderBackground(renpy.Displayable):
        """A procedural background placeholder with gradient and label."""

        def __init__(self, name, **kwargs):
            super(PlaceholderBackground, self).__init__(**kwargs)
            self.name = name
            self.colors = get_bg_colors_for_name(name)

        def render(self, width, height, st, at):
            render = renpy.Render(width, height)

            # Create gradient background
            import pygame
            surf = pygame.Surface((width, height), pygame.SRCALPHA)

            color1 = pygame.Color(self.colors[0])
            color2 = pygame.Color(self.colors[1])

            # Vertical gradient
            for y in range(height):
                ratio = y / float(height)
                r = int(color1.r + (color2.r - color1.r) * ratio)
                g = int(color1.g + (color2.g - color1.g) * ratio)
                b = int(color1.b + (color2.b - color1.b) * ratio)
                pygame.draw.line(surf, (r, g, b), (0, y), (width, y))

            # Add decorative elements based on type
            name_lower = self.name.lower()

            if "library" in name_lower:
                # Draw book shapes
                for i in range(5):
                    x = 100 + i * 300
                    pygame.draw.rect(surf, (60, 40, 80), (x, height - 200, 40, 150))
                    pygame.draw.rect(surf, (80, 60, 100), (x + 50, height - 180, 35, 130))

            elif "valley" in name_lower:
                # Draw tree shapes
                for i in range(4):
                    x = 150 + i * 400
                    pygame.draw.polygon(surf, (30, 80, 30), [(x, height - 100), (x - 60, height), (x + 60, height)])
                    pygame.draw.polygon(surf, (40, 100, 40), [(x, height - 200), (x - 50, height - 100), (x + 50, height - 100)])

            elif "conservatory" in name_lower or "crystal" in name_lower:
                # Draw crystal shapes
                for i in range(6):
                    x = 120 + i * 280
                    pygame.draw.polygon(surf, (100, 60, 120, 180), [(x, height - 250), (x - 30, height - 50), (x + 30, height - 50)])

            elif "clocktower" in name_lower or "clock" in name_lower:
                # Draw gear shapes
                cx, cy = width // 2, height // 2
                pygame.draw.circle(surf, (80, 60, 40), (cx, cy), 150, 20)
                pygame.draw.circle(surf, (100, 80, 60), (cx, cy), 80, 15)

            elif "skybridge" in name_lower or "sky" in name_lower:
                # Draw cloud shapes
                for i in range(5):
                    x = 100 + i * 350
                    y = 150 + (i % 3) * 100
                    pygame.draw.ellipse(surf, (255, 255, 255, 60), (x, y, 200, 80))

            elif "hub" in name_lower or "crossroads" in name_lower:
                # Draw path shapes
                pygame.draw.line(surf, (60, 40, 80), (width // 2, 0), (width // 2, height), 40)
                pygame.draw.line(surf, (60, 40, 80), (0, height // 2), (width, height // 2), 40)

            # Draw border
            pygame.draw.rect(surf, (100, 100, 100), (0, 0, width, height), 4)

            # Draw label
            font = pygame.font.Font(None, 48)
            label = "BG: " + self.name
            text_surf = font.render(label, True, (255, 255, 255))
            text_rect = text_surf.get_rect(center=(width // 2, 50))

            # Text background
            bg_rect = text_rect.inflate(20, 10)
            pygame.draw.rect(surf, (0, 0, 0, 180), bg_rect)
            surf.blit(text_surf, text_rect)

            # "PLACEHOLDER" watermark
            font_small = pygame.font.Font(None, 36)
            watermark = font_small.render("[ PLACEHOLDER ]", True, (255, 255, 255, 100))
            surf.blit(watermark, (width // 2 - watermark.get_width() // 2, height - 60))

            render.blit(surf, (0, 0))
            return render

        def visit(self):
            return []


    class PlaceholderCharacter(renpy.Displayable):
        """A procedural character placeholder with silhouette and label."""

        def __init__(self, name, expression="default", **kwargs):
            super(PlaceholderCharacter, self).__init__(**kwargs)
            self.name = name
            self.expression = expression
            self.color = get_color_for_name(name)

        def render(self, width, height, st, at):
            # Standard character sprite size
            char_width = 400
            char_height = 600

            render = renpy.Render(char_width, char_height)

            import pygame
            surf = pygame.Surface((char_width, char_height), pygame.SRCALPHA)

            color = pygame.Color(self.color)
            darker = pygame.Color(
                max(0, color.r - 40),
                max(0, color.g - 40),
                max(0, color.b - 40)
            )

            # Draw body silhouette (simple humanoid shape)
            cx = char_width // 2

            # Head
            pygame.draw.ellipse(surf, color, (cx - 50, 30, 100, 120))

            # Neck
            pygame.draw.rect(surf, color, (cx - 20, 140, 40, 30))

            # Torso
            pygame.draw.polygon(surf, color, [
                (cx - 80, 170),  # Left shoulder
                (cx + 80, 170),  # Right shoulder
                (cx + 60, 380),  # Right hip
                (cx - 60, 380),  # Left hip
            ])

            # Arms
            pygame.draw.polygon(surf, darker, [
                (cx - 80, 170),
                (cx - 120, 320),
                (cx - 100, 330),
                (cx - 70, 200),
            ])
            pygame.draw.polygon(surf, darker, [
                (cx + 80, 170),
                (cx + 120, 320),
                (cx + 100, 330),
                (cx + 70, 200),
            ])

            # Legs
            pygame.draw.polygon(surf, darker, [
                (cx - 50, 380),
                (cx - 60, 580),
                (cx - 20, 580),
                (cx - 10, 380),
            ])
            pygame.draw.polygon(surf, darker, [
                (cx + 50, 380),
                (cx + 60, 580),
                (cx + 20, 580),
                (cx + 10, 380),
            ])

            # Eyes (simple dots)
            pygame.draw.circle(surf, (255, 255, 255), (cx - 20, 80), 12)
            pygame.draw.circle(surf, (255, 255, 255), (cx + 20, 80), 12)
            pygame.draw.circle(surf, (0, 0, 0), (cx - 20, 80), 6)
            pygame.draw.circle(surf, (0, 0, 0), (cx + 20, 80), 6)

            # Draw expression indicator
            if "talking" in self.expression.lower():
                # Open mouth
                pygame.draw.ellipse(surf, (80, 40, 40), (cx - 15, 100, 30, 20))
            elif "smile" in self.expression.lower() or "happy" in self.expression.lower():
                # Smile arc
                draw_arc(surf, (80, 40, 40), (cx - 20, 90, 40, 30), 3.14, 6.28, 3)
            elif "sad" in self.expression.lower() or "worried" in self.expression.lower():
                # Frown arc
                draw_arc(surf, (80, 40, 40), (cx - 20, 105, 40, 20), 0, 3.14, 3)

            # Draw name label at top
            font = pygame.font.Font(None, 28)
            name_text = self.name.upper()
            if self.expression and self.expression != "default":
                name_text += " (" + self.expression + ")"
            text_surf = font.render(name_text, True, (255, 255, 255))
            text_rect = text_surf.get_rect(center=(cx, 15))

            # Background for text
            bg_rect = text_rect.inflate(10, 4)
            pygame.draw.rect(surf, (0, 0, 0, 200), bg_rect)
            surf.blit(text_surf, text_rect)

            render.blit(surf, (0, 0))
            return render

        def visit(self):
            return []


    class PlaceholderTitle(renpy.Displayable):
        """A procedural title screen element placeholder."""

        def __init__(self, name, **kwargs):
            super(PlaceholderTitle, self).__init__(**kwargs)
            self.name = name

        def render(self, width, height, st, at):
            # Full screen size for title elements
            w, h = 1920, 1080

            render = renpy.Render(w, h)

            import pygame
            surf = pygame.Surface((w, h), pygame.SRCALPHA)

            name_lower = self.name.lower()
            cx, cy = w // 2, h // 2

            if "background" in name_lower or "title_bg" in name_lower:
                # Dark starfield background
                for y in range(h):
                    ratio = y / float(h)
                    r = int(10 + 20 * ratio)
                    g = int(5 + 15 * ratio)
                    b = int(30 + 40 * ratio)
                    pygame.draw.line(surf, (r, g, b), (0, y), (w, y))

                # Add stars
                import random
                random.seed(42)  # Consistent stars
                for _ in range(200):
                    sx = random.randint(0, w)
                    sy = random.randint(0, h)
                    brightness = random.randint(100, 255)
                    size = random.choice([1, 1, 1, 2])
                    pygame.draw.circle(surf, (brightness, brightness, brightness), (sx, sy), size)

            elif "beacon" in name_lower:
                # Central glowing beacon
                beacon_y = int(h * 0.45)
                # Outer glow
                for radius in range(150, 30, -10):
                    alpha = int(50 * (1 - radius / 150))
                    pygame.draw.circle(surf, (255, 220, 100, alpha), (cx, beacon_y), radius)
                # Inner beacon
                pygame.draw.circle(surf, (255, 240, 180), (cx, beacon_y), 40)
                pygame.draw.circle(surf, (255, 255, 220), (cx, beacon_y), 25)

            elif "text" in name_lower and "sub" not in name_lower:
                # Main title text
                font = pygame.font.Font(None, 80)
                title = "SPARKS OF THE BEACON"
                text_surf = font.render(title, True, (255, 220, 150))
                text_rect = text_surf.get_rect(center=(cx, int(h * 0.5)))
                # Glow effect
                glow_font = pygame.font.Font(None, 84)
                glow_surf = glow_font.render(title, True, (255, 180, 50, 100))
                glow_rect = glow_surf.get_rect(center=(cx, int(h * 0.5)))
                surf.blit(glow_surf, glow_rect)
                surf.blit(text_surf, text_rect)

            elif "subtitle" in name_lower:
                # Subtitle
                font = pygame.font.Font(None, 40)
                subtitle = "A Twin Sparks Adventure"
                text_surf = font.render(subtitle, True, (200, 200, 220))
                text_rect = text_surf.get_rect(center=(cx, int(h * 0.65)))
                surf.blit(text_surf, text_rect)

            elif "rays" in name_lower:
                # Light rays emanating from center
                beacon_y = int(h * 0.45)
                for i in range(16):
                    angle = i * (3.14159 * 2 / 16) + st * 0.1
                    x2 = cx + int(600 * math.cos(angle))
                    y2 = beacon_y + int(600 * math.sin(angle))
                    pygame.draw.line(surf, (255, 220, 100, 60), (cx, beacon_y), (x2, y2), 8)

            elif "sparks" in name_lower:
                # Floating sparks/particles
                import random
                random.seed(int(st * 10) % 100)
                for i in range(30):
                    sx = random.randint(int(w * 0.2), int(w * 0.8))
                    sy = random.randint(int(h * 0.3), int(h * 0.7))
                    sy += int(math.sin(st + i) * 20)  # Gentle floating
                    size = random.randint(2, 5)
                    brightness = random.randint(180, 255)
                    pygame.draw.circle(surf, (brightness, brightness, 100), (sx, sy), size)

            else:
                # Generic title element
                font = pygame.font.Font(None, 36)
                text_surf = font.render(f"[TITLE: {self.name}]", True, (255, 255, 255))
                text_rect = text_surf.get_rect(center=(cx, cy))
                surf.blit(text_surf, text_rect)

            render.blit(surf, (0, 0))
            if "rays" in name_lower or "sparks" in name_lower:
                renpy.redraw(self, 0.05)  # Animate
            return render

        def visit(self):
            return []


    class PlaceholderEffect(renpy.Displayable):
        """A procedural effect placeholder (for light_burst, rain, etc.)."""

        def __init__(self, name, **kwargs):
            super(PlaceholderEffect, self).__init__(**kwargs)
            self.name = name

        def render(self, width, height, st, at):
            effect_size = 200
            render = renpy.Render(effect_size, effect_size)

            import pygame
            surf = pygame.Surface((effect_size, effect_size), pygame.SRCALPHA)

            cx, cy = effect_size // 2, effect_size // 2

            name_lower = self.name.lower()

            if "light" in name_lower or "burst" in name_lower:
                # Starburst effect
                for i in range(8):
                    angle = i * (3.14159 * 2 / 8) + st
                    x2 = cx + int(80 * math.cos(angle))
                    y2 = cy + int(80 * math.sin(angle))
                    pygame.draw.line(surf, (255, 255, 200, 200), (cx, cy), (x2, y2), 4)
                pygame.draw.circle(surf, (255, 255, 150, 220), (cx, cy), 30)

            elif "rain" in name_lower:
                # Rain drops
                for i in range(20):
                    x = (i * 47 + int(st * 100)) % effect_size
                    y = (i * 31 + int(st * 200)) % effect_size
                    pygame.draw.line(surf, (150, 150, 255, 150), (x, y), (x - 5, y + 20), 2)

            else:
                # Generic sparkle
                pygame.draw.circle(surf, (255, 255, 255, 180), (cx, cy), 20)
                pygame.draw.circle(surf, (255, 255, 200, 100), (cx, cy), 40, 2)

            render.blit(surf, (0, 0))
            renpy.redraw(self, 0.05)  # Animate
            return render

        def visit(self):
            return []


# ============================================================================
# MISSING IMAGE CALLBACK
# ============================================================================

init -99 python:

    def placeholder_missing_image(name):
        """
        Called when Ren'Py can't find an image.
        Returns a placeholder displayable based on the image name.
        """
        name_str = " ".join(name) if isinstance(name, tuple) else str(name)
        name_lower = name_str.lower()

        # Determine type of placeholder needed
        if name_lower.startswith("bg") or "background" in name_lower:
            return PlaceholderBackground(name_str)

        elif name_lower.startswith("title") or "title_" in name_lower:
            return PlaceholderTitle(name_str)

        elif "light_burst" in name_lower or "rain" in name_lower or "effect" in name_lower:
            return PlaceholderEffect(name_str)

        elif any(char in name_lower for char in ["tristan", "henry", "pipwick", "kayla",
                                                   "ryan", "lauren", "jeff", "gmom", "bedimurk",
                                                   " t ", " h ", " p ", " k ", " r ", " l ", " j ", " g ", " b "]):
            # Character sprite
            parts = name_str.split()
            char_name = parts[0] if parts else name_str
            expression = parts[1] if len(parts) > 1 else "default"
            return PlaceholderCharacter(char_name, expression)

        else:
            # Generic placeholder - treat as character
            return PlaceholderCharacter(name_str, "default")

    # Register the callback
    config.missing_image_callback = placeholder_missing_image


# ============================================================================
# IMAGE WRAPPER FUNCTION
# ============================================================================

init -98 python:

    def safe_image(path, fallback_name=None):
        """
        Returns the image at path if it exists, otherwise returns a placeholder.
        Use this for dynamic image loading.
        """
        if renpy.loadable(path):
            return path
        else:
            name = fallback_name or path.split("/")[-1].replace(".png", "").replace("_", " ")
            if "bg" in path.lower():
                return PlaceholderBackground(name)
            elif "character" in path.lower():
                return PlaceholderCharacter(name)
            else:
                return PlaceholderEffect(name)


# ============================================================================
# PLACEHOLDER-AWARE IMAGE DEFINITIONS
# ============================================================================
# These override the standard image definitions to add fallback support

init -97:
    # Light burst placeholder (commonly used effect)
    image light_burst = PlaceholderEffect("light_burst")


# ============================================================================
# DEBUG OVERLAY (optional - toggle with 'p' key in developer mode)
# ============================================================================

init python:

    placeholder_debug_mode = False

    def toggle_placeholder_debug():
        global placeholder_debug_mode
        placeholder_debug_mode = not placeholder_debug_mode
        renpy.restart_interaction()

# Screen to show placeholder status
screen placeholder_debug_overlay():
    if placeholder_debug_mode and config.developer:
        frame:
            xalign 1.0
            yalign 0.0
            xpadding 10
            ypadding 10
            background "#00000080"

            vbox:
                text "PLACEHOLDER MODE" size 20 color "#ff0"
                text "Missing images show as" size 14 color "#fff"
                text "procedural graphics" size 14 color "#fff"
                text "" size 8
                text "Press 'P' to toggle" size 12 color "#aaa"

# Key binding for debug toggle (only in developer mode)
init python:
    if config.developer:
        config.keymap['placeholder_debug'] = ['p']

        def placeholder_debug_action():
            toggle_placeholder_debug()
            return None
