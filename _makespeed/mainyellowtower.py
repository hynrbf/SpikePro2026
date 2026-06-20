from pybricks.tools import wait, multitask  # multitask

from colorcontroller import MatColor
from handcontroller import HandController
from shared import Speed
from wheelcontroller import WheelController


class MissionYellowTower:
    @staticmethod
    async def exec_mission():
        # 1st bangga
        await WheelController.move_backward(400, with_brake=True)
        await WheelController.move_forward(225)
        await WheelController.left_turn()
        await WheelController.move_forward(175)
        await WheelController.move_towards_mat_color(MatColor.Black, speed=Speed.Slow)

        # Picking up 2 yellow towers
        await WheelController.move_forward(200, speed=Speed.Medium, with_brake=True)
        await WheelController.move_backward(30, speed=Speed.Medium)
        await multitask(HandController.lift_left(40), HandController.lift_right(40))

        # adjust tower holding
        await WheelController.right_turn(120, turn_speed=90)
        await multitask(HandController.lift_left(-10), HandController.lift_right(-10))
        await WheelController.move_forward(100, speed=Speed.Medium)
        await multitask(HandController.lift_left(32), HandController.lift_right(32))
        await WheelController.move_forward(150)
        await WheelController.left_turn(30, turn_speed=90)

        # long drive
        await WheelController.move_forward(600)
        await WheelController.move_towards_mat_color(MatColor.Black)
        await WheelController.move_forward(175)

        # Straightening of yellow towers
        await WheelController.left_turn(turn_speed=120)
        await multitask(HandController.lift_left(-10), HandController.lift_right(-10))
        await WheelController.move_forward(185, speed=Speed.Medium, with_brake=True)
        await WheelController.move_backward(25)
        await multitask(HandController.lift_left(32), HandController.lift_right(32))
        await WheelController.right_turn(180, turn_speed=120)
        await WheelController.move_backward(150, speed=Speed.Medium, with_brake=True)
        await multitask(HandController.lift_left(-10), HandController.lift_right(-10))
        await WheelController.move_forward(225, speed=Speed.Fast)  # float is: 85 in game map; 225 in BGBES
        await multitask(HandController.lift_left(32), HandController.lift_right(32))

        # placing 1st yellow tower
        await WheelController.right_turn(turn_speed=120)
        await multitask(HandController.lift_left(-10), HandController.lift_right(-10))
        await WheelController.move_forward(40, speed=Speed.Medium)
        await WheelController.move_towards_mat_color(MatColor.Black)
        await multitask(HandController.lift_left(32), HandController.lift_right(32))
        await WheelController.left_turn(180, turn_speed=120)
        await multitask(HandController.lift_right(-10, speed=200),
                        HandController.lift_left(90, speed=200))
        await WheelController.move_forward(355, speed=Speed.Medium)
        await multitask(HandController.lift_left(40, speed=200), HandController.lift_right(28))
        await WheelController.move_backward(120, speed=Speed.Medium)
        await HandController.lift_left(-10)
        await WheelController.move_backward(80)

        # Moving to the other side
        await multitask(HandController.lift_left(-10, speed=200), HandController.lift_right(28))
        await WheelController.right_turn(turn_speed=120)
        await WheelController.move_forward(520)
        await HandController.lift_right(80, speed=200)
        await WheelController.move_towards_mat_color(MatColor.White)  # MatColor.Green

        # clear the artifacts
        await WheelController.right_turn(turn_speed=120)
        await WheelController.move_forward(200)
        await multitask(HandController.lift_left(), HandController.lift_right(80, speed=200))
        await WheelController.move_backward(220)
        await multitask(WheelController.left_turn(turn_speed=120), HandController.lift_left(-10))
        await WheelController.move_backward(10, speed=Speed.Slow)
        await HandController.lift_right(-10, speed=Speed.Slow)

        # straightening 2nd yellow tower
        await WheelController.move_forward(80, speed=Speed.Medium, with_brake=True)
        await WheelController.move_backward(25)
        await multitask(HandController.lift_left(-10), HandController.lift_right(28))
        await WheelController.right_turn(180, turn_speed=120)

        # position to place the 2nd tower
        await multitask(HandController.lift_left(-10), HandController.lift_right(28))
        await WheelController.move_backward(150, speed=Speed.Fast, with_brake=True)
        await multitask(HandController.lift_left(-10), HandController.lift_right(-10))
        await WheelController.move_forward(220, speed=Speed.Fast)  # float is: 85 in condo; 220 in BGBES
        await HandController.lift_right(28)
        await multitask(WheelController.left_turn(turn_speed=120), HandController.lift_left())
        await WheelController.move_forward(100, speed=Speed.Fast)
        await WheelController.move_towards_mat_color(MatColor.Black)

        # placing the 2nd yellow tower
        await WheelController.right_turn(180, turn_speed=120)
        await multitask(HandController.lift_left(-10), HandController.lift_right(80, speed=Speed.Slow))
        await WheelController.move_forward(342, speed=Speed.Medium)
        await HandController.lift_right(32, speed=200)
        await WheelController.move_backward(120, speed=Speed.Medium)

        # positioning for getting red towers
        await multitask(HandController.lift_left(-10), HandController.lift_right(-10),
                        WheelController.move_backward(1150, speed=Speed.Fastest))
        await WheelController.move_backward(350, with_brake=True)
        await wait(100)
