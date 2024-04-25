# Rail-mounted Robot Assistant

The objective of this project is to create a mobile rail-mounted robot assistant that can aid users in their tasks. This robot can be used as a third hand, a tool support, or a storage device. Its usage is straightforward: the user simply selects the workstation where they want to work, and the robot automatically moves to the selected workstation.

**Visual:** [https://a360.co/3oJu6gQ](https://a360.co/3oJu6gQ)

## Table of Contents:

- [Implementation](#implementation)
    - [Programming](#programming)
    - [Electronics](#electronics)
    - [Mechanics](#mechanics)
- [Components](#components)
- [Instructions](#instructions)
- [Enhancements](#enhancements)

---

## Implementation:

#### **Programming:**

- [Code](/Code/rail.py)

#### **Electronics:**

- [Wiring Diagram](/Electronics/workstation.kicad_sch)

#### **Mechanics:**

- [Project Modeling](/3D_Modeling/rail-mounted_robot.f3z)

---

## Components:

- [20X40 Profile](/Datasheet/DS_Profile.pdf) (quantity as needed)
- Assembly Bracket (X3)
- T-Nut (X3)
- [DC Motor](/Datasheet/DS_DC_motor.pdf) (X1)
- [Inductive Proximity Sensor](/Datasheet/DS_inductive_sensor.pdf) (X1)
- [ESP32-WROOM 32](/Datasheet/DS_ESP32-WROOM32.pdf) (X1)
- [L298N Motor Driver](/Datasheet/DS_L298N.pdf) (X1)
- [Push Buttons](/Datasheet/DS_button.pdf) (X3)
- [3D Printer Wheels](https://www.amazon.com/Printer-Bearing-Plastic-Bearings-Machined/dp/B0BD8XQ4Y4/ref=sr_1_22?keywords=3d+printer+wheel&qid=1686215897&sr=8-22) (X3)
- [Battery](/Datasheet/DS_battery.pdf) (X1)

---

## Instructions:

- **Assembly**
    1. Upload the [code](/Code/rail.py) to the ESP32.
    2. Perform the electrical wiring and place it in the dedicated compartment.
    3. Mount the DC motor, the inductive sensor, and the push buttons in their designated slots.
    4. Attach the assembly brackets to the profile using T-nuts at the desired workstations.
    5. Slide one end of the rail (profile) into the first support.
    6. Slide the robot along the rail.
    7. Slide the second support onto the other end of the rail.

- **Usage**
    1. Press the button corresponding to the desired workstation.

---

## Enhancements:

Several enhancements can be considered to improve the system:
    - Complete the 3D modeling to have printable and functional parts.
    - Add alligator clips on the left side to enable the robot to act as a third hand.
