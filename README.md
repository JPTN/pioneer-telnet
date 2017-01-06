# pioneer-telnet
Simple loop to control the volume on a Pioneer receiver via telnet.

**DEMO**: https://www.youtube.com/watch?v=93PE8avLq5M&index=10&list=PLOooGQo9IS-Fl3464YiImY_kJGHWdfZVE

Based off of telnet commands listed at http://www.pioneerelectronics.com/StaticFiles/PUSA/Files/Home%20Custom%20Install/SC-35-RS232.pdf and http://blog.raymondjulin.com/2012/07/15/remote-control-your-pioneer-vsx-receiver-over-telnet/, this script takes in a single command-line argument (integer) and runs a loop to in/decrease the volume to the desired level.

**NOTE**: Pioneer receivers use a different numerical scale for volume than what shows up in the volume display/settings of a connected TV (in my case a Sony KDL-65W850A) or the LCD display of the receiver itself (dB). The value in this script has been scaled for my TV and may differ depending on your TV and receiver.

**REQUIREMENTS**:
- update the IP address
- adjust the upper limit as needed
- adjust the scaling, if necessary

**SYNTAX**: 
```
python set-volume.py #
```
