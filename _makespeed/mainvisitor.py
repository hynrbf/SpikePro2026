from pybricks.tools import multitask, wait

from handcontroller import HandController
from shared import Speed
from wheelcontroller import WheelController


class MissionVisitor:
    @staticmethod
    async def exec_mission():
        await multitask(WheelController.move_forward(40),
                        HandController.lift_right(), HandController.lift_left())
        await WheelController.left_turn()

        # 1st bangga
        await  WheelController.move_backward(450, with_brake=True)
        await multitask(WheelController.move_forward(73), HandController.lift_right(),
                        HandController.lift_left())
        await WheelController.right_turn()

        # getting 2 visitors slowly
        await multitask(HandController.lift_left(10), HandController.lift_right(10))
        await WheelController.move_forward(40, speed=Speed.Slow)
        await WheelController.left_turn(32, turn_speed=30)
        await WheelController.move_forward(100, speed=Speed.Slow)
        await WheelController.move_backward(100, speed=Speed.Slow)
        await WheelController.right_turn(32)
        await WheelController.move_forward(180, speed=Speed.Slow)
        await WheelController.left_turn(30, turn_speed=30)
        await WheelController.move_forward(250, speed=Speed.Slow)
        await multitask(HandController.lift_right(-10, speed=Speed.Slow),
                        HandController.lift_left(-3, speed=Speed.Slow))
        await WheelController.move_backward(90, speed=Speed.Slow)
        await multitask(HandController.lift_right(10),
                        HandController.lift_left())
        await WheelController.move_forward(145, speed=Speed.Slow)
        await HandController.lift_left(15)

        # putting green visitor
        await WheelController.move_forward(100, speed=Speed.Slow)
        await WheelController.right_turn(40, turn_speed=30)
        await multitask(WheelController.move_forward(200, speed=Speed.Medium),
                        HandController.lift_left(15))
        await WheelController.right_turn(40, turn_speed=30)
        await WheelController.move_forward(125, speed=Speed.Medium)
        await HandController.lift_right(0)
        await WheelController.move_backward(145, speed=Speed.Slow)

        # going to the other side
        await WheelController.left_turn(120, turn_speed=90)
        await WheelController.move_forward(500, speed=Speed.Fastest)

        # putting the red visitor
        await WheelController.move_forward(250, speed=Speed.Medium, with_brake=True)
        await WheelController.move_backward(20, speed=Speed.Medium)
        await HandController.lift_left(speed=Speed.Slow)
        await wait(100)
