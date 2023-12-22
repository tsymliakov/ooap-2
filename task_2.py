# Класс- родитель
class FuelCar:
    def __init__(self, max_speed, fuel_consumption, tank_capacity):
        self.max_speed = max_speed
        self.fuel_consumption = fuel_consumption
        self.tank_capacity = tank_capacity

    def drive(self, acceleration):
        """
        Едет и тратит топливо
        """
        pass

    # Прочие методы

# Наследование- специализация
# Наследник обязан обладать рейтингом безопасности
class FamilyCar(FuelCar):
    def __init__(self,
                 max_speed,
                 fuel_consumption,
                 tank_capacity,
                 safety_rating):
        self.safety_rating = safety_rating
        super().__init__(max_speed, fuel_consumption, tank_capacity)


# Наследование- расширение
# Наследник расширяет родителя, позволяя ему работать не только от топлива, но и
# от электричества
class Car(FuelCar):
    def __init__(self,
                 max_speed,
                 engine,
                 energy_consumption,
                 energy_storage_volume):
        self.max_speed = max_speed
        self.engine = engine
        self.energy_consumption = energy_consumption
        self.energy_storage_volume = energy_storage_volume

    def drive(self, acceleration):
    # А тут должна быть прописана логика взаимодействия с объектом- двигателем,
    # который может быть как двигателем сгорания, а может быть и электрическим
