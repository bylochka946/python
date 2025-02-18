class Car:
    """Базовый класс автомобиля"""

    def __init__(self, make: str, model: str, seats: int):
        self.make = make
        self.model = model
        self.seats = seats

    def __str__(self) -> str:
        """Магический метод __str__"""

        return f"Автомобиль марки {self.make}, модели {self.model}, вместимостью {self.seats}"

    def __repr__(self) -> str:
        """Магический метод __repr__"""

        return f"{self.__class__.__name__}(make = {self.make!r}, model = {self.model!r}, seats = {self.seats!r})"

    def move(self) -> str:
        """Метод выводящий в консоль информацию о том, что автомобиль движется"""

        return f"Транспортное средство {self.make} {self.model} движется"

    def capacity_(self) -> str:
        """Метод, выводящий в консоль информацию о вместительности автомобиля"""

        return f"Транспортное средство вмещает в себя {self.seats}"


class PassengerCar(Car):
    """Дочерний класс автомобиля"""

    def __init__(self, make: str, model: str, seats: int, people: int):
        super().__init__(make, model, seats)  # вызов конструктора родительского класса с помощью функции super()
        self.people = people

    def __str__(self) -> str:
        """Магический метод __str__
        Перегружен с целью уточнения типа автомобиля"""

        return f"Легковой автомобиль марки {self.make}, модели {self.model}, вместимостью {self.seats} человек"

    def __repr__(self) -> str:
        """Магический метод __repr__"""

        return f"{self.__class__.__name__}(make = {self.make!r}, model = {self.model!r}, seats = {self.seats!r})"

    def capacity_(self) -> None:
        """Перегруженный метод capacity, который проверяет поместиться ли заданное количество людей в машину"""
        if not isinstance(self.people, int):
            raise TypeError("Количество людей должно быть типа int")
        if self.people < 0:
            raise ValueError("Количество людей не может быть меньше 0")
        if self.seats < self.people:
            raise ValueError("Количество людей не может быть равно больше количества мест в машине")


if __name__ == "__main__":
    car = Car("BMW", "Coupe", 5)
    print(car)
    print(car.move())
    print(car.capacity_())

    passengerCar = PassengerCar("Audi", "Q7", 5, 2)
    print(passengerCar)
    print(passengerCar.move())
    print(passengerCar.capacity_())
pass
