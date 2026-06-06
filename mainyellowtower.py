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
        await WheelController.move_forward(265, speed=Speed.Medium)
        await WheelController.left_turn()
        await WheelController.move_backward(260)
        await WheelController.left_turn()
        # Picking up 2 yellow towers
        await WheelController.move_forward(270, speed=Speed.Slow, with_brake=True)
        await WheelController.move_backward(30, speed=Speed.Medium)
        await multitask(HandController.lift_right(55), HandController.lift_left(55))
        await WheelController.move_backward(300, with_brake=True, speed=Speed.Medium)
        await multitask(HandController.lift_left(35), HandController.lift_left(35))
        # positioning to prep for another bangga
        await WheelController.right_turn(140, turn_speed=90)
        await WheelController.move_forward(400, speed=Speed.Medium)
        await WheelController.left_turn(40, turn_speed=90)
        await WheelController.move_forward(600, speed=Speed.Medium)
        await WheelController.move_towards_mat_color(MatColor.Black)
        await WheelController.move_forward(150, speed=Speed.Medium)
        # 2nd bangga
        await WheelController.left_turn(turn_speed=90)
        await multitask(HandController.lift_left(40), HandController.lift_right(55))
        await WheelController.move_backward(400, with_brake=True)
        # Straightening of yellow towers
        await multitask(HandController.lift_right(-10, speed=Speed.Slow),
                        HandController.lift_left(-10, speed=Speed.Slow))
        await WheelController.move_forward(50)
        await multitask(HandController.lift_right(35, speed=Speed.Slow),
                        HandController.lift_left(35, speed=Speed.Slow))
        await WheelController.move_forward(170, speed=Speed.Medium)
        await WheelController.left_turn(turn_speed=Speed.Slow)
        await WheelController.move_towards_mat_color(MatColor.Black, Speed.Slow)
        await WheelController.right_turn(180)
        # placing 1st tower
        await WheelController.move_forward(275, speed=Speed.Medium)
        await HandController.lift_right(80, speed=Speed.Slow)
        await HandController.lift_left(-10)
        await WheelController.move_forward(70)
        await HandController.lift_right(40, speed=Speed.Slow)
        # placing 2nd tower
        await HandController.lift_left(35, speed=Speed.Slow)
        await WheelController.move_backward(120, speed=Speed.Slow)
        await HandController.lift_right(-10)
        await WheelController.left_turn(turn_speed=90)
        await WheelController.move_forward(515)
        await WheelController.right_turn(turn_speed=90)
        await HandController.lift_left(90, speed=Speed.Slow)
        await WheelController.move_forward(160, speed=Speed.Slow)
        await HandController.lift_left(40, speed=Speed.Slow)
        await WheelController.move_backward(120, speed=Speed.Slow)
        await multitask(HandController.lift_left(), HandController.lift_right(), WheelController.right_turn(180))

        # long drive before detecting black line
        await WheelController.move_forward(650)
        await WheelController.left_turn()
        await WheelController.move_backward(400, with_brake=True)
        await WheelController.move_forward(300)
        await WheelController.right_turn()
        await WheelController.move_forward(200)
        await WheelController.move_towards_mat_color(MatColor.Black)
        await wait(100)
