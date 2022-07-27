from djitellopy import TelloSwarm

swarm = TelloSwarm.fromIps([
    "192.168.0.48",
    "192.168.0.69",
    "192.168.0.196"
])

swarm.connect()
print("HELLO")
swarm.takeoff()

# run in parallel on all tellos
# 同时在所有Tello上执行
swarm.move_up(100)

swarm.land()
swarm.end()