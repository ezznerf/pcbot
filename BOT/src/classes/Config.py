import os
import sys


class Config:

    __params = dict()

    def __init__(self, file):
        try:
            params = file.readlines()
            for row in params:
                values = row.split('=')
                self.__params[values[0].strip()] = values[1].strip()

            self.__params['root_dir'] = os.getcwd()
        except BaseException:
            sys.exit('Ошибка в конфигурационном файле')

    def get_available_params(self):
        return self.__params.keys()

    def get_param(self, key):
        return self.__params.get(key, None)

    def set_param(self, key, value):
        self.__params[key] = value