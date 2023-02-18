import pygame
import random
import time
import sys
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import os

# initialize Pygame
pygame.init()

# create a function for the snake game
def launch_ghost_shooter():
    if os.path.isfile('ghost_shooter.py'):
        os.system('python ghost_shooter.py')
    else:
        print("Cannot find ghost_shooter.py")

def launch_chicken_shooter():
    if os.path.isfile('chicken_shooter.py'):
        os.system('python chicken_shooter.py')
    else:
        print("Cannot find chicken_shooter.py")

def launch_snake():
    if os.path.isfile('snake2.py'):
        os.system('python snake2.py')
    else:
        print("Cannot find snake2.py")

# create a function to open the snake game
def open_snake_game():
    launch_snake()

# create a function to open the car racing game
def open_car_racing_game():
    launch_ghost_shooter()

# create a function to open the shooting game
def open_shooting_game():
    launch_chicken_shooter()

# create the main window
root = tk.Tk()
root.title("Game Launcher")
root.geometry("1080x600")

# add a label for each game
snake_label = ttk.Label(root, text="Snake Game")
car_racing_label = ttk.Label(root, text="Car Racing Game")
shooting_label = ttk.Label(root, text="Shooting Game")

# add images for each game
# load the images
snake_image = Image.open("img1.jpg")
car_racing_image = Image.open("img2.jpg")
shooting_image = Image.open("img3.jpg")

# resize the images to a specific width and height
width = 250
height = 300
snake_image = snake_image.resize((width, height), Image.ANTIALIAS)
car_racing_image = car_racing_image.resize((width, height), Image.ANTIALIAS)
shooting_image = shooting_image.resize((width, height), Image.ANTIALIAS)

# convert the images to PhotoImage format
snake_image = ImageTk.PhotoImage(snake_image)
car_racing_image = ImageTk.PhotoImage(car_racing_image)
shooting_image = ImageTk.PhotoImage(shooting_image)


# create buttons for each game
# create buttons for each game
snake_button = ttk.Button(root, image=snake_image, command=open_snake_game)
car_racing_button = ttk.Button(
    root, image=car_racing_image, command=open_car_racing_game)
shooting_button = ttk.Button(
    root, image=shooting_image, command=open_shooting_game)

# add the labels and buttons to the window
snake_label.grid(row=0, column=0)
car_racing_label.grid(row=0, column=1)
shooting_label.grid(row=0, column=2)

snake_button.grid(row=1, column=0, padx=50, pady=50)
car_racing_button.grid(row=1, column=1, padx=50, pady=50)
shooting_button.grid(row=1, column=2, padx=50, pady=50)

# set weight to center the buttons
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
# root = tk.Tk()
# image = Image.open("my_image.jpg")
# photo = ImageTk.PhotoImage(image)
# label = tk.Label(root, image=photo)
# label.pack()
# start the event loop
root.configure(background='grey')
root.mainloop()


# quit Pygame
pygame.quit()
