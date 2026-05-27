from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Stop
from shared import Speed


class GripperController:
    __left_motor = Motor(Port.E)
    __right_motor = Motor(Port.A)

    @staticmethod
    async def reset():
        await GripperController.__left_motor.run_target(Speed.Fast, 0, Stop.COAST)
        await GripperController.__right_motor.run_target(Speed.Fast, 0, Stop.COAST)

    @staticmethod
    async def lift_left(degree: float = 80):
        degree = degree if degree >= 0 else 0
        await GripperController.__left_motor.run_target(Speed.Fast, degree, Stop.HOLD)

    @staticmethod
    async def lift_right(degree: float = -80):
        degree = degree if degree <= 0 else 0
        await GripperController.__right_motor.run_target(Speed.Fast, degree, Stop.HOLD)
