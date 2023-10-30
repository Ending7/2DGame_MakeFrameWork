import pico2d
from pico2d import load_image, clear_canvas, update_canvas, get_events, get_time, SDL_KEYDOWN, SDLK_ESCAPE
from sdl2 import SDLK_SPACE, SDL_QUIT

import game_framework
import game_world
import play_mode
from pannel import Pannel


def init():
    global pannel
    pannel = Pannel()
    game_world.add_object(pannel, 3)
def finish():
    game_world.remove_object(pannel)
    pass

def update():
    game_world.update()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.change_mode(play_mode)
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_mode() #change mode 현재 모드를 날려버리고 push_mode는 그대로 유지한다. pop모드는 push됬던 상태로 이동
                case pico2d.SDLK_0:
                    play_mode.boy.item = None
                    game_framework.pop_mode()
                case pico2d.SDLK_1:
                    play_mode.boy.item = 'Ball'
                    game_framework.pop_mode()
                case pico2d.SDLK_2:
                    play_mode.boy.item = 'BigBall'
                    game_framework.pop_mode()
    pass


