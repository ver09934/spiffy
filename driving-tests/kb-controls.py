# https://stackoverflow.com/questions/10693256/how-to-accept-keypress-in-command-line-python

import curses
import drivecontroller

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
stdscr.addstr(0, 0 , "Use arrow keys to drive, press any key to stop.")
stdscr.refresh()

currentDirection = "Stop"

fwb = 0xfe
bwb = 0x00
nb = 0x80
sb = 0xff

try:
    while True:

        stdscr.refresh()
        key = stdscr.getch()
        stdscr.clear()

        if key == curses.KEY_UP:
            stdscr.addstr(0, 0, "Forwards")
            newDirection = "Forwards"
        elif key == curses.KEY_DOWN:
            stdscr.addstr(0, 0, "Backwards")
            newDirection = "Backwards"
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
                drivecontroller.writeByte(fwb)
                drivecontroller.writeByte(fwb)
            elif currentDirection == "Backwards":
                drivecontroller.writeByte(bwb)
                drivecontroller.writeByte(bwb)
            elif currentDirection == "Left":
                drivecontroller.writeByte(bwb)
                drivecontroller.writeByte(fwb)
            elif currentDirection == "Right":
                drivecontroller.writeByte(fwb)
                drivecontroller.writeByte(bwb)
            elif currentDirection == "Stop":
                drivecontroller.writeByte(nb)
                drivecontroller.writeByte(nb)

            drivecontroller.writeByte(sb)

except:
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()
    print("Killed it!")
