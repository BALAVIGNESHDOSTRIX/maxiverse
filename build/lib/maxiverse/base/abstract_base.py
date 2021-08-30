from abc import ABC, abstractmethod

class AbstractEval(ABC):
    
    @abstractmethod
    def _perform_validate(self, nmdl=[]):
        pass
    
    @abstractmethod
    def _cross_validate(self, model):
        pass