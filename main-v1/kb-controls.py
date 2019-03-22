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
stdscr.addstr(0, 0, "Use up/left/right to drive, any key to stop, i/o for relays, p for gantry.")
stdscr.refresh()

currentDirection = "Stop"

relay1 = False
relay2 = False
gantryToggle = False

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
        elif key == ord('i'):
            relay1 = not relay1
            stdscr.addstr(0, 0, "Relay 1 Toggle: " + str(relay1))
        elif key == ord('o'):
            relay2 = not relay2
            stdscr.addstr(0, 0, "Relay 2 Toggle: " + str(relay2))
        elif key == ord('p'):
            gantryToggle = not gantryToggle
            stdscr.addstr(0, 0, "Gantry Toggle: " + str(gantryToggle))
        else:
            stdscr.addstr(0, 0, "Stop")
            newDirection = "Stop"
        
        if currentDirection != newDirection:
            currentDirection = newDirection
            if currentDirection == "Forwards":
                writer.setLeftPowerMapped(0.4)
                writer.setRightPowerMapped(0.4)
            elif currentDirection == "Left":
                writer.setLeftPowerMapped(0)
                writer.setRightPowerMapped(0.4)
            elif currentDirection == "Right":
                writer.setLeftPowerMapped(0.4)
                writer.setRightPowerMapped(0)
            elif currentDirection == "Stop":
                writer.setLeftPowerMapped(0)
                writer.setRightPowerMapped(0)

        if relay1:
            writer.setBit(1, 1)
        else:
            writer.setBit(1, 0)

        if relay2:
            writer.setBit(2, 1)
        else:
            writer.setBit(2, 0)

        if gantryToggle:
            writer.setStepperPositionMapped(1)
        else:
            writer.setStepperPositionMapped(0)
         
        writer.writeAllBytes()

except:
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()
    print("Killed it!")
