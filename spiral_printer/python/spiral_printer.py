eg_array = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]


class SpirtalPrinter:
    def __init__(self,
                 array_2d,
                 start_print_dimension='row',
                 start_print_direction='asc'):
        self.start_array_2d = [[*item] for item in array_2d]
        self.start_print_dimension = start_print_dimension
        self.start_print_direction = start_print_direction

    def _transpose(self, array_2d):
        return list(map(list, zip(*array_2d)))

    def _reverse(self, array_2d):
        return [item for item in reversed(array_2d)]

    def print(self):
        array_2d = [[*item] for item in self.start_array_2d]

        if self.start_print_dimension == 'col':
            array_2d = self._transpose(array_2d)

        if self.start_print_direction == 'desc':
            array_2d = self._reverse(array_2d)

        array_2d_copy = [[*item] for item in array_2d]

        string_to_print = ''

        while array_2d:
            for _ in array_2d[0]:
                string_to_print += str(array_2d_copy[0][0]) + ' '
                array_2d_copy[0].pop(0)
            array_2d_copy = [item for item in array_2d_copy if item]
            array_2d_copy = self._transpose(array_2d_copy)
            array_2d_copy = self._reverse(array_2d_copy)
            array_2d = [[*item] for item in array_2d_copy]

        return print(string_to_print.strip())

printer = SpirtalPrinter(eg_array)
printer.print()
