# firestick-kodi-installer

Find the IP of a firestick on the network, optionally download the apk, and wireless install it through ADB on the target firestick.

What can it do for you?
  - Automatically install kodi on your firestick
  - Manually install kodi on your firestick


### Installation

firestick-kodi-installer requires adb to run.

Download and extract the [latest release](https://github.com/Bradart/firestick-kodi-installer/releases).

Install the dependencies:

```
Install adb from package manager or from source.
```

Auto Install Dependencies:

```
Install adb, and nmap from package manager or from source. 
```
Edit the following line (9) with your interface name:
```
myiface = 'enp0s5'
```
eg. (eth0)
```
myiface = 'eth0'
```

### Todos

 - Add NMAP Check
 - Add ADB Check
 - Add Code Comments


