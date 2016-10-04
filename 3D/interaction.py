# coding=utf-8
from collections import defaultdict
from OpenGL.GLUT import glutGet, glutKeyboardFunc, glutMotionFunc, glutMouseFunc, glutPassiveMotionFunc, \
                        glutPostRedisplay, glutSpecialFunc
from OpenGL.GLUT import GLUT_LEFT_BUTTON, GLUT_RIGHT_BUTTON, GLUT_MIDDLE_BUTTON, \
                        GLUT_WINDOW_HEIGHT, GLUT_WINDOW_WIDTH, \
                        GLUT_DOWN, GLUT_KEY_UP, GLUT_KEY_DOWN, GLUT_KEY_LEFT, GLUT_KEY_RIGHT
import trackball


class Interaction(object):
    def __init__(self):
        """ 处理用户接口 """
        # 被用户按下的键
        self.pressed = None
        # 轨迹球
        self.trackball = trackball.Trackball(theta = -25, distance = 15)
        # 当前鼠标位置
        self.mouse_loc = None
        # 回调函数字典
        self.callbacks = defaultdict(list)

        self.register()

    def register(self):
        """ 注册glut的事件回调函数 """
        glutMouseFunc(self.handle_mouse_button)
        glutMotionFunc(self.handle_mouse_move)
        glutKeyboardFunc(self.handle_keystroke)
        glutSpecialFunc(self.handle_keystroke)

    def handle_mouse_button(self, button, mode, x, y):
        """ 当鼠标被点击或释放的时候调用 """
        xSize, ySize = glutGet(GLUT_WINDOW_WIDTH), glutGet(GLUT_WINDOW_HEIGHT)
        y = ySize - y
        # OpenGL原点在窗口左下角,窗口原点在左上角,所以需要转换
        self.mouse_loc = (x,y)

        if mode == GLUT_DOWN:
            # 当鼠标按键被按下
            self.pressed = button
            if button == GLUT_RIGHT_BUTTON:
                pass
            elif button == GLUT_LEFT_BUTTON:
                self.trigger('pick', x, y)
        else: # 鼠标按键被释放的时候
            self.pressed = None
            #标记当前窗口需要重新绘制
            glutPostRedisplay()

    def handle_mouse_move(self, x, screen_y):
        xSize, ySize = glutGet(GLUT_WINDOW_WIDTH), glutGet(GLUT_WINDOW_HEIGHT)
        y = ySize - screen_y
        if self.pressed is not None:
            dx = x - self.mouse_loc[0]
            dy = y - self.mouse_loc[1]
            if self.pressed == GLUT_RIGHT_BUTTON and self.trackball is not None:
                # 变化场景的角度
                self.trackball.drag_to(self.mouse_loc[0], self.mouse_loc[1], dx, dy)
            elif self.pressed == GLUT_LEFT_BUTTON:
                self.trigger('move', x, y)
            elif self.pressed == GLUT_MIDDLE_BUTTON:
                self.translate(dx/60.0, dy/60.0)
            else:
                pass
            glutPostRedisplay()
        self.mouse_loc = (x, y)

    def handle_keystroke(self, key, x, screen_y):
        """ 键盘输入时调用 """
        xSize, ySize = glutGet(GLUT_WINDOW_WIDTH), glutGet(GLUT_WINDOW_HEIGHT)
        y = ySize - screen_y
        if key == 's':
            self.trigger('place', 'sphere', x, y)
        elif key == 'c':
            self.trigger('place', 'cube', x, y)
        elif key == GLUT_KEY_UP:
            self.trigger('scale', up = True)
        elif key == GLUT_KEY_DOWN:
            self.trigger('scale', up = False)
        elif key == GLUT_KEY_LEFT:
            self.trigger('rotate_color', forward = True)
        elif key == GLUT_KEY_RIGHT:
            self.trigger('rotate_color', forward = False)
        glutPostRedisplay()

    def trigger(self, name, *args, **kwargs):
        for func in self.callbacks[name]:
            func(*args, **kwargs)

    def register_callback(self, name, func):
        self.callbacks[name].append(func)


