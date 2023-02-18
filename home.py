import pygame
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

# initialize Pygame
pygame.init()

# create a function for the snake game
def snake_game():
    # add your code to create the snake game here
    pass

# create a function for the car racing game
def car_racing_game():
    # add your code to create the car racing game here
    pass

# create a function for the shooting game
def shooting_game():
    # add your code to create the shooting game here
    pass

# create a function to open the snake game
def open_snake_game():
    snake_game()

# create a function to open the car racing game
def open_car_racing_game():
    car_racing_game()

# create a function to open the shooting game
def open_shooting_game():
    shooting_game()

# create the main window
root = tk.Tk()
root.title("Game Center")

# add a label for each game
snake_label = ttk.Label(root, text="Snake Game")
car_racing_label = ttk.Label(root, text="Car Racing Game")
shooting_label = ttk.Label(root, text="Shooting Game")

# add images for each game
snake_image = ImageTk.PhotoImage(Image.open("img1.jpg"))
car_racing_image = ImageTk.PhotoImage(Image.open("img2.jpg"))
shooting_image = ImageTk.PhotoImage(Image.open("img3.jpg"))

# create buttons for each game
snake_button = ttk.Button(root, image=snake_image, command=open_snake_game)
car_racing_button = ttk.Button(root, image=car_racing_image, command=open_car_racing_game)
shooting_button = ttk.Button(root, image=shooting_image, command=open_shooting_game)

# add the labels and buttons to the window
snake_label.grid(row=0, column=0)
car_racing_label.grid(row=0, column=1)
shooting_label.grid(row=0, column=2)

snake_button.grid(row=1, column=0)
car_racing_button.grid(row=1, column=1)
shooting_button.grid(row=1, column=2)

# start the event loop
root.mainloop()

# quit Pygame
pygame.quit()
