# Incomplete app!

MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


# You may want to create a function for this code
def addMovie():

    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
            'title': title,
            'director': director,
            'year': year
        })

# Create other functions for:
#   - listing movies
def listingMovies():
    for index in movies:
        print(index["title"])
        print(index["director"])
        print(index["year"])

#   - finding movies
def findingMovies():
    InMovie = input("Enter your title movie")
    for index in movies:
        if InMovie == index["title"]:
            print(index["title"])
            print(index["director"])
            print(index["year"])
        else:
            print("movie no found")


# And another function here for the user menu
selection = input(MENU_PROMPT)
while selection != 'q':
    if selection == "a":
        addMovie()
    elif selection == "l":
        listingMovies()
    elif selection == "f":
        findingMovies()
    else:
        print('Unknown command. Please try again.')

    selection = input(MENU_PROMPT)


# Remember to run the user menu function at the end!