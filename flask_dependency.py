"""
处理Flask中依赖问题

Usage:

    # ext.py
    service, init_service = Dependency(Service)

    # app.py
    from .ext import service, init_service
    init_service(*args, **kwargs)

    # others
    from .ext import service
    service.xxx

性能: 速度比普通方法调用慢10倍左右
"""
from werkzeug.local import LocalProxy


class Dependency:

    def __init__(self, cls):
        self.cls = cls

    def init(self, *args, **kwargs):
        self.dependency = self.cls(*args, **kwargs)
        return self.dependency

    def __call__(self):
        try:
            return self.dependency
        except AttributeError:
            raise ValueError("%s not inited" % self.cls.__name__)

    def __iter__(self):
        return iter([LocalProxy(self), self.init])
