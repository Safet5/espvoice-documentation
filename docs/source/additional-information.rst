Additional Information
======================

.. _espvoice_control_text_output:

EspVoice control text output
------------------------------

EspVoice will output a text value for every voice command or action. 
EspVoice will automatically output a subsequent "000" after 1s.
The table below summarizes the value for available commands:

+-------+-----------------------------+
| Value | Description                 |
+=======+=============================+
| 101   | Voice control 01 triggered  |
+-------+-----------------------------+
| 102   | Voice control 02 triggered  |
+-------+-----------------------------+
| 103   | Voice control 03 triggered  |
+-------+-----------------------------+
| 104   | Voice control 04 triggered  |
+-------+-----------------------------+
| 105   | Voice control 05 triggered  |
+-------+-----------------------------+
| 106   | Voice control 06 triggered  |
+-------+-----------------------------+
| 107   | Voice control 07 triggered  |
+-------+-----------------------------+
| 108   | Voice control 08 triggered  |
+-------+-----------------------------+
| 109   | Voice control 09 triggered  |
+-------+-----------------------------+
| 110   | Voice control 10 triggered  |
+-------+-----------------------------+
| 111   | Voice control 11 triggered  |
+-------+-----------------------------+
| 112   | Voice control 12 triggered  |
+-------+-----------------------------+
| 901   | Wake word detected          |
+-------+-----------------------------+
| 911   | Emergency Command triggered |
+-------+-----------------------------+

+-------+-------------------------+
| Value | Description             |
+=======+=========================+
| 201   | Welcome scene activated |
+-------+-------------------------+
| 202   | GoodBye scene activated |
+-------+-------------------------+
| 203   | Morning scene activated |
+-------+-------------------------+
| 204   | Evening scene activated |
+-------+-------------------------+


Hex command to initiate learning
--------------------------------

+--------------------------------+---------------------------+
| HEX                            | Description               |
+================================+===========================+
| [0xAA, 0x55, 0x65, 0x55, 0xAA] | Learn voice control 01    |
+--------------------------------+---------------------------+
| [0xAA, 0x55, 0x66, 0x55, 0xAA] | Learn voice control 02    |
+--------------------------------+---------------------------+
| [0xAA, 0x55, 0x67, 0x55, 0xAA] | Learn voice control 03    |
+--------------------------------+---------------------------+
| [0xAA, 0x55, 0x68, 0x55, 0xAA] | Learn voice control 04    |
+--------------------------------+---------------------------+
| [0xAA, 0x55, 0x69, 0x55, 0xAA] | Learn voice control 05    |
+--------------------------------+---------------------------+
| [0xAA, 0x55, 0x6A, 0x55, 0xAA] | Learn voice control 06    |
+--------------------------------+---------------------------+
| [0xAA, 0x55, 0x6B, 0x55, 0xAA] | Learn voice control 07    |
+--------------------------------+---------------------------+
| [0xAA, 0x55, 0x6C, 0x55, 0xAA] | Learn voice control 08    |
+--------------------------------+---------------------------+
| [0xAA, 0x55, 0x6D, 0x55, 0xAA] | Learn voice control 09    |
+--------------------------------+---------------------------+
| [0xAA, 0x55, 0x6E, 0x55, 0xAA] | Learn voice control 10    |
+--------------------------------+---------------------------+
| [0xAA, 0x55, 0x6F, 0x55, 0xAA] | Learn voice control 11    |
+--------------------------------+---------------------------+
| [0xAA, 0x55, 0x70, 0x55, 0xAA] | Learn voice control 12    |
+--------------------------------+---------------------------+

+--------------------------------+----------------------------------------------+
| HEX                            | Description                                  |
+================================+==============================================+
| [0xAA, 0x55, 0x00, 0x55, 0xAA] | Learn wake word                              |
+--------------------------------+----------------------------------------------+
| [0xAA, 0x55, 0x01, 0x55, 0xAA] | Learn confirm phrase                         |
+--------------------------------+----------------------------------------------+
| [0xAA, 0x55, 0x02, 0x55, 0xAA] | Learn emergency trigger phrase               |
+--------------------------------+----------------------------------------------+
| [0xAA, 0x55, 0x03, 0x55, 0xAA] | Learn voice recognition deactivation phrase  |
+--------------------------------+----------------------------------------------+


Hex command for various settings
--------------------------------

