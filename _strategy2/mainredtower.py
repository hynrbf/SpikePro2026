from colorcontroller import MatColor
from handcontroller import HandController
from shared import Speed
from wheelcontroller import WheelController
from pybricks.tools import wait, multitask  # multitask


class MissionRedTower:
    @staticmethod
    async def exec_mission():
        await WheelController.right_turn(35)
        await WheelController.move_forward(750, speed=Speed.Fastest)
        await WheelController.right_turn(180)
        await WheelController.move_backward(350, with_brake=True)
        await WheelController.move_forward(275)
        await WheelController.left_turn()
        await WheelController.move_forward(370)
        await WheelController.move_towards_mat_color(MatColor.Black, speed=Speed.Slow)
        await WheelController.move_forward(40)
        await WheelController.left_turn()

        # get the red towers
        await WheelController.move_forward(209, speed=Speed.Medium, with_brake=True)
        await WheelController.move_backward(27, speed=Speed.Slow)
        await multitask(HandController.lift_left(30, speed=Speed.Slow),
                        HandController.lift_right(28, speed=Speed.Slow))
        await WheelController.left_turn(180, turn_speed=60)
        await multitask(HandController.lift_left(0, speed=Speed.Slow),
                        HandController.lift_right(0, speed=Speed.Slow))
        await WheelController.move_forward(100)
        await multitask(HandController.lift_left(30, speed=Speed.Slow),
                        HandController.lift_right(27, speed=Speed.Slow))
        await WheelController.right_turn(50, turn_speed=90)

        # moving towards other side
        await WheelController.move_forward(750)
        await WheelController.left_turn(50, turn_speed=90)
        await WheelController.move_forward(350)
        await WheelController.move_towards_mat_color(MatColor.Black, speed=Speed.Slow)
        await WheelController.move_forward(145)
        await WheelController.right_turn(turn_speed=90)
        await WheelController.move_forward(400, with_brake=True)
        await WheelController.move_backward(30, speed=Speed.Slow)
        await WheelController.right_turn(180, turn_speed=90)
        await WheelController.move_backward(210, with_brake=True)
        await multitask(HandController.lift_left(-10),
                        HandController.lift_right(-10))
        await WheelController.move_forward(320, speed=Speed.Medium)
        await WheelController.move_towards_mat_color(MatColor.Black)
        await multitask(HandController.lift_left(30, speed=Speed.Slow),
                        HandController.lift_right(27, speed=Speed.Slow))

        # placing the 1st tower
        await WheelController.right_turn(61, turn_speed=90)
        await multitask(HandController.lift_left(-10, speed=Speed.Slow),
                        HandController.lift_right(-10, speed=Speed.Slow))
        await WheelController.move_forward(200, speed=Speed.Slow)
        await HandController.lift_right(26, speed=Speed.Slow)
        await WheelController.move_backward(170, speed=Speed.Slow)

        # placing the 2nd tower
        await WheelController.right_turn(42, turn_speed=90)
        await multitask(HandController.lift_left(-10, speed=Speed.Slow),
                        HandController.lift_right(-10, speed=Speed.Slow))
        await WheelController.move_forward(110, speed=Speed.Slow)
        await WheelController.move_backward(115, speed=Speed.Slow)

        # positioning going to visitors
        await WheelController.right_turn(170)  # 180+(90-(61+42))
        await WheelController.move_forward(1000, speed=Speed.Fastest)
        await WheelController.right_turn(177)
        await WheelController.move_backward(500, with_brake=True)
        await wait(100)
