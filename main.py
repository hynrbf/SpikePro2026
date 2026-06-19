from pybricks.tools import run_task  # , wait
from pybricks import version

from mainredtower import MissionRedTower
from mainyellowtower import MissionYellowTower
from mainvisitor import MissionVisitor

async def main():
    print("\nStart, pb version: ", version)

    await MissionYellowTower.exec_mission()
    await MissionRedTower.exec_mission()
    await MissionVisitor.exec_mission()
    print("DONE!")


run_task(main())
