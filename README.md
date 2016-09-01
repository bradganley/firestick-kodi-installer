# firestick-kodi-installer

Find the IP of a firestick on the network, optionally download the apk, and wireless install it through ADB on the target firestick using python!

What can it do for you?
  - Automatically install kodi on your firestick
  - Manually install kodi on your firestick


### Installation

firestick-kodi-installer requires adb to run.

Download and extract the [latest release](https://github.com/Bradart/firestick-kodi-installer/).

Install the dependencies:

```
Install adb from package manager or from source.
(apt-get install android-tools-adb android-tools-fastboot on ubuntu/debian based linux distros)[We may add this to checks/auto-installs later. Who knows? We're sexy and ready to party.]
```

Auto Install Dependencies:
```
Install [netifaces library](https://pypi.python.org/pypi/netifaces#downloads) for python.
```

```
Install adb, and nmap from package manager or from source. 
```
### Instructions

1.) Download the script.
2.) Make sure dependencies from above are installed.
3.) Run the script and select the option you would like.

### Todos

 - Add Detailed Code Comments
 - Check for and help install dependencies?
 - Change multi install option to a switch in download and variable to minimize code


