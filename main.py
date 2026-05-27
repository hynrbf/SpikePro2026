from pybricks.tools import run_task
from pybricks import version
from pybricks.tools import multitask  # wait

from grippercontroller import GripperController
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
        await WheelController.move_backward(355)
        await WheelController.left_turn()
        await WheelController.move_forward(120)
        await WheelController.right_turn()
        await WheelController.move_forward(258)
        await WheelController.right_turn()
        await WheelController.move_forward(260, Speed.Slow, with_brake=True)
        await multitask(WheelController.move_backward(30), GripperController.lift_left(speed=Speed.Slow),
                        GripperController.lift_right(speed=Speed.Slow))
        await WheelController.move_backward(200)
        await WheelController.left_turn()
        await WheelController.move_backward(120)
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
