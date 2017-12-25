from copy import deepcopy

class manager:
    obj = {
        'arr_dict': [],
        'arr_arr': [],
    }
    @classmethod
    def make_obj(cls):
        return deepcopy(cls.obj)

