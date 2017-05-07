"""Discover devices."""
from . import BaseDiscoverable

class Discoverable(BaseDiscoverable):
    """Add support for discovering a device."""

    def __init__(self, netdis):
        """Initialize discovery."""
        self._netdis = netdis

    def get_entries(self):
        """Get all details."""
        print("Returning....")
        #TODO Filter on BD address of PS3
        #TODO Check for class of 0x2c0108
        #props.Get("org.bluez.Device1", "Class")
        ps3s = [entry for entry in self._netdis.bluetooth.entries if entry.bluetooth_class == 2883848]
        print("PS3sssss")
        print(ps3s)
        return ps3s
