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
* Add aliases to `.bashrc`
    ```
    alias la="ls -a"
    alias ll="ls -al"
    alias venvy=". /venv/bin/activate"
    ```
* Install libraries (run pip install in virtual environment, create one with `python3 -m venv venv`)
    ```
    $ sudo apt install python-serial python3-serial
    $ pip install pyserial
    ```
* Hardware configuration
    ```
    $ sudo raspi-config
    ```
    * Enable serial (no login shell, but hardware enabled)
