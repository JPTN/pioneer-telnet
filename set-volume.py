import sys
import telnetlib

HOST = "192.168.1.100" # update to your receiver's IP (recommend setting a static/DHCP reserved IP)
tn = telnetlib.Telnet(HOST,23,120)

tn.write("?V\r\n") # send "?V" command to get the current volume level
output = tn.read_until("\r\n")
currentlevel = int(output[3:])  # Pioneer responds with "VOL###" (ignore the "VOL" part of the string)

goal = (int(sys.argv[1]) - 5) * 2 # input argument: convert from my Sony TV's volume scale to Pioneer's

if goal < 160: # my set upper limit to prevent damage to speakers
  if currentlevel > goal:
    for x in range(currentlevel, goal, -1):
      tn.write("VD\r\n") # send "VD" command (volume down)
  else:
    for x in range(currentlevel, goal, 1):
      tn.write("VU\r\n") # send "VU" command (volume up)
  tn.close()
else:
  print "Out of range"
