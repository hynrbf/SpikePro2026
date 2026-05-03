from pybricks.tools import run_task
from pybricks import version

from wheelcontroller import WheelController


async def main():
    print("\nStart, pb version: ", version)

    # await WheelController.move_forward(float(180))
    # await WheelController.right_turn()
    # await WheelController.move_backward(float(500))
    # await WheelController.move_forward(float(390))
    # await WheelController.left_turn(float(83))
    await WheelController.follow_the_line(145)
    await WheelController.follow_the_line(145, 0.90)

    # done only, do not remove
    print("DONE!")


run_task(main())
