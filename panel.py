import gi
import battery
import time
import os
from threading import Thread

gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')

from gi.repository import Gtk as gtk, AppIndicator3 as AppIndicator

def quit(_):
    os._exit(0)

class Indicator:
    def __init__(self):
        self.h, self.level = battery.get_battery_level()
        self.id = "cloud-ii-battery-indicator"
        self.icon_path = "audio-headset"
        self.indicator = AppIndicator.Indicator.new(self.id, self.icon_path, AppIndicator.IndicatorCategory.SYSTEM_SERVICES)
        self.indicator.set_status(AppIndicator.IndicatorStatus.ACTIVE)
        self.indicator.set_menu(self.build_menu())
        self.update = Thread(target=self.update_battery_level)
        self.update.start()
        gtk.main()
    def build_menu(self):
        menu = gtk.Menu()
        item_battery = gtk.MenuItem(label = "")
        menu.append(item_battery)

        item_quit = gtk.MenuItem(label = 'Quit')
        item_quit.connect('activate', quit)
        menu.append(item_quit)
        menu.show_all()
        self.menu = menu
        self.item_battery = item_battery
        self.item_quit = item_quit
        return menu

    def update_battery_level(self):
        while True:
            self.level = battery.get_battery_level(self.h)[1]
            self.item_battery.set_label("Battery Level: " + str(self.level) + "%")
            self.indicator.set_label(str(self.level) +"%", "")
            time.sleep(60)
            


if __name__ == "__main__":
    indicator = Indicator()