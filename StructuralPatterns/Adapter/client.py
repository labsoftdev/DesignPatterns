"""Adapter design pattern presentation"""
from target import Target
from adapter import Adapter
from adaptee import Adaptee


def client_code(target: Target):
    """Client use Target interface"""
    print(target.request(), end="")


if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    _target = Target()
    client_code(_target)
    print("\n")

    adaptee = Adaptee()
    print(
        "Client: The Adaptee class has a weird interface. "
        "See, I don't understand it:"
    )
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Client: But I can work with it via the Adapter:")
    adapter = Adapter(adaptee)
    client_code(adapter)
    print("\n")
