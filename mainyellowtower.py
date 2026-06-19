from pybricks.tools import wait, multitask  # multitask

from colorcontroller import MatColor
from handcontroller import HandController
from shared import Speed
from wheelcontroller import WheelController


class MissionYellowTower:
    @staticmethod
    async def exec_mission():
        # finding black line
        await multitask(WheelController.move_forward(160), HandController.lift_left(),
                        HandController.lift_right())
        await WheelController.left_turn()
        await WheelController.move_forward(180)
        await WheelController.left_turn()
        await WheelController.move_towards_mat_color(MatColor.Black)
        await WheelController.move_backward(70)
        await WheelController.left_turn()

        # 1st bangga
        await WheelController.move_backward(350, with_brake=True)
        await WheelController.move_forward(215, speed=Speed.Medium)
        await multitask(HandController.lift_left(-10), HandController.lift_right(-10), WheelController.left_turn())
        await WheelController.move_backward(256, speed=Speed.Medium)
        await multitask(WheelController.left_turn(), HandController.lift_left(-10),
                        HandController.lift_right(-10))

        # Picking up 2 yellow towers
        await WheelController.move_forward(200, speed=Speed.Slow, with_brake=True)
        await WheelController.move_backward(30, speed=Speed.Medium)
        await multitask(HandController.lift_left(40), HandController.lift_right(40))

        # adjust tower holding
        await WheelController.right_turn(120, turn_speed=90)
        await multitask(HandController.lift_left(-10), HandController.lift_right(-10))
        await WheelController.move_forward(100, speed=Speed.Slow)
        await multitask(HandController.lift_left(32), HandController.lift_right(28))
        await WheelController.move_forward(150, speed=Speed.Medium)
        await WheelController.left_turn(30, turn_speed=90)

        # long drive
        await WheelController.move_forward(600)
        await WheelController.move_towards_mat_color(MatColor.Black)
        await WheelController.move_forward(175)

        # Straightening of yellow towers
        await WheelController.left_turn(turn_speed=90)
        await multitask(HandController.lift_left(-10), HandController.lift_right(-10))
        await WheelController.move_forward(280, speed=Speed.Medium, with_brake=True)
        await WheelController.move_backward(25)
        await multitask(HandController.lift_left(32), HandController.lift_right(28))
        await WheelController.right_turn(180, turn_speed=90)
        await multitask(HandController.lift_left(-10), HandController.lift_right(-10))
        await WheelController.move_towards_mat_color(MatColor.DarkGreen)
        await multitask(HandController.lift_left(32), HandController.lift_right(28))
        await WheelController.move_forward(85, speed=Speed.Slow)  # float is: 85 in game map; 91 in BGBS

        # placing 1st yellow tower
        await WheelController.right_turn(turn_speed=90)
        await multitask(HandController.lift_left(-10), HandController.lift_right(-10))
        await WheelController.move_forward(40, speed=Speed.Slow)
        await WheelController.move_towards_mat_color(MatColor.Black)
        await multitask(HandController.lift_left(32), HandController.lift_right(28))
        await WheelController.left_turn(180, turn_speed=90)
        await multitask(HandController.lift_right(-10, speed=Speed.Slow),
                        HandController.lift_left(90, speed=Speed.Slow))
        await WheelController.move_forward(355, speed=Speed.Medium)
        await multitask(HandController.lift_left(40, speed=Speed.Slow), HandController.lift_right(28))
        await WheelController.move_backward(120, speed=Speed.Slow)
        await HandController.lift_left(-10)
        await WheelController.move_backward(80, speed=Speed.Medium)

        # Moving to the other side
        await multitask(HandController.lift_left(-10, speed=Speed.Slow), HandController.lift_right(28))
        await WheelController.right_turn(turn_speed=90)
        await WheelController.move_forward(520)
        await HandController.lift_right(80, speed=Speed.Slow)
        await WheelController.move_towards_mat_color(MatColor.Green)

        # clear the artifacts
        await WheelController.right_turn(turn_speed=80)
        await WheelController.move_forward(170)
        await multitask(HandController.lift_left(), HandController.lift_right(80, speed=Speed.Slow))
        await WheelController.move_backward(190, speed=Speed.Medium)
        await multitask(WheelController.left_turn(turn_speed=90), HandController.lift_left(-10))
        await WheelController.move_backward(10, speed=Speed.Slow)
        await HandController.lift_right(-10, speed=Speed.Slow)

        # straightening 2nd yellow tower
        await WheelController.move_forward(80, speed=Speed.Medium, with_brake=True)
        await WheelController.move_backward(25)
        await multitask(HandController.lift_left(-10), HandController.lift_right(28))
        await WheelController.right_turn(180, turn_speed=90)

        # position to place the 2nd tower
        await multitask(HandController.lift_left(-10), HandController.lift_right(-10))
        await WheelController.move_towards_mat_color(MatColor.LightGreen)
        await HandController.lift_right(28)
        await WheelController.move_forward(69, speed=Speed.Slow)  # BGBES 70
        await multitask(WheelController.left_turn(turn_speed=90), HandController.lift_left())
        await WheelController.move_towards_mat_color(MatColor.Black)

        # placing the 2nd yellow tower
        await WheelController.right_turn(180, turn_speed=90)
        await multitask(HandController.lift_left(-10), HandController.lift_right(80, speed=Speed.Slow))
        await WheelController.move_forward(342, speed=Speed.Medium)
        await HandController.lift_right(32, speed=Speed.Slow)
        await WheelController.move_backward(120, speed=Speed.Slow)

        # positioning for getting red towers
        await multitask(HandController.lift_left(-10), HandController.lift_right(-10),
                        WheelController.move_backward(400, speed=Speed.Fastest))
        await WheelController.left_turn(210)
        await wait(100)
