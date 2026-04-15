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
        if 200 <= color_int <= 205:
            return MatColor.White

        # when it detects black return 1, swerving to the right
        if 165 <= color_int <= 199:
            return MatColor.Black

        # when detects other color return -1, swerving to the left
        return MatColor.Others
