const arr = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10,11, 12],
    [13, 14, 15, 16]
]

class SpriralPrinter {
    constructor(array_2d) {
        this.start_array_2d = array_2d
    }

    _transpose(matrix) {
        const rows = matrix.length, cols = matrix[0].length
        const transposed_matrix = []
        for (let j = 0; j < cols; j++) {
            transposed_matrix[j] = Array(rows)
        }
        for (let i = 0; i < rows; i++) {
            for (let j = 0; j < cols; j++) {
                transposed_matrix[j][i] = matrix[i][j]
            }
        }
        return transposed_matrix
    }

    _reverse(array) {
        return array.reverse()
    }

    print() {
        let array_2d = [...this.start_array_2d]
        console.log('input matrix: ', array_2d)

        let string = ''

        while (array_2d.length > 0) {
            const row = array_2d.splice(0, 1)[0]
            row.forEach(element => { string += ` ${element} `})

            if (array_2d.length > 0) {
                array_2d = this._transpose(array_2d)
                array_2d = this._reverse(array_2d)
            }
        }

        console.log('output: ', string.trim())
    }
}

const printer = new SpriralPrinter(arr)
printer.print()


