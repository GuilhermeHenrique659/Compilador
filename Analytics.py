from abc import ABC, abstractmethod

class AbstractAnalytics(ABC):

    @abstractmethod
    def analytics(self):
        pass
