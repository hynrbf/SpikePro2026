from pybricks.tools import multitask

from handcontroller import HandController
from shared import Speed
from wheelcontroller import WheelController


class MissionVisitor:
    @staticmethod
    async def exec_mission():
        await multitask(WheelController.move_backward(400, with_brake=True),
                        HandController.lift_right(), HandController.lift_left())
        await WheelController.move_forward(40)
        await WheelController.left_turn()
        await WheelController.move_backward(560, with_brake=True)
        await WheelController.move_forward(80)
        await WheelController.right_turn()
        await multitask(HandController.lift_left(10), HandController.lift_right(10))
        await WheelController.move_forward(40, speed=Speed.Slow)
        await WheelController.left_turn(20, turn_speed=30)
        await WheelController.move_forward(100, speed=Speed.Slow)
