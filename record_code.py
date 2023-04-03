from pynput.keyboard import Key, Controller
from time import sleep
from os import system
k = Controller()

def recording(x):
    k.press(x)
    sleep(0.1)
    k.release(x)

def switch(x):
    k.press(Key.ctrl)
    k.press(Key.shift)
    k.press(x)
    k.release(Key.ctrl)
    k.release(Key.shift)
    k.release(x)
    sleep(1)

def start():
    switch(Key.left)
    system("konsole &")
    sleep(1)
    recording(Key.f9)

def end():
    system("ps -a | grep konsole > /tmp/pid")
    for line in open("/tmp/pid").readlines():
        pid = int(line.split()[0])
        system(f"sudo kill -9 {pid}")
    recording(Key.f10)

def slow_type(text):
    for char in text:
        k.type(char)
        sleep(0.08)

def main():
    filename = "0001.py"
    contents = open(filename).read()[:-1]

    start()
    sleep(1)
    slow_type(f"nvim {filename}\n")
    k.type("VGd:set paste\n:")
    k.press(Key.esc)
    k.release(Key.esc)

    slow_type('i')
    sleep(1)
    slow_type(contents)
    sleep(1)
    k.press(Key.esc)
    k.release(Key.esc)
    sleep(2)
    slow_type(":wq\n")
    sleep(0.5)
    slow_type(f"python {filename}\n")
    sleep(5)
    end()

if __name__ == "__main__":
    main()
