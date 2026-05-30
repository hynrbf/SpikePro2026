from colorcontroller import ColorController, MatColor
from handcontroller import HandController
from shared import Speed
from wheelcontroller import WheelController
from pybricks.tools import multitask, wait


class MissionRandomized:
    @staticmethod
    async def exec_mission():
        # await multitask(WheelController.move_forward(450), HandController.lift_left(),
        #                 HandController.lift_right())
        # await WheelController.left_turn()
        # await WheelController.move_backward(520, with_brake=True)
        # await WheelController.move_forward(150, speed=Speed.Slow)
        # await WheelController.right_turn()
        # await WheelController.move_forward(230, speed=Speed.Medium)
        # await wait(500)
        # await ColorController.get_element_color()
        #
        # await WheelController.move_forward(125, speed=Speed.Medium)
        # await wait(500)
        # await ColorController.get_element_color()
        #
        # await WheelController.move_forward(127, speed=Speed.Medium)
        # await wait(500)
        # await ColorController.get_element_color()
        #
        # await WheelController.move_forward(125, speed=Speed.Medium)
        # await wait(500)
        # await ColorController.get_element_color()
        #
        # await multitask(WheelController.move_backward(110), HandController.lift_left(),
        #                 HandController.lift_right())
        # await WheelController.left_turn()
        # await WheelController.move_forward(70)
        # await multitask(WheelController.right_turn(180), HandController.lift_left(0),
        #                 HandController.lift_right(0))
        # await WheelController.move_forward(150, speed=Speed.Medium, with_brake=True)
        # await WheelController.move_backward(25)
        # await MissionRandomized.slowly_turning()
        # await multitask(WheelController.move_forward(100), HandController.reset())
        # await multitask(WheelController.move_forward(550), HandController.lift_left(10),
        #                 HandController.lift_right(10))
        # await WheelController.move_towards_mat_color(MatColor.Maroon)
        # await WheelController.move_backward(10)
        await multitask(HandController.lift_left(15),
                        HandController.lift_right(10))
        await wait(500)
        await WheelController.right_turn(turn_speed=50)
        await WheelController.move_towards_mat_color(MatColor.Green)
        await WheelController.right_turn(turn_speed=50)
        await WheelController.move_backward(150, with_brake=True)
        await WheelController.move_forward(135, speed=Speed.Medium)
        await WheelController.right_turn(turn_speed=50)
        await WheelController.move_forward(170, speed=Speed.Medium)
        await WheelController.right_turn(turn_speed=50)
        await HandController.reset()
        await WheelController.move_backward(100)

    @staticmethod
    async def slowly_turning():
        await multitask(HandController.lift_right(10, speed=Speed.Slow),
                        HandController.lift_left(10, speed=Speed.Slow))
        await WheelController.right_turn(5, turn_speed=50)
        await WheelController.move_backward(10)
        await WheelController.right_turn(175, turn_speed=50)
