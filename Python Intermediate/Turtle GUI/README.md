## All 3 files:
This code uses Python's turtle module for graphics and the random module to introduce randomness in the turtle's colors. 

The colormode(255) function is called to enable RGB color mode, allowing colors to be specified using values between 0 and 255 for red, green, and blue components. The turtle object tommy is created using the Turtle class, and its shape is set to "turtle" for a more thematic appearance. The turtle's speed is set to the fastest (speed(0)), and its pen size is set to 10 using pensize(10) to make the trail more prominent.

The ranc() function is defined to generate a random RGB color. It uses random.randint(0, 255) to generate random values for red, green, and blue components and applies the color to the turtle using tommy.color(r, b, g). The turtle's speed is set to the fastest (speed(0)).

The ranc() function is defined to generate a random RGB color. It uses random.randint(0, 255) to generate random values for red, green, and blue components and applies the color to the turtle using tommy.color(r, b, g).

Finally, the Screen object is created to display the turtle's movements. The program waits for the user to click on the screen to exit, using SCREEN.exitonclick(). This ensures that the window remains open until the user decides to close it, allowing them to observe the turtle's movements and the colorful trail it leaves behind.

## Random Walk:
This code creates a program where a turtle named tommy takes a random walk on the screen, leaving a colorful trail behind.
The program is designed to be visually engaging, as the turtle moves in random directions while changing its pen color dynamically.

The pen size is set to 10 using pensize(10) to make the trail more prominent.

This ranc function is called repeatedly during the turtle's random walk to ensure that the trail is colorful and dynamic.

The turtle's movement is controlled by a for loop that iterates 150 times. In each iteration, the ranc() function is called to change the turtle's color, and the turtle's heading is set to a random direction chosen from the list [0, 90, 180, 270] using random.choice(angle). These angles correspond to the four cardinal directions (right, up, left, down). The turtle then moves forward by 20 units using tommy.fd(20).

## Shapes:
The provided code creates a program that uses Python's turtle module to draw shapes with an increasing number of sides, starting from a triangle (3 sides) and ending with a decagon (10 sides). The program also incorporates random colors for each shape, making the output visually dynamic and engaging.

The tommy.color(r, b, g) method is then called to apply the generated color to the turtle's pen, ensuring that each shape is drawn in a unique color.

The main part of the program is a for loop that iterates through numbers from 3 to 10, representing the number of sides for each shape. For each iteration, the ranc() function is called to set a random color for the shape. A nested for loop is used to draw the shape by repeatedly turning the turtle by an angle of 360/t degrees (where t is the number of sides) and moving it forward by 100 units. This ensures that the turtle completes a full rotation and draws a closed polygon.

## Spirograph:
The provided code creates a program that uses Python's turtle module to draw a spirograph, a geometric pattern consisting of overlapping circles.

The tommy.color(r, b, g) method is then called to apply the generated color to the turtle's pen, ensuring that each circle in the spirograph is drawn in a unique color.

The main part of the program is a for loop that iterates 50 times, as specified by the times variable. In each iteration, the turtle draws a circle with a radius of 100 units using the circle(100) method. After completing the circle, the turtle turns left by an angle of 360/times degrees, ensuring that the circles are evenly spaced around the center of the spirograph. The ranc() function is called in each iteration to change the turtle's pen color, adding variety to the pattern.

