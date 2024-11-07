class House:                                                # 1
    def __init__(self, name, number_of_floors):             # 2
        self.name = name                                    # 3
        self.number_of_floors = number_of_floors            # 3

    def go_to(self, new_floor):                             # 4
        if 1 <= new_floor <= self.number_of_floors:
            for i in range(1, new_floor + 1):
                print (i)
        else:
            print ('Такого этажа не существует')
            # а по заданию надо поставить вместо 0 (или убрать) => 1



h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
