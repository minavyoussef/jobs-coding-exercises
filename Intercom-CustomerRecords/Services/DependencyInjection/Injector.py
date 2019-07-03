from threading import Lock

_lock = Lock()
_injector = None


def get_injector():
    """
    Global DependencyInjection getter (thread-safe)

    :return: Injector object
    :rtype: Injector
    """
    global _injector
    with _lock:
        if _injector is None:
            _injector = Injector()
        return _injector


class Injector:
    """
    Class Injector implements simple DependencyInjection container.
    """

    def __init__(self):
        self._types_dict = {}

    def clear(self):
        self._types_dict.clear()

    def register(self, name, target_type):
        self._types_dict[name] = target_type

    def resolve(self, name, raise_exception=False):
        if name not in self._types_dict.keys():
            if raise_exception:
                raise TypeError(f'Type name {name} not associated with given type')
            else:
                return

        return self._types_dict[name]()

    @property
    def get_registered(self):
        return self._types_dict
