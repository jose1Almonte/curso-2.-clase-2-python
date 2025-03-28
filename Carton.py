import random


class Carton:

    def __init__(self, ids):
        self.id = self.generate_id(ids)
        self.carton = self.inicializarCarton()

    def show_card(self):
        print(f"      {self.id}        ")
        print("B  I  N  G  O")
        for row in self.carton:
            for i in range(len(row)):
                if i == len(row)-1:
                    print(f"{row[i]}")
                elif len(str(row[i])) < 2:
                    print(f"{row[i]}  ", end="")
                else:
                    print(f"{row[i]} ", end="")

    def generate_id(self, ids:list):
        while True:
            id = random.randint(1,100)
            if id not in ids:
                ids.append(id)
                return id
    
    def inicializarCarton(self):
        completed_carton = []

        putted_numbers = []
        nmbr_rows_putted = 0
        
        while nmbr_rows_putted < 5:
            row = [1,16,31,46,61]
            column_counter = 0
            while(column_counter < 5):
                if (column_counter < 4):
                    random_number = round(random.randint(row[column_counter],row[column_counter+1]-1))
                else:
                    random_number = round(random.randint(row[column_counter],75))

                if random_number not in putted_numbers:
                    putted_numbers.append(random_number)
                    row[column_counter] = random_number
                else:
                    continue

                column_counter+=1
            completed_carton.append(row)
            nmbr_rows_putted += 1
        return completed_carton
    
    def marcar_carton(self,letra: str, ficha: int):
        match(letra):
            case "B":
                column = 0
            case "I":
                column = 1
            case "N":
                column = 2
            case "G":
                column = 3
            case "O":
                column = 4
        
        for i in range(len(self.carton)):
            if self.carton[i][column] == ficha:
                self.carton[i][column] = "X"

    def gano_carton_lleno(self):
        gano = True
        for row in self.carton:
            for element in row:
                if element != "X":
                    gano = False
        
        return gano, "Carton lleno"

ids = []
carton = Carton(ids)

carton.show_card()
