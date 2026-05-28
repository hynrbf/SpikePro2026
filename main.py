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

    finally:
        # await wait(2000)
        # await GripperController.reset()
        # await WheelController.reset()
        pass

    print("DONE!")


run_task(main())
