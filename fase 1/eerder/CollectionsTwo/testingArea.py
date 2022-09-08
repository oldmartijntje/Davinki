print("\"\n\n\n\"")

def clear_console():
    print("\033[H\033[J", end="")

def clear_last_line():
    import sys
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')

def move_up():
    import sys
    sys.stdout.write('\x1b[1A')

def move_whatever(y, x):
    print(f"\033[{y};{x}H")

# change variable line
clear_console()
print("dQw4w9WgXcQ\ndQw4w9WgXcQ\ndQw4w9WgXcQ\ndQw4w9WgXcQ\ndQw4w9WgXcQ\ndQw4w9WgXcQ\ndQw4w9WgXcQ\ndQw4w9WgXcQ\n")
line = 4
move_whatever(line, 0)
print(f"{line, line, line, line, line, line, line, line, line}")

clear_last_line()
move_up()
clear_last_line()
move_up()
move_whatever(8, 0)
print("finished")