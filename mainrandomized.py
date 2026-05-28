from handcontroller import HandController
from shared import Speed
from wheelcontroller import WheelController
from pybricks.tools import multitask, wait


class MissionRandomized:
    @staticmethod
    async def exec_mission():
        await WheelController.move_forward(450)
        await WheelController.left_turn()
        await WheelController.move_backward(520, with_brake=True)
        await WheelController.move_forward(180)
        await WheelController.right_turn()
        await WheelController.move_forward(230)
        await WheelController.move_forward(125)
        await WheelController.move_backward(120)
        await multitask(HandController.lift_left(speed=Speed.Slow),
                        HandController.lift_right(speed=Speed.Slow))
        await WheelController.right_turn()
        await WheelController.move_forward(125, speed=Speed.Slow)
        await multitask(HandController.lift_left(30, speed=Speed.Slow),
                        HandController.lift_right(30, speed=Speed.Slow))
        await multitask(WheelController.move_backward(100, speed=Speed.Slow),
                        HandController.lift_left(17, speed=Speed.Slow),
                        HandController.lift_right(17, speed=Speed.Slow))
        await WheelController.move_backward(850, with_brake=True)
        await WheelController.move_forward(300)
        await WheelController.right_turn()
        await WheelController.move_forward(20)
        await WheelController.right_turn()
        await multitask(HandController.lift_left(speed=Speed.Slow),
                        HandController.lift_right(speed=Speed.Slow))
        await WheelController.move_forward(200, speed=Speed.Slow)
        await wait(500)
        await WheelController.move_backward(900, with_brake=True)
        await WheelController.move_forward(180)
        await WheelController.right_turn()
        await WheelController.move_forward(255)
        await WheelController.move_forward(135)
        await WheelController.move_backward(100)
        await multitask(HandController.lift_left(speed=Speed.Slow),
                        HandController.lift_right(speed=Speed.Slow))
        await WheelController.right_turn()
        await WheelController.move_forward(130, speed=Speed.Slow)
        await multitask(HandController.lift_left(30, speed=Speed.Slow),
                        HandController.lift_right(30, speed=Speed.Slow))
        await multitask(WheelController.move_backward(100, speed=Speed.Slow),
                        HandController.lift_left(17, speed=Speed.Slow),
                        HandController.lift_right(17, speed=Speed.Slow))
        await WheelController.move_backward(850, with_brake=True)
        await WheelController.move_forward(350)
        await WheelController.left_turn()
        await WheelController.move_forward(95)
        await WheelController.left_turn()
        await multitask(HandController.lift_left(speed=Speed.Slow),
                        HandController.lift_right(speed=Speed.Slow))
        await WheelController.move_forward(275, speed=Speed.Slow)
        await wait(500)
