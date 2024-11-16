class Registry:

    def __init__(self):
        self.registry = {}

    def put(self, impl, beanname=None):
        if beanname is None:
            beanname = self.__fullname(impl.__class__)
        self.registry[beanname] = impl

    def get(self, cls):
        # beanname = self.__fullname(cls)
        if cls in self.registry:
            return self.registry[cls]
        else:
            raise Exception(f"No such bean in registry: {cls}")

    def clear(self):
        self.registry.clear()

    @staticmethod
    def __fullname(cls):
        return cls.__module__ + '.' + cls.__qualname__


REGISTRY = Registry()
