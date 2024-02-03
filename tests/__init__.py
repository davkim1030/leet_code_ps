import abc


class PSTestCase(abc.ABC):
    @abc.abstractmethod
    def solution(self, *args, **kwargs) -> any:
        pass
