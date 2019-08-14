"""(b == True and b == False) да дава True."""


class Schrodinger:
    def __eq__(self, *args, **kwargs):
        return True


b = Schrodinger()
