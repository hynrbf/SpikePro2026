from colorcontroller import ColorController
from handcontroller import HandController
from shared import Speed
from wheelcontroller import WheelController
from pybricks import version
from pybricks.tools import run_task, wait  # , multitask


async def test_gripper():
    await HandController.lift_right()
    await wait(1000)
    await HandController.lift_left()
    await wait(1000)
    await HandController.lift_right(30)
    await wait(1000)
    await HandController.lift_left(30)
    await wait(1000)


async def test_wheel():
    await WheelController.move_forward(float(100), Speed.Fast)
    await WheelController.right_turn()
    await WheelController.left_turn()
    await WheelController.move_backward(float(100), Speed.Fast)


async def test_element_color():
    await ColorController.get_element_color()


async def test_mat_color():
    await WheelController.move_towards_mat_color(175)


async def main():
    print("Start, pb version: ", version)

    try:
        await HandController.reset()
        await WheelController.reset()

        await test_gripper()
        await test_wheel()
        await test_element_color()
        await test_mat_color()
    finally:
        await HandController.reset()
        await WheelController.reset()
        pass

    print("DONE!")


run_task(main())
