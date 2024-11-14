class Computer:

    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def info_cpu(self):
        return self.__cpu

    @info_cpu.setter
    def set_cpu(self, value):
        self.__cpu = value

    @property
    def info_memory(self):
        return self.__memory

    @info_memory.setter
    def set_memory(self, value):
        self.__memory = value

    def make_computations(self):
        return self.__cpu * self.__memory

    def __str__(self):
        return f"Процессор:{self.__cpu} Память: {self.__memory}"

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory


class Phone:

    def __init__(self, sim_card_list):
        self.__sim_card_list = sim_card_list

    @property
    def sim_info(self):
        return self.__sim_card_list

    @sim_info.setter
    def set_sim(self, value):
        self.__sim_card_list = value

    def call(self, sim_card_number, call_to_number):
        print(f"Идет звонок на номер: {call_to_number}, с сим карты {sim_card_number}")

    def __str__(self):
        return f"Ваша сим карта {self.__sim_card_list}"


class SmartPhone(Computer, Phone):

    def __init__(self, cpu, memory, sim_card_list):
        Computer.__init__(self,cpu, memory)
        Phone.__init__(self,sim_card_list)


    def use_gps(self,location):
        print(f"До обьекта {location} осталось 1.5 км")

    def __str__(self):
        return f"Процессор:{self.info_cpu} Память: {self.info_memory} Сим карта: {self.sim_info}"

computer = Computer("intel core i7 7700",32)

phone = Phone("996 555 456 743")

android = SmartPhone("snapdragon", 64 , "996 554 212 456")

iphone = SmartPhone("Apple Silicon", 32,"996 555 723 111")

device = [computer,phone,iphone,android]

for i in device:
    print(i)

android.use_gps("Дом культуры")
phone.call("1 Белайн",iphone.sim_info)
print(f"У андроида боьше памяти чем у айфона {android > iphone}")
print(f"У айфона больше памяти чем у андроида {android < iphone}")
print(f"У компьютера и андроида одинаково памяти   {android == computer}")
print(f"У компьютера и афйона разное колличество памяти {iphone != computer}")
print(f"У компьютера меньше памяти или равно как у андроида {android <= computer}")
print(f"У компьютера больше памяти или равно как у андроида  {android >= computer}")




