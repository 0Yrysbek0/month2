class Computer:
    def init(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @property
    def memory(self):
        return self.__memory

    @cpu.setter
    def cpu(self, new_cpu):
        self.__cpu = new_cpu

    @memory.setter
    def memory(self, new_memory):
        self.__memory = new_memory

    def make_computations(self):
        # Выполнить арифметические вычисления с cpu и memory
        result = self.cpu + self.memory
        return result

    def str(self):
        return f"Компьютер: CPU - {self.cpu}, Память - {self.memory}"


class Phone:
    def init(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, new_sim_cards_list):
        self.__sim_cards_list = new_sim_cards_list

    def call(self, sim_card_number, call_to_number):
        print(f"Симуляция звонка с сим-карты-{sim_card_number} на номер {call_to_number}")

    def str(self):
        return f"Телефон: Список сим-карт - {self.__sim_cards_list}"


class SmartPhone(Computer, Phone):
    def init(self, cpu, memory, sim_cards_list):
        Computer.init(self, cpu, memory)
        Phone.init(self, sim_cards_list)

    def use_gps(self, location):
        print(f"Симуляция прокладывания маршрута до {location}")

    def str(self):
        return f"Смартфон: CPU - {self.cpu}, Память - {self.memory}, Сим-карты - {self.sim_cards_list}"


# Создание объектов
computer_obj = Computer(cpu="Intel i5", memory = 8)
phone_obj = Phone(sim_cards_list = ["Билайн", "Мегафон"])
smartphone1_obj = SmartPhone(cpu = "Snapdragon", memory=6, sim_cards_list=["МТС", "Теле2"])
smartphone2_obj = SmartPhone(cpu = "Apple A14", memory=4, sim_cards_list=["T-Mobile", "AT&T"])

# Вывод информации о созданных объектах
print(computer_obj)
print(phone_obj)
print(smartphone1_obj)
print(smartphone2_obj)

# Тестирование методов
result_computations = computer_obj.make_computations()
phone_obj.call(sim_card_number=1, call_to_number="123-456-7890")
smartphone1_obj.use_gps(location="Дом")

# Тестирование магических методов
print(computer_obj == smartphone1_obj)
print(computer_obj < smartphone2_obj)