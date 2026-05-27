from pybricks.tools import run_task
from pybricks import version
from pybricks.tools import multitask  # wait

from grippercontroller import GripperController
from wheelcontroller import WheelController


async def main():
    print("\nStart, pb version: ", version)

    try:
        await WheelController.move_backward(380, with_brake=True)
        await WheelController.move_forward(220)
        await multitask(WheelController.left_turn(), GripperController.lift_right())
        await multitask(WheelController.move_forward(370, with_brake=True), GripperController.down_left(20))
        await GripperController.down_right()
        await WheelController.move_backward(355)
        await WheelController.right_turn()
        await WheelController.move_forward(330)

        # await WheelController.move_backward(float(500))
        # await WheelController.move_forward(float(390))
        # await WheelController.left_turn(float(83))
        # await WheelController.follow_the_line(120)
        # await WheelController.follow_the_line(150, 0.90)
        # await GripperController.reset()
        # await GripperController.up()
        # await wait(100)
        # await GripperController.down()

        # await GripperController.close()
        # await wait(100)
        # await GripperController.opening()

        # done only, do not remove
    finally:
        # await wait(2000)
        # await GripperController.reset()
        # await WheelController.reset()
        pass

    print("DONE!")


run_task(main())
