from djitellopy import Tello
from random import randint
import time

# create and connect
# 创建Tello对象并连接
tello = Tello()
tello.connect()

# configure drone
# 设置无人机
tello.enable_mission_pads()
tello.set_mission_pad_detection_direction(2)  # all directions  只识别前方

print("initial battery is " , tello.get_battery())

tello.takeoff()


pad = tello.get_mission_pad_id()

# detect and react to pads until we see pad #1
# 发现并识别挑战卡直到看见1号挑战卡

#Move drone up to get better fov
#tello.move_up(60)
current_pos =(tello.get_mission_pad_distance_x(),tello.get_mission_pad_distance_y(),tello.get_mission_pad_distance_z())



while tello.get_battery()>55:
    #move command from Shahab's code, needs integration
    # if move_command(x,y,z)
    #     tello.go_xyz_speed(x,y,z,20)
    #     current_pos_x += current_pos_x+x
    #     current_pos_y += current_pos_y+y
    #     current_pos_z += current_pos_z+z

    move = randint(0,1)
    move_amount = (randint(-50,50),randint(-50,50),randint(-50,50))


    if move == 1:
        tello.go_xyz_speed(move_amount[0], move_amount[1], move_amount[2], 10)
        current_pos = (current_pos[0]+move_amount[0],current_pos[1]+move_amount[1],current_pos[2]+move_amount[2])

    if pad !=-1:
        current_pos = (tello.get_mission_pad_distance_x(),tello.get_mission_pad_distance_y(),tello.get_mission_pad_distance_z())

    pad = tello.get_mission_pad_id()
    print(current_pos , tello.get_mission_pad_id())
    tello.get_battery()
    print("current battery is " , tello.get_battery())


# while pad != 1:
#     if pad == 3:
#         print(tello.get_mission_pad_distance_x())
#         print(tello.get_mission_pad_distance_y())
#         print(tello.get_mission_pad_distance_z())
#         print(pad)
#         tello.move_left(20)
#     pad = tello.get_mission_pad_id()
#
#     if pad == 4:
#         x = tello.get_mission_pad_distance_x()
#         y = tello.get_mission_pad_distance_y()
#         z = tello.get_mission_pad_distance_z()
#         print("distance from pad 4 is ", x, y, z)
#         tello.go_xyz_speed(-x,-y,-z,20)
#
#
#         break


#tello.go_xyz_speed(0,100,0,20)
#tello.go_xyz_speed(100,-100,0,20)
#tello.go_xyz_speed(-100,-100,0,20)
#tello.go_xyz_speed(0,100,0,20)


# graceful termination
# 安全结束程序
tello.disable_mission_pads()
tello.land()
tello.end()