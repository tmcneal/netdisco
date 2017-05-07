"""Add support for discovering mDNS services."""
from netdisco.bluefang import connection
import threading

class Bluetooth(object):
    """Base class to discover Tellstick devices."""

    def __init__(self):
        """Initialize the TEllstick discovery."""
        self.entries = []
        self._lock = threading.RLock()

    def scan(self):
        """Scan the network."""
        with self._lock:
            self.update()

    def all(self):
        """Scan and return all found entries."""
        self.scan()
        return self.entries

    def update(self):
        """Scan network for Tellstick devices."""
        print("in it")
        bluetooth = connection.Bluefang()
        self.entries = bluetooth.scan()
