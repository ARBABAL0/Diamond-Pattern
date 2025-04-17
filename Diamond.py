def draw_diamond(height):
    # Top half (regular pyramid)
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)
    
    # Bottom half (inverted pyramid)
    for i in range(height - 1, 0, -1):
        spaces = " " * (height - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

# Main program
if __name__ == "__main__":
    height = int(input("Enter the height of the diamond: "))
    draw_diamond(height)