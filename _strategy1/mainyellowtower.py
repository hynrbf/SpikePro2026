from pybricks.tools import wait, multitask  # multitask

from colorcontroller import MatColor
from handcontroller import HandController
from shared import Speed
from wheelcontroller import WheelController


class MissionYellowTower:
    @staticmethod
    async def exec_mission():
        # 1st bangga
        await WheelController.move_backward(500, with_brake=True)
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
        await WheelController.move_forward(100, speed=Speed.Slow)
        await multitask(HandController.lift_left(32), HandController.lift_right(28))
        await WheelController.move_forward(150, speed=Speed.Medium)
        await WheelController.left_turn(30, turn_speed=90)

        # long drive
        await WheelController.move_forward(600)
        await WheelController.move_towards_mat_color(MatColor.Black, mat_color_range_alt=MatColor.BlackTwo, 
                mat_color_range_alt_2=MatColor.BlackThree, mat_color_range_alt_2=MatColor.BlackFour, speed=Speed.Slow)
        await WheelController.move_forward(175)

        # Straightening of yellow towers
        await WheelController.left_turn(turn_speed=90)
        await multitask(HandController.lift_left(-10), HandController.lift_right(-10))
        await WheelController.move_forward(185, speed=Speed.Medium, with_brake=True)
        await WheelController.move_backward(25)
        await multitask(HandController.lift_left(34), HandController.lift_right(32))
        await WheelController.right_turn(180, turn_speed=90)
        await WheelController.move_backward(225, speed=Speed.Medium, with_brake=True)
        await multitask(HandController.lift_left(-10), HandController.lift_right(-10))
        await WheelController.move_forward(235, speed=Speed.Medium)  # ToDo.adjust. float is: 85 in condo; 225 in BGBES
        await multitask(HandController.lift_left(32), HandController.lift_right(32))

        # placing 1st yellow tower
        await WheelController.right_turn(turn_speed=90)
        await multitask(HandController.lift_left(-10), HandController.lift_right(-10))
        await WheelController.move_forward(40, speed=Speed.Slow)
        await WheelController.move_towards_mat_color(MatColor.BlackTwo)
        await multitask(HandController.lift_left(32), HandController.lift_right(28))
        await WheelController.left_turn(180, turn_speed=90)
        await multitask(HandController.lift_right(-10),
                        HandController.lift_left(-10))
        await WheelController.move_forward(100, speed=Speed.Medium)
        await multitask(HandController.lift_right(-10, speed=Speed.Slow),
                        HandController.lift_left(80, speed=Speed.Slow))
        await WheelController.move_forward(255, speed=Speed.Medium)
        await multitask(HandController.lift_left(40, speed=Speed.Slow), HandController.lift_right(28))
        await WheelController.move_backward(120, speed=Speed.Slow)
        await HandController.lift_left(-10)
        await WheelController.move_backward(80, speed=Speed.Medium)

        # Moving to the other side
        await multitask(HandController.lift_left(-10, speed=Speed.Slow), HandController.lift_right(28))
        await WheelController.right_turn(turn_speed=90)
        await WheelController.move_forward(540)
        await HandController.lift_right(80, speed=Speed.Slow)
        await WheelController.move_towards_mat_color(MatColor.Brown, mat_color_range_alt=MatColor.BrownTwo,
                                                     speed=Speed.Slow, is_print=True)
        await WheelController.move_backward(10, speed=Speed.Medium)

        # clear the artifacts
        await WheelController.right_turn(turn_speed=80)
        await multitask(HandController.lift_left(), HandController.lift_right(80, speed=Speed.Slow))
        await WheelController.move_forward(170)
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
        await multitask(HandController.lift_left(-10), HandController.lift_right(28))
        await WheelController.move_backward(150, speed=Speed.Medium, with_brake=True)
        await multitask(HandController.lift_left(-10), HandController.lift_right(-10))
        await WheelController.move_forward(230, speed=Speed.Medium)  # ToDo.adjust. float is: 85 in condo; 220 in BGBES
        await HandController.lift_right(28)
        await multitask(WheelController.left_turn(turn_speed=90), HandController.lift_left())
        await WheelController.move_towards_mat_color(MatColor.BlackThree)

        # placing the 2nd yellow tower
        await WheelController.right_turn(180, turn_speed=90)
        await multitask(HandController.lift_left(-10), HandController.lift_right(80, speed=Speed.Slow))
        await WheelController.move_forward(350, speed=Speed.Medium)
        await HandController.lift_right(32, speed=Speed.Slow)
        await WheelController.move_backward(120, speed=Speed.Slow)

        # positioning for visitors mission
        await multitask(HandController.lift_left(-10), HandController.lift_right(-10),
                        WheelController.move_backward(400, speed=Speed.Fastest))
        await WheelController.left_turn(210)
        await WheelController.right_turn(60)
        await WheelController.move_forward(250, speed=Speed.Fastest)
        await WheelController.right_turn(150)
        await WheelController.move_backward(900, with_brake=True, speed=Speed.Fastest)
        await wait(100)
