Title: RaspberryPi Temperature Monitor, Mark II
Date: 2013-08-17 17:22
Modified: 2013-09-18 08:32
Category: Ops
Tags: ds18b20, raspberrypi, rpi-temp-monitor
Slug: rpi-temp-monitor-mk2
Author: Kai Blin
Summary: A new case for the temperature monitor.

A while ago I set up a Raspberry Pi based temperature monitoring system, to
monitor temperatures for the equipment room and the server rack and freezers
located in there. I still need to write a post detailing the software and
hardware used for this, hopefully I'll get around to that soon. In short, I'm
using a bunch of 1-wire DS18B20 digital temperature sensors connected to the
Raspberry Pi. Today, though, I spent my time upgrading the case and fixation of
the temperature monitor.
Mark I had a simple plastic back and a cardboard front, and was taped to the
network/electricity rail in the room, like so:

[![Mark I case]({filename}/images/thumbs/rpi_temp_monitor_mk1.jpg)](http://www.imagemagick.org/script/convert.php)

While expedient to get set up and move the mess of cable out of the way, this
setup has some problems. First, the Raspberry Pi tended to crash a lot. Not the
software, but the hardware. That's because this yellow tape sucks, and that's
why eventually I brought some proper duct tape and "fixed it". Still, it was
clear that eventually even duct tape would succumb to the pull of gravity. Also,
we'll lose power for a scheduled test of the emergency power system on Thursday,
and I wanted to get my little Pi into the server rack so I could hook it up to
the UPS.
For the Mark II case, I wanted to get a proper plastic case, front and back.
Fortunately, when you work in a lab, there are a lot of petri dishes around. We
also have the large square ones. Two of those, a drill, a hand saw and half an
hour later, the Mark II case was ready to go.

[![Mark II case]({filename}/images/thumbs/rpi_temp_monitor_mk2.jpg)]({filename}/images/rpi_temp_monitor_mk2.jpg)

It's attached to the rack door mesh with cable ties (yay, cable ties), and
nicely out of the way of the 19" slots. Also visible is the custom board with
audio jacks that the sensors are connected to. The falcon tube cap on the right
is a stand-off so the add-on board won't push down too far, that still feels a
bit hacked. Oh well, we're getting there.

*Update 2013-09-18, 08:32 UTC*: Turns out there is one unexpected feature with
mounting the "in-rack" sensor on the door as well. It is now possible to track
when I open and close the door, and of course the temperatures are off in that
case.

[![Temperature changes when door is open]({filename}/images/thumbs/sensor_in_door.png)]({filename}/images/sensor_in_door.png)

