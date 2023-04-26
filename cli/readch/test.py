import readchar

# Define the menu items
menu_items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]

# Set the initial selected item
selected_item = 0

while True:
    # Clear the screen
    print("\033c", end="")

    # Print the menu items
    for i, item in enumerate(menu_items):
        if i == selected_item:
            print(f"> {item}")
        else:
            print(f"  {item}")

    # Get the user input
    key = readchar.readkey()

    # Update the selected item based on the user input
    if key == "\x1b[A":
        selected_item = max(0, selected_item - 1)
    elif key == "\x1b[B":
        selected_item = min(len(menu_items) - 1, selected_item + 1)
    elif key == "\r":
        # Clear the screen
        print("\033c", end="")

        # Print the selected item
        print(f"You selected: {menu_items[selected_item]}")

        # Wait for the user to press a key before returning to the menu
        input("Press any key to continue...")

    elif key == "q":
        # Quit the application if the user presses "q"
        break
