from pybricks.tools import wait, multitask  # multitask

from colorcontroller import MatColor
from handcontroller import HandController
from shared import Speed
from wheelcontroller import WheelController


class MissionYellowTower:
    @staticmethod
    async def exec_mission():
        # 1st bangga
        await multitask(HandController.lift_left(),
                        HandController.lift_right())
        await WheelController.move_backward(500, with_brake=True)
        await WheelController.move_forward(250)
        await WheelController.left_turn()
        await WheelController.move_forward(125)
        await WheelController.move_towards_mat_color(MatColor.Black, speed=Speed.Slow)
        await WheelController.right_turn(180)
        await WheelController.move_backward(25)
        await multitask(HandController.lift_left(0), HandController.lift_right(0),
                        WheelController.right_turn())

        # get the yellow towers
        await WheelController.move_forward(209, speed=Speed.Medium, with_brake=True)
        await WheelController.move_backward(27, speed=Speed.Slow)
        await multitask(HandController.lift_left(30, speed=Speed.Slow),
                        HandController.lift_right(28, speed=Speed.Slow))
        await WheelController.left_turn(turn_speed=60)
        await multitask(HandController.lift_left(0, speed=Speed.Slow),
                            HandController.lift_right(0, speed=Speed.Slow))
        await WheelController.move_forward(200)
        await multitask(HandController.lift_left(30, speed=Speed.Slow),
                        HandController.lift_right(27, speed=Speed.Slow))
        await WheelController.left_turn(turn_speed=90)

        # LOOOOOOOONG DRIVE
        await WheelController.move_forward(925)
        await WheelController.move_towards_mat_color(MatColor.Black)

        # Straightening of yellow towers
        await WheelController.left_turn(turn_speed=90)
        await multitask(HandController.lift_left(-10), HandController.lift_right(-10))
        await WheelController.move_forward(485, speed=Speed.Medium, with_brake=True)
        await WheelController.move_backward(25)
        await multitask(HandController.lift_left(32), HandController.lift_right(32))
        await WheelController.right_turn(180, turn_speed=90)
        await WheelController.move_backward(150, speed=Speed.Medium, with_brake=True)
        await multitask(HandController.lift_left(-10), HandController.lift_right(-10))
        await WheelController.move_forward(400, speed=Speed.Medium)  # float is: 85 in game map; 91 in BGBES
        # await WheelController.move_towards_mat_color(MatColor.DarkGreen)
        await multitask(HandController.lift_left(32), HandController.lift_right(32))

        # placing 1st yellow tower
        await WheelController.left_turn(turn_speed=90)
        await multitask(HandController.lift_right(-10, speed=Speed.Slow),
                            HandController.lift_left(80, speed=Speed.Slow))
        await WheelController.move_forward(295, speed=Speed.Medium)
        await multitask(HandController.lift_left(40, speed=Speed.Slow), HandController.lift_right(28))
        await WheelController.move_backward(150, speed=Speed.Slow)
        await HandController.lift_left(-10)
        await WheelController.move_backward(80)

        # Moving to the other side
        await multitask(HandController.lift_left(32), HandController.lift_right(32))
        await WheelController.right_turn(turn_speed=90)
        await WheelController.move_forward(200, speed=Speed.Medium)

        # placing 2nd yellow tower
        await WheelController.left_turn(turn_speed=90)
        await multitask(HandController.lift_left(-10, speed=Speed.Slow),
                            HandController.lift_right(80, speed=Speed.Slow))
        await WheelController.move_forward(225, speed=Speed.Medium)
        await multitask(HandController.lift_right(40, speed=Speed.Slow), HandController.lift_left(28))
        await WheelController.move_backward(150, speed=Speed.Slow)
        await multitask(HandController.lift_left(-10, speed=Speed.Slow), HandController.lift_right(-10))
        await WheelController.move_backward(80)

        # # positioning for getting red towers
        # await multitask(HandController.lift_left(-10), HandController.lift_right(-10),
        #                 WheelController.move_backward(400, speed=Speed.Fastest))
        # await WheelController.left_turn(210)
        # await wait(100)
