from flask import Flask, render_template, request, jsonify
from sudoku_solver import solve_sudoku

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    data = request.json
    puzzle = data['puzzle']
    solution = solve_sudoku(puzzle)
    return jsonify({'solution': solution})

if __name__ == '__main__':
    app.run(debug=True)
