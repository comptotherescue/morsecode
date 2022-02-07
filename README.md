# morsecode

## Implementation details

This project creates morse code for the given string and displays it on the LED lights attached to raspberry pi at the USB port.

This is achieved by turning the USB port power on/off using hub-ctrl command.
You need to get that using this package: https://github.com/codazoda/hub-ctrl.c

Code converts the string into morse code, you can see this on the console.

### How to run it?

To run this file use the following command

```
pi@raspberrypi:~ $ python lights.py --m "Happy new year"
('H', 'morse_code:', '. . . .')
('A', 'morse_code:', '. -')
('P', 'morse_code:', '. - - .')
('P', 'morse_code:', '. - - .')
('Y', 'morse_code:', '- . - -')
('Blank', 'morse_code:', '. . . . . . .')
('N', 'morse_code:', '- .')
('E', 'morse_code:', '.')
('W', 'morse_code:', '. - -')
('Blank', 'morse_code:', '. . . . . . .')
('Y', 'morse_code:', '- . - -')
('E', 'morse_code:', '.')
('A', 'morse_code:', '. -')
('R', 'morse_code:', '. - .')
pi@raspberrypi:~ $ 
```