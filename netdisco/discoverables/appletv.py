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
        appletvs = [entry for entry in self._netdis.bluetooth.entries if entry.name == 'Apple TV']
        print(appletvs)
        return appletvs
