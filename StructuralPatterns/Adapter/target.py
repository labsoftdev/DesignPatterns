"""Target - defines the domain-specific interface that Client uses."""


class Target:
    """Target Interface"""

    def request(self):
        """some request method"""
        return "Target: The default target's behavior."

    def another_request(self):
        """some other request method"""
        return "Target: The optional target's behavior."
