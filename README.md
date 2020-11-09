Makelangelo-firmware-pio

Conversion of the great Makelangelo project to Platformio https://github.com/MarginallyClever/Makelangelo-firmware
Arduino IDE is a pain for debugging, therefore I try to setup a different structure.

Important note:
The Makelangelo-firmware repository is currently only a Submodule and I did several changes locally.
- Removed all libraries (they are fetched via lib_deps in plaformio.ini)
- resolved namespace conflict for EEPROM include by changing the files and the functions as well as includes to Meeprom, mEeprom ... 
- 


Currently only tested and working for RUMBA board (others will probably follow and be selectable via build options, but then the complete master of Makelangelo-firmware needs some rework)

Thanks to Dan Royer for his great work for so many years
My Plans
- Get it working on an esp32 (m5stack... because of the nice lcd display)
- Write a companion software in nodejs for art creation and easier management
- Revamp hardware for special purposes

I am creating and following several polar drawing robots so far, created my own and every project has its advantages and weaknesses. Trying to combine the best of all worlds is my top goal. All credits go to the initial creators and contributors.


