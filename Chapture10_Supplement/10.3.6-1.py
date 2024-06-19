#  需要在硬件上直接运行
from pprint import pprint
import keyboard
import random

def on_key(event):
    if event.name == 'esc':
        print('Exiting...')
        keyboard.unhook_all()
        exit()
    if event.name == 'space':
        print(deck.pop())

values = list(range(1, 11)) + 'Jack Queen King'.split()
suits = 'diamonds clubs hearts spades'.split()
deck = ['%s of %s' % (v, s) for v in values for s in suits]
pprint(deck[:12])
random.shuffle(deck)
pprint(deck[:12])
keyboard.add_hotkey('ctrl+alt+a', print, args=('You pressed ctrl+alt+a',))
keyboard.on_press(on_key)
while deck:
    keyboard.wait()
    if not deck:
        print('No more cards.')
        break
