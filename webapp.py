# File name: webapp.py 
from flask import Flask,request
from flask import jsonify
import UserWishListDao as sqlDao

app = Flask(__name__) 

@app.route("/allusers", methods=['GET']) 
def allusers(): 
   result = sqlDao.getAllUsers()
   return jsonify(result)

@app.route("/allwishlists", methods=['GET']) 
def allwishlists(): 
   result = sqlDao.getAllWishLists()
   return jsonify(result)

@app.route('/addwishlist', methods=['POST']) 
def addwishlist(): 
   userid = request.args.get('userid', '')
   isbn = request.args.get('isbn', '')
   response = sqlDao.addWishList(userid, isbn)
   return jsonify(response)

@app.route('/updatewishlist', methods=['PUT']) 
def updatewishlist(): 
   userid = request.args.get('userid', '')
   oldisbn = request.args.get('oldisbn', '')
   newisbn = request.args.get('newisbn', '')
   response = sqlDao.updateWishList(userid, oldisbn, newisbn)
   return jsonify(response)

@app.route('/deletewishlist', methods=['GET']) 
def deletewishlist(): 
   userid = request.args.get('userid', '')
   isbn = request.args.get('isbn', '')
   response = sqlDao.deleteWishList(userid, isbn)
   return jsonify(response)

if __name__ == '__main__': 
   app.run(port=5000, debug=True) #
