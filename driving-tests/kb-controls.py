# https://stackoverflow.com/questions/10693256/how-to-accept-keypress-in-command-line-python

import curses

stdscr = curses.initscr()

curses.noecho()
curses.cbreak()

stdscr.keypad(True)

stdscr.addstr(0, 0 , "Use arrow keys to drive, press any key to stop.")
stdscr.refresh()

try:
    while True:

        key = stdscr.getch()

        stdscr.clear()

        if key == curses.KEY_UP:
            stdscr.addstr(0, 0, "Forwards")
        elif key == curses.KEY_DOWN:
            stdscr.addstr(0, 0, "Backwards")
        elif key == curses.KEY_LEFT:
            stdscr.addstr(0, 0, "Left")
        elif key == curses.KEY_RIGHT:
            stdscr.addstr(0, 0, "Right")
        else:
            stdscr.addstr(0, 0, "Stop")
        
        stdscr.refresh()

except:
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()
    print("Killed it!")
