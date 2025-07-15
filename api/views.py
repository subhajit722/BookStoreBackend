from rest_framework.decorators import api_view
from rest_framework.response import Response

#data
books = [
    {
        "id": 1,
        "title": "Harry Potter and the Sorcerer's Stone",
        "author": "J.K. Rowling",
        "price": 399,
        "image": "https://m.media-amazon.com/images/I/81YOuOGFCJL._AC_UF1000,1000_QL80_.jpg",
        "description": "A young wizard begins his magical journey at Hogwarts School of Witchcraft and Wizardry."
    },
    {
        "id": 2,
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "price": 299,
        "image": "https://m.media-amazon.com/images/I/91b0C2YNSrL._AC_UF1000,1000_QL80_.jpg",
        "description": "Bilbo Baggins sets out on an adventure with dwarves to reclaim a lost kingdom from a dragon."
    },
    {
        "id": 3,
        "title": "1984",
        "author": "George Orwell",
        "price": 199,
        "image": "https://m.media-amazon.com/images/I/71kxa1-0mfL._AC_UF1000,1000_QL80_.jpg",
        "description": "A dystopian novel that explores totalitarianism and surveillance in a frightening future."
    },
 
    {
        "id": 7,
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "price": 229,
        "image": "https://m.media-amazon.com/images/I/71aFt4+OTOL._AC_UF1000,1000_QL80_.jpg",
        "description": "A mystical tale about finding one's destiny and listening to your heart."
    },
    
  
]



orders = []

@api_view(['GET'])
def get_books(request):
    return Response(books)

@api_view(['POST'])
def create_order(request):
    data = request.data

    # ✅ Use `.get()` to safely access dict keys
    book_id = data.get("book_id")
    customer_name = data.get("customer_name")

    if not book_id or not customer_name:
        return Response({"error": "Missing book_id or customer_name"}, status=400)

    new_order = {
        "book_id": book_id,
        "customer_name": customer_name,
    }
    orders.append(new_order)
    return Response({"message": "Order placed successfully", "order": new_order}, status=201)
