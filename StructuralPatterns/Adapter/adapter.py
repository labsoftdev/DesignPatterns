"""Adapter: adapts the interface of Adaptee to the Target interface."""
from target import Target
from adaptee import Adaptee


class Adapter(Target):
    """Adapter class that adapts Adaptee"""

    def __init__(self, adaptee: Adaptee):
        self._adaptee = adaptee

    def request(self):
        """Adapting the specific request"""
        return f"Adapter: (TRANSLATED) {self._adaptee.specific_request()[::-1]}"

    def another_request(self):
        """Adapting the another specific request"""
        return f"Adapter: (TRANSLATED) {self._adaptee.another_specific_request()[::-1]}"
