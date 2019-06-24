import importlib


class FunctionUtils(object):
    def get_function_by_str(function_string):
        mod_name, func_name = function_string.rsplit('.', 1)
        mod = importlib.import_module(mod_name)
        func = getattr(mod, func_name)
        return func
