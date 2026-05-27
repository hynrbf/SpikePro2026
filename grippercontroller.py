from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Stop
from shared import Speed


class GripperController:
    __right_motor = Motor(Port.A)
    __left_motor = Motor(Port.E)

    @staticmethod
    async def reset():
        await GripperController.__left_motor.run_target(Speed.Fast, 0, Stop.COAST)
        await GripperController.__right_motor.run_target(Speed.Fast, 0, Stop.COAST)

    @staticmethod
    async def lift_left():
        await GripperController.__left_motor.run_target(Speed.Fast, 80, Stop.HOLD)

    @staticmethod
    async def down_left(degree: float = 0):
        degree = degree if degree <= 0 else degree * -1
        await GripperController.__left_motor.run_target(Speed.Fast, degree, Stop.HOLD)

    @staticmethod
    async def lift_right():
        await GripperController.__right_motor.run_target(Speed.Fast, 20, Stop.HOLD)

    @staticmethod
    async def down_right(degree: float = 0):
        degree = degree if degree <= 0 else degree * -1
        await GripperController.__right_motor.run_target(Speed.Fast, degree, Stop.HOLD)
