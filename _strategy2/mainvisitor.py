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

        # pushing all visitors
        await multitask(HandController.lift_left(10), HandController.lift_right(10))
        await WheelController.move_forward(900, speed=Speed.Medium)
        await wait(100)

        # Suprise rule
        await WheelController.move_backward(1300, speed=Speed.Medium, with_brake=True)
        await WheelController.move_forward(450)
        await WheelController.right_turn()
        await multitask(HandController.lift_left(-10), HandController.lift_right(-10))
        await WheelController.move_forward(600, speed=Speed.Medium)
        await multitask(HandController.lift_left(35), HandController.lift_right(35))
        await WheelController.right_turn()
        await WheelController.move_forward(600, speed=Speed.Medium, with_brake=True)
        await WheelController.move_backward(25, speed=Speed.Medium)
        await multitask(HandController.lift_left(-10), HandController.lift_right(-10))
        await WheelController.move_backward(205, speed=Speed.Medium)
