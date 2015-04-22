Title: The anatomy of a freezer failure
Date: 2013-08-15 15:35
Category: Ops
Tags: ds18b20, graphite, raspberrypi, rpi-temp-monitor, statsd
Slug: freezer-failure
Author: Kai Blin
Summary: Analysing the first live-action test of our new temperature monitoring

A while ago I built a system to monitor temperatures in my server and freezer
room. Yes it's the same room, but I could only get the space and air
conditioning once. I still need to write the blog post on how I set up the
temperature monitor system, but basically it's a Raspberry Pi with a number of
DS18B20 1-wire digital temperature sensors. I'm using statsd and graphite to
graph the data, and a separate set of scripts to send email alerts when specific
sensors go above their configured temperatures.
Today was the first time the system was put to use, and I'm pretty happy with
how it all worked out. I can even reconstruct what probably happened. Looking at
my graphite temperature graph for that freezer, the following story unfolds:

[![Freezer temperature plot]({filename}/images/thumbs/freezer_fail.png)]({filename}/images/freezer_fail.png)

A bit after 11:00, someone opened the freezer. They used the top drawer, which
is pretty full with boxes holding Eppendorf cups. These boxes come in a low and
a high version. The inner ceiling of the freezer is lower in the back than it is
in the front, and care must be taken that the last row of boxes in the drawer
only consists of the low boxes. If you place a high box there, the drawer will
not slide in all the way but will stick out about 5 mm. These additional 5 mm
will prevent the door from creating a seal when closed. At around 11:05, the
temperature control of the freezer notices that the temperature is too high and
starts to cool more. Note that my own temperature sensor is sitting right in the
cold air vent rigth on the top of the freezer, so it's probably measuring more
extreme temperatures than the built-in sensor.
After running the compressor at full whack for about 100 minutes, the cooling
finally fails and the freezer starts to thaw. At 12:45, the temperature rises
above -10 °C, triggering an alert email. Thus alerted, yours truly walks over to
the freezer room and notices that the door doesn't close correctly. After
shuffling some boxes around, the door closes correctly again and the temperature
begins to fall.
Unfortunately, the controller of the freezer must have crashed at 12:40 as well,
because the freezer does not resume cooling. The rising temperature triggers a
second warning email at 13:06. This time, it takes a bit longer to realize what
the actual problem is about, but eventually I realize that the cooling isn't
doing anything and toggle power on the freezer. The cooling comes back on, and
the situation is improving again.
The first live failure has shown that for our purposes the temperature
monitoring systems is working nicely. While the freezer did fail during the day,
the controller got stuck somehow and didn't trigger the acoustic alarm we should
have gotten in case of a failure. The email-based system works, and the response
time during the day is sufficient to avoid serious problems. For a cost of about
100 EUR in electronics, the Raspberry Pi / DS18B20 combination is a
cost-effective way to monitor a room full of freezers.
