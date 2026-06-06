from colorcontroller import MatColor
from handcontroller import HandController
from shared import Speed
from wheelcontroller import WheelController
from pybricks.tools import multitask, wait


class MissionRedTower:
    @staticmethod
    async def exec_mission():
        await multitask(HandController.lift_left(), HandController.lift_right(),
                        WheelController.move_forward(160))
        await WheelController.left_turn()
        await WheelController.move_backward(360, with_brake=True)
        await WheelController.move_forward(209)
        await multitask(HandController.lift_left(-10), HandController.lift_right(-10),
                        WheelController.right_turn())
        # get the red towers
        await WheelController.move_forward(170, speed=Speed.Medium, with_brake=True)
        await WheelController.move_backward(27, speed=Speed.Slow)
        await multitask(HandController.lift_left(32, speed=Speed.Slow),
                        HandController.lift_right(26, speed=Speed.Slow))
        await WheelController.left_turn(180, turn_speed=60)
        await multitask(HandController.lift_left(0, speed=Speed.Slow),
                        HandController.lift_right(0, speed=Speed.Slow))
        await WheelController.move_forward(100)
        await multitask(HandController.lift_left(30, speed=Speed.Slow),
                        HandController.lift_right(29, speed=Speed.Slow))
        await WheelController.right_turn(50, turn_speed=90)
        await WheelController.move_forward(600)
        await WheelController.left_turn(50, turn_speed=90)
        await WheelController.move_forward(500)
        await WheelController.move_towards_mat_color(MatColor.Black, speed=Speed.Slow)
        await WheelController.move_forward(100)
        await WheelController.right_turn(turn_speed=90)
        await WheelController.move_forward(380, speed=Speed.Medium, with_brake=True)
        await WheelController.move_backward(30, speed=Speed.Slow)
        await WheelController.right_turn(180, turn_speed=90)
        await multitask(HandController.lift_left(-10),
                        HandController.lift_right(-10))
        await WheelController.move_forward(25, speed=Speed.Medium)
        await WheelController.move_backward(180, with_brake=True)
        await WheelController.move_forward(300, speed=Speed.Slow)
        await multitask(WheelController.move_forward(114, speed=Speed.Slow),
                        HandController.lift_left(30, speed=Speed.Slow),
                        HandController.lift_right(30, speed=Speed.Slow))

        # placing 1st red tower
        await WheelController.right_turn(turn_speed=90)
        await WheelController.move_forward(142)
        await multitask(HandController.lift_right(-10, speed=Speed.Slow), HandController.lift_left(45))

        # placing 2nd red tower
        await WheelController.move_backward(200, speed=Speed.Medium)
        await WheelController.left_turn(turn_speed=90)
        await WheelController.move_forward(170, speed=Speed.Medium)
        await WheelController.right_turn(turn_speed=90)
        await WheelController.move_forward(228, speed=Speed.Slow)
        await HandController.lift_left(-10, speed=Speed.Slow)
        await WheelController.move_backward(200, speed=Speed.Slow)
        await wait(500)
