from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port


class ColorController:
    __mat_sensor = ColorSensor(Port.C)

    @staticmethod
    async def get_mat_color() -> int:
        color = await ColorController.__mat_sensor.hsv()
        color_int = color.h

        # when it detects white then 0, which is center
        if 231 <= color_int <= 232:
            return 0

        # when it detects black return 1, swerving to the rigth
        if 40 <= color_int <= 65:
            return 1

        # when detects other color return -1, swerving to the left
        return -1
