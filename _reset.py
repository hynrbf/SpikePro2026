from grippercontroller import GripperController
from wheelcontroller import WheelController
from pybricks import version
from pybricks.tools import run_task


async def main():
    print("Start, pb version: ", version)

    await GripperController.reset()
    await WheelController.reset()


print("DONE!")

run_task(main())
