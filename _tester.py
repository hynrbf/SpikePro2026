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
    await HandController.lift_right(-10)
    await wait(1000)
    await HandController.lift_left(-10)
    await wait(1000)
    await HandController.reset()


async def test_wheel():
    await WheelController.move_towards_mat_color(-133, speed=Speed.Slow, is_print=True)
    # await WheelController.move_forward(float(900), Speed.Fast)
    # await WheelController.right_turn()
    # await WheelController.left_turn()
    # await WheelController.move_backward(float(100), Speed.Fast)
    # await wait(2000)
    pass


async def test_mat_color():
    await ColorController.print_mat_color(True)
    # await ColorController.print_mat_color_non_hsv(True)
    # await WheelController.move_towards_mat_color(348)


async def get_element_color():
    el_color = await ColorController.get_element_color()
    print(f"Box3 color: {el_color}.")


async def main():
    print("Start, pb version: ", version)

    # await HandController.reset()
    # await WheelController.reset()

    # await test_gripper()
    await test_wheel()
    # await test_element_color()
    # await test_mat_color()
    # await get_element_color()

    print("DONE!")


run_task(main())
