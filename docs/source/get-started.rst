.. _getting-started:

Getting Started
================

This section provides a step-by-step guide to setting up and integrating ESPVoice into your Home Assistant instance. It is assumed that you already have a working Home Assistant installation. If you do not have Home Assistant set up, please visit |ha_link| website for more information.

.. |ha_link| raw:: html

   <a href="https://www.home-assistant.io/" target="_blank">Home Assistant</a>


First power on
--------------

When ESPVoice is first powered on, it will enter a Wake Word learning phase, followed by a Voice Command learning phase for Control 01.

A wake word is a specific phrase that prompts ESPVoice to wake up and listen for the user's voice commands. Users will be instructed to speak the wake word three times in order to complete the wake word learning process.

After completing the wake word learning, ESPVoice will prompt for a voice command input for Control 01. Similarly user will be prompted to speak the voice command three times in order to complete the voice command learning process.

Congratulations! You have successfully completed the setup process for ESPVoice. You're now ready to move on to the next step to integrate ESPVoice into your Home Assistant.


.. raw:: html
    
    <div style="position: relative;  margin-bottom: 2em; height: 0; overflow: hidden; max-width: 100%; height: auto;" align="center">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/-nxbrpbBXz4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    </div>

Connecting to Home Assistant
----------------------------

.. admonition:: Prerequisite

    ESPHome is required to be installed in your Home Assistant for ESPVoice to work correctly. Please make sure |esphome_link| is installed before hand. 


.. |esphome_link| raw:: html

   <a href="https://www.home-assistant.io/integrations/esphome/" target="_blank">ESPHome</a>
    

#. Connect ESPVoice to a 5V Power Supply Unit using the provided USB-C cable.

#. ESPVoice will create a WIFI hotspot with the name "ESPVoice WIFI AP" if it cannot connect to any existing network. Seach and connect to "ESPVoice WIFI AP" via using any mobile devices/PC. The default password is *espvoice*

    .. image:: images/espvoice-hotspot.png
      :align: center

#. Once you are connected to ESPVoice's wifi hotspot, you will be automatically directed to ESPVoice's network connection page. If not, click the following link |espvoice_ap_link| to launch the page. Select your home wifi network and key in the correct credentials. 

    .. image:: images/espvoice-wifi-settings-2.png

    |

    ESPVoice will attempt to join your wifi network. 

    .. image:: images/espvoice-wifi-settings-3.png

    .. |espvoice_ap_link| raw:: html

        <a href="http://192.168.4.1" target="_blank">http://192.168.4.1</a>

#. Reconnect to your home network. Go to your Home Assistant -> Settings -> Devices & Services

    .. image:: images/connect-to-ha-step4.png
      :align: center

#. Home Assistant will automatically detects "ESPVoice-XXXXXX" as a new device. Click on "Add Device" to add ESPVoice to your Home Assistant.

    .. image:: images/connect-to-ha-step5.png
      :align: center

#. If no new device is detected, you may manually add it via "Add Integration" -> "ESPHome"-> enter the IP address of ESPVoice connected to your wifi network

    .. image:: images/connect-to-ha-step6-1.png
      :width: 300

    .. image:: images/connect-to-ha-step6-2.png
      :width: 300

Testing ESPVoice
----------------

To test whether you have successfully integrated ESPVoice into your Home Assistant:

#. Press "Firmware version" button in the ESPVoice control panel

#. Check the "Text Sensor" of ESPVoice for a valid firmware version, for example: V1.0.0. 
   See :ref:`ESPVoice Firmware Versions` for version info.


Creating your first voice activated automation
----------------------------------------------
Coming soon.