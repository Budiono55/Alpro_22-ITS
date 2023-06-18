import turtle

# Set up the turtle window
window = turtle.Screen()
window.bgcolor("white")

# Create a turtle object
pen = turtle.Turtle()
pen.color("blue")
pen.penup()
pen.speed(1)

# Define the coordinates for each letter
coordinates = [(0, 0), (-100, 0), (-200, 0), (-300, 0), (-400, 0), (-500, 0)]

# Define the letter shapes as a dictionary
letter_shapes = {
    "M": [(0, 0), (0, 100), (50, 50), (100, 100), (100, 0)],
    "a": [(0, 0), (0, 50), (25, 75), (50, 50), (50, 0), (25, 25)],
    "t": [(25, 100), (25, 0), (0, 0), (50, 0)],
    "t2": [(0, 25), (50, 25)],
    "h": [(0, 0), (0, 100), (0, 50), (50, 50), (50, 100), (50, 0)],
    "e": [(0, 0), (0, 100), (50, 100), (0, 50), (50, 50), (0, 50), (0, 0)],
    "w": [(0, 0), (0, 100), (25, 75), (50, 100), (50, 0)],
}

# Iterate over each letter in the word
word = "Matthew"
for i, letter in enumerate(word):
    # Set the pen position to the corresponding coordinates
    x, y = coordinates[i]
    pen.goto(x, y)

    # Get the letter shape from the dictionary
    shape = letter_shapes.get(letter)

    if shape:
        # Draw the letter
        pen.pendown()
        pen.goto(x, y)
        for point in shape:
            pen.goto(x + point[0], y + point[1])
        pen.penup()

# Close the turtle window
turtle.done()