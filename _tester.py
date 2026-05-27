from colorcontroller import ColorController
from grippercontroller import GripperController
from shared import Speed
from wheelcontroller import WheelController
from pybricks import version
from pybricks.tools import run_task, wait  # , multitask


async def test_gripper():
    await GripperController.lift_right()
    await wait(1000)
    await GripperController.lift_left()
    await wait(1000)
    await GripperController.lift_right(30)
    await wait(1000)
    await GripperController.lift_left(30)
    await wait(1000)


async def test_wheel():
    await WheelController.move_forward(float(100), Speed.Fast)
    await WheelController.right_turn()
    await WheelController.left_turn()
    await WheelController.move_backward(float(100), Speed.Fast)


async def test_color():
    await ColorController.get_element_color()
    pass


async def main():
    print("Start, pb version: ", version)

    try:
        await GripperController.reset()
        await WheelController.reset()

        # await test_gripper()
        # await test_wheel()
        await test_color()
    finally:
        await GripperController.reset()
        await WheelController.reset()
        pass

    print("DONE!")


run_task(main())
