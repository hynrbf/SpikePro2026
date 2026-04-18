from pybricks.tools import run_task
from pybricks import version

from wheelcontroller import WheelController


async def main():
    print("\nStart, pb version: ", version)

    await WheelController.move_forward(float(180))
    await WheelController.right_turn()
    await WheelController.move_backward(float(500))
    await WheelController.move_forward(float(380))
    await WheelController.left_turn(float(85))
    await WheelController.follow_the_line()

    # done only, do not remove
    print("DONE!")


run_task(main())
