# flask-dependency

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
