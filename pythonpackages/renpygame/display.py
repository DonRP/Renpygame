from typing import Any, Optional, Union
import renpy.exports as renpy
from pygame_sdl2.display import *

import pythonpackages.renpygame.pygame as pygame


class RenpyGameSurface(renpy.Displayable):
    """pygame: https://www.pygame.org/docs/ref/surface.html
    pygame_sdl2: https://github.com/renpy/pygame_sdl2/blob/48e9c45667152a4ccf98d6d9251eeb3c8858b5f1/src/pygame_sdl2/surface.pyx#L53"""

    def __init__(self, **kwargs):
        # renpy.Displayable init
        super(RenpyGameSurface, self).__init__(**kwargs)

        self.renderMainSurface = renpy.Render(300, 300)

    def blit(
        self,
        source,  # Surface
        dest: tuple[int, int],
        area: Optional[tuple[int, int]] = None,
        special_flags: int = 0
    ):
        # renpy.show_screen(
        #     "rect", left=dest[0], top=dest[1], width=self.size[0], height=self.size[1])
        return self.renderMainSurface.blit(source, (0, 0))

    def render(self, width, height, st, at) -> renpy.Render:
        # Create the render we will return.
        render = renpy.Render(width, width)

        # Create a render from the child.
        child_render = renpy.render(renpy.displayable(
            "background.gif"), width, height, st, at)

        # Get the size of the child.
        self.width, self.height = child_render.get_size()

        # Blit (draw) the child's render to our render.
        render.blit(child_render, (self.left, self.top))

        # Return the render.
        return render


def set_mode(size: tuple[int, int] = (0, 0), flags: int = 0, depth: int = 0, display: int = 0, vsync: int = 0) -> RenpyGameSurface:
    """If it is commented out it will replace the renpy screen creating an error when returning to renpy. https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode"""
    # * It has the job of replacing the original so nothing happens
    surface = RenpyGameSurface()
    renpy.show_screen("renpygame_surface", surface=surface)
    return surface


def mode_ok(size: tuple[int, int], flags: int = 0, depth: int = 0, display: int = 0) -> int:
    """https://www.pygame.org/docs/ref/display.html#pygame.display.mode_ok"""
    return pygame.display.mode_ok(size, flags, depth)


def set_icon(Surface) -> None:
    """https://www.pygame.org/docs/ref/display.html#pygame.display.set_icon"""
    return pygame.display.set_icon(Surface)


def flip() -> None:
    """https://www.pygame.org/docs/ref/display.html#pygame.display.flip"""
    return pygame.display.flip()


def update(rectangle: Optional[Union[list, Any]] = None) -> None:
    """https://www.pygame.org/docs/ref/display.html#pygame.display.update"""
    return pygame.display.update(rectangle)
