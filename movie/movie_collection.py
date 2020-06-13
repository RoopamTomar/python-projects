Selection ="Enter 'a' to add movies,'s' to search movie,'l' to find the list of all movies in database,'d' to delete,'q' to quit : "
movies = []
titlee = []


def add_movie():
    number = int(input("how many movies you want to add : "))
    for movie in range(number):
            title = input("Enter Movie name : ").title().strip("")
            director_name = input("Enter Director name : ").title()
            release_year = int(input("Enter Release year of movie :"))
            movies.append({ 'title': title,
                            'director_name': director_name,
                            'release_year': release_year
                            })
    for name in movies:
        titlee.append(name['title'])


def search():
    movie_name = input("Enter the name of the movie which you want to search in database: ").title()
    if movie_name in titlee:
        for movie in movies:
            if movie_name == movie['title']:
                print("{} released in year {} by {}".format(movie['title'],movie['release_year'],movie['director_name']))
    else:
         print("The movie that you want to search is not in the database")



def movie_details():
    for movie in movies:
        print("{} released in year {} by {}".format(movie['title'], movie['release_year'], movie['director_name']))

def delete_movie():
    del_movie = input("Enter the name of the movie that you want to delete : ").title().strip("")
    count = -1
    if del_movie in titlee:
        for movie in movies:
            count += 1
            if del_movie == movie['title']:
                del(movies[count])
                del(titlee[count])

    else:
        print("The movie that you want to delete does not exist")

def menu():
    user_input= input(Selection)
    while user_input != 'q':
        if user_input == 'a':
               add_movie()
        elif user_input == 's':
                search()
        elif user_input == 'l':
             movie_details()
        elif user_input == 'd':
             delete_movie()
        else:
               print("Please enter from given instructions")
        user_input = input(Selection)



menu()




