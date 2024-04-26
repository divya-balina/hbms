import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Hotel Booking Management System")

# Set the window size
root.geometry("400x300")

# Create a welcome label
welcome_label = tk.Label(root, text="Welcome to the Hotel Booking System!", font=("Arial", 20))
welcome_label.pack(pady=20)

# Create buttons for different functionalities
booking_button = tk.Button(root, text="Book a Room", font=("Arial", 14), command=booking_function)
room_info_button = tk.Button(root, text="View Rooms and Amenities", font=("Arial", 14), command=room_info_function)
restaurant_button = tk.Button(root, text="Order Food", font=("Arial", 14), command=restaurant_function)

# Arrange the buttons horizontally
booking_button.pack(side=tk.LEFT, padx=10, pady=10)
room_info_button.pack(side=tk.LEFT, padx=10, pady=10)
restaurant_button.pack(side=tk.LEFT, padx=10, pady=10)

# Define functions for each button (placeholders for now)
def booking_function():
    print("Booking function called.")

def room_info_function():
    print("Room info function called.")

def restaurant_function():
    print("Restaurant function called.")

# Start the main event loop
root.mainloop()