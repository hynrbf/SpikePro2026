from pybricks.tools import run_task  # , wait
from pybricks import version

# from handcontroller import HandController
from mainrandomized import MissionRandomized

from mainredtower import MissionRedTower
from mainyellowtower import MissionYellowTower


# from wheelcontroller import WheelController


async def main():
    print("\nStart, pb version: ", version)

    # await MissionRandomized.exec_mission()
    # await MissionYellowTower.exec_mission()
    await MissionRedTower.exec_mission()
    print("DONE!")


run_task(main())
