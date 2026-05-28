from pybricks.tools import run_task
from pybricks import version

import wheelcontroller
from handcontroller import HandController
from pybricks.tools import multitask, wait

# from handcontroller import HandController
from mainrandomized import MissionRandomized
from shared import Speed
from wheelcontroller import WheelController


# from shared import Speed
# from wheelcontroller import WheelController


async def main():
    print("\nStart, pb version: ", version)

    try:
        # await MissionRandomized.exec_mission()
        await WheelController.move_backward(220)
        await WheelController.left_turn()
        await WheelController.move_forward(750)
        await WheelController.move_towards_mat_color(210, Speed.Medium)
        await WheelController.move_backward(190)
        await WheelController.left_turn()
        await WheelController.move_backward(300)
        await WheelController.move_forward(280)
        await WheelController.right_turn()
        await WheelController.move_forward(410)
        await WheelController.right_turn()
        await multitask(HandController.lift_left(0, speed=Speed.Slow),
                        HandController.lift_right(0, speed=Speed.Slow))
        await WheelController.move_forward(170, Speed.Medium, with_brake=True)
        await multitask(HandController.lift_left(60, speed=Speed.Slow),
                        HandController.lift_right(60, speed=Speed.Slow))
        await WheelController.move_backward(70, Speed.Medium)
        await WheelController.right_turn(180)
        await WheelController.move_backward(240, Speed.Medium, with_brake=True)
        await WheelController.move_forward(200, Speed.Medium)
        await WheelController.left_turn()
        await WheelController.move_forward(580)
        await WheelController.move_towards_mat_color(210, Speed.Slow)
        await WheelController.move_forward(300)
        await WheelController.right_turn()
        await WheelController.move_backward(230, Speed.Medium)
        await WheelController.move_forward(230, Speed.Medium)
        await WheelController.left_turn()
        await HandController.lift_left(85, speed=Speed.Slow)
        await WheelController.move_forward(115, Speed.Slow)
        await HandController.lift_left(45, speed=Speed.Slow)
        await WheelController.move_backward(115, Speed.Slow)
        await WheelController.right_turn()
        await WheelController.move_backward(230, Speed.Medium)
        await WheelController.move_forward(230, Speed.Medium)
        await WheelController.right_turn(180)
        await WheelController.move_backward(760, Speed.Medium, with_brake=True)
        await WheelController.move_forward(230, Speed.Medium)
        await WheelController.right_turn()
        await HandController.lift_right(85, speed=Speed.Slow)
        await WheelController.move_forward(95, Speed.Slow)
        await HandController.lift_right(40, speed=Speed.Slow)
        await WheelController.move_backward(115, Speed.Slow)

    finally:
        # await wait(2000)
        # await GripperController.reset()
        # await WheelController.reset()
        pass

    print("DONE!")


run_task(main())
