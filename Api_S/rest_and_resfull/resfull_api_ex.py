from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
books = [
    {"id": 1, "title": "Python Programming", "author": "John Doe"},
    {"id": 2, "title": "Web Development", "author": "Jane Smith"}
]

@app.route('/books', methods=['GET', 'POST'])
def handle_books():
    if request.method == 'GET':
        return jsonify(books)
    elif request.method == 'POST':
        new_book = request.json
        books.append(new_book)
        return jsonify({"message": "Book added successfully"}), 201

@app.route('/books/<int:book_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_book(book_id):
    if request.method == 'GET':
        for book in books:
            if book['id'] == book_id:
                return jsonify(book)
        return jsonify({"error": "Book not found"}), 404
    elif request.method == 'PUT':
        for idx, book in enumerate(books):
            if book['id'] == book_id:
                books[idx] = request.json
                return jsonify({"message": "Book updated successfully"})
        return jsonify({"error": "Book not found"}), 404
    elif request.method == 'DELETE':
        for idx, book in enumerate(books):
            if book['id'] == book_id:
                del books[idx]
                return jsonify({"message": "Book deleted successfully"})
        return jsonify({"error": "Book not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
