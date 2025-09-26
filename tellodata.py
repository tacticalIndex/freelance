from easytello import tello
import time

# Initialize the drone
my_drone = tello.Tello()

# Define 4 points (in cm, relative to takeoff position)
points = [
    (0, 0),      # Point 1: start
    (100, 0),    # Point 2: 1 meter forward
    (100, 100),  # Point 3: 1 meter right
    (0, 100)     # Point 4: back to Y axis
]

results = []

# Takeoff
my_drone.takeoff()
time.sleep(5)

for i, (x, y) in enumerate(points):
    # Move to the next point
    if i > 0:
        dx = points[i][0] - points[i-1][0]
        dy = points[i][1] - points[i-1][1]
        if dx != 0:
            if dx > 0:
                my_drone.move_forward(dx)
            else:
                my_drone.move_back(-dx)
        if dy != 0:
            if dy > 0:
                my_drone.move_right(dy)
            else:
                my_drone.move_left(-dy)
        time.sleep(2)
    
    # Collect sensor data
    baro = my_drone.get_baro()
    battery = my_drone.get_battery()
    temp = my_drone.get_temp()
    results.append({
        'point': (x, y),
        'baro': baro,
        'battery': battery,
        'temp': temp
    })
    print(f'Point {i+1}: Baro={baro}, Battery={battery}, Temp={temp}')
    time.sleep(1)

# Land
my_drone.land()

# Write results to a TXT file
with open("tello_data_log.txt", "w") as f:
    for entry in results:
        f.write(f"Point: {entry['point']}, Baro: {entry['baro']}, Battery: {entry['battery']}, Temp: {entry['temp']}\n")

print("Data saved to tello_data_log.txt")
