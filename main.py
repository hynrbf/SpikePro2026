from pybricks.tools import run_task, wait
from pybricks import version

from handcontroller import HandController
from mainrandomized import MissionRandomized
# from mainredtower import MissionRedTower
# from mainyellowtower import MissionYellowTower
from wheelcontroller import WheelController


async def main():
    print("\nStart, pb version: ", version)

    try:
        await MissionRandomized.exec_mission()
        # await MissionYellowTower.exec_mission()
        # await MissionRedTower.exec_mission()
        print("DONE!")
    finally:
        # await wait(2000)
        # await HandController.reset()
        # await WheelController.reset()
        pass


run_task(main())