+--------------------------------+------------------------------+
| HEX                            | Description                  |
+================================+==============================+
| [0xAA, 0x55, 0x20, 0x55, 0xAA] | Delete all trained data      |
+--------------------------------+------------------------------+
| [0xAA, 0x55, 0x21, 0x55, 0xAA] | Mute speaker                 |
+--------------------------------+------------------------------+
| [0xAA, 0x55, 0x22, 0x55, 0xAA] | Unmute speaker               |
+--------------------------------+------------------------------+
| [0xAA, 0x55, 0x23, 0x55, 0xAA] | Start voice recognition      |
+--------------------------------+------------------------------+
| [0xAA, 0x55, 0x24, 0x55, 0xAA] | Enable voice recognition     |
+--------------------------------+------------------------------+
| [0xAA, 0x55, 0x25, 0x55, 0xAA] | Disable voice recognition    |
+--------------------------------+------------------------------+
| [0xAA, 0x55, 0x26, 0x55, 0xAA] | Volume down                  |
+--------------------------------+------------------------------+
| [0xAA, 0x55, 0x27, 0x55, 0xAA] | Volume up                    |
+--------------------------------+------------------------------+
| [0xAA, 0x55, 0x28, 0x55, 0xAA] | Auto reply off               |
+--------------------------------+------------------------------+
| [0xAA, 0x55, 0x29, 0x55, 0xAA] | Auto reply on                |
+--------------------------------+------------------------------+
| [0xAA, 0x55, 0x2A, 0x55, 0xAA] | Set volume to low            |
+--------------------------------+------------------------------+
| [0xAA, 0x55, 0x2B, 0x55, 0xAA] | Set volume to med            |
+--------------------------------+------------------------------+
| [0xAA, 0x55, 0x2C, 0x55, 0xAA] | Set volume to high           |
+--------------------------------+------------------------------+
| [0xAA, 0x55, 0x2D, 0x55, 0xAA] | Reset device                 |
+--------------------------------+------------------------------+
| [0xAA, 0x55, 0x2E, 0x55, 0xAA] | Get firmware version         |
+--------------------------------+------------------------------+


Hex command for scene trigger 
-----------------------------

+--------------------------------+-----------------------+
| HEX                            | Description           |
+================================+=======================+
| [0xAA, 0x55, 0x31, 0x55, 0xAA] | Trigger welcome scene |
+--------------------------------+-----------------------+
| [0xAA, 0x55, 0x32, 0x55, 0xAA] | Trigger goodBye scene |
+--------------------------------+-----------------------+
| [0xAA, 0x55, 0x33, 0x55, 0xAA] | Trigger morning scene |
+--------------------------------+-----------------------+
| [0xAA, 0x55, 0x34, 0x55, 0xAA] | Trigger evening scene |
+--------------------------------+-----------------------+
| [0xAA, 0x55, 0x35, 0x55, 0xAA] | Cancel scene trigger  |
+--------------------------------+-----------------------+


Hex code for public annoucement 
-------------------------------

+--------------------------------+-----------------------------+
| HEX                            | Description                 |
+================================+=============================+
| [0xAA, 0x55, 0x40, 0x55, 0xAA] | Alarm beep                  |
+--------------------------------+-----------------------------+
| [0xAA, 0x55, 0x41, 0x55, 0xAA] | Siren                       |
+--------------------------------+-----------------------------+
| [0xAA, 0x55, 0x42, 0x55, 0xAA] | Someone is at the main door |
+--------------------------------+-----------------------------+
| [0xAA, 0x55, 0x43, 0x55, 0xAA] | Someone is at the backyard  |
+--------------------------------+-----------------------------+
| [0xAA, 0x55, 0x44, 0x55, 0xAA] | Main door is opened         |
+--------------------------------+-----------------------------+
| [0xAA, 0x55, 0x45, 0x55, 0xAA] | Main door is closed         |
+--------------------------------+-----------------------------+
| [0xAA, 0x55, 0x46, 0x55, 0xAA] | Garage door is opened       |
+--------------------------------+-----------------------------+
| [0xAA, 0x55, 0x47, 0x55, 0xAA] | Garage door is closed       |
+--------------------------------+-----------------------------+
| [0xAA, 0x55, 0x48, 0x55, 0xAA] | Window is opened            |
+--------------------------------+-----------------------------+
| [0xAA, 0x55, 0x49, 0x55, 0xAA] | Window is closed            |
+--------------------------------+-----------------------------+
| [0xAA, 0x55, 0x4A, 0x55, 0xAA] | Alarm is armed away         |
+--------------------------------+-----------------------------+
| [0xAA, 0x55, 0x4B, 0x55, 0xAA] | Alarm is armed home         |
+--------------------------------+-----------------------------+
| [0xAA, 0x55, 0x4C, 0x55, 0xAA] | Alarm is disarmed           |
+--------------------------------+-----------------------------+
| [0xAA, 0x55, 0x4D, 0x55, 0xAA] | Door Bell                   |
+--------------------------------+-----------------------------+
