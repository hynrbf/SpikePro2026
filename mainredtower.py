from colorcontroller import MatColor
from handcontroller import HandController
from shared import Speed
from wheelcontroller import WheelController
from pybricks.tools import multitask, wait


class MissionRedTower:
    @staticmethod
    async def exec_mission():
        await WheelController.left_turn()
        await WheelController.move_backward(300, with_brake=True)
        await WheelController.move_forward(200)
        await WheelController.right_turn()
        await WheelController.move_forward(315, speed=Speed.Medium)
        await multitask(HandController.lift_left(30, speed=Speed.Slow),
                        HandController.lift_right(26, speed=Speed.Slow))
        await WheelController.left_turn(180, turn_speed=Speed.Slow)
        await multitask(HandController.lift_left(0, speed=Speed.Slow),
                        HandController.lift_right(0, speed=Speed.Slow))
        await WheelController.move_forward(100)
        await multitask(HandController.lift_left(30, speed=Speed.Slow),
                        HandController.lift_right(26, speed=Speed.Slow))
        await WheelController.move_forward(660)
        await WheelController.move_towards_mat_color(MatColor.Black, speed=Speed.Slow)
        await WheelController.move_forward(150)
        await WheelController.right_turn()
        await WheelController.move_forward(500)
        await WheelController.right_turn(180)
        await WheelController.move_backward(490, with_brake=True)

        await multitask(HandController.lift_left(30, speed=Speed.Slow),
                        HandController.lift_right(26, speed=Speed.Slow))
        await WheelController.move_forward(378)
        await WheelController.right_turn(turn_speed=Speed.Slow)
        await WheelController.move_forward(116, speed=Speed.Slow)
        await multitask(HandController.lift_left(30, speed=Speed.Slow),
                        HandController.lift_right(0, speed=Speed.Slow))
        await WheelController.move_backward(120, speed=Speed.Slow)
        await WheelController.left_turn(turn_speed=Speed.Slow)
        await WheelController.move_forward(185)
        await WheelController.right_turn(turn_speed=Speed.Slow)
        await WheelController.move_forward(116, speed=Speed.Slow)
        await HandController.lift_left(0, speed=Speed.Slow)
        await WheelController.move_backward(120, speed=Speed.Slow)
        await wait(500)
