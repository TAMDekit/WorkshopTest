input_movie = input("Enter movie name: ")

if input_movie == "spiderMan":
    print(f"Selected {input_movie}")

elif input_movie == "onePiece":
    input_movie = "onePiece"
    print(f"Selected {input_movie}")

    # select seat when pick movie already.
    pick_a_seat = input("Enter seat: ")

    if pick_a_seat == "A5":
        print(f"Seat {pick_a_seat} selected!")

elif input_movie == "oneDay":
    print(f"Selected {input_movie}")

else:
    print("No movie selected!")