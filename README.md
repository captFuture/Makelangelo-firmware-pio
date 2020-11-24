Makelangelo-firmware-pio

Conversion of the great Makelangelo project to Platformio https://github.com/MarginallyClever/Makelangelo-firmware
Arduino IDE is a pain for debugging, therefore I try to setup a different structure.

How to set this up:
- Clone repository to your local machine
- Copy or clone the original Makelangelo-firmware Repository inside (master of 24.11.2020 works)
- delete content of libraries folder of the makelangelo repository (or it won't compile on platformio)

You find all configuration files for supported boards in the subfolder /configs/ of this project.
Currently the necessary file for the board you want to compile gets copied into the Makelangelo-firmware folder as local_config.h

RUMBA, RAMPS, MKS, SANGUINOLULU and SIXI_MEGA compile successfully as POLARGRAPH 
after adding #define LIMIT_SWITCH_PIN_LEFT     (MOTOR_0_LIMIT_SWITCH_PIN) and #define LIMIT_SWITCH_PIN_RIGHT    (MOTOR_1_LIMIT_SWITCH_PIN) to the board_xxxx.h files
(although I know that these probably are not Makelangelo boards)

The compiled .hex file is then copied to the /releases folder with the version number defined in the local_xxx_config.h file

This Project is specially created for keeping both Arduino IDE and Platformio compiling possible.

If you just klick compile in the bottom left corner of Vscode ALL environments defined in platformio.ini get compiled.
In order to just compile for ONE, you have to switch then env from default to a distinct one (also in the bottom left corner)

Thanks to Dan Royer for his great work for so many years
My Plans
- Get it working on an esp32 (m5stack... because of the nice lcd display)
- Write a companion software in nodejs for art creation and easier management
- Revamp hardware for special purposes

I am creating and following several polar drawing robots so far, created my own and every project has its advantages and weaknesses. Trying to combine the best of all worlds is my top goal. All credits go to the initial creators and contributors.

NOTE: I removed melzi, cncv3 (as this is for an UNO board and won't compile because of the size), and teensylu and commented out some work in progress environments (esp32, wemos...)
