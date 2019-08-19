class Diskspace(object):
    def __init__(self, *args, **kwargs):
        self._path = kwargs.get("path", "")
        self._label = kwargs.get("label", "")
        self._free_space = kwargs.get("freeSpace", "")
        self._total_space = kwargs.get("totalSpace", "")

    @property
    def path(self):
        return self._path

    @property
    def label(self):
        return self._label

    @property
    def free_space(self):
        return self._free_space

    @property
    def total_space(self):
        return self._total_space
