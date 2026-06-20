from colorcontroller import MatColor
from handcontroller import HandController
from shared import Speed
from wheelcontroller import WheelController
from pybricks.tools import wait, multitask  # multitask


class MissionRedTower:
    @staticmethod
    async def exec_mission():
        # after bangga, forward
        await WheelController.move_forward(275)
        await WheelController.left_turn()
        await WheelController.move_forward(335)
        await WheelController.move_towards_mat_color(MatColor.Black, mat_color_range_alt=MatColor.BlackTwo,
                                                     speed=Speed.Slow)
        await WheelController.move_forward(40)
        await WheelController.left_turn()

        # get the red towers
        await WheelController.move_forward(209, speed=Speed.Medium, with_brake=True)
        await WheelController.move_backward(27, speed=Speed.Medium)
        await multitask(HandController.lift_left(30, speed=120),
                        HandController.lift_right(28, speed=120))
        await WheelController.left_turn(180, turn_speed=60)
        await multitask(HandController.lift_left(-10),
                        HandController.lift_right(-10))
        await WheelController.move_forward(100)
        await multitask(HandController.lift_left(30),
                        HandController.lift_right(27))
        await WheelController.right_turn(50, turn_speed=120)

        # moving towards other side
        await WheelController.move_forward(750)
        await WheelController.left_turn(50, turn_speed=120)
        await WheelController.move_forward(350)
        await WheelController.move_towards_mat_color(MatColor.Black, speed=Speed.Slow)
        await WheelController.move_forward(145)
        await WheelController.right_turn(turn_speed=120)
        await WheelController.move_forward(400, with_brake=True)
        await WheelController.move_backward(30, speed=Speed.Medium)
        await WheelController.right_turn(180, turn_speed=120)
        await WheelController.move_backward(210, with_brake=True)
        await multitask(HandController.lift_left(-10),
                        HandController.lift_right(-10))
        await WheelController.move_forward(320, speed=Speed.Fast)
        await WheelController.move_towards_mat_color(MatColor.Black)
        await multitask(HandController.lift_left(30, speed=120),
                        HandController.lift_right(27, speed=120))

        # placing the 1st tower
        await WheelController.right_turn(61, turn_speed=120)
        await multitask(HandController.lift_left(-10),
                        HandController.lift_right(-10))
        await WheelController.move_forward(200, speed=Speed.Medium)
        await HandController.lift_right(26, speed=200)
        await WheelController.move_backward(170, speed=Speed.Medium)

        # placing the 2nd tower
        await WheelController.right_turn(42, turn_speed=120)
        await multitask(HandController.lift_left(-10),
                        HandController.lift_right(-10))
        await WheelController.move_forward(110, speed=Speed.Medium)
        await WheelController.move_backward(115, speed=Speed.Fast)

        # positioning going to visitors
        await WheelController.right_turn(170)  # 180+(90-(61+42))
        await WheelController.move_forward(1000, speed=Speed.Fastest)
        await WheelController.right_turn(177)
        await WheelController.move_backward(500, with_brake=True)
        await wait(100)
