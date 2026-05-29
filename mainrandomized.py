from colorcontroller import ColorController
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
        await WheelController.move_forward(150, speed=Speed.Slow)
        await WheelController.right_turn()
        await WheelController.move_forward(230, speed=Speed.Medium)
        await wait(500)
        await ColorController.get_element_color()
        await WheelController.move_forward(125, speed=Speed.Medium)
        await wait(500)
        await ColorController.get_element_color()
        await multitask(WheelController.move_backward(110), HandController.lift_left(),
                        HandController.lift_right())
        await WheelController.left_turn(turn_speed=90)
        await WheelController.move_forward(70)
        await multitask(WheelController.right_turn(180), HandController.lift_left(0),
                        HandController.lift_right(0))
        await WheelController.move_forward(150, speed=Speed.Slow, with_brake=True)
        await WheelController.move_backward(30)
        await multitask(HandController.lift_right(20, speed=Speed.Slow), HandController.lift_left(20, speed=Speed.Slow))
        await WheelController.right_turn(180, turn_speed=50)

        # await WheelController.move_backward(850, with_brake=True)
        # await WheelController.move_forward(300)
        # await WheelController.right_turn()
        # await WheelController.move_forward(20)
        # await WheelController.right_turn()
        # await multitask(HandController.lift_left(speed=Speed.Slow),
        #                 HandController.lift_right(speed=Speed.Slow))
        # await WheelController.move_forward(200, speed=Speed.Slow)
        # await wait(500)
        # await WheelController.move_backward(900, with_brake=True)
        # await WheelController.move_forward(180)
        # await WheelController.right_turn()
        # await WheelController.move_forward(255)
        # await WheelController.move_forward(135)
        # await WheelController.move_backward(100)
        # await multitask(HandController.lift_left(speed=Speed.Slow),
        #                 HandController.lift_right(speed=Speed.Slow))
        # await WheelController.right_turn()
        # await WheelController.move_forward(130, speed=Speed.Slow)
        # await multitask(HandController.lift_left(30, speed=Speed.Slow),
        #                 HandController.lift_right(30, speed=Speed.Slow))
        # await multitask(WheelController.move_backward(100, speed=Speed.Slow),
        #                 HandController.lift_left(17, speed=Speed.Slow),
        #                 HandController.lift_right(17, speed=Speed.Slow))
        # await WheelController.move_backward(850, with_brake=True)
        # await WheelController.move_forward(350)
        # await WheelController.left_turn()
        # await WheelController.move_forward(95)
        # await WheelController.left_turn()
        # await multitask(HandController.lift_left(speed=Speed.Slow),
        #                 HandController.lift_right(speed=Speed.Slow))
        # await WheelController.move_forward(275, speed=Speed.Slow)
        await wait(500)
