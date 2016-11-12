"""
flask-dependency性能测试

结果:
    normal: 0.210586
    proxy: 2.427060
"""

from timeit import timeit
from flask_dependency import Dependency


class Service(object):

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


normal = Service('normal')

proxy, init_proxy = Dependency(Service)
init_proxy('proxy')

print(normal.get_name())
print(proxy.get_name())

test = "service.get_name()"
print("normal: {:.6f}".format(timeit(test, globals={"service": normal})))
print("proxy: {:.6f}".format(timeit(test, globals={"service": proxy})))
