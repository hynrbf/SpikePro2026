from pybricks.tools import multitask, wait

from colorcontroller import MatColor
from handcontroller import HandController
from shared import Speed
from wheelcontroller import WheelController


class MissionYellowTower:
    @staticmethod
    async def exec_mission():
        await WheelController.left_turn()
        await WheelController.move_backward(350, with_brake=True)
        await WheelController.move_forward(220)
        await WheelController.right_turn()
        await WheelController.move_forward(220)
        await WheelController.right_turn()
        await multitask(HandController.reset(), WheelController.move_forward(100, Speed.Slow, with_brake=True))
        await multitask(HandController.lift_left(50, speed=Speed.Slow), HandController.lift_right(50, speed=Speed.Slow))
        await WheelController.move_backward(90, Speed.Medium)
        await WheelController.right_turn(turn_speed=90)
        await WheelController.move_forward(580)
        await WheelController.move_towards_mat_color(MatColor.Black, Speed.Slow)
        await WheelController.right_turn(turn_speed=120)
        await WheelController.move_backward(300, speed=Speed.Medium, with_brake=True)
        await WheelController.move_forward(230)
        await WheelController.left_turn(turn_speed=120)
        await multitask(HandController.lift_right(20), HandController.lift_left(85))
        await WheelController.move_forward(420, speed=Speed.Medium)
        await multitask(HandController.lift_left(50), HandController.lift_right(80))
        await WheelController.move_backward(150, speed=Speed.Medium)
        await multitask(HandController.lift_left(80), WheelController.left_turn(turn_speed=90))
        await WheelController.move_backward(900, with_brake=True)
        await WheelController.move_forward(230)
        await WheelController.right_turn(turn_speed=90)
        await multitask(HandController.lift_right(80), WheelController.move_forward(140, speed=Speed.Slow))
        await HandController.lift_right(50)
        await WheelController.move_backward(150)
        await wait(500)
