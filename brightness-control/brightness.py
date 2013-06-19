#!/usr/bin/env python

import gtk
import subprocess

class BrightnessScale:
    def __init__(self):
        window = gtk.Window()
        window.set_title('Brightness Scale')
        window.set_default_size(250, 50)
        #Find display monitor
        self.monitor = subprocess.check_output("xrandr -q | grep ' connected' | cut -d ' ' -f1", shell=True)
        self.monitor = self.monitor.strip().rstrip('\n')

        #Find current brightness
        currBrightness = subprocess.check_output("xrandr --verbose | grep -i brightness | cut -f2 -d:", shell=True)
        currBrightness = int(float(currBrightness) * 100)
        
        adjustment = gtk.Adjustment(currBrightness, 0, 100, 1, 10, 0)
        self.scale = gtk.HScale(adjustment)
        self.scale.set_digits(0)
        self.scale.set_update_policy(gtk.UPDATE_DELAYED)
        
        window.connect("destroy", lambda w: gtk.main_quit())
        self.scale.connect("value-changed", self.scale_moved)
        
        window.add(self.scale)
        window.show_all()

    def scale_moved(self, event):
        #Change brightness
        newBrightness = float(self.scale.get_value())/100
        cmd = "xrandr --output %s --brightness %.2f" % (self.monitor, newBrightness)
        cmdStatus = subprocess.check_output(cmd, shell=True)

BrightnessScale()
gtk.main()
