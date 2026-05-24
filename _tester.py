from grippercontroller import GripperController
# from wheelcontroller import WheelController
from pybricks import version
from pybricks.tools import run_task, wait  # , multitask


async def test_gripper():
    await GripperController.reset()
    await wait(1000)
    await GripperController.close()
    await wait(1000)
    await GripperController.lift()
    await wait(1000)
    await GripperController.down()
    await wait(1000)
    await GripperController.opening()
    await wait(1000)


# async def test_wheel():
#     await WheelController.move_forward(float(100))
#     await WheelController.right_turn()
#     await WheelController.left_turn()
#     await WheelController.move_backward(float(100))


async def main():
    print("Start, pb version: ", version)
    # await GripperController.reset_both_arms()

    try:
        await test_gripper()
        # await test_wheel()
        # await test_color()
        # await WheelController.move_towards_white_floor()
    finally:
        await GripperController.reset()

    print("DONE!")


run_task(main())
