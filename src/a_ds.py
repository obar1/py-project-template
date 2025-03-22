from abc import ABC


class ADS(ABC):
    """
    A generic data structure
    """

    @property
    def get_id(self):
        return "id"

    @property
    def ds_func(self):
        return {x for x in self.__class__.__dict__ if not str(x).startswith("_")}
