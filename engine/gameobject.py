from typing import List


class GameObject:

    def __init__(self):
        self._children : List[GameObject] = []
        self._enabled = True

    @property
    def children(self):
        return self._children

    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        self._enabled = value

    def enable(self):
        self._enabled = True

    def disable(self):
        self._enabled = False

    def awake(self):
        pass

    def _awake(self):
        if not self.enabled:
            return

        self.awake()

        for child in self.children:
            child._awake()

    def start(self):
        pass

    def _start(self):
        if not self.enabled:
            return

        self.start()

        for child in self.children:
            child._start()

    def early_update(self, dt: float):
        pass

    def _early_update(self, dt: float):
        if not self.enabled:
            return

        self.early_update(dt)

        for child in self.children:
            child._early_update(dt)

    def update(self, dt: float):
        pass

    def _update(self, dt: float):
        if not self.enabled:
            return

        self.update(dt)

        for child in self.children:
            child._update(dt)

    def late_update(self, dt: float):
        pass

    def _late_update(self, dt: float):
        if not self.enabled:
            return

        self.late_update(dt)

        for child in self.children:
            child._late_update(dt)

    def end(self):
        pass

    def _end(self):
        if not self.enabled:
            return

        self.end()

        for child in self.children:
            child._end()

    def finalize(self):
        pass

    def _finalize(self):
        if not self.enabled:
            return

        self.finalize()

        for child in self.children:
            child._finalize()
