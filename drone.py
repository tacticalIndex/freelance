from easytello import tello

mydrone = tello.Tello()

while(True):
    print("Input Command:")
    x = input()
    match(x):
        case "takeoff":
            mydrone.takeoff()
        case "land":
            mydrone.land()
        case "left":
            mydrone.left(50)
        case "right":
            mydrone.right(50)
        case "forward":
            mydrone.forward(50)
        case "backward":
            mydrone.back(50)
        case "up":
            mydrone.up(50)
        case "down":
            mydrone.down(50)
        case "quit":
            mydrone.land()
        case "battery":
            mydrone.get_battery()
            break