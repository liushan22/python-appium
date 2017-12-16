# -*- coding: utf-8 -*-


class TranType:
    def __init__(self):
        pass

    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False

    def tran_type(self, *s):
        new_s = []
        for ss in s:
            if self.is_number(ss):
                ss = str(int(ss))
            else:
                ss = str(ss)
            new_s.append(ss)
        return new_s