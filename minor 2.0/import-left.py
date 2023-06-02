import traci
import csv

# start a SUMO simulation
traci.start(["sumo-gui", "-c", r"C:\Users\KIIT\Sumo\minor\left-side driving.sumocfg"])

# open a CSV file to write vehicle data
with open("vehicle_data.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Vehicle ID", "Latitude", "Longitude", "Direction"])

    # run the simulation for 1000 time steps
    for i in range(1000):
        # advance the simulation by one step
        traci.simulationStep()

        # get the IDs of all vehicles in the simulation
        vehicle_ids = traci.vehicle.getIDList()

        # loop over all vehicles and get their GPS coordinates and direction
        for vehicle_id in vehicle_ids:
            x, y = traci.vehicle.getPosition(vehicle_id)
            direction = traci.vehicle.getAngle(vehicle_id)
            writer.writerow([vehicle_id, x, y, direction])

# stop the simulation
traci.close()
