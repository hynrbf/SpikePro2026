# from pybricks import version
# from pybricks.tools import run_task, multitask
#
# from colorcontroller import ColorController
# from grippercontroller import GripperController
# from shared import Speed
# from wheelcontroller import WheelController
#
# color_front_hook = ""
# color_front_grip = ""
# is_color_blue_detected = False
#
#
# async def green_blue_placement():
#     print("green_blue_placement")
#     await multitask(WheelController.move_forward(float(370)), GripperController.front_hook())
#     await WheelController.right_turn(20)
#     await WheelController.move_forward(10)
#     await WheelController.move_backward(10)
#     await WheelController.left_turn(20)
#     await WheelController.move_backward(250)
#     await GripperController.front_hook_down()
#     await WheelController.move_backward(120)
#     await WheelController.left_turn(20)
#     await WheelController.move_forward(50)
#     await WheelController.left_turn(70)
#     await WheelController.move_forward(150)
#     await WheelController.right_turn()
#     await WheelController.move_forward(930)
#     await multitask(WheelController.right_turn(), GripperController.back_grip_up())
#     await WheelController.move_backward(300)
#     await GripperController.back_grip()
#     await WheelController.move_backward(700, with_brake=True)
#
#
# async def blue_green_placement():
#     print("blue_green_placement")
#     await multitask(WheelController.left_turn(20), GripperController.front_hook_down())
#     await WheelController.move_forward(235)
#     await WheelController.right_turn(90)
#     await GripperController.front_hook()
#     await WheelController.move_forward(30, Speed.Slow)
#     await WheelController.move_backward(110)
#     await WheelController.left_turn(45)
#     await WheelController.move_forward(200)
#     await WheelController.right_turn(20)
#     await GripperController.front_hook_down()
#     await WheelController.move_backward(250)
#     # left 20+45, right 90+10
#     await WheelController.left_turn(45)
#     await WheelController.move_forward(740)
#     await multitask(WheelController.right_turn(), GripperController.back_grip_up())
#     await WheelController.move_backward(300)
#     await GripperController.back_grip()
#     await WheelController.move_backward(400, with_brake=True)
#
#
# async def yellow_green_placement():
#     print("yellow_green_placement")
#     await multitask(WheelController.left_turn(20), GripperController.front_hook_down())
#     await WheelController.move_forward(210)
#     await WheelController.right_turn(90)
#     await GripperController.front_hook()
#     await WheelController.move_backward(70)
#     await WheelController.left_turn(70)
#     await WheelController.move_forward(470)
#     await WheelController.right_turn()
#     await WheelController.move_forward(50)
#     await GripperController.front_hook_down()
#     await WheelController.move_backward(80)
#     await WheelController.left_turn()
#     await WheelController.move_forward(310)
#     await multitask(WheelController.right_turn(), GripperController.back_grip_up())
#     await WheelController.move_backward(300)
#     await GripperController.back_grip()
#     await WheelController.move_backward(600, with_brake=True)
#
#
# async def green_yellow_placement():
#     print("green_yellow_placement")
#     await multitask(WheelController.move_forward(float(534)), GripperController.front_hook())
#     await WheelController.move_backward(430)
#     await GripperController.front_hook_down()
#     await WheelController.move_backward(120)
#     await WheelController.left_turn(20)
#     await WheelController.move_forward(50)
#     await WheelController.left_turn(70)
#     await WheelController.move_forward(150)
#     await WheelController.right_turn()
#     await WheelController.move_forward(910)
#     await multitask(WheelController.right_turn(), GripperController.back_grip_up())
#     await WheelController.move_backward(300)
#     await GripperController.back_grip()
#     await WheelController.move_backward(500, with_brake=True)
#
#
# async def white_green_placement():
#     print("white_green_placement")
#     await multitask(WheelController.move_forward(float(150)), GripperController.front_hook_down())
#     await WheelController.left_turn(20)
#     await WheelController.move_backward(80)
#     await WheelController.left_turn(70)
#     await WheelController.move_forward(170)
#     await WheelController.right_turn()
#     await WheelController.move_forward(90)
#     await WheelController.move_backward(90)
#     await WheelController.left_turn()
#     await WheelController.move_forward(830)
#     await multitask(WheelController.right_turn(), GripperController.back_grip_up())
#     await WheelController.move_backward(130)
#     await GripperController.back_grip()
#     await WheelController.move_backward(580)
#
#
# async def green_white_placement():
#     print("green_white_placement")
#     await GripperController.front_hook_down(25)
#     await WheelController.move_backward(float(80))
#     await GripperController.front_hook()
#     await WheelController.move_backward(100)
#     await WheelController.left_turn(20)
#     await WheelController.move_forward(50)
#     await WheelController.left_turn(70)
#     await WheelController.move_forward(130)
#     await WheelController.right_turn()
#     await WheelController.move_forward(300)
#     await WheelController.right_turn(70)
#     await multitask(GripperController.front_hook_down(), WheelController.move_forward(20))
#     await WheelController.move_backward(80)
#     await WheelController.left_turn(70)
#     await WheelController.move_forward(780)
#     await multitask(WheelController.right_turn(), GripperController.back_grip_up())
#     await WheelController.move_backward(130)
#     await GripperController.back_grip()
#     await WheelController.move_backward(580)
#
#
# async def white_yellow_placement():
#     print("white_yellow_placement")
#     await multitask(WheelController.move_forward(float(560)), GripperController.front_hook_down(25))
#     await GripperController.front_hook(speed=Speed.Slow)
#     await WheelController.move_backward(660)
#     await GripperController.front_hook_down()
#     await WheelController.move_backward(80)
#     await WheelController.left_turn(20)
#     await WheelController.move_forward(50)
#     await WheelController.left_turn(70)
#     await WheelController.move_forward(150)
#     await WheelController.right_turn()
#     await WheelController.move_forward(1110)
#     await multitask(WheelController.right_turn(), GripperController.back_grip_up())
#     await WheelController.move_backward(150)
#     await GripperController.back_grip()
#     await WheelController.move_backward(650, with_brake=True)
#
#
# async def yellow_white_placement():
#     print("yellow_white_placement")
#     await GripperController.front_hook_down(25)
#     await WheelController.move_backward(float(65))
#     await GripperController.front_hook(speed=Speed.Slow)
#     await WheelController.move_backward(100)
#     await WheelController.left_turn(20)
#     await WheelController.move_forward(50)
#     await WheelController.left_turn(70)
#     await WheelController.move_forward(130)
#     await WheelController.right_turn()
#     await WheelController.move_forward(700)
#     await WheelController.right_turn(70)
#     await multitask(GripperController.front_hook_down(), WheelController.move_forward(20))
#     await WheelController.move_backward(80)
#     await WheelController.left_turn(70)
#     await WheelController.move_forward(405)
#     await multitask(WheelController.right_turn(), GripperController.back_grip_up())
#     await WheelController.move_backward(130)
#     await GripperController.back_grip()
#     await WheelController.move_backward(570, with_brake=True)
#
#
# async def white_red_placement():
#     print("white_red_placement")
#     await GripperController.front_hook_down(25)
#     await WheelController.move_forward(float(740))
#     await WheelController.right_turn(20)
#     await WheelController.move_forward(20)
#     await GripperController.front_hook()
#     await WheelController.move_backward(20)
#     await WheelController.left_turn(20)
#     await WheelController.move_backward(850)
#     await GripperController.front_hook_down()
#     await WheelController.move_backward(100)
#     await WheelController.left_turn(20)
#     await WheelController.move_forward(50)
#     await WheelController.left_turn(70)
#     await WheelController.move_forward(150)
#     await WheelController.right_turn()
#     await WheelController.move_forward(1125)
#     await multitask(WheelController.right_turn(), GripperController.back_grip_up())
#     await WheelController.move_backward(130)
#     await GripperController.back_grip()
#     await WheelController.move_backward(700, with_brake=True)
#
#
# async def red_white_placement():
#     print("red_white_placement")
#     await GripperController.front_hook_down(25)
#     await WheelController.move_backward(float(80))
#     await GripperController.front_hook(speed=Speed.Slow)
#     await WheelController.move_backward(100)
#     await WheelController.left_turn(20)
#     await WheelController.move_forward(50)
#     await WheelController.left_turn(70)
#     await WheelController.move_forward(130)
#     await WheelController.right_turn()
#     await WheelController.move_forward(900)
#     await WheelController.right_turn(70)
#     await WheelController.move_forward(30)
#     await GripperController.front_hook_down()
#     await WheelController.move_backward(70)
#     await WheelController.left_turn(70)
#     await WheelController.move_forward(202)
#     await multitask(WheelController.right_turn(), GripperController.back_grip_up())
#     await WheelController.move_backward(150)
#     await GripperController.back_grip()
#     await WheelController.move_backward(755, with_brake=True)
#
#
# async def blue_white_placement():
#     print("blue_white_placement")
#     await GripperController.front_hook_down()
#     await WheelController.move_backward(float(60))
#     await WheelController.right_turn(20)
#     await GripperController.front_hook()
#     await WheelController.move_backward(60)
#     await WheelController.left_turn(20)
#     await WheelController.move_backward(60)
#     await WheelController.left_turn(20)
#     await WheelController.move_forward(50)
#     await WheelController.left_turn(70)
#     await WheelController.move_forward(130)
#     await WheelController.right_turn()
#     await WheelController.move_forward(500)
#     await WheelController.right_turn(70)
#     await multitask(GripperController.front_hook_down(), WheelController.move_forward(70))
#     await WheelController.move_backward(90)
#     await WheelController.left_turn(70)
#     await WheelController.move_forward(580)
#     await multitask(WheelController.right_turn(), GripperController.back_grip_up())
#     await WheelController.move_backward(140)
#     await GripperController.back_grip()
#     await WheelController.move_backward(690, with_brake=True)
#
#
# async def white_blue_placement():
#     print("white_blue_placement")
#     await multitask(GripperController.front_hook_down(25), WheelController.move_forward(float(360)))
#     await GripperController.front_hook(speed=Speed.Slow)
#     await WheelController.move_backward(470)
#     await GripperController.front_hook_down()
#     await WheelController.move_backward(80)
#     await WheelController.left_turn(20)
#     await WheelController.move_forward(50)
#     await WheelController.left_turn(70)
#     await WheelController.move_forward(130)
#     await WheelController.right_turn()
#     await WheelController.move_forward(1080)
#     await multitask(WheelController.right_turn(), GripperController.back_grip_up())
#     await WheelController.move_backward(130)
#     await GripperController.back_grip()
#     await WheelController.move_backward(690)
#
#
# async def blue_yellow_placement():
#     print("blue_yellow_placement")
#     await WheelController.move_forward(570)
#     await WheelController.right_turn(20)
#     await WheelController.move_forward(10)
#     await GripperController.front_hook()
#     await WheelController.move_backward(80)
#     await WheelController.left_turn(40)
#     await WheelController.move_backward(100)
#     await WheelController.right_turn(20)
#     await WheelController.move_backward(95)
#     await GripperController.front_hook_down()
#     await WheelController.move_backward(95)
#     await WheelController.left_turn(20)
#     await WheelController.move_forward(40)
#     await WheelController.left_turn(70)
#     await WheelController.move_forward(200)
#     await WheelController.right_turn()
#     await WheelController.move_forward(710)
#     await multitask(WheelController.right_turn(), GripperController.back_grip_up())
#     await WheelController.move_backward(130)
#     await GripperController.back_grip()
#     await WheelController.move_backward(600)
#
#
# async def yellow_blue_placement():
#     print("yellow_blue_placement")
#     await WheelController.move_forward(360)
#     await GripperController.front_hook(speed=Speed.Slow)
#     await WheelController.move_backward(220)
#     await WheelController.left_turn(20)
#     await WheelController.move_forward(50)
#     await WheelController.left_turn(70)
#     await WheelController.move_forward(160)
#     await WheelController.right_turn()
#     await WheelController.move_forward(460)
#     await WheelController.right_turn()
#     await WheelController.move_forward(60)
#     await GripperController.front_hook_down()
#     await WheelController.move_backward(100)
#     await WheelController.left_turn()
#     await WheelController.move_forward(325)
#     await multitask(WheelController.right_turn(), GripperController.back_grip_up())
#     await WheelController.move_backward(100)
#     await GripperController.back_grip()
#     await WheelController.move_backward(610)
#
#
# async def yellow_red_placement():
#     print("yellow_red_placement")
#     # putting red
#     await WheelController.move_forward(770)
#     await WheelController.right_turn(16)
#     await GripperController.front_hook(speed=Speed.Slow)
#     await WheelController.move_backward(75)
#
#     # putting yellow
#     await WheelController.left_turn(32)
#     await WheelController.move_backward(100)
#     await WheelController.right_turn(16)
#     await WheelController.move_backward(65)
#     await GripperController.front_hook_down()
#     await WheelController.move_backward(100)
#
#     # going to base 3
#     await WheelController.left_turn(20)
#     await WheelController.move_forward(50)
#     await WheelController.left_turn(70)
#     await WheelController.move_forward(200)
#     await WheelController.right_turn()
#     await WheelController.move_forward(490)
#     await multitask(WheelController.right_turn(), GripperController.back_grip_up())
#     await WheelController.move_backward(130)
#     await GripperController.back_grip()
#     await WheelController.move_backward(590)
#
#
# async def red_yellow_placement():
#     print("red_yellow_placement")
#     await WheelController.move_forward(560)
#     await GripperController.front_hook()
#     await WheelController.move_backward(100)
#     await WheelController.move_backward(120)
#     await WheelController.left_turn(20)
#     await WheelController.move_forward(50)
#     await WheelController.left_turn(70)
#     await WheelController.move_forward(150)
#     await WheelController.right_turn()
#     await WheelController.move_forward(460)
#     await WheelController.right_turn()
#     await GripperController.front_hook_down()
#     await WheelController.move_backward(50)
#     await WheelController.left_turn()
#     await WheelController.move_forward(100)
#     await multitask(WheelController.right_turn(), GripperController.back_grip_up())
#     await WheelController.move_backward(130)
#     await GripperController.back_grip()
#     await WheelController.move_backward(580)
#
#
# async def green_red_placement():
#     print("green_red_placement")
#     await WheelController.move_forward(770)
#     await GripperController.front_hook()
#     await WheelController.move_backward(675)
#     await GripperController.front_hook_down()
#     await WheelController.move_backward(100)
#     await WheelController.left_turn(20)
#     await WheelController.move_forward(50)
#     await WheelController.left_turn(70)
#     await WheelController.move_forward(200)
#     await WheelController.right_turn()
#     await WheelController.move_forward(925)
#     await multitask(WheelController.right_turn(), GripperController.back_grip_up())
#     await WheelController.move_backward(150)
#     await GripperController.back_grip()
#     await WheelController.move_backward(580)
#
#
# async def red_green_placement():
#     print("red_green_placement")
#     # putting green
#     await WheelController.move_forward(160)
#     await GripperController.front_hook()
#     await WheelController.move_backward(220)
#     await WheelController.left_turn(20)
#     await WheelController.move_forward(50)
#     await WheelController.left_turn(70)
#     await WheelController.move_forward(150)
#     await WheelController.right_turn()
#
#     # putting the red
#     await WheelController.move_forward(850)
#     await WheelController.right_turn()
#     await WheelController.move_forward(45)
#     await GripperController.front_hook_down()
#     await WheelController.move_backward(90)
#     await WheelController.left_turn()
#     await WheelController.move_forward(100)
#
#     # get red cube
#     await multitask(WheelController.right_turn(), GripperController.back_grip_up())
#     await WheelController.move_backward(150)
#     await GripperController.back_grip()
#     await WheelController.move_backward(580)
#
#
# async def blue_red_placement():
#     print("blue_red_placement")
#     await WheelController.move_forward(760)
#     await GripperController.front_hook()
#     await WheelController.move_backward(475)
#     await GripperController.front_hook_down()
#     await WheelController.move_backward(100)
#     await WheelController.left_turn(20)
#     await WheelController.move_forward(50)
#     await WheelController.left_turn(70)
#     await WheelController.move_forward(200)
#     await WheelController.right_turn()
#     await WheelController.move_forward(725)
#     await multitask(WheelController.right_turn(), GripperController.back_grip_up())
#     await WheelController.move_backward(150)
#     await GripperController.back_grip()
#     await WheelController.move_backward(560)
#
#
# async def red_blue_placement():
#     print("red_blue_placement")
#     await WheelController.move_forward(350)
#     await GripperController.front_hook()
#     await WheelController.move_backward(100)
#     await WheelController.move_backward(120)
#     await WheelController.left_turn(20)
#     await WheelController.move_forward(50)
#     await WheelController.left_turn(70)
#     await WheelController.move_forward(150)
#     await WheelController.right_turn()
#     await WheelController.move_forward(660)
#     await WheelController.right_turn()
#     await WheelController.move_forward(30)
#     await GripperController.front_hook_down()
#     await WheelController.move_backward(80)
#     await WheelController.left_turn()
#     await WheelController.move_forward(100)
#     await multitask(WheelController.right_turn(), GripperController.back_grip_up())
#     await WheelController.move_backward(150)
#     await GripperController.back_grip()
#     await WheelController.move_backward(560)
#
#
# async def normal_flow():
#     print("normal_flow")
#     # picking 1st satellite
#     await WheelController.move_backward(130)
#     await GripperController.front_hook_down()
#     await WheelController.move_forward(130, Speed.Slow)
#     await GripperController.front_hook(angle_degrees=85, speed=Speed.Slow)
#
#     # picking up 2nd satellites
#     await WheelController.move_forward(127)
#     await WheelController.left_turn(13)
#     await WheelController.move_forward(55, Speed.Slow)
#     global color_front_grip
#     color_front_grip = await ColorController.get_color()
#
#     # Tapal
#     global is_color_blue_detected
#     if (color_front_grip == "Blue" or color_front_grip == "White") and not is_color_blue_detected:
#         color_front_grip = "Blue"
#         is_color_blue_detected = True
#     elif color_front_grip == "Blue" or color_front_grip == "White":
#         color_front_grip = "White"
#
#     print("Color detect: ", color_front_grip)
#     await GripperController.front_hook_down(30)
#
#     # going to the center line a bit
#     await WheelController.right_turn(20)
#     await WheelController.move_backward(70)
#     await WheelController.left_turn(65)
#     await WheelController.move_forward(215)
#     await WheelController.right_turn(45)
#
#     # going to place the fuel
#     await WheelController.move_forward(1020)
#     await WheelController.right_u_turn()
#     await WheelController.move_backward(260)
#     await WheelController.right_turn(72)
#     await WheelController.move_forward(50)
#
#     # move the rocket
#     await GripperController.back_grip_up(140)
#     await WheelController.move_forward(540)
#
#     # getting red block
#     await WheelController.move_forward(50)
#     await WheelController.right_turn(72)
#     await WheelController.move_backward(355)
#     # 270 = 72 + 72 + 126, ginawa 128 because natatabingi
#     await multitask(WheelController.right_turn(128), GripperController.back_grip_up())
#     await WheelController.move_backward(250)
#     await GripperController.back_grip()
#     await WheelController.move_backward(175)
#
#
# async def blank_satellite1_flow():
#     print("blank_satellite1_flow")
#     # getting 1 satellite if there is no satellite in the first spot
#     await WheelController.move_backward(50)
#     await WheelController.left_turn(13)
#     await WheelController.move_forward(150)
#     await WheelController.left_turn()
#     await WheelController.move_backward(150)
#     await WheelController.move_forward(35)
#     await multitask(WheelController.right_turn(103), GripperController.front_hook())
#     await WheelController.move_forward(70, Speed.Slow)
#     global color_front_hook
#     color_front_hook = await ColorController.get_color()
#
#     # Tapal
#     global is_color_blue_detected
#     if (color_front_hook == "Blue" or color_front_hook == "White") and not is_color_blue_detected:
#         color_front_hook = "Blue"
#         is_color_blue_detected = True
#     elif color_front_hook == "Blue" or color_front_hook == "White":
#         color_front_hook = "White"
#
#     print("Color detect: ", color_front_hook)
#     await WheelController.move_backward(130)
#     await GripperController.front_hook_down()
#     await WheelController.move_forward(130, Speed.Slow)
#     await GripperController.front_hook(angle_degrees=85, speed=Speed.Slow)
#
#     # Getting second satellite if there is no satellite in the first spot
#     await WheelController.move_forward(117)
#     await WheelController.left_turn(13)
#     await WheelController.move_forward(70, Speed.Slow)
#     global color_front_grip
#     color_front_grip = await ColorController.get_color()
#
#     # Tapal
#     global is_color_blue_detected
#     if (color_front_grip == "Blue" or color_front_grip == "White") and not is_color_blue_detected:
#         color_front_grip = "Blue"
#         is_color_blue_detected = True
#     elif color_front_grip == "Blue" or color_front_grip == "White":
#         color_front_grip = "White"
#
#     print("Color detect: ", color_front_grip)
#     await GripperController.front_hook_down(30)
#
#     # going to the center line a bit
#     await WheelController.right_turn(20)
#     await WheelController.move_backward(70)
#     await WheelController.left_turn(65)
#     await WheelController.move_forward(205)
#     await WheelController.right_turn(45)
#
#     # going to place the fuel
#     await WheelController.move_forward(1000)
#     await WheelController.right_u_turn()
#     await WheelController.move_backward(115)
#     await WheelController.right_turn(72)
#     await WheelController.move_forward(70)
#
#     # move the rocket
#     await GripperController.back_grip_up(138)
#     await WheelController.move_forward(535)
#     await GripperController.back_grip()
#
#     # getting red block
#     await WheelController.move_forward(50)
#     await WheelController.right_turn(72)
#     await WheelController.move_backward(350)
#     # 270 = 72 + 72 + 126, ginawa 128 because natatabingi
#     await multitask(WheelController.right_turn(128), GripperController.back_grip_up())
#     await WheelController.move_backward(250)
#     await GripperController.back_grip()
#     await WheelController.move_backward(200)
#
#
# # For the last 20 pairings before the finish
#
#
# async def final_normal_flow():
#     # picking 3rd satellite
#     await WheelController.move_backward(135)
#     await multitask(GripperController.front_hook_down())
#     await WheelController.move_forward(135, Speed.Slow)
#     await GripperController.front_hook(angle_degrees=85, speed=Speed.Slow)
#
#     # Collecting satellite No.4
#     await WheelController.move_forward(107)
#     await WheelController.left_turn(13)
#     await WheelController.move_forward(70, Speed.Slow)
#     global color_front_grip
#     color_front_grip = await ColorController.get_color()
#
#     # Tapal
#     global is_color_blue_detected
#     if (color_front_grip == "Blue" or color_front_grip == "White") and not is_color_blue_detected:
#         color_front_grip = "Blue"
#         is_color_blue_detected = True
#     elif color_front_grip == "Blue" or color_front_grip == "White":
#         color_front_grip = "White"
#
#     print("Color detect: ", color_front_grip)
#
#     # getting red cube
#     await multitask(WheelController.move_forward(380), GripperController.front_hook_down(30))
#     await WheelController.right_turn(20)
#     await WheelController.move_backward(100)
#     await WheelController.left_turn(110)
#     await GripperController.back_grip()
#     await WheelController.move_backward(100)
#     await WheelController.move_forward(350)
#     await multitask(WheelController.right_u_turn(), GripperController.back_grip_up())
#     await WheelController.move_backward(150)
#     await GripperController.back_grip()
#     await WheelController.left_u_turn()
#
#
# async def final_blank3_satellite():
#     # getting no 3 satellite
#     await WheelController.move_backward(135)
#     await WheelController.left_turn(13)
#     await WheelController.move_forward(230)
#     await WheelController.left_turn()
#     await WheelController.move_backward(150)
#     await WheelController.move_forward(35)
#     await multitask(WheelController.right_turn(103), GripperController.front_hook())
#     await WheelController.move_forward(55, Speed.Slow)
#     global color_front_hook
#     color_front_hook = await ColorController.get_color()
#
#     # Tapal
#     global is_color_blue_detected
#     if (color_front_hook == "Blue" or color_front_hook == "White") and not is_color_blue_detected:
#         color_front_hook = "Blue"
#         is_color_blue_detected = True
#     elif color_front_hook == "Blue" or color_front_hook == "White":
#         color_front_hook = "White"
#
#     print("color detect: ", color_front_hook)
#     await WheelController.move_backward(130)
#     await GripperController.front_hook_down()
#     await WheelController.move_forward(130, Speed.Slow)
#     await GripperController.front_hook(angle_degrees=85, speed=Speed.Slow)
#
#     # getting no 4 satellite
#     await WheelController.move_forward(115)
#     await WheelController.left_turn(13)
#     await WheelController.move_forward(80)
#     global color_front_grip
#     color_front_grip = await ColorController.get_color()
#
#     # Tapal
#     global is_color_blue_detected
#     if (color_front_grip == "Blue" or color_front_grip == "White") and not is_color_blue_detected:
#         color_front_grip = "Blue"
#         is_color_blue_detected = True
#     elif color_front_grip == "Blue" or color_front_grip == "White":
#         color_front_grip = "White"
#
#     print("color detect: ", color_front_grip)
#     await WheelController.move_forward(140)
#     await GripperController.front_hook_down(30)
#
#     # avoid wall friction
#     await WheelController.move_backward(185)
#     await WheelController.right_turn(20)
#     await WheelController.move_backward(150)
#     await WheelController.left_turn(20)
#     await WheelController.move_forward(235)
#
#     # getting red cube
#     await WheelController.left_turn()
#     await WheelController.move_backward(100)
#     await WheelController.move_forward(350)
#     await multitask(WheelController.right_u_turn(), GripperController.back_grip_up())
#     await WheelController.move_backward(165)
#     await GripperController.back_grip()
#     await WheelController.left_u_turn()
#
#
# async def final_yellow_white_placement():
#     print("final_yellow_white_placement")
#     await WheelController.move_forward(150)
#     await WheelController.right_turn()
#     await GripperController.front_hook()
#     await WheelController.move_forward(160)
#     await WheelController.move_backward(160)
#     await WheelController.left_turn()
#     await WheelController.move_forward(630)
#     await WheelController.right_turn()
#     await GripperController.front_hook_down()
#     await WheelController.move_forward(140)
#     await WheelController.move_backward(130)
#
#
# async def final_white_yellow_placement():
#     print("final_white_yellow_placement")
#     await WheelController.move_forward(780)
#     await WheelController.right_turn()
#     await GripperController.front_hook()
#     await WheelController.move_forward(145)
#     await WheelController.move_backward(145)
#     await WheelController.left_turn()
#     await WheelController.move_backward(605)
#     await WheelController.right_turn()
#     await GripperController.front_hook_down()
#     await WheelController.move_forward(90)
#     await WheelController.move_backward(90)
#
#
# async def final_blue_yellow_placement():
#     print("final_blue_yellow_placement")
#     await WheelController.move_forward(760)
#     await WheelController.right_turn()
#     await GripperController.front_hook()
#     await WheelController.move_forward(165)
#     await WheelController.move_backward(165)
#     await WheelController.left_turn()
#     await WheelController.move_backward(185)
#     await WheelController.right_turn()
#     await GripperController.front_hook_down()
#     await WheelController.move_forward(100)
#     await WheelController.move_backward(100)
#
#
# async def final_yellow_blue_placement():
#     print("final_yellow_blue_placement")
#     await WheelController.move_forward(575)
#     await WheelController.right_turn()
#     await GripperController.front_hook()
#     await WheelController.move_forward(150)
#     await WheelController.move_backward(150)
#     await WheelController.left_turn()
#     await WheelController.move_forward(185)
#     await WheelController.right_turn()
#     await GripperController.front_hook_down()
#     await WheelController.move_forward(125)
#     await WheelController.move_backward(125)
#     await WheelController.left_turn()
#
#
# async def final_yellow_green_placement():
#     await WheelController.move_forward(350)
#     await WheelController.right_turn()
#     await GripperController.front_hook()
#     await WheelController.move_forward(150)
#     await WheelController.move_backward(150)
#     await WheelController.left_turn()
#     await WheelController.move_forward(410)
#     await WheelController.right_turn()
#     await GripperController.front_hook_down()
#     await WheelController.move_forward(125)
#     await WheelController.move_backward(125)
#     await WheelController.left_turn()
#
#
# async def final_green_yellow_placement():
#     print("final_green_yellow_placement")
#     await WheelController.move_forward(760)
#     await WheelController.right_turn()
#     await GripperController.front_hook()
#     await WheelController.move_forward(165)
#     await WheelController.move_backward(165)
#     await WheelController.left_turn()
#     await WheelController.move_backward(390)
#     await WheelController.right_turn()
#     await GripperController.front_hook_down(25)
#     await WheelController.move_forward(100)
#     await GripperController.front_hook_down()
#     await WheelController.move_backward(100)
#
#
# async def final_red_white_placement():
#     await WheelController.move_forward(165)
#     await WheelController.right_turn()
#     await GripperController.front_hook()
#     await WheelController.move_forward(160)
#     await WheelController.move_backward(160)
#     await WheelController.left_turn()
#     await WheelController.move_forward(830)
#     await WheelController.right_turn()
#     await GripperController.front_hook_down(25)
#     await WheelController.move_forward(50)
#     await GripperController.front_hook_down()
#     await WheelController.move_backward(50)
#
#
# async def final_white_red_placement():
#     await WheelController.move_forward(970)
#     await WheelController.right_turn()
#     await GripperController.front_hook()
#     await WheelController.move_forward(145)
#     await WheelController.move_backward(145)
#     await WheelController.left_turn()
#     await WheelController.move_backward(755)
#     await WheelController.right_turn()
#     await GripperController.front_hook_down(25)
#     await WheelController.move_forward(100)
#     await GripperController.front_hook_down()
#     await WheelController.move_backward(100)
#
#
# async def final_blue_white_placement():
#     print("final_blue_white_placement")
#     await WheelController.move_forward(155)
#     await WheelController.right_turn()
#     await GripperController.front_hook()
#     await WheelController.move_forward(160)
#     await WheelController.move_backward(160)
#     await WheelController.left_turn()
#     await WheelController.move_forward(420)
#     await WheelController.right_turn()
#     await multitask(WheelController.move_forward(105), GripperController.front_hook_down(25))
#     await GripperController.front_hook_down()
#     await WheelController.move_backward(100)
#
#
# async def final_white_blue_placement():
#     print("final_white_blue_placement")
#     # putting blue
#     await WheelController.move_forward(570)
#     await WheelController.right_turn()
#     await GripperController.front_hook()
#     await WheelController.move_forward(150)
#     await WheelController.move_backward(150)
#     await WheelController.left_turn()
#
#     # putting white
#     await WheelController.move_backward(390)
#     await WheelController.right_turn()
#     await multitask(WheelController.move_forward(90), GripperController.front_hook_down(25))
#     await GripperController.front_hook_down()
#     await WheelController.move_backward(100)
#
#
# async def final_blue_green_placement():
#     print("final_blue_green_placement")
#     await WheelController.move_forward(360)
#     await WheelController.right_turn()
#     await GripperController.front_hook()
#     await WheelController.move_forward(150)
#     await WheelController.move_backward(150)
#     await WheelController.left_turn()
#     await WheelController.move_forward(220)
#     await WheelController.right_turn()
#     await multitask(WheelController.move_forward(95), GripperController.front_hook_down(25))
#     await GripperController.front_hook_down()
#     await WheelController.move_backward(100)
#
#
# async def final_green_blue_placement():
#     print("final_green_blue_placement")
#     await WheelController.move_forward(575)
#     await WheelController.right_turn()
#     await GripperController.front_hook()
#     await WheelController.move_forward(150)
#     await WheelController.move_backward(150)
#     await WheelController.left_turn()
#     await WheelController.move_backward(215)
#     await WheelController.right_turn()
#     await multitask(WheelController.move_forward(95), GripperController.front_hook_down(25))
#     await GripperController.front_hook_down()
#     await WheelController.move_backward(100)
#
#
# async def final_blue_red_placement():
#     print("final_blue_red_placement")
#     await WheelController.move_forward(970)
#     await WheelController.right_turn()
#     await GripperController.front_hook()
#     await WheelController.move_forward(150)
#     await WheelController.move_backward(150)
#     await WheelController.left_turn()
#     await WheelController.move_backward(395)
#     await WheelController.right_turn()
#     await multitask(WheelController.move_forward(95), GripperController.front_hook_down(25))
#     await GripperController.front_hook_down()
#     await WheelController.move_backward(100)
#
#
# async def final_red_blue_placement():
#     print("final_red_blue_placement")
#     await WheelController.move_forward(575)
#     await WheelController.right_turn()
#     await GripperController.front_hook()
#     await WheelController.move_forward(150)
#     await WheelController.move_backward(150)
#     await WheelController.left_turn()
#     await WheelController.move_forward(400)
#     await WheelController.right_turn()
#     await multitask(WheelController.move_forward(95), GripperController.front_hook_down(25))
#     await GripperController.front_hook_down()
#     await WheelController.move_backward(100)
#
#
# async def final_green_white_placement():
#     print("final_green_white_placement")
#     await WheelController.move_forward(155)
#     await WheelController.right_turn()
#     await GripperController.front_hook()
#     await WheelController.move_forward(160)
#     await WheelController.move_backward(160)
#     await WheelController.left_turn()
#     await WheelController.move_forward(215)
#     await WheelController.right_turn()
#     await multitask(WheelController.move_forward(160), GripperController.front_hook_down(25))
#     await GripperController.front_hook_down()
#     await WheelController.move_backward(100)
#
#
# async def final_white_green_placement():
#     print("final_white_green_placement")
#     await WheelController.move_forward(370)
#     await WheelController.right_turn()
#     await GripperController.front_hook()
#     await WheelController.move_forward(160)
#     await WheelController.move_backward(160)
#     await WheelController.left_turn()
#     await WheelController.move_backward(215)
#     await WheelController.right_turn()
#     await multitask(WheelController.move_forward(160), GripperController.front_hook_down(25))
#     await GripperController.front_hook_down()
#     await WheelController.move_backward(100)
#
#
# async def main():
#     print("\nStart, pb version: ", version)
#
#     # Base 1 position. The starting position
#     # reset gripper only
#     await GripperController.reset()
#     global color_front_grip
#     color_front_grip = ""
#     global color_front_hook
#     color_front_hook = ""
#     global is_color_blue_detected
#     is_color_blue_detected = False
#
#     # capturing fuel
#     await multitask(WheelController.move_backward(140, with_brake=True), GripperController.back_grip_up())
#     await GripperController.back_grip()
#     await multitask(WheelController.left_u_turn(), GripperController.front_hook())
#     await WheelController.move_backward(290)
#
#     # getting color of 1st satellite
#     await WheelController.move_forward(35)
#     await WheelController.right_turn()
#     await WheelController.move_forward(335)
#     await WheelController.left_turn()
#     await WheelController.move_backward(150)
#     await WheelController.move_forward(35)
#     # 90 + 13 angle
#     await multitask(WheelController.right_turn(103), GripperController.front_hook())
#     await WheelController.move_forward(55, Speed.Slow)
#     color_front_hook = await ColorController.get_color()
#
#     # Tapal
#     if (color_front_hook == "Blue" or color_front_hook == "White") and not is_color_blue_detected:
#         color_front_hook = "Blue"
#         is_color_blue_detected = True
#     elif color_front_hook == "Blue" or color_front_hook == "White":
#         color_front_hook = "White"
#
#     print("color detect: ", color_front_hook)
#
#     if color_front_hook == "":
#         await blank_satellite1_flow()
#     else:
#         await normal_flow()
#
#     # Base 2 position. making a position where all if and else statements start
#     # important 95-96!!
#     await WheelController.move_forward(30)
#     await WheelController.right_turn(95)
#     await WheelController.move_towards_white_floor()
#     print("Base 2 pos")
#
#     # # ToDo. add here right turn then bangga sa wall, after combination placement na
#     # # For testing. placing only
#     # color_front_hook = "Green"
#     # color_front_grip = "Blue"
#
#     if color_front_hook == "Green" and color_front_grip == "Blue":
#         await green_blue_placement()
#     elif color_front_hook == "Blue" and color_front_grip == "Green":
#         await blue_green_placement()
#     elif color_front_hook == "Yellow" and color_front_grip == "Green":
#         await yellow_green_placement()
#     elif color_front_hook == "Green" and color_front_grip == "Yellow":
#         await green_yellow_placement()
#     elif color_front_hook == "White" and color_front_grip == "Green":
#         await white_green_placement()
#     elif color_front_hook == "Green" and color_front_grip == "White":
#         await green_white_placement()
#     elif color_front_hook == "White" and color_front_grip == "Yellow":
#         await white_yellow_placement()
#     elif color_front_hook == "Yellow" and color_front_grip == "White":
#         await yellow_white_placement()
#     elif color_front_hook == "White" and color_front_grip == "Red":
#         await white_red_placement()
#     elif color_front_hook == "Red" and color_front_grip == "White":
#         await red_white_placement()
#     elif color_front_hook == "Blue" and color_front_grip == "White":
#         await blue_white_placement()
#     elif color_front_hook == "White" and color_front_grip == "Blue":
#         await white_blue_placement()
#     elif color_front_hook == "Blue" and color_front_grip == "Yellow":
#         await blue_yellow_placement()
#     elif color_front_hook == "Yellow" and color_front_grip == "Blue":
#         await yellow_blue_placement()
#     elif color_front_hook == "Red" and color_front_grip == "Yellow":
#         await red_yellow_placement()
#     elif color_front_hook == "Yellow" and color_front_grip == "Red":
#         await yellow_red_placement()
#     elif color_front_hook == "Green" and color_front_grip == "Red":
#         await green_red_placement()
#     elif color_front_hook == "Red" and color_front_grip == "Green":
#         await red_green_placement()
#     elif color_front_hook == "Blue" and color_front_grip == "Red":
#         await blue_red_placement()
#     elif color_front_hook == "Red" and color_front_grip == "Blue":
#         await red_blue_placement()
#     else:
#         print("did not detect placement")
#
#     # Base 3 position
#     # important 185!!
#     await WheelController.move_forward(35)
#     await WheelController.left_turn()
#     await WheelController.move_towards_white_floor()
#     await WheelController.right_turn(182)
#     print("Base 3 pos")
#
#     # Collecting satellite No.3
#     await multitask(GripperController.front_hook(), GripperController.back_grip_up())
#     await WheelController.move_forward(100)
#     await multitask(WheelController.move_forward(450), GripperController.back_grip())
#     await WheelController.left_turn()
#     await WheelController.move_backward(150)
#     await WheelController.move_forward(35)
#     # 90 + 13 angle
#     await WheelController.right_turn(103)
#     await WheelController.move_forward(85)
#     color_front_hook = await ColorController.get_color()
#
#     # Tapal
#     global is_color_blue_detected
#     if (color_front_hook == "Blue" or color_front_hook == "White") and not is_color_blue_detected:
#         color_front_hook = "Blue"
#         is_color_blue_detected = True
#     elif color_front_hook == "Blue" or color_front_hook == "White":
#         color_front_hook = "White"
#
#     print("color detect: ", color_front_hook)
#
#     if color_front_hook == "":
#         await final_blank3_satellite()
#     else:
#         await final_normal_flow()
#
#     # Base 4 position
#     await WheelController.move_towards_white_floor()
#     await WheelController.move_forward(20)
#     await WheelController.right_turn()
#     await multitask(WheelController.move_towards_white_floor_line_edge(), GripperController.front_hook())
#     await WheelController.right_u_turn()
#     print("Base 4 pos")
#
#     # # ToDo. add here right turn then bangga sa wall, after combination placement na
#     # # For testing. placing only
#     # color_front_hook = "Red"
#     # color_front_grip = "Blue"
#
#     if color_front_hook == "Yellow" and color_front_grip == "White":
#         await final_yellow_white_placement()
#     elif color_front_hook == "White" and color_front_grip == "Yellow":
#         await final_white_yellow_placement()
#     elif color_front_hook == "Blue" and color_front_grip == "Yellow":
#         await final_blue_yellow_placement()
#     elif color_front_hook == "Yellow" and color_front_grip == "Blue":
#         await final_yellow_blue_placement()
#     elif color_front_hook == "Yellow" and color_front_grip == "Green":
#         await final_yellow_green_placement()
#     elif color_front_hook == "Green" and color_front_grip == "Yellow":
#         await final_green_yellow_placement()
#     elif color_front_hook == "Red" and color_front_grip == "White":
#         await final_red_white_placement()
#     elif color_front_hook == "White" and color_front_grip == "Red":
#         await final_white_red_placement()
#     elif color_front_hook == "Blue" and color_front_grip == "White":
#         await final_blue_white_placement()
#     elif color_front_hook == "White" and color_front_grip == "Blue":
#         await final_white_blue_placement()
#     elif color_front_hook == "Blue" and color_front_grip == "Green":
#         await final_blue_green_placement()
#     elif color_front_hook == "Green" and color_front_grip == "Blue":
#         await final_green_blue_placement()
#     elif color_front_hook == "Blue" and color_front_grip == "Red":
#         await final_blue_red_placement()
#     elif color_front_hook == "Red" and color_front_grip == "Blue":
#         await final_red_blue_placement()
#     elif color_front_hook == "Green" and color_front_grip == "White":
#         await final_green_white_placement()
#     elif color_front_hook == "White" and color_front_grip == "Green":
#         await final_white_green_placement()
#
#     # done only, do not remove
#     print("DONE!")
#
#
# run_task(main())
