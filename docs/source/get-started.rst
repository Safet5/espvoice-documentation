.. _getting-started:

Getting Started
================

This section will guide you to setup and integrate ESPVoice into your Home Assistant. We assume you have a working Home Assistant. For those who do not have Home Assistant set up, please visit |ha_link| for more details.

.. |ha_link| raw:: html

   <a href="https://www.home-assistant.io/" target="_blank">Home Assistant</a>


Connecting to Home Assistant
----------------------------

#. Connect ESPVoice to a 5V Power Supply Unit using the provided USB-C cable.

#. Connect to "ESPVoice WIFI AP" via using any mobile devices/PC. The default password is *espvoice*

    .. image:: images/espvoice-hotspot.png
      :align: center

#. Go to |espvoice_ap_link| via any web browser. Connect the device to WiFi network (same as the ESPHome) by keying in the WiFi credential 

    .. image:: images/espvoice-wifi-settings.png
      :align: center

    .. |espvoice_ap_link| raw:: html

        <a href="http://192.168.4.1" target="_blank">Home Assistant</a>

#. Go to your Home Assistant -> Settings -> Devices & Services

    .. image:: images/connect-to-ha-step4.png
      :align: center

#. "ESPVoice-XXXXXX" is detected as new device. Click on "Add Device" and voila it is connected to your Home Assistant server.

    .. image:: images/connect-to-ha-step5.png
      :align: center

#. If no new device is detected, you may manually add it via "Add Integration" -> "ESPHome"-> enter the IP address of ESPVoice connected to your wifi network

    .. image:: images/connect-to-ha-step6-1.png
      :width: 300

    .. image:: images/connect-to-ha-step6-2.png
      :width: 300


.. _learn_wake_words:

Learn Wake Word
---------------

A wake word is a phrase that causes ESPVoice to wake up and begin listening for user's voice command. When ESPVoice is powered up for the first time, wake word learning process will be started. Users will be instructed to speak the "Wake words" for 3 times to complete the wake word learning process and to activate the device.

To manually retrain or change the wake word:

#. Click on "ESPVoice-XXXXXX" under ESPHome integration

    .. image:: images/learn-wake-words-step1.png
      :width: 800

#. Press "[Learn Wake Words]" under "Device"-> "Control". Follow the voice instructions from ESPVoice to Learn the Wake words. 

    .. image:: images/learn-wake-words-step2.png
      :width: 800

#. You are required to say the same wake word in a quiet environment for 3 times to complete the learning process. It is recommended to use a wake word with more than 4 syllables for better recognition accuracy. Maximum allowable length of a wake word is 1.5 seconds. Do not pause when saying the wake word.

#. If ESPVoice fails to recognize the wake word, i.e. ESPVoice fails to match the second voice input with the first voice input, it will prompt the user for another voice input. The learning process is completed once ESPVoice has recorded 3 successful matches.

#. If more than 5 unsuccessful matches, ESPVoice will exit the learning process. You may restart the learning process by pressing "[Learn] Wake Word" button again.

#. Once learning is completed, ESPVoice will response with "I'm here" upon detecting the trained wake word. ESPVoice will also send a "900" text to Home Assistant.


.. _learn_voice_command:

Learn Voice Command
---------------------------

ESPVoice can recognize 12 customizable action voice commands + 1 "call-for-emergency" voice command. Users can initiate the learning of each customizable voice command by pressing the "Learning Voice Command" buttons in Home Assistant/ESPHome interface. Users will be instructed to say the command words for 3 times to complete the learning process. 

Users are free to assign any command to any of the voice command slot. For example, "Voice Command 01" can be set to "Switch on Kitchen Lights"; "Voice Command 02" can be set to "Off living room heaters" and etc. 

#. Click on "ESPVoice" under ESPHome integration

    .. image:: images/learn-voice-control-command-step1.png
      :align: center

#. Press "[Learn Control 01]" under "Device"-> "Control". Follow the voice instructions from ESPVoice to learn voice control command. 

    .. image:: images/learn-voice-control-command-step2.png
      :align: center

#. You are required to say the same voice command words in a quiet environment for 3 times to complete the learning process. It is recommended to use voice command with more than 4 syllables. Maximum allowable length of voice command is 1.5 seconds. Do not pause when saying the voice command.

#. If ESPVoice fails to recognize the voice command, for. e.g. ESPVoice fails to match the second voice input with the first voice input, it will prompt the user for another voice input. The learning process is completed once ESPVoice has recorded 3 successful matches. 

#. If more than 5 unsuccessful matches, ESPVoice will exit learning process. You may restart the learning by pressing "[Learn] Control 01" button again.

#. Once learning is complete, try to say the wake word (which you have trained earlier). After hearing "I’m Here" reply from ESPVoice, say the Voice command you have trained ESPVoice to execute the command. 

#. If recognition is successful, ESPVoice will response with "Okay". ESPVoice will also send a "101" text (for Control 01) to Home Assistant.







