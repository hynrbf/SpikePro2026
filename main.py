from pybricks.tools import run_task
from pybricks import version

import wheelcontroller
from handcontroller import HandController
from pybricks.tools import multitask, wait

# from handcontroller import HandController
from mainrandomized import MissionRandomized
from mainyellowtower import MissionYellowTower
from shared import Speed
from wheelcontroller import WheelController


# from shared import Speed
# from wheelcontroller import WheelController


async def main():
    print("\nStart, pb version: ", version)

    try:
        # await MissionRandomized.exec_mission()
        # await MissionYellowTower.exec_mission()
        pass
        await WheelController.move_backward(1600, with_brake=True)
        await WheelController.move_forward(300)
        await WheelController.right_turn()
        await WheelController.move_backward(900, with_brake=True)
        await WheelController.move_forward(200)
        await multitask(WheelController.right_turn(), HandController.lift_left(50),
                        HandController.lift_right(50))
        await WheelController.move_forward(200, speed=Speed.Slow)
        await multitask(HandController.lift_left(80, speed=Speed.Slow),
                        HandController.lift_right(80, speed=Speed.Slow))
        await WheelController.left_turn(180, turn_speed=Speed.Slow)
        await multitask(HandController.lift_left(50, speed=Speed.Slow),
                        HandController.lift_right(50, speed=Speed.Slow))
        await WheelController.move_forward(700)
        await WheelController.move_towards_mat_color(210, speed=Speed.Slow)
        await WheelController.move_forward(250)
        await multitask(HandController.lift_left(80, speed=Speed.Slow),
                        HandController.lift_right(80, speed=Speed.Slow))
        await WheelController.right_turn(turn_speed=Speed.Slow)
        await WheelController.move_backward(200, with_brake=True)


    finally:
        # await wait(2000)
        # await GripperController.reset()
        # await WheelController.reset()
        pass

    print("DONE!")


run_task(main())
