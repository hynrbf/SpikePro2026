from wheelcontroller import WheelController
from pybricks import version
from pybricks.tools import run_task
from pybricks.tools import wait


async def test_wheel():
    WheelController.follow_the_line()
    await wait(1000)
    # await WheelController.move_forward(float(400))
    # await WheelController.left_turn()
    # await wait(1000)
    # await WheelController.right_turn()
    # await wait(1000)
    # await WheelController.right_turn()
    # await wait(1000)
    # await WheelController.left_turn()


async def main():
    print("Start, pb version: ", version)
    # await GripperController.reset_both_arms()

    # await test_gripper()
    await test_wheel()
    # await test_color()
    # await WheelController.move_towards_white_floor()

    print("DONE!")


run_task(main())
