from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Stop
from shared import Speed


class GripperController:
    __front_motor = Motor(Port.E)
    __back_motor = Motor(Port.F)

    @staticmethod
    async def reset():
        await GripperController.__back_motor.run_target(Speed.Fast, 0, Stop.COAST)
        await GripperController.__front_motor.run_target(Speed.Fast, 0, Stop.COAST)

    @staticmethod
    async def lift():
        await GripperController.__back_motor.run_target(Speed.Fast, 160, Stop.HOLD)

    @staticmethod
    async def down(degree: float = 0):
        degree = degree if degree <= 0 else degree * -1
        await GripperController.__back_motor.run_target(Speed.Fast, degree, Stop.HOLD)

    @staticmethod
    async def close():
        await GripperController.__front_motor.run_target(Speed.Fast, 20, Stop.HOLD)

    @staticmethod
    async def opening():
        await GripperController.__front_motor.run_target(Speed.Fast, -20, Stop.HOLD)
