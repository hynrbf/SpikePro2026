from handcontroller import HandController
from wheelcontroller import WheelController
from pybricks import version
from pybricks.tools import run_task
from pybricks.tools import multitask, wait

async def main():
    print("Start, pb version: ", version)

    # await HandController.reset()
    await WheelController.reset()
    await multitask(HandController.lift_left(80),
                        HandController.lift_right(80))
    print("DONE!")


run_task(main())
