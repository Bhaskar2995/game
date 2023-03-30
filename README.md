# Game (CRUD operations)
This is a an api (Application Programming Interface) where one can perform CRUD operations.

Website : http://bhaskar007.pythonanywhere.com

**GET request**:  http://bhaskar007.pythonanywhere.com/games

output: All the games which are present in the database gets displayed

**POST request**: http://bhaskar007.pythonanywhere.com/games

example body : {
    "name": "Cricket",
    "url":"https://www.ea.com/games/cricket",
    "author": "Some author",
    "published_date": "2006-05-21"
    }
    
**PUT request**: http://bhaskar007.pythonanywhere.com/games/{id}

example: http://bhaskar007.pythonanywhere.com/games/2
body: 
{
    "name": "Cricket",
    "url":"https://www.ea.com/games/cricket",
    "author": "changed author name",
    "published_date": "2006-05-21"
    }
    
**DELETE request**: http://bhaskar007.pythonanywhere.com/games/{id}

example: http://bhaskar007.pythonanywhere.com/games/2
Game with id=2 will be deleted
