from flask import Flask, request, jsonify
from flask_cors import CORS
from elasticsearch import Elasticsearch

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests
es = Elasticsearch(
    ["https://localhost:9200"],  # URL of the Elasticsearch instance
    basic_auth=("elastic", "VveuHxqi2inw=SlGgGTc"),  # Replace with the correct credentials
    verify_certs=False  # Disable certificate verification for local testing
)

INDEX_NAME = "books"  # Index for book data

# Search for books
@app.route("/search", methods=["GET"])
def search_books():
    query = request.args.get("query", "")
    page = int(request.args.get("page", 1))
    size = 20
    start = (page - 1) * size
    body = {
        "query": {
            "multi_match": {
                "query": query,
                "fields": ["title", "author", "genre", "description"]
            }
        },
        "from": start,
        "size": size
    }
    res = es.search(index=INDEX_NAME, body=body)
    return jsonify({
        "books": [hit["_source"] | {"id": hit["_id"]} for hit in res["hits"]["hits"]],
        "total": res["hits"]["total"]["value"]
    })

# Fuzzy search for suggestions
@app.route("/fuzzy_search", methods=["GET"])
def fuzzy_search():
    query = request.args.get("query", "")
    body = {
        "query": {
        "match": {
            "title": {
                "query": query,
                "fuzziness": "AUTO",
                "operator": "and"  # Ensure all terms are considered
            }
        }
    },
    "size": 5  # Limit the number of suggestions
    }
    res = es.search(index=INDEX_NAME, body=body)
    suggestions = [hit["_source"]["title"] for hit in res["hits"]["hits"]]
    return jsonify({"suggestions": suggestions})

# Add a new book
@app.route("/add", methods=["POST"])
def add_book():
    book = request.json
    es.index(index=INDEX_NAME, body=book)
    return jsonify({"message": "Book added successfully"}), 201

# Update a book
@app.route("/update/<id>", methods=["PUT"])
def update_book(id):
    book = request.json
    try:
        es.update(index=INDEX_NAME, id=id, body={"doc": book})
        return jsonify({"message": "Book updated successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Delete a book
@app.route("/delete/<id>", methods=["DELETE"])
def delete_book(id):
    es.delete(index=INDEX_NAME, id=id)
    return jsonify({"message": "Book deleted successfully"})

# Wishlist and Read Books Management
wishlist = []
read_books = []


@app.route("/wishlist", methods=["GET", "POST"])
def manage_wishlist():
    if request.method == "GET":
        return jsonify(wishlist)
    elif request.method == "POST":
        book = request.json
        if book not in wishlist:
            wishlist.append(book)
        return jsonify({"message": "Book added to wishlist"})

@app.route("/wishlist_remove", methods=["POST"])
def remove_from_wishlist():
    global wishlist
    book = request.json
    # Filter out the book to remove it from the wishlist
    wishlist = [w for w in wishlist if w.get("id") != book.get("id")]
    return jsonify({"message": "Book removed from wishlist"}), 200


@app.route("/mark_as_read", methods=["POST"])
def mark_as_read():
    book = request.json
    if book in wishlist:
        wishlist.remove(book)
    if book not in read_books:
        read_books.append(book)
    return jsonify({"message": "Book marked as read"})

@app.route("/read_books", methods=["GET", "POST"])
def manage_read_books():
    global read_books
    if request.method == "GET":
        return jsonify(read_books)
    elif request.method == "POST":
        action = request.json.get("action")
        book = request.json.get("book")

        if action == "remove":
            read_books = [rb for rb in read_books if rb.get("id") != book.get("id")]
            return jsonify({"message": "Book removed from Read Books"}), 200

        return jsonify({"error": "Invalid action"}), 400
    
@app.after_request
def add_no_cache_header(response):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response



if __name__ == "__main__":
    app.run(debug=True)
