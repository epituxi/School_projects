def add_new_movie_and_rating(dictionary, movie, rating):
#Implement your code here

    if movie in dictionary.keys():
        print(f"{movie} is already in the database. Choose 2 if you want to change the rating of the movie.")
    else:
        dictionary[movie] = rating
        print(f"{movie} has been added into the database.\n")

    return dictionary

def change_rating(dictionary, movie, rating):
    # Implement your code here
    pass

def print_all_movies(dictionary):
    # Implement your code here
    pass

def find_movies_with_rating(dictionary, rating):
    # Implement your code here
    pass

def ask_user_input():
    print("Choose 1-5.")
    print("1: Add a new movie and rating.")
    print("2: Change the rating of the movie.")
    print("3: Print all movies and their ratings.")
    print("4: Find all movies with a specific rating.")
    print("5: Exit.")
    while True:
        #mode = int(input())
        mode = 1
        if 1 <= mode <= 5:
            return mode
        print("You chose an invalid number.")

def main():
    print("Welcome to the database of the movie ratings.\n")
    # Implement your code here
    movies = dict()
    while True:
        mode = ask_user_input()
        if mode == 1:
            movie_name = str(input("Enter the movie.\n"))
            movie_rating = int(input("Enter the rating (4-10).\n"))
            movies = add_new_movie_and_rating(movies, movie_name, movie_rating)
            print(movies)
        elif mode == 5:
            break



main()