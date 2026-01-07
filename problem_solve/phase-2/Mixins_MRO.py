"""
Problem:
- Create:
    - LoggerMixin
    - AuthMixin

- Create a Service class that inherits both
- Call a method and observe MRO

Hint:
Use super() correctly
"""

class LoggerMixin:
    def log(self, *args, **kwargs):
        print(f"[LOG]", *args)
        super().log(*args, **kwargs)

    def auth(self, *args, **kwargs):
        super().auth(*args, **kwargs)

class AuthMixin:
    def auth(self, *args, **kwargs):
        print(f"[AUTH]", *args)
        super().auth(*args, **kwargs)

    def log(self, *args, **kwargs):
        super().log(*args, **kwargs)

class LoggerAuthService(LoggerMixin, AuthMixin):
    def service(self, name: str) -> None:
        self.name = name
        print("LoggerAuthSerive", self.name)
        super().log("Service Started")
        super().auth("authentication done")


print(LoggerAuthService.__mro__)
service = LoggerAuthService()
service.service("text")