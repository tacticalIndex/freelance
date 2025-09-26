from easytello import tello
import time

# Initialize the drone
my_drone = tello.Tello()

# Define 4 points (in cm, relative to takeoff position, assuming z=50cm altitude)
points = [
    (0, 0, 50),      # Point 1: start
    (100, 0, 50),    # Point 2: 1 meter forward
    (100, 100, 50),  # Point 3: 1 meter right
    (0, 100, 50)     # Point 4: back to Y axis
]

results = []

my_drone.takeoff()
time.sleep(5)

for i, (x, y, z) in enumerate(points):
    my_drone.go(x, y, z, 20)  # speed set to 20cm/s; adjust as needed
    time.sleep(5)  # wait to reach point

    baro = my_drone.get_baro()
    battery = my_drone.get_battery()
    temp = my_drone.get_temp()
    results.append({
        'point': (x, y, z),
        'baro': baro,
        'battery': battery,
        'temp': temp
    })
    print(f'Point {i+1}: Baro={baro}, Battery={battery}, Temp={temp}')
    time.sleep(1)

my_drone.land()

# Write results to a TXT file
with open("tello_data_log.txt", "w") as f:
    for entry in results:
        f.write(f"Point: {entry['point']}, Baro: {entry['baro']}, Battery: {entry['battery']}, Temp: {entry['temp']}\n")

print("Data saved to tello_data_log.txt")
