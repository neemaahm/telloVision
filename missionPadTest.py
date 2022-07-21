from djitellopy import Tello
import time

tello = Tello()
tello.connect()

# configure drone
# 设置无人机
tello.enable_mission_pads()
tello.set_mission_pad_detection_direction(1)  # forward detection only  只识别前方

print(tello.get_battery())

tello.takeoff()

pad = tello.get_mission_pad_id()
# detect and react to pads until we see pad #1
# 发现并识别挑战卡直到看见1号挑战卡
while True:
    pad = tello.get_mission_pad_id()
    print(pad)
    time.sleep(1)

# graceful termination
# 安全结束程序
tello.disable_mission_pads()
tello.land()
tello.end()