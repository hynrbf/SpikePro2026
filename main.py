from pybricks.tools import run_task
from pybricks import version
from pybricks.tools import multitask, wait

from handcontroller import HandController
from shared import Speed
from wheelcontroller import WheelController


async def main():
    print("\nStart, pb version: ", version)

    try:
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
        await WheelController.right_turn(180)
        await multitask(HandController.lift_left(speed=Speed.Slow),
                        HandController.lift_right(speed=Speed.Slow))
        await WheelController.move_forward(200, speed=Speed.Slow)
        await wait(500)

        # done only, do not remove
    finally:
        # await wait(2000)
        # await GripperController.reset()
        # await WheelController.reset()
        pass

    print("DONE!")


run_task(main())
