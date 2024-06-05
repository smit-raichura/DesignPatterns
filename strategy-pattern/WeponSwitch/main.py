from abc import ABC, abstractmethod

## Wepons Class

class Wepon_Strategy(ABC):
    @abstractmethod
    def type(self):
        pass

class HandGun(Wepon_Strategy):
    def type(self):
        return "This is a HandGun! Pew Pew Pew..."

class Melle(Wepon_Strategy):
    def type(self):
        return "This is a Melle! Slash Slash Slash..."

class AutomatedRifle(Wepon_Strategy):
    def type(self):
        return "This is a AR! =><=*=><="
    

class EquipWepon:
    def __init__(self, wepon: Wepon_Strategy):
        self._wepon = wepon
    
    def set_wepon(self, wepon: Wepon_Strategy):
        self._wepon = wepon

    def get_type(self):
        return self._wepon.type()


## driver function

wepon = EquipWepon(Melle())
wepon_type = wepon.get_type() 
print(wepon_type)

wepon.set_wepon(AutomatedRifle())
print(wepon.get_type())