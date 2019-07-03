from common.Validator import Validator


class Publisher:
    """
    Class Publisher represents publisher part in publisher/subscriber pattern.
    """

    def __init__(self):
        self._subscribers = []

    def subscribe(self, sub):
        Validator.is_type(sub, Subscriber)
        self._subscribers.append(sub)

    def unsubscribe(self, sub):
        Validator.is_type(sub, Subscriber)
        self._subscribers.remove(sub)

    def notify(self, value):
        for subscriber in self._subscribers:
            subscriber.notify(value)


class Subscriber:
    """
    Class Subscriber represents subscriber part in publisher/subscriber pattern.
    """

    def notify(self, value):
        raise NotImplemented
