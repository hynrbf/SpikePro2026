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

6. Checklist
   check the wheels palagi natatangalan
   stabilize the hand
   do basic test _tester.py

7. getting red tower
await WheelController.move_forward(100, Speed.Slow, with_brake=True)
await multitask(HandController.lift_right(35,speed=Speed.Slow), HandController.lift_left(35,speed=Speed.Slow))
await WheelController.left_turn(180, turn_speed=80)
await WheelController.move_forward(500, speed=Speed.Medium)

8. If

 == ToDo==
 1.issues to fix
   black red - dapat front bangga the black to accurate
   all random - review all and fix accuracy
              - also fix if kabaliktad
