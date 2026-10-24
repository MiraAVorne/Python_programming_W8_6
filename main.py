from drawLib import drawCircle, drawSquare, saveSvg, Drawing, ask_int
from svgwrite import cm

def main() -> None:
    # Initialize the drawing object
    Dwg = Drawing(size=(20*cm, 20*cm))
    print("Program starting.")
    while True:
        showOptions()
        choice = askChoice()

        if choice == 1:
            drawSquare(Dwg)
        
        elif choice == 2:
            drawCircle(Dwg)

        elif choice == 3:
            saveSvg(Dwg)

        elif choice == 0:
            print("Exiting program.")
            break

        else:
            print("Unknown option.")
    
    print("Program ending.")

def showOptions() -> None:
    print("Options:")
    print("1 - Draw square")
    print("2 - Draw circle")
    print("3 - Save svg")
    print("0 - Exit")

def askChoice() -> int:
    return int(input("Your choice: "))

if __name__ == "__main__":
    main()

