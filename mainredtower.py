from colorcontroller import MatColor
from handcontroller import HandController
from shared import Speed
from wheelcontroller import WheelController
from pybricks.tools import multitask #, wait


class MissionRedTower:
    @staticmethod
    async def exec_mission():
        await WheelController.left_turn()
        await WheelController.move_backward(360, with_brake=True)
        await WheelController.move_forward(200)
        await WheelController.right_turn()
        await WheelController.move_forward(285, speed=Speed.Medium, with_brake=True)
        await multitask(HandController.lift_left(32, speed=Speed.Slow),
                        HandController.lift_right(26, speed=Speed.Slow))
        await WheelController.left_turn(180, turn_speed=Speed.Slow)
        await multitask(HandController.lift_left(0, speed=Speed.Slow),
                        HandController.lift_right(0, speed=Speed.Slow))
        await WheelController.move_forward(100)
        await multitask(HandController.lift_left(32, speed=Speed.Slow),
                        HandController.lift_right(30, speed=Speed.Slow))
        await WheelController.right_turn(50, turn_speed=90)
        await WheelController.move_forward(500)
        await WheelController.left_turn(50, turn_speed=90)
        await WheelController.move_forward(500)
        await WheelController.move_towards_mat_color(MatColor.Black, speed=Speed.Slow)
        await WheelController.move_forward(100)
        await WheelController.right_turn()
        await WheelController.move_forward(380, speed=Speed.Medium, with_brake=True)
        await WheelController.move_backward(30, speed=Speed.Slow)
        await WheelController.right_turn(180, turn_speed=90)

        return
        await WheelController.move_backward(300, with_brake=True)

        # await multitask(HandController.lift_left(30, speed=Speed.Slow),
        #                 HandController.lift_right(26, speed=Speed.Slow))
        # await WheelController.move_forward(350)
        # await WheelController.right_turn(turn_speed=60)
        # await WheelController.move_towards_mat_color(MatColor.GrayRock, speed=Speed.Slow)
        # await WheelController.move_backward(85)
        # await WheelController.left_turn(15, turn_speed=Speed.Slow)
        # await multitask(HandController.lift_left(30, speed=Speed.Slow),
        #                 HandController.lift_right(-10, speed=Speed.Slow))
        # await WheelController.move_backward(120, speed=Speed.Slow)
        # await WheelController.right_turn(15, turn_speed=Speed.Slow)
        # await WheelController.left_turn(turn_speed=60)
        # await WheelController.move_forward(300)
        # await WheelController.right_turn(turn_speed=60)
        # await WheelController.move_towards_mat_color(MatColor.Gray, speed=Speed.Slow)
        # await WheelController.move_backward(85)
        # await WheelController.left_turn(15, turn_speed=Speed.Slow)
        # await multitask(HandController.lift_left(30, speed=Speed.Slow),
        #                 HandController.lift_right(-10, speed=Speed.Slow))
        # await WheelController.move_backward(120, speed=Speed.Slow)
        # await WheelController.right_turn(15, turn_speed=Speed.Slow)

        # await WheelController.move_forward(115, speed=Speed.Slow)
        # await multitask(HandController.lift_left(30, speed=Speed.Slow),
        #                 HandController.lift_right(0, speed=Speed.Slow))
        # await WheelController.move_backward(120, speed=Speed.Slow)
        # await WheelController.left_turn(turn_speed=Speed.Slow)
        # await WheelController.move_forward(185)
        # await WheelController.right_turn(turn_speed=Speed.Slow)
        # await WheelController.move_forward(120, speed=Speed.Slow)
        # await HandController.lift_left(0, speed=Speed.Slow)
        # await WheelController.move_backward(125, speed=Speed.Slow)
        # await wait(500)
