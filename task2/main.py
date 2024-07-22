import turtle

def koch_curve(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_curve(t, length, level-1)
        t.left(60)
        koch_curve(t, length, level-1)
        t.right(120)
        koch_curve(t, length, level-1)
        t.left(60)
        koch_curve(t, length, level-1)

def koch_snowflake(t, length, level):
    for _ in range(3):
        koch_curve(t, length, level)
        t.right(120)

def main():
    level = int(input("Введіть рівень рекурсії: "))
    length = 300  # Довжина сторони сніжинки

    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-length / 2, length / 3)
    t.pendown()

    koch_snowflake(t, length, level)

    screen.mainloop()

if __name__ == "__main__":
    main()
