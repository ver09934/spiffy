# https://stackoverflow.com/questions/10693256/how-to-accept-keypress-in-command-line-python

import curses
import time
import serialwriter

writer = serialwriter.SerialWriter()
time.sleep(3)

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
stdscr.addstr(0, 0 , "Use arrow keys to drive, press any key to stop.")
stdscr.refresh()

currentDirection = "Stop"

try:
    while True:

        stdscr.refresh()
        key = stdscr.getch()
        stdscr.clear()

        if key == curses.KEY_UP:
            stdscr.addstr(0, 0, "Forwards")
            newDirection = "Forwards"
        elif key == curses.KEY_LEFT:
            stdscr.addstr(0, 0, "Left")
            newDirection = "Left"
        elif key == curses.KEY_RIGHT:
            stdscr.addstr(0, 0, "Right")
            newDirection = "Right"
        else:
            stdscr.addstr(0, 0, "Stop")
            newDirection = "Stop"
        
        if currentDirection != newDirection:
            currentDirection = newDirection
            if currentDirection == "Forwards":
                writer.setLeftPower(0xB0)
                writer.setRightPower(0xB0)
            elif currentDirection == "Left":
                writer.setLeftPower(0x80)
                writer.setRightPower(0xB0)
            elif currentDirection == "Right":
                writer.setLeftPower(0xB0)
                writer.setRightPower(0x80)
            elif currentDirection == "Stop":
                writer.setLeftPower(0x80)
                writer.setRightPower(0x80)
         
        writer.writeAllBytes()

except:
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()
    print("Killed it!")
