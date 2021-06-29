# thiru sadagopan python poc
python based user book wish list CRUD REST App.
This POC offers creation, update, delete , listing of a user’s book wish list. Following are the application setup and test execution info.
Prerequisites
1. Flask (for REST )
2. Sqllite (Database)
3. Postman (for REST testing)
4. python

Checkout the project, and in the python_poc_1 folder (or your checked out folder)\

$<dir> python webapp.py (this runs the REST App)

# Code Info:- \
  1. webapp.py - REST Controller \
  2. UserWishListDao.py - Data Access Class that does the I/O with SQLLite DB \
  3. zonar.db - SQLLite DB with test-data

If you use the uploaded zonar db it has pre-loaded data , else you can refer to the following to upload data)

Connect to sqlliite ->Sqlite3 zonar.db

# DDL <br />
create table user (id integer, firstname text, lastname text, email text, password text, primary key(id)); <br />
Create table book(title text, author text, isbn text, date_of_publication date, primary key(isbn)); <br />
Create table user_wish_list(userid integer, bookid text, foreign key(userid) references user(id), foreign key(bookid) references book(isbn)); <br />

# Data insertion scripts:- <br />
insert into user values(1,"john", "doe", "john.doe@yahoo.com", "pass121”); <br />
insert into user values(2,”David”, “sams”, “david.sams@yahoo.com", "pass122”); <br />
insert into user values(3,”sam”, “johns”, “sam.johns@yahoo.com", "pass123"); <br />
insert into user values(4,”fred”, "murphy”, “fred.murphy@yahoo.com", "pass124”); <br />
insert into user values(5”Kevin”, “prince”, “Kevin.prince@yahoo.com", "pass125”); <br />

insert into book values("lake athabasca","Desmond bagely","1234-5678-9012-3456","2018-05-10"); <br />
insert into book values(“cry wolf”,”Desmond bagely","1114-3678-7012-3157”,”2017-04-10");<br />
insert into book values("Roads Unseen","Alistar McLean","1214-3679-4012-3147","2017-03-15"); <br />
insert into book values("Space Odyssey","Alistar McLean","1714-4679-1012-2147","2018-06-03"); <br />
insert into book values("Space Odyssey 2000","Alistar McLean","1794-4688-1011-2187","2019-04-02"); <br />

Insert into user_wish_list values(1, "1234-5678-9012-3456"); <br />
Insert into user_wish_list values(2, "1234-5678-9012-3456"); <br />
Insert into user_wish_list values(3, "1114-3678-7012-3157”,”2017-04-10"); <br />
Insert into user_wish_list values(4, "1794-4688-1011-2187"); <br />


You can use postman REST testing tool to run the following request and verify the responses <br />

# List all users  in the system<br />
http://127.0.0.1:5000/allusers <br />
   [ \
        "userid : 1",\
        "name : john doe",\
        "email : john.doe@yahoo.com"\
    ],\
    [\
        "userid : 2",\
        "name : David Sams",\
        "email : david.sams@yahoo.com"\
    ],\
    [\
        "userid : 3",\
        "name : Sam Johns",\
        "email : sam.johns@yahoo.com"\
    ],\
    [\
        "userid : 4",\
        "name : Fred Murphy",\
        "email : fred.murphy@yahoo.com"\
    ],\
    [\
        "userid : 5",\
        "name : Kevin Prince",\
        "email : kevin.prince@yahoo.com"\
    ]\

# List all Wishlists in the system<br />
http://127.0.0.1:5000/allwishlists <br />
[\
    [\
        "user name : Fred Murphy",\
        "book title : Space Odyssey 2000",\
        "isbn : 1794-4688-1011-2187"\
    ],\
    [\
        "user name : Sam Johns",\
        "book title : cry wolf",\
        "isbn : 1114-3678-7012-3157"\
    ]\
]
# Add Wish Lists <br/>
Add Wish List Success\
http://127.0.0.1:5000/addwishlist?userid=2&isbn=1234-5678-9012-3456<br />
[\
    "rowcount : 1",\
    "errorcode : SUCCESS”,\
    "message : successfully created David Sams's wish list for Book - lake athabasca"\
]\
Add Wish List with non-existing book/title\
http://127.0.0.1:5000/addwishlist?userid=2&isbn=1234-5678-9012-3499 \
[\
    "rowcount : 0",\
    "errorcode : BOOK_DETAILS_NOT_FOUND",\
    "message : Book 1234-5678-9012-3499 Not Found. Please Try Again"\
]
Add Wish List with non-existing User Id\
http://127.0.0.1:5000/addwishlist?userid=44&isbn=1234-5678-9012-3499\
[\
    "rowcount : 0",\
    "errorcode : USER_NOT_FOUND",\
    "message : User 44 Not Found. Please Try Again"\
]
# Update Wish List <br/>
Update Wish List with non-existing user id\
http://127.0.0.1:5000/updatewishlist?userid=99&oldisbn=1234-5678-9012-3456&newisbn=1794-4688-1011-2187\
[\
    "rowcount : 0",\
    "errorcode : USER_NOT_FOUND",\
    "message : User 99 Not Found. Please Try Again"\
]\
Update Wish List with non-existing book/title\
http://127.0.0.1:5000/updatewishlist?userid=2&oldisbn=1234-5678-9012-3456&newisbn=1794-4688-1011-ppppp\
[\
    "rowcount : 0",\
    "errorcode : BOOK_DETAILS_NOT_FOUND",\
    "message : New Book 1794-4688-1011-ppppp Not Found. Please Try Again"\
]\
Update Wish List - Success\
http://127.0.0.1:5000/updatewishlist?userid=2&oldisbn=1114-3678-7012-3157&newisbn=1794-4688-1011-2187\
[\
    "rowcount : 1",\
    "errorcode : SUCCESS”,\
    "message : successfully updated David Sams's wish list with Book - Space Odyssey 2000"\
]
# Delete Wish Lists<br />
Delete wish list non-existing book\
http://127.0.0.1:5000/deletewishlist?userid=2&isbn=1234-5678-9012-345\
[\
    "rowcount : 0",\
    "errorcode : BOOK_DETAILS_NOT_FOUND",\
    "message : Book 1234-5678-9012-345 Not Found. Please Try Again"\
]\
Delete wish list non-existing user id\
http://127.0.0.1:5000/deletewishlist?userid=99&isbn=1234-5678-9012-345\
[\
    "rowcount : 0",\
    "errorcode : USER_NOT_FOUND",\
    "message : User 99 Not Found. Please Try Again"\
]\
Delete Wish List - Success\
http://127.0.0.1:5000/deletewishlist?userid=2&isbn=1794-4688-1011-2187\
[\
    "rowcount : 1",\
    "errorcode : SUCCESS”,\
    "message : successfully deleted David Sams's wish list for Space Odyssey 2000"\
]
