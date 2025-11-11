movie_names = ["Avengers", "Inception", "The Lion King", "Joker"]
available_seats = [5, 3, 4, 2]
ticket_price = [400, 350, 300, 450]
booked_movies = [] 

admin_username = "admin"
admin_password = "1234"

while True:
    print("\n*************************************")
    print("Welcome to the Movie Ticket Booking System")
    print("*************************************")
    print("1. Show Movies")
    print("2. Book Ticket")
    print("3. Cancel Booking")
    print("4. Add New Movie (Admin Only)")
    print("5. Exit")
    print("*************************************")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("\n--- Option 1: Show Movies ---")
        print("ID   Movie Name        Seats   Price")
        print("-------------------------------------------")
        for i in range(len(movie_names)):
            print(f"{i+1}.   {movie_names[i]}       {available_seats[i]}       Rs.{ticket_price[i]}")

    elif choice == "2":
        print("\n--- Option 2: Book Ticket ---")
        for i in range(len(movie_names)):
            print(f"{i+1}. {movie_names[i]} ({available_seats[i]} seats left) - Rs.{ticket_price[i]}")
        movie_id = int(input("Enter movie ID to book: ")) - 1
        if 0 <= movie_id < len(movie_names):
            if available_seats[movie_id] > 0:
                name = input("Enter your name: ")
                confirm = input(f"Confirm booking for '{movie_names[movie_id]}' (Y/N): ")
                if confirm.upper() == "Y":
                    available_seats[movie_id] -= 1
                    booked_movies.append(movie_names[movie_id])  # Store the booked movie
                    print("\n--- Ticket Booked Successfully! ---")
                    print(f"Customer: {name}")
                    print(f"Movie: {movie_names[movie_id]}")
                    print(f"Amount: Rs.{ticket_price[movie_id]}")
                else:
                    print("Booking cancelled.")
            else:
                print("Sorry, no seats available.")
        else:
            print("Invalid movie ID.")

    elif choice == "3":
        print("\n--- Option 3: Cancel Booking ---")
        if not booked_movies:
            print("You have not booked any movies yet!")
        else:
            print("Your Booked Movies:")
            for i, movie in enumerate(booked_movies, 1):
                print(f"{i}. {movie}")
            movie_to_cancel = int(input("Enter the movie number to cancel booking: ")) - 1
            if 0 <= movie_to_cancel < len(booked_movies):
                movie_name = booked_movies.pop(movie_to_cancel)  # Remove from booked list
                movie_id = movie_names.index(movie_name)
                available_seats[movie_id] += 1  # Revert seat count
                print(f"Booking for '{movie_name}' has been cancelled.")
            else:
                print("Invalid selection.")

    elif choice == "4":
        print("\n--- Option 4: Add New Movie ---")
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")
        if username == admin_username and password == admin_password:
            new_movie = input("Enter movie name: ")

            while True:
                try:
                    new_seats = int(input("Enter number of available seats: "))
                    if new_seats > 0:
                        break  # Exit the loop if the input is valid
                    else:
                        print("Please enter a number greater than 0 for available seats.")
                except ValueError:
                    print("Invalid input! Please enter a valid number.")

            new_price = int(input("Enter ticket price: Rs."))
            movie_names.append(new_movie)
            available_seats.append(new_seats)
            ticket_price.append(new_price)
            print(f"Movie '{new_movie}' added successfully.")
        else:
            print("Invalid admin credentials.")

    elif choice == "5":
        print("\nThank you for using the Movie Ticket Booking System!")
        break

    else:
        print("Invalid choice! Please select from 1 to 5.")
