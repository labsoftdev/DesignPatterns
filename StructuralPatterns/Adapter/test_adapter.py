"""Test module for Adapter design pattern"""

import unittest
from target import Target
from adaptee import Adaptee
from adapter import Adapter


class TestAdapter(unittest.TestCase):
    """Test class for Adapter design pattern"""

    def test_should_return_default_and_optional_behavior(self):
        """Test return from target requests"""
        _target = Target()
        self.assertEqual(_target.request(), "Target: The default target's behavior.")
        self.assertEqual(
            _target.another_request(), "Target: The optional target's behavior."
        )

    def test_should_return_unusable_responses(self):
        """Test Adaptee that returns unusable responses"""
        _adaptee = Adaptee()
        self.assertEqual(
            _adaptee.specific_request(), ".eetpadA eht fo roivaheb laicepS"
        )
        self.assertEqual(_adaptee.another_specific_request(), ".noitatpada deen I")

    def test_should_return_adapted_responses(self):
        """Test Adaptee that returns unusable responses"""
        _adaptee = Adaptee()
        _adapter = Adapter(_adaptee)
        self.assertEqual(
            _adapter.request(),
            "Adapter: (TRANSLATED) Special behavior of the Adaptee.",
        )
        self.assertEqual(
            _adapter.another_request(), "Adapter: (TRANSLATED) I need adaptation."
        )


if __name__ == "__main__":
    unittest.main()
