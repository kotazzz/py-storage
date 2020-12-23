#One Screen Prj
import keyboard
import os
import sys
import random
from ColorModule import MCC, ACC

class Cursor(object):
    def __init__(self, max_x, max_y, storage):
        self.max_x = max_x
        self.max_y = max_y
        self.x = 0
        self.y = 0
        self.update_storage(storage)
    def check_x(self):
        if self.x == self.max_x-1:
            return False
        return True
    def check_y(self):
        if self.y == self.max_y:
            return False
        return True
    def get_x(self): 
        return self.x
    def get_y(self):  
        return self.y
    def set_x(self, x):  
        self.x = x
    def set_y(self, y):  
        self.y = y
    def get_pos(self):  
        return [self.x, self.y]
    def set_pos(self, x, y):  
        self.x = x 
        self.y = y
    def left(self, count = 1):  
        self.x -= count
    def right(self, count = 1):  
        self.x += count
    def down(self, count = 1):  
        self.y -= count
    def up(self, count = 1):  
        self.y += count
    def newline(self, count = 1):
        self.x = 0
        self.y = self.y + count 
    def resetpos(self):
        self.x = 0 
        self.y = 0
    def update_storage(self,storage):
        self.local_storage = storage
    def out(self,text):
        for letter in text:
            if self.check_x():
                self.right(1)
            else:
                if self.check_y():
                    self.right()
                    self.newline()
                else:
                    self.resetpos()
                
            
            try:
                self.local_storage[self.y][self.x] = letter
            except:
                pass
            
    def push_data(self):
        return self.local_storage

class Window(object):
    def __init__(self, x, y):
        print(MCC.CURSOR_HIDE)
        self.size_x = 0 
        self.size_y = 0
        self.window_storage = self.resize(x, y)
        self.cursor = Cursor(x, y, self.window_storage)
    def resize(self,x,y, winsizeupd = True):
        window_storage = []
        for yi in range(y):
            xa = []
            for xi in range(x):
                xa.append(f' ')
            window_storage.append(xa)
        if winsizeupd:
            os.system(f"mode con cols={x} lines={y}")
        return window_storage
    def draw(self):
        self.window_storage = self.cursor.push_data()
        s = ''
        for line in self.window_storage:
            s += ''.join(line)+'\n'
        sys.stdout.write(s[:-1])
    def flush(self):
        self.window_storage = self.resize(self.size_x, self.size_y, winsizeupd = False)
        self.cursor.update_storage(self.window_storage)
    redraw = lambda self: exec("self.draw()\nself.flush()")
    def get_size_x(self): pass
    def get_size_y(self): pass
    def set_size_x(self): pass
    def set_size_y(self): pass
    def get_data(self): pass
    def set_data(self): pass
    def destroy(self): pass
     
class Display(object):
    def __init__(self, x, y):
        self.winsize_x = x 
        self.winsize_y = y 
        self.window = Window(x, y)
        self.tasks = []
    def attach(self, f):
        self.tasks.append(f)
    def start(self):
        while True:
            for task in self.tasks:
                task(self.window)
            self.window.redraw()
            
            
# Functions:
# out(text) = print(text)
# in(text) = input(text)
# cls(sym)
# resize(x, y)

def main(win):
    win.cursor.out('*-')
    win.cursor.out('s')

display = Display(120, 30)
display.attach(main)
display.start()
