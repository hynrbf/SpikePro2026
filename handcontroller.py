from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Stop
from shared import Speed


class HandController:
    __left_motor = Motor(Port.E)
    __right_motor = Motor(Port.A)

    @staticmethod
    async def reset():
        await HandController.__left_motor.run_target(Speed.Fast, 0, Stop.COAST)
        await HandController.__right_motor.run_target(Speed.Fast, 0, Stop.COAST)

    @staticmethod
    async def lift_left(degree: float = 80, speed: float = Speed.Fast):
        degree = degree if degree >= 0 else 0
        await HandController.__left_motor.run_target(speed, degree, Stop.HOLD)

    @staticmethod
    async def lift_right(degree: float = 80, speed: float = Speed.Fast):
        degree = degree if degree <= 0 else degree * -1
        await HandController.__right_motor.run_target(speed, degree, Stop.HOLD)
