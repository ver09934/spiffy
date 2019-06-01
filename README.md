# spiffy
The hospital disinfection robot.

## Raspberry Pi Setup Procedure

### Flash OS
* Flash raspbian lite image to SD card using `dd` or other utility
* Create the following files in the root directory of the boot partition:
    * A file called `ssh`
    * A file called `wpa_supplicant.conf` with the following contents:
        ```
        country=US
        ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
        update_config=1

        network={
            ssid="network-ssid-name"
            scan_ssid=1
            psk="network-password"
            key_mgmt=WPA-PSK
        }
        ```

### Config and Setup
* Change `pi`user password
* Update and install libraries
    ```
    $ sudo apt update && sudo apt upgrade
    $ sudo apt install tmux vim python3-venv tree
    ```
* Add aliases to `~/.bashrc`
    ```
    alias la="ls -a"
    alias ll="ls -al"
    alias venvy=". /venv/bin/activate"
    alias mkvenv="python3 -m venv venv"
    alias temp="vcgencmd measure_temp"
    ```
* Basic `~/.vimrc`
    ```
    set number
    syntax enable
    ```
* Setup `~/.gitconfig` (can also be through by individual commands)
    ```
    [user]
        name = example
        email = example@example.com
    [alias]
            lg = log --all --decorate --oneline --graph --color
            st = status
    [credential]
            helper = cache --timeout=36000
    ```
* Install libraries (run pip install in virtual environment, create one with `python3 -m venv venv`)
    ```
    $ sudo apt install python-serial python3-serial
    $ sudo apt install fswebcam ffmpeg arduino git xvfb
    $ sudo apt install python-dev python3-dev
    $ sudo apt install libatlas3-base libsz2 libharfbuzz0b libtiff5 libjasper1 libilmbase12 libopenexr22 libilmbase12 libgstreamer1.0-0 libavcodec57 libavformat57 libavutil55 libswscale4 libqtgui4 libqt4-test libqtcore4
    $ pip install pyserial opencv-python imutils numpy aruco
    ```
* Hardware configuration
    ```
    $ sudo raspi-config
    ```
    * Enable serial (no login shell, but hardware enabled)
