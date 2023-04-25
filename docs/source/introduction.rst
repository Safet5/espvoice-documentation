Introduction
=====================

.. image:: images/espvoice.png
  :width: 250
  :align: center


The ESPVoice is a smart offline speech recognition device designed to work under ESPHome and Home Assistant platforms. It is equipped with an offline voice recognition module that performs speech detection and recognition for various smart home applications. ESPVoice is capable of training and recognizing speech in any language or dialect spoken by the user. All the detection and recognition outputs are transmitted to ESPHome or Home Assistant via an ESP32 module. 

Compare to existing smart speakers, ESPVoice offers several advantages, such as:

* **Fast Recognition:** It comes equipped with a built-in AI speech recognition module, enabling instant local speech detection and recognition without the need for internet connectivity.
* **Customized Recognition:**  Users can create their own voice commands and activate them with any desired name. The AI speech recognition module can be trained using the user's own voices in any language or dialect.
* **Open source hardware and customizable:** ESPVoice is integrated with an ESP32 module for WIFI and Bluetooth data communication, making it highly compatible with various open-source platforms. Users are able to reprogram the ESP32 module to fit to their specific project requirements. 

Features
---------

* Self-learning capability: ESPVoice can be trained using your voice in any languages or dialects  
* 12 x Customizable Voice Control Commands
* 1 x Customizable Wake Word
* 1 x Call for Emergency Help
* 4 x Scene Confirmation Controls 
* 14 x Standard announcements used for PA system
* ESP32 provides WiFi/Bluetooth connectivity
* Bluetooth Proxy for Home Assistant
* Attached with a mono 3W tweeter for speech recognition response and PA applications
* ESPVoice is reprogrammable
* Powered with USB-C Port (Power supply unit is not supplied)


How does it work?
-----------------

.. image:: images/intro-how-it-works.png
  :width: 800
  
ESPVoice can detect 1 customizable wake word and recognize up to 13 customizable voice commands. 

**Wake word**

| ESPVoice's wake word is fully customizable and can be set to any languages, for example "Hey ESPVoice", "Jarvis", "Sr. Elástico" etc. 
| For more information, see :ref:`learn_wake_word`.

**Voice commands**

| ESPVoice can be trained to recognize 12 customizable action voice commands + 1 "call-for-emergency" voice command. Users can initiate the learning of each customizable voice command using the "Learning Voice Command" buttons in Home Assistant/ESPHome interface. 
| For more information, see :ref:`learn_voice_command`.

**Voice Detection and Recognition**

ESPVoice works in two-stages, Detection Stage and Recognition Stage. At rest, ESPVoice is in Detection Stage, i.e. ESPVoice is constantly listening to the wake-word (which was set in the learning process earlier).  Once the "wake-word" is detected, ESPVoice will enter into Recogntion Stage where ESPVoice is alerted to recognize any voice captured from the built in microphone. If the voice data matches with the voice-learning database (which was built during the voice command learning process earlier), ESPVoice will output the corresponding command code via a TEXT sensor to Home Assistant/ESPHome. 

For example if "Switch on Kitchen lights" was recognized, ESPVoiceControl text sensor will output "101" to represent "Voice Control 01"; if "Off living room heaters" was recognized, ESPVoiceControl text sensor will output "102" to represent "Voice Control 02" etc. Table belows demonstrate the text sensor outputs for each voice control commands. If no voice command is detected for more than 10 seconds, ESPVoice goes back to Detection Stage.
The output for corresponding voice command are summarized in :ref:`espvoice_control_text_output`

Similarly, users can set any Emergency Phrase to trigger Emergency Action in ESPVoice. For e.g. "Call 911", "Jarvis call for Help", etc. Once Emergency phrase is detected, ESPVoice will set the volume to Maximum and play a Siren Tune for 3 sec, and simultaneously output "911" to ESPVoice control text sensor to Home assistant for further action.


Head on to the next section to :ref:`get started <getting-started>` with ESPVoice!



Where to buy?
-------------

Head to our |online shop| to check out ESPVoice!

.. |online shop| raw:: html

   <a href="https://esp-voice.com/shop/" target="_blank">online shop</a>
