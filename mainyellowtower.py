from pybricks.tools import wait, multitask  # multitask

from colorcontroller import MatColor
from handcontroller import HandController
from shared import Speed
from wheelcontroller import WheelController


class MissionYellowTower:
    @staticmethod
    async def exec_mission():
        await WheelController.move_backward(70)
        await WheelController.left_turn()
        # 1st bangga
        await WheelController.move_backward(350, with_brake=True)
        await WheelController.move_forward(250, speed=Speed.Medium)
        await WheelController.left_turn()
        await WheelController.move_backward(245)
        await WheelController.left_turn()
        # Picking up 1st tower
        await WheelController.move_forward(270, speed=Speed.Slow, with_brake=True)
        await WheelController.move_backward(30, speed=Speed.Medium)
        await HandController.lift_right(55)
        await WheelController.move_backward(50, speed=Speed.Medium)
        await HandController.lift_right(30)
        # picking up 2nd tower
        await WheelController.move_forward(50, speed=Speed.Medium)
        await HandController.lift_left(55)
        await WheelController.move_backward(300, with_brake=True, speed=Speed.Medium)
        await HandController.lift_left(35)
        await WheelController.right_turn()
        await WheelController.move_forward(1050, speed=Speed.Medium)
        await WheelController.left_turn()
        await WheelController.move_backward(670, with_brake=True)
        # Straightening of yellow towers
        await multitask(HandController.lift_right(0, speed=Speed.Slow),
                        HandController.lift_left(0, speed=Speed.Slow))
        await wait(200)
        await WheelController.move_forward(20)
        await multitask(HandController.lift_right(35, speed=Speed.Slow),
                        HandController.lift_left(35, speed=Speed.Slow))
        await WheelController.move_forward(200, speed=Speed.Medium)
        await WheelController.left_turn(turn_speed=Speed.Slow)
        await WheelController.move_towards_mat_color(MatColor.Black, Speed.Slow)
        await WheelController.right_turn(180)
        await wait(500)
        # placing 1st tower
        await WheelController.move_forward(275, speed=Speed.Medium)
        await HandController.lift_right(80)
        await HandController.lift_left(-10)
        await WheelController.move_forward(70)
        await HandController.lift_right(40)
        # placing 2nd tower
        await HandController.lift_left(35, speed=Speed.Slow)
        await WheelController.move_backward(120, speed=Speed.Slow)
        await HandController.lift_right(-10)
        await WheelController.left_turn(turn_speed=Speed.Slow)
        await WheelController.move_forward(515)
        await HandController.lift_left(90)
        await WheelController.right_turn(turn_speed=Speed.Slow)
        await WheelController.move_forward(160, speed=Speed.Slow)
        await HandController.lift_left(40, speed=Speed.Slow)
        await WheelController.move_backward(120, speed=Speed.Slow)
        await HandController.lift_left(0)
        await WheelController.right_turn(180)
        await WheelController.move_forward(850)
        await WheelController.move_towards_mat_color(MatColor.Black)
        await wait(500)
