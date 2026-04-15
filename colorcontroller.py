from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port


class ColorController:
    __mat_sensor = ColorSensor(Port.C)

    @staticmethod
    async def get_mat_color() -> int:
        color = await ColorController.__mat_sensor.hsv()
        color_int = color.h
        print("mat color: ", color_int)

        # when it detects white then 0, which is center
        if 200 <= color_int <= 205:
            return 0

        # when it detects black return 1, swerving to the right
        if color_int <= 199:
            return 1

        # when detects other color return -1, swerving to the left
        return -1
