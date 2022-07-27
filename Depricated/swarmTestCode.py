from djitellopy import TelloSwarm

swarm = TelloSwarm.fromIps([
    "192.168.178.48",
    "192.168.178.69",
    "192.168.178.196"
])

swarm.connect()
swarm.takeoff()

# run in parallel on all tellos
# 同时在所有Tello上执行
swarm.move_up(100)

swarm.land()
swarm.end()