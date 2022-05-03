from typing import Any, Dict, Tuple

class Status:
    def __init__(self, name: str) -> None:
        self.name = name
        self._werror = None
        self._value = None
        self._status = None

    
    @property
    def vvalue(self) -> Any:
        return self._value

    @vvalue.setter
    def vvalue(self, _value: Any):
        self._value = _value
        self.status = True


    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, _status):
        self._status = _status

    @property
    def werror(self)-> Dict:
        return self._werror
    
    @werror.setter
    def werror(self, args: Tuple[Any, str]):
        _type, _message = args
        self.status = False
        _error = {
            'type': _type,
            "message": _message
        }
        self._werror = _error

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        return self.value
