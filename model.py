class Figure:

    def __init__(self, length, width) -> None:
        self.length = int(length)
        self.width = int(width)
        self.area = self.calculate_area()

    def calculate_area(self):
        return self.length * self.width / 1000000

    def get_area(self):
        return self.area

    def __str__(self) -> str:
        return f"Length = {self.length}, width = {self.width}, area = {self.area:.2f}"

    def update(self, new_length, new_width):
        self.length = int(new_length)
        self.width = int(new_width)
        self.area = self.calculate_area()


class ListFigures:

    def __init__(self) -> None:
        self.list = []

    def add_figure(self, figure: Figure):
        self.list.append(figure)

    def get_list_figures(self):
        return self.list

    def __iter__(self):
        return iter(self.list)

    def __len__(self):
        return len(self.list)

    def __str__(self) -> str:
        ret_str = ''
        k = 1
        for i in self.get_list_figures():
            ret_str += str(k) + ". " + str(i) + "\n"
            k += 1
        return ret_str


def all_area_figures(list_figures: ListFigures):
    result = 0
    for i in list_figures:
        result += i.get_area()
    return f'{(result / 2.8 * 1.15):.2f}'
