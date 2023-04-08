class A:
    def __init__(self):
        self._var = 0

    def _get_var(self):
        print("The value is being read")
        return self._var

    def _set_var(self, x):
        print("The value is being written")
        self._var: int = x

    var = property(fget=_get_var, fset=_set_var)


a = A()
a.var = 10
print(a.var)
