1.python installation
C:\Program Files\Python313

2. sensors spike
https://education.lego.com/en-us/product-resources/spike-prime/downloads/technical-specifications/

3. checking wrong code
ruff check .
ruff check . --fix

4. pycharm powershell
winget search --id Microsoft.PowerShell
winget install --id Microsoft.PowerShell --source winget

5. Ports from back view
    A=left hand
    B=right motor
    C=color mat
    D=color side
    E=right hand
    F=left motor

6. basic test in actual mat
a. color values
    if 200 <= color_int <= 205:

    # when it detects black return 1, swerving to the right
    if 165 <= color_int <= 199:

7.
color = await ColorController.mat_sensor.hsv()
color_int = color.h
print(color_int)

 == ToDo==
 1. coach Mike, to make front to bangga
    likod to check if ok
 2. to tidy up