class MenuItem:
    def __init__(self, code: str, name: str, price: float):
        self.code = code
        self.name = name
        self.price = price
    
    @property
    def get_code(self) -> str:
        return self.code
    
    @get_code.setter
    def set_code(self, code: str) -> None:
        self.code = code

    @property
    def get_name(self) -> str:
        return self.name

    @get_name.setter
    def set_name(self, name: str) -> None:
        self.name = name

    @property
    def get_price(self) -> float:
        return self.price
    
    @get_price.setter
    def set_price(self, price: float) -> None:
        self.price = price

    # without this, printing MenuItem object will show memory location --> eg: <__main__.MenuItem object at 0x7fabc1234cd0>
    # with this, it will show a more meaningful representation of the object --> eg: MenuItem(code='M01', name='Pasta', price=1200)
    
    def __repr__(self):
        return f"MenuItem(code='{self.code}', name='{self.name}', price={self.price})"
