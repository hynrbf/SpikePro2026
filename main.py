from pybricks.tools import run_task
from pybricks import version
from mainrandomized import MissionRandomized
from mainredtower import MissionRedTower
from mainyellowtower import MissionYellowTower


async def main():
    print("\nStart, pb version: ", version)

    try:
        await MissionRandomized.exec_mission()
        await MissionYellowTower.exec_mission()
        await MissionRedTower.exec_mission()
    finally:
        # await wait(2000)
        # await GripperController.reset()
        # await WheelController.reset()
        pass

    print("DONE!")


run_task(main())
