import json
import requests

def test_add_wishlist_success():
 # response = requests.post("http://127.0.0.1:5000/addwishlist?userid=2&isbn=1234-5678-9012-3499")
 response = requests.get("http://127.0.0.1:5000/allwishlists")
 assert response.headers["Content-Type"] == "application/json"
 response_body = response.json()
 assert response.status_code == 200
 print(str(response_body))
