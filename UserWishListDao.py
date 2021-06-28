import sqlite3 

def getAllUsers():
	conn = sqlite3.connect('zonar.db')
	cursor = conn.cursor()
	result = cursor.execute("SELECT 'userid : '||id,'name : '||(firstname ||\" \"|| lastname), 'email : '||email from user").fetchall()
	return result

def getAllWishLists():
	conn = sqlite3.connect('zonar.db')
	cursor = conn.cursor()
	result = cursor.execute("SELECT 'user name : '||(u.firstname ||\" \"|| u.lastname) , 'book title : '||b.title, 'isbn : '||b.isbn "+
		"from user_wish_list uw, user u, book b "+
		"where uw.userid=u.id and uw.bookid=b.isbn").fetchall()
	return result

def getUserDetails(userid):
	conn = sqlite3.connect('zonar.db')
	cursor = conn.cursor()
	id = int(userid)
	row = cursor.execute("SELECT firstname, lastname from user where id = ?",[id]).fetchone()
        if row is None:
         return "USER_NOT_FOUND"
        else :
	 return row[0]+" "+row[1]

def getBookTitle(isbn):
	conn = sqlite3.connect('zonar.db')
	cursor = conn.cursor()
	row = cursor.execute("SELECT title from book where isbn = ?",[isbn]).fetchone()
        if row is None:
         return "BOOK_DETAILS_NOT_FOUND" 
        else :
	 return row[0]

def addWishList(userid, isbn):
   try:
    sqliteConnection = sqlite3.connect('zonar.db')
    response = []
    cursor = sqliteConnection.cursor()

    user_detail = getUserDetails(userid)
    if user_detail == "USER_NOT_FOUND" :
     response.append("rowcount : 0")
     response.append("errorcode : USER_NOT_FOUND")
     response.append("message : User "+userid+" Not Found. Please Try Again")
     return response

    book_detail = getBookTitle(isbn)
    if book_detail == "BOOK_DETAILS_NOT_FOUND" :
     response.append("rowcount : 0")
     response.append("errorcode : BOOK_DETAILS_NOT_FOUND")
     response.append("message : Book "+isbn+" Not Found. Please Try Again")
     return response

    sqlite_insert_query = "INSERT INTO user_wish_list (userid, bookid) VALUES (?, ?)"
    id = int(userid)
    result = cursor.execute(sqlite_insert_query, (id, isbn))
    sqliteConnection.commit()
    response.append("rowcount : "+str(result.rowcount))
    if result.rowcount == 1 :
     response.append("errorcode : SUCCESS")
     response.append("message : successfully created "+getUserDetails(userid)+"'s wish list for Book - "+getBookTitle(isbn))
    else :
     response.append("errorcode : FAILURE")
     response.append("message : failed to add ["+user_detail+"-"+userid+"] Book - "+newisbn+" "+book_detail)

    return response
    cursor.close()

   except sqlite3.Error as error:
    print("Failed to insert data into user_wish_list table", error)
    return {'rowcount' : 0, 'message':"Failed to insert data into user_wish_list table - "+error}
   finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")

def updateWishList(userid, oldisbn, newisbn):
   try:
    sqliteConnection = sqlite3.connect('zonar.db')
    cursor = sqliteConnection.cursor()

    user_detail = getUserDetails(userid)
    response = []

    if user_detail == "USER_NOT_FOUND" :
     response.append("rowcount : 0")
     response.append("errorcode : USER_NOT_FOUND")
     response.append("message : User "+userid+" Not Found. Please Try Again")
     return response

    book_detail = getBookTitle(oldisbn)
    if book_detail == "BOOK_DETAILS_NOT_FOUND" :
     response.append("rowcount : 0")
     response.append("errorcode : BOOK_DETAILS_NOT_FOUND")
     response.append("message : Book "+oldisbn+" Not Found. Please Try Again")
     return response

    book_detail = getBookTitle(newisbn)
    if book_detail == "BOOK_DETAILS_NOT_FOUND" :
     response.append("rowcount : 0")
     response.append("errorcode : BOOK_DETAILS_NOT_FOUND")
     response.append("message : New Book "+newisbn+" Not Found. Please Try Again")
     return response

    sqlite_update_query = "UPDATE user_wish_list set bookid = ? where userid = ? and bookid = ?"
    result = cursor.execute(sqlite_update_query, (newisbn, int(userid), oldisbn))
    sqliteConnection.commit()
    response.append("rowcount : "+str(result.rowcount))

    if result.rowcount == 1 :
     response.append("errorcode : SUCCESS")
     response.append("message : successfully updated "+user_detail+"'s wish list with Book - "+getBookTitle(newisbn))
    else :
     response.append("errorcode : FAILURE")
     response.append("message : failed to update ["+user_detail+"] Book - "+newisbn+" "+book_detail)

    return response
    cursor.close()
   except sqlite3.Error as error:
    print("Failed to update data in user_wish_list table", error)
    return "Failed to update data in user_wish_list table - "+error
   finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")

def deleteWishList(userid, isbn):
   try:
    sqliteConnection = sqlite3.connect('zonar.db')
    cursor = sqliteConnection.cursor()
    response = []

    user_detail = getUserDetails(userid)
    if user_detail == "USER_NOT_FOUND" :
     response.append("rowcount : 0")
     response.append("errorcode : USER_NOT_FOUND")
     response.append("message : User "+userid+" Not Found. Please Try Again")
     return response

    book_detail = getBookTitle(isbn)
    if book_detail == "BOOK_DETAILS_NOT_FOUND" :
     response.append("rowcount : 0")
     response.append("errorcode : BOOK_DETAILS_NOT_FOUND")
     response.append("message : Book "+isbn+" Not Found. Please Try Again")
     return response

    sqlite_delete_query = "DELETE FROM user_wish_list where bookid = ? and userid = ?"
    result = cursor.execute(sqlite_delete_query, (isbn, int(userid)))
    sqliteConnection.commit()
    response.append("rowcount : "+str(result.rowcount))
    if result.rowcount == 1 :
     response.append("errorcode : SUCCESS")
     response.append("message : successfully deleted "+user_detail+"'s wish list for "+book_detail)
    else :
     response.append("errorcode : FAILURE")
     response.append("message : failed to delete ["+user_detail+"-"+userid+"] Book - "+isbn+" "+book_detail)

    return response
    cursor.close()

   except sqlite3.Error as error:
    print("Failed to delete data in user_wish_list table", error)
    return {'rowcount' : 0, 'message':"Failed to delete data in user_wish_list table - "+error}
   finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("deleteWishList() - The SQLite connection is closed")


