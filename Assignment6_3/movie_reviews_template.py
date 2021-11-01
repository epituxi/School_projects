def add_new_movie_and_rating(dictionary, movie, rating):
    
    #Implement your code here

    if movie in dictionary.keys():
        return False
    else:
        dictionary[movie] = rating

    return True

def change_rating(dictionary, movie, rating):

    # Implement your code here

    if movie in dictionary.keys():
        dictionary[movie] = rating
    else:
        return False

    return True

def print_all_movies(dictionary):
    
    # Implement your code here
    
    dictionary_items = dictionary.items()
    sorted_items = sorted(dictionary_items)

    for movie, rating in sorted_items:
        print(movie, rating)
        
    return

def find_movies_with_rating(dictionary, rating):

    # Implement your code here
    
    movie_list = []
    for movie, wanted_rating in dictionary.items():
        if wanted_rating == rating:
            movie_list.append(movie)

    return movie_list

def ask_user_input():
    while True:
        print("Choose 1-5.")
        print("1: Add a new movie and rating.")
        print("2: Change the rating of the movie.")
        print("3: Print all movies and their ratings.")
        print("4: Find all movies with a specific rating.")
        print("5: Exit.")
        mode = int(input())
        if 1 <= mode <= 5:
            return mode
        print('')
        print("You chose an invalid number.\n")

def main():

    print("Welcome to the database of the movie ratings.\n")
    
    # Implement your code here
    
    movies = dict()

    while True:

        mode = ask_user_input()
        print('')

        if mode == 1:
            movie_name = str(input("Enter the movie.\n"))
            movie_rating = int(input("Enter the rating (4-10).\n"))
            bool_movies = add_new_movie_and_rating(movies, movie_name, movie_rating)
            if bool_movies == False:
                print(f"{movie_name} is already in the database. Choose 2 if you want to change the rating of the movie.\n")
            if bool_movies == True: 
                print(f"{movie_name} has been added into the database.\n")
            
        if mode == 2:
            movie_name = str(input("Enter the movie.\n"))
            movie_rating = int(input("Enter the new rating (4-10).\n"))
            bool_movies = change_rating(movies, movie_name, movie_rating)
            if bool_movies == False:
                print(f"{movie_name} is not in the database. Choose 1 if you want to add the movie.\n")
            if bool_movies == True:
                print(f"The rating of {movie_name} has been changed.\n")

        if mode == 3:
            print("The movies in the database:")
            print_all_movies(movies)
            print('')

        if mode == 4:
            rating_value = int(input("Enter the rating.\n"))
            movies_with_rating = find_movies_with_rating(movies, rating_value)
            if movies_with_rating != []:
                print(*movies_with_rating, sep = "\n")
            else:
                print(f"There are no movies with rating {rating_value} in the database.\n")

            
        if mode == 5:
            break

main()