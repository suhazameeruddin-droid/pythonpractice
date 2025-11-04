def book_seat(booked_seats, seat_number, total_seats):
    if seat_number in booked_seats:
        print(f"Seat {seat_number} is already booked.")
    elif seat_number < 1 or seat_number > total_seats:
        print(f"Seat {seat_number} is invalid.")
    else:
        booked_seats.append(seat_number)
    return booked_seats

def cancel_seat(booked_seats, seat_number):
    if seat_number in booked_seats:
        booked_seats.remove(seat_number)
    else:
        print(f"Seat {seat_number} is not booked yet.")
    return booked_seats

def get_available_seats(total_seats, booked_seats):
    return [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]

# Example input
total_seats = 10
booked_seats = [2, 5, 7]
book_seat_num = 3
cancel_seat_num = 5

# Operations
booked_seats = book_seat(booked_seats, book_seat_num, total_seats)
booked_seats = cancel_seat(booked_seats, cancel_seat_num)
available_seats = get_available_seats(total_seats, booked_seats)

# Output
print("Available seats:", available_seats)
