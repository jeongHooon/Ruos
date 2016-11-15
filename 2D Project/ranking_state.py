import game_framework
from pico2d import *


import main_state

score_data = [{"Time":10.5,"x":100,"y":500},{"Time":20.5,"x":300,"y":200},{"Time":30.5,"x":150,"y":400},{"Time":40.5,"x":100,"y":500},{"Time":50.5,"x":300,"y":200},{"Time":60.5,"x":150,"y":400},{"Time":70.5,"x":150,"y":400},{"Time":90.5,"x":150,"y":400},{"Time":57.5,"x":150,"y":400},{"Time":67,"x":150,"y":400}]
name = "RankingState"
image = None

def enter():
    global image, font
    font = load_font('ENCR10B.TTF', 40)
    image = load_image('blackboard.png')

def exit():
    global image, font
    del(image)
    del(font)


def pause():
    pass

def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()



def update(frame_time):
    pass


def bubble_sort(data_list):
    for i in range(0, len(data_list)):
        for j in range(i + 1, len(data_list)):
            if data_list[i]['Time'] < data_list[j]['Time']:
                data_list[i], data_list[j] = data_list[j], data_list[i]
def draw_ranking():
    def print_score(score):
        font.draw(200, score*50,"Time :%4.1f, x :%3d, y :%3d" % (score['Time'], score['x'], score['y']))
    f = open('ranking_data.txt', 'r')
    score_data = json.load(f)
    f.close()
    bubble_sort(score_data)
    score_data = score_data[:10]

    y=0
    for score in score_data:
        font.draw(100, 500 - y*50, "Time :%4.1f, x :%3d, y :%3d" % (score['Time'], score['x'], score['y']))
        y = y+1

#draw_ranking()


def draw(frame_time):
    global image, font
    clear_canvas()
    image.draw(400, 300)
    font.draw(290, 550,'[RANKING]', (255, 0, 0))




    draw_ranking()
    update_canvas()



