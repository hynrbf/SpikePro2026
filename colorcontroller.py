from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port


class MatColor:
    White = 0
    Black = 1
    Others = -1


class ColorController:
    __mat_sensor = ColorSensor(Port.C)

    @staticmethod
    async def get_mat_color() -> int:
        color = await ColorController.__mat_sensor.hsv()
        color_int = color.h
        print("mat color: ", color_int)

        # when it detects white then 0, which is center
        if 10 <= color_int <= 99:
            return MatColor.White

        # when it detects black return 1, swerving to the right
        if 111 <= color_int <= 280:
            return MatColor.Black

        # when detects other color return -1, swerving to the left
        if 100 <= color_int <= 110:
            return MatColor.Others

        # when it detects outside the above, just treat it as White so wheels move straight
        return MatColor.White
