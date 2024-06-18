---
title: QSL4A API Documentation

language_tabs: # must be one of https://github.com/rouge-ruby/rouge/wiki/List-of-supported-languages-and-lexers
  - python

toc_footers:
  - 

#includes:
#  - errors

search: true

code_clipboard: true

meta:
  - name: description
    content: Documentation for QPython's QSL4A API
---

# QSL4A APIs Documentation

The Scripting Layer for Android (abridged as SL4A, and previously named Android Scripting Environment or ASE) is a library that allows the creation and running of scripts written in various scripting languages directly on Android devices. QPython start to extend the SL4A project and integrate it.


There are many SL4A APIs, if you found any issue, please `report an issue <https://github.com/qpython-android/qpython/issues>`_.

# 01 AndroidFacade

## 0101 Clipboard APIs

### setClipboard(text)

   Put text in the clipboard

   :param str text: text

### getClipboard()

   Read text from the clipboard

   :return: The text in the clipboard


> Please run below script within your QPython


```python

    from androidhelper import Android
    droid = Android()

    #setClipboard
    droid.setClipboard("Hello World")

    #getClipboard
    clipboard = droid.getClipboard().result
```


## 0102 Intent & startActivity APIs

### makeIntent(action, uri, type, extras, categories, packagename, classname, flags)

   Starts an activity and returns the result

   :param str action: action
   :param str uri(Optional): uri
   :param str type(Optional): MIME type/subtype of the URI
   :param object extras(Optional): a Map of extras to add to the Intent
   :param list categories(Optional): a List of categories to add to the Intent
   :param str packagename(Optional): name of package. If used, requires classname to be useful
   :param str classname(Optional): name of class. If used, requires packagename to be useful
   :param int flags(Optional): Intent flags

   :return: An object representing an Intent



> sample code to show makeIntent


### getIntent()

   Returns the intent that launched the script


> sample code to show getIntent


### startActivityForResult(action, uri, type, extras, packagename, classname)

   Starts an activity and returns the result

   :param str action: action
   :param str uri(Optional): uri
   :param str type(Optional): MIME type/subtype of the URI
   :param object extras(Optional): a Map of extras to add to the Intent
   :param str packagename(Optional): name of package. If used, requires classname to be useful
   :param str classname(Optional): name of class. If used, requires packagename to be useful

   :return: A Map representation of the result Intent



> sample code to show startActivityForResult


### startActivityForResultIntent(intent)

   Starts an activity and returns the result

   :param Intent intent: Intent in the format as returned from makeIntent

   :return: A Map representation of the result Intent


> sample code to show startActivityForResultIntent

### startActivityIntent(intent, wait)

   Starts an activity

   :param Intent intent: Intent in the format as returned from makeIntent
   :param bool wait(Optional): block until the user exits the started activity


> sample code to show startActivityIntent


### startActivity(action, uri, type, extras, wait, packagename, classname)

   Starts an activity

   :param str action: action
   :param str uri(Optional): uri
   :param str type(Optional): MIME type/subtype of the URI
   :param object extras(Optional): a Map of extras to add to the Intent
   :param bool wait(Optional): block until the user exits the started activity
   :param str packagename(Optional): name of package. If used, requires classname to be useful
   :param str classname(Optional): name of class. If used, requires packagename to be useful


> sample code to show startActivityForResultIntent


## 0103 SendBroadcast APIs

### sendBroadcast(action, uri, type, extras, packagename, classname)

   Send a broadcast

   :param str action: action
   :param str uri(Optional): uri
   :param str type(Optional): MIME type/subtype of the URI
   :param object extras(Optional): a Map of extras to add to the Intent
   :param str packagename(Optional): name of package. If used, requires classname to be useful
   :param str classname(Optional): name of class. If used, requires packagename to be useful


> sample code to show sendBroadcast

### sendBroadcastIntent(intent)

   Send a broadcast

   :param Intent intent: Intent in the format as returned from makeIntent


> sample code to show sendBroadcastIntent


## 0104 Vibrate

### vibrate(intent)

   Vibrates the phone or a specified duration in milliseconds

   :param int duration: duration in milliseconds


> sample code to show vibrate


## 0105 NetworkStatus

### getNetworkStatus()

   Returns the status of network connection


> sample code to show getNetworkStatus

## 0106 PackageVersion APIs

### requiredVersion(requiredVersion)

   Checks if version of QPython SL4A is greater than or equal to the specified version

   :param int requiredVersion: requiredVersion

   :return: true or false


### getPackageVersionCode(packageName)

   Returns package version code

   :param str packageName: packageName

   :return: Package version code

### getPackageVersion(packageName)

   Returns package version name

   :param str packageName: packageName

   :return: Package version name


> sample code to show getPackageVersionCode & getPackageVersion


## 0107 System APIs

### getConstants(classname)

   Get list of constants (static final fields) for a class

   :param str classname: classname

   :return: list


> sample code to show getConstants

### environment()

   A map of various useful environment details

   :return: environment map object includes id, display, offset, TZ, SDK, download, appcache, availblocks, blocksize, blockcount, sdcard


> sample code to show environment

### log(message)

   Writes message to logcat

   :param str message: message


> sample code to show log


## 0108 SendEmail

### sendEmail(to, subject, body, attachmentUri)

   Launches an activity that sends an e-mail message to a given recipient

   :param str to: A comma separated list of recipients
   :param str subject: subject
   :param str body: mail body
   :param str attachmentUri(Optional): message


> sample code to show sendEmail


## 0109 Toast, getInput, getPassword, notify APIs

### makeToast(message)

   Displays a short-duration Toast notification

   :param str message: message


> sample code to show makeToast

### getInput(title, message)

   Queries the user for a text input

   :param str title: title of the input box
   :param str message: message to display above the input box


> sample code to show getInput

### getPassword(title, message)

   Queries the user for a password

   :param str title: title of the input box
   :param str message: message to display above the input box


> sample code to show getPassword

### notify(title, message, url)

   Displays a notification that will be canceled when the user clicks on it

   :param str title: title
   :param str message: message
   :param str url(optional): url

> Sample code of notify

```python
    import androidhelper
    droid = androidhelper.Android()
    droid.notify('Hello','QPython','http://qpython.org') 
    #You could set the 3rd parameter None also

```



# 02 ApplicationManagerFacade


## 0201 Manager APIs


### getLaunchableApplications()

   Returns a list of all launchable application class names

   :return: map object


> sample code to show getLaunchableApplications


### launch(classname)

   Start activity with the given class name

   :param str classname: classname


> sample code to show launch

### getRunningPackages()

   Returns a list of packages running activities or services

   :return: List of packages running activities


> sample code to show getRunningPackages

### forceStopPackage(packageName)

   Force stops a package

   :param str packageName: packageName


> sample code to show forceStopPackage


# 03 CameraFacade


## 0301 Camera APIs

### cameraCapturePicture(targetPath)

   Take a picture and save it to the specified path

   :return: A map of Booleans autoFocus and takePicture where True indicates success

### cameraInteractiveCapturePicture(targetPath)

   Starts the image capture application to take a picture and saves it to the specified path

# 04 CommonIntentsFacade

## 0401 Barcode APIs

### scanBarcode()

   Starts the barcode scanner

   :return: A Map representation of the result Intent

## 0402 View APIs

### pick(uri)

   Display content to be picked by URI (e.g. contacts)

   :return: A map of result values

### view(uri, type, extras)

   Start activity with view action by URI (i.e. browser, contacts, etc.)

### viewMap(query)

   Opens a map search for query (e.g. pizza, 123 My Street)

### viewContacts()

   Opens the list of contacts

### viewHtml(path)

   Opens the browser to display a local HTML file

### search(query)

   Starts a search for the given query

# 05 ContactsFacade

## 0501 Contacts APIs

### pickContact()

   Displays a list of contacts to pick from

   :return: A map of result values

### pickPhone()

   Displays a list of phone numbers to pick from

   :return: The selected phone number

### contactsGetAttributes()

   Returns a List of all possible attributes for contacts

   :return: a List of contacts as Maps

### contactsGetIds()

   Returns a List of all contact IDs

### contactsGet(attributes)

   Returns a List of all contacts

### contactsGetById(id)

   Returns contacts by ID

### contactsGetCount()

   Returns the number of contacts

### queryContent(uri, attributes, selection, selectionArgs, order)

   Content Resolver Query

   :return: result of query as Maps

### queryAttributes(uri)

   Content Resolver Query Attributes

   :return: a list of available columns for a given content uri

# 06 EventFacade


## 0601 Event APIs

### eventClearBuffer()

   Clears all events from the event buffer

### eventRegisterForBroadcast(category, enqueue)

   Registers a listener for a new broadcast signal

### eventUnregisterForBroadcast(category)

   Stop listening for a broadcast signal

### eventGetBrodcastCategories()

   Lists all the broadcast signals we are listening for

### eventPoll(number_of_events)

   Returns and removes the oldest n events (i.e. location or sensor update, etc.) from the event buffer

   :return: A List of Maps of event properties

### eventWaitFor(eventName, timeout)

   Blocks until an event with the supplied name occurs. The returned event is not removed from the buffer

   :return: Map of event properties

### eventWait(timeout)

   Blocks until an event occurs. The returned event is removed from the buffer

   :return: Map of event properties

### eventPost(name, data, enqueue)

   Post an event to the event queue

### rpcPostEvent(name, data)

   Post an event to the event queue

### receiveEvent()

   Returns and removes the oldest event (i.e. location or sensor update, etc.) from the event buffer

   :return: Map of event properties

### waitForEvent(eventName, timeout)

   Blocks until an event with the supplied name occurs. The returned event is not removed from the buffer

   :return: Map of event properties

### startEventDispatcher(port)

   Opens up a socket where you can read for events posted

### stopEventDispatcher()

   Stops the event server, you can't read in the port anymore

# 07 LocationFacade


## 0701 Providers APIs

### locationProviders()

   Returns availables providers on the phone

### locationProviderEnabled(provider)

   Ask if provider is enabled

## 0702 Location APIs

### startLocating(minDistance, minUpdateDistance)

   Starts collecting location data

### readLocation()

   Returns the current location as indicated by all available providers

   :return: A map of location information by provider

### stopLocating()

   Stops collecting location data

getLastKnownLocation()

   Returns the last known location of the device

   :return: A map of location information by provider


```python

    Droid = androidhelper.Android()
    location = Droid.getLastKnownLocation().result
    location = location.get('network', location.get('gps'))
```


## 0703 GEO

### geocode(latitude, longitude, maxResults)

   Returns a list of addresses for the given latitude and longitude

   :return: A list of addresses

# 08 PhoneFacade

## 0801 PhoneStat APIs


### startTrackingPhoneState()

   Starts tracking phone state

### readPhoneState()

   Returns the current phone state and incoming number

   :return: A Map of "state" and "incomingNumber"

### stopTrackingPhoneState()

   Stops tracking phone state


## 0802 Call & Dia APIs

### phoneCall(uri)

   Calls a contact/phone number by URI

### phoneCallNumber(number)

   Calls a phone number

### phoneDial(uri)

   Dials a contact/phone number by URI

### phoneDialNumber(number)

   Dials a phone number

## 0803 Get information APIs

### getCellLocation()

   Returns the current cell location

### getNetworkOperator()

   Returns the numeric name (MCC+MNC) of current registered operator

### getNetworkOperatorName()

   Returns the alphabetic name of current registered operator

### getNetworkType()

   Returns a the radio technology (network type) currently in use on the device

### getPhoneType()

   Returns the device phone type

### getSimCountryIso()

   Returns the ISO country code equivalent for the SIM provider's country code

### getSimOperator()

   Returns the MCC+MNC (mobile country code + mobile network code) of the provider of the SIM. 5 or 6 decimal digits

### getSimOperatorName()

   Returns the Service Provider Name (SPN)

### getSimSerialNumber()

   Returns the serial number of the SIM, if applicable. Return null if it is unavailable

### getSimState()

   Returns the state of the device SIM card

### getSubscriberId()

   Returns the unique subscriber ID, for example, the IMSI for a GSM phone. Return null if it is unavailable

### getVoiceMailAlphaTag()

   Retrieves the alphabetic identifier associated with the voice mail number

### getVoiceMailNumber()

   Returns the voice mail number. Return null if it is unavailable

### checkNetworkRoaming()

   Returns true if the device is considered roaming on the current network, for GSM purposes

### getDeviceId()

   Returns the unique device ID, for example, the IMEI for GSM and the MEID for CDMA phones. Return null if device ID is not available

### getDeviceSoftwareVersion()

   Returns the software version number for the device, for example, the IMEI/SV for GSM phones. Return null if the software version is not available

### getLine1Number()

   Returns the phone number string for line 1, for example, the MSISDN for a GSM phone. Return null if it is unavailable

### getNeighboringCellInfo()

   Returns the neighboring cell information of the device

# 09 MediaRecorderFacade

## 0901 Audio

### recorderStartMicrophone(targetPath)

   Records audio from the microphone and saves it to the given location

## 0902 Video APIs

### recorderStartVideo(targetPath, duration, videoSize)

   Records video from the camera and saves it to the given location.
   Duration specifies the maximum duration of the recording session.
   If duration is 0 this method will return and the recording will only be stopped
   when recorderStop is called or when a scripts exits.
   Otherwise it will block for the time period equal to the duration argument.
   videoSize: 0=160x120, 1=320x240, 2=352x288, 3=640x480, 4=800x480.


### recorderCaptureVideo(targetPath, duration, recordAudio)

   Records video (and optionally audio) from the camera and saves it to the given location.
   Duration specifies the maximum duration of the recording session.
   If duration is not provided this method will return immediately and the recording will only be stopped
   when recorderStop is called or when a scripts exits.
   Otherwise it will block for the time period equal to the duration argument.

### startInteractiveVideoRecording(path)

   Starts the video capture application to record a video and saves it to the specified path


## 0903 Stop

### recorderStop()

   Stops a previously started recording

# 10 SensorManagerFacade

## 1001 Start & Stop

### startSensingTimed(sensorNumber, delayTime)

   Starts recording sensor data to be available for polling

### startSensingThreshold(ensorNumber, threshold, axis)

   Records to the Event Queue sensor data exceeding a chosen threshold

### startSensing(sampleSize)

   Starts recording sensor data to be available for polling

### stopSensing()

   Stops collecting sensor data

## 1002 Read data APIs

### readSensors()

   Returns the most recently recorded sensor data

### sensorsGetAccuracy()

   Returns the most recently received accuracy value

### sensorsGetLight()

   Returns the most recently received light value

### sensorsReadAccelerometer()

   Returns the most recently received accelerometer values

   :return: a List of Floats [(acceleration on the) X axis, Y axis, Z axis]

### sensorsReadMagnetometer()

   Returns the most recently received magnetic field values

   :return: a List of Floats [(magnetic field value for) X axis, Y axis, Z axis]

sensorsReadOrientation()

   Returns the most recently received orientation values

   :return: a List of Doubles [azimuth, pitch, roll]

```python

    Droid = androidhelper.Android()
    Droid.startSensingTimed(1, 250)
    sensor = Droid.sensorsReadOrientation().result
    Droid.stopSensing()
```


# 11 SettingsFacade

## 1101 Screen

### setScreenTimeout(value)

   Sets the screen timeout to this number of seconds

   :return: The original screen timeout

### getScreenTimeout()

   Gets the screen timeout

   :return: the current screen timeout in seconds

## 1102 AirplanerMode


### checkAirplaneMode()

   Checks the airplane mode setting

   :return: True if airplane mode is enabled

### toggleAirplaneMode(enabled)

   Toggles airplane mode on and off

   :return: True if airplane mode is enabled

## 1103 Ringer Silent Mode

### checkRingerSilentMode()

   Checks the ringer silent mode setting

   :return: True if ringer silent mode is enabled

### toggleRingerSilentMode(enabled)

   Toggles ringer silent mode on and off

   :return: True if ringer silent mode is enabled

## 1104 Vibrate Mode

### toggleVibrateMode(enabled)

   Toggles vibrate mode on and off. If ringer=true then set Ringer setting, else set Notification setting

   :return: True if vibrate mode is enabled

### getVibrateMode(ringer)

   Checks Vibration setting. If ringer=true then query Ringer setting, else query Notification setting

   :return: True if vibrate mode is enabled

## 1105 Ringer & Media Volume

### getMaxRingerVolume()

   Returns the maximum ringer volume

### getRingerVolume()

   Returns the current ringer volume

### setRingerVolume(volume)

   Sets the ringer volume

### getMaxMediaVolume()

   Returns the maximum media volume

### getMediaVolume()

   Returns the current media volume

### setMediaVolume(volume)

   Sets the media volume

## 1105 Screen Brightness

### getScreenBrightness()

   Returns the screen backlight brightness

   :return: the current screen brightness between 0 and 255

### setScreenBrightness(value)

   Sets the the screen backlight brightness

   :return: the original screen brightness

### checkScreenOn()

   Checks if the screen is on or off (requires API level 7)

   :return: True if the screen is currently on


# 12 SmsFacade

## 1201 Sms API

### smsSend(destinationAddress, text)

   Sends an SMS

   :param str destinationAddress: typically a phone number
   :param str text:

### smsGetMessageCount(unreadOnly, folder)

   Returns the number of messages

   :param bool unreadOnly: typically a phone number
   :param str folder(optional): default "inbox"

### smsGetMessageIds(unreadOnly, folder)

   Returns a List of all message IDs

   :param bool unreadOnly: typically a phone number
   :param str folder(optional): default "inbox"

### smsGetMessages(unreadOnly, folder, attributes)

   Returns a List of all messages

   :param bool unreadOnly: typically a phone number
   :param str folder: default "inbox"
   :param list attributes(optional): attributes

   :return: a List of messages as Maps

### smsGetMessageById(id, attributes)

   Returns message attributes

   :param int id: message ID
   :param list attributes(optional): attributes

   :return: a List of messages as Maps

### smsGetAttributes()

   Returns a List of all possible message attributes

### smsDeleteMessage(id)

   Deletes a message

   :param int id: message ID

   :return: True if the message was deleted

### smsMarkMessageRead(ids, read)

   Marks messages as read

   :param list ids: List of message IDs to mark as read
   :param bool read:  true or false

   :return: number of messages marked read

# 13 SpeechRecognitionFacade

## 1301 Speech API

### recognizeSpeech(prompt, language, languageModel)

   Recognizes user's speech and returns the most likely result

   :param str prompt(optional): text prompt to show to the user when asking them to speak
   :param str language(optional): language override to inform the recognizer that it should expect speech in a language different than the one set in the java.util.Locale.getDefault()
   :param str languageModel(optional): informs the recognizer which speech model to prefer (see android.speech.RecognizeIntent)

   :return: An empty string in case the speech cannot be recongnized


# 14 ToneGeneratorFacade

## 1401 Tones API

### generateDtmfTones(phoneNumber, toneDuration)

   Generate DTMF tones for the given phone number

   :param str phoneNumber: phone number
   :param int toneDuration(optional): default 100, duration of each tone in milliseconds


# 15 WakeLockFacade

## 1501 Wake API

### wakeLockAcquireFull()

   Acquires a full wake lock (CPU on, screen bright, keyboard bright)

### wakeLockAcquirePartial()

   Acquires a partial wake lock (CPU on)

### wakeLockAcquireBright()

   Acquires a bright wake lock (CPU on, screen bright)

### wakeLockAcquireDim()

   Acquires a dim wake lock (CPU on, screen dim)

### wakeLockRelease()

   Releases the wake lock

# 16 WifiFacade

## 1601 Wifi APIs

### wifiGetScanResults()

   Returns the list of access points found during the most recent Wifi scan

### wifiLockAcquireFull()

   Acquires a full Wifi lock

### wifiLockAcquireScanOnly()

   Acquires a scan only Wifi lock

### wifiLockRelease()

   Releases a previously acquired Wifi lock

### wifiStartScan()

   Starts a scan for Wifi access points

   :return: True if the scan was initiated successfully

### checkWifiState()

   Checks Wifi state

   :return: True if Wifi is enabled

### toggleWifiState(enabled)

   Toggle Wifi on and off

   :param bool enabled(optional): enabled

   :return: True if Wifi is enabled

### wifiDisconnect()

   Disconnects from the currently active access point

   :return: True if the operation succeeded

### wifiGetConnectionInfo()

   Returns information about the currently active access point

### wifiReassociate()

   Returns information about the currently active access point

   :return: True if the operation succeeded

### wifiReconnect()

   Reconnects to the currently active access point

   :return: True if the operation succeeded


# 18 BatteryManagerFacade

## 1801 Battery APIs

### readBatteryData()

   Returns the most recently recorded battery data

### batteryStartMonitoring()

   Starts tracking battery state

### batteryStopMonitoring()

   Stops tracking battery state

### batteryGetStatus()

   Returns  the most recently received battery status data:
   1 - unknown;
   2 - charging;
   3 - discharging;
   4 - not charging;
   5 - full

### batteryGetHealth()

   Returns the most recently received battery health data:
   1 - unknown;
   2 - good;
   3 - overheat;
   4 - dead;
   5 - over voltage;
   6 - unspecified failure

### batteryGetPlugType()

   Returns the most recently received plug type data:
   -1 - unknown
   0 - unplugged
   1 - power source is an AC charger
   2 - power source is a USB port


### batteryCheckPresent()

   Returns the most recently received battery presence data

### batteryGetLevel()

   Returns the most recently received battery level (percentage)

### batteryGetVoltage()

   Returns the most recently received battery voltage

### batteryGetTemperature()

   Returns the most recently received battery temperature

### batteryGetTechnology()

   Returns the most recently received battery technology data


# 19 ActivityResultFacade


## 1901 Activity APIs

### setResultBoolean(resultCode, resultValue)

   Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(),
   the resulting intent will contain SCRIPT_RESULT extra with the given value

   :param int resultCode:
   :param byte resultValue:


### setResultByte(resultCode, resultValue)

   Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(),
   the resulting intent will contain SCRIPT_RESULT extra with the given value

   :param int resultCode:
   :param byte resultValue:

### setResultShort(resultCode, resultValue)

   Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(),
   the resulting intent will contain SCRIPT_RESULT extra with the given value

   :param int resultCode:
   :param byte resultValue:

### setResultChar(resultCode, resultValue)

   Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(),
   the resulting intent will contain SCRIPT_RESULT extra with the given value

   :param int resultCode:
   :param byte resultValue:


### setResultInteger(resultCode, resultValue)

   Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(),
   the resulting intent will contain SCRIPT_RESULT extra with the given value

   :param int resultCode:
   :param byte resultValue:

### setResultLong(resultCode, resultValue)

   Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(),
   the resulting intent will contain SCRIPT_RESULT extra with the given value

   :param int resultCode:
   :param byte resultValue:

### setResultFloat(resultCode, resultValue)

   Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(),
   the resulting intent will contain SCRIPT_RESULT extra with the given value

   :param int resultCode:
   :param byte resultValue:

### setResultDouble(resultCode, resultValue)

   Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(),
   the resulting intent will contain SCRIPT_RESULT extra with the given value

   :param int resultCode:
   :param byte resultValue:

### setResultString(resultCode, resultValue)

   Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(),
   the resulting intent will contain SCRIPT_RESULT extra with the given value

   :param int resultCode:
   :param byte resultValue:

### setResultBooleanArray(resultCode, resultValue)

   Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(),
   the resulting intent will contain SCRIPT_RESULT extra with the given value

   :param int resultCode:
   :param byte resultValue:

### setResultByteArray(resultCode, resultValue)

   Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(),
   the resulting intent will contain SCRIPT_RESULT extra with the given value

   :param int resultCode:
   :param byte resultValue:

### setResultShortArray(resultCode, resultValue)

   Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(),
   the resulting intent will contain SCRIPT_RESULT extra with the given value

   :param int resultCode:
   :param byte resultValue:

### setResultCharArray(resultCode, resultValue)

   Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(),
   the resulting intent will contain SCRIPT_RESULT extra with the given value

   :param int resultCode:
   :param byte resultValue:

### setResultIntegerArray(resultCode, resultValue)

   Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(),
   the resulting intent will contain SCRIPT_RESULT extra with the given value

   :param int resultCode:
   :param byte resultValue:

### setResultLongArray(resultCode, resultValue)

   Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(),
   the resulting intent will contain SCRIPT_RESULT extra with the given value

   :param int resultCode:
   :param byte resultValue:

### setResultFloatArray(resultCode, resultValue)

   Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(),
   the resulting intent will contain SCRIPT_RESULT extra with the given value

   :param int resultCode:
   :param byte resultValue:

### setResultDoubleArray(resultCode, resultValue)

   Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(),
   the resulting intent will contain SCRIPT_RESULT extra with the given value

   :param int resultCode:
   :param byte resultValue:

### setResultStringArray(resultCode, resultValue)

   Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(),
   the resulting intent will contain SCRIPT_RESULT extra with the given value

   :param int resultCode:
   :param byte resultValue:

### setResultSerializable(resultCode, resultValue)

   Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(),
   the resulting intent will contain SCRIPT_RESULT extra with the given value

   :param int resultCode:
   :param byte resultValue:


# 20 MediaPlayerFacade


## 2001 Control

### mediaPlay(url, tag, play)

   Open a media file

   :param str url: url of media resource
   :param str tag(optional): string identifying resource (default=default)
   :param bool play(optional): start playing immediately

   :return: true if play successful

### mediaPlayPause(tag)

   pause playing media file

   :param str tag: string identifying resource (default=default)

   :return: true if successful

### mediaPlayStart(tag)

   start playing media file

   :param str tag: string identifying resource (default=default)

   :return: true if successful

### mediaPlayClose(tag)

   Close media file

   :param str tag: string identifying resource (default=default)

   :return: true if successful

### mediaIsPlaying(tag)

   Checks if media file is playing

   :param str tag: string identifying resource (default=default)

   :return: true if successful


### mediaPlaySetLooping(enabled, tag)

   Set Looping

   :param bool enabled: default true
   :param str tag: string identifying resource (default=default)

   :return: True if successful

### mediaPlaySeek(msec, tag)

   Seek To Position

   :param int msec: default true
   :param str tag: string identifying resource (default=default)

   :return: New Position (in ms)

## 2002 Get Information

### mediaPlayInfo(tag)

   Information on current media

   :param str tag: string identifying resource (default=default)

   :return: Media Information

### mediaPlayList()

   Lists currently loaded media

   :return: List of Media Tags


# 21 PreferencesFacade

## Preferences APIs

### prefGetValue(key, filename)

   Read a value from shared preferences

   :param str key: key
   :param str filename(optional): Desired preferences file. If not defined, uses the default Shared Preferences.


### prefPutValue(key, value, filename)

   Write a value to shared preferences

   :param str key: key
   :param str value: value
   :param str filename(optional): Desired preferences file. If not defined, uses the default Shared Preferences.

### prefGetAll(filename)

   Get list of Shared Preference Values

   :param str filename(optional): Desired preferences file. If not defined, uses the default Shared Preferences.


# 22 QPyInterfaceFacade

## 2201 QPyInterface APIs

### executeQPy(script)

   Execute a qpython script by absolute path

   :param str script: The absolute path of the qpython script

   :return: bool


# 23 TextToSpeechFacade

## 2301 TTS APIs

### ttsSpeak(message)

   Speaks the provided message via TTS

   :param str message: message

### ttsIsSpeaking()

   Returns True if speech is currently in progress


### ttsSpeak(message)

   Speaks the provided message via TTS

   :param str message: message


# 24 EyesFreeFacade

## 2401 EyesFree APIs


# 25 BluetoothFacade

## 2501 Bluetooth APIs

### bluetoothActiveConnections()

   Returns active Bluetooth connections


### bluetoothWriteBinary(base64, connID)

   Send bytes over the currently open Bluetooth connection

   :param str base64: A base64 encoded String of the bytes to be sent
   :param str connID(optional): Connection id

### bluetoothReadBinary(bufferSize, connID)

   Read up to bufferSize bytes and return a chunked, base64 encoded string

   :param int bufferSize: default 4096
   :param str connID(optional): Connection id

### bluetoothConnect(uuid, address)

   Connect to a device over Bluetooth. Blocks until the connection is established or fails

   :param str uuid: The UUID passed here must match the UUID used by the server device
   :param str address(optional): The user will be presented with a list of discovered devices to choose from if an address is not provided

   :return: True if the connection was established successfully

### bluetoothAccept(uuid, timeout)

   Listens for and accepts a Bluetooth connection. Blocks until the connection is established or fails

   :param str uuid: The UUID passed here must match the UUID used by the server device
   :param int timeout: How long to wait for a new connection, 0 is wait for ever (default=0)

### bluetoothMakeDiscoverable(duration)

   Requests that the device be discoverable for Bluetooth connections

   :param int duration: period of time, in seconds, during which the device should be discoverable (default=300)

### bluetoothWrite(ascii, connID)

   Sends ASCII characters over the currently open Bluetooth connection

   :param str ascii: text
   :param str connID: Connection id

### bluetoothReadReady(connID)

   Sends ASCII characters over the currently open Bluetooth connection

   :param str ascii: text
   :param str connID: Connection id

### bluetoothRead(bufferSize, connID)

   Read up to bufferSize ASCII characters

   :param int bufferSize: default=4096
   :param str connID(optional): Connection id

### bluetoothReadLine(connID)

   Read the next line

   :param str connID(optional): Connection id

### bluetoothGetRemoteDeviceName(address)

   Queries a remote device for it's name or null if it can't be resolved

   :param str address: Bluetooth Address For Target Device

### bluetoothGetLocalName()

   Gets the Bluetooth Visible device name

### bluetoothSetLocalName(name)

   Sets the Bluetooth Visible device name, returns True on success

   :param str name: New local name

### bluetoothGetScanMode()

   Gets the scan mode for the local dongle.
   Return values:
   -1 when Bluetooth is disabled.
   0 if non discoverable and non connectable.
   1 connectable non discoverable.
   3 connectable and discoverable.

### bluetoothGetConnectedDeviceName(connID)

   Returns the name of the connected device

   :param str connID: Connection id

### checkBluetoothState()

   Checks Bluetooth state

   :return: True if Bluetooth is enabled

### toggleBluetoothState(enabled, prompt)

   Toggle Bluetooth on and off

   :param bool enabled:
   :param str prompt: Prompt the user to confirm changing the Bluetooth state, default=true

   :return: True if Bluetooth is enabled

### bluetoothStop(connID)

   Stops Bluetooth connection

   :param str connID: Connection id

### bluetoothGetLocalAddress()

   Returns the hardware address of the local Bluetooth adapter

### bluetoothDiscoveryStart()

   Start the remote device discovery process

   :return: true on success, false on error

### bluetoothDiscoveryCancel()

   Cancel the current device discovery process

   :return: true on success, false on error

### bluetoothIsDiscovering()

   Return true if the local Bluetooth adapter is currently in the device discovery process


# 26 SignalStrengthFacade

## 2601 SignalStreagth APIs

### startTrackingSignalStrengths()

   Starts tracking signal strengths

### readSignalStrengths()

   Returns the current signal strengths

   :return: A map of gsm_signal_strength

### stopTrackingSignalStrengths()

   Stops tracking signal strength


# 27 WebCamFacade


## 2701 WebCam APIs

### webcamStart(resolutionLevel, jpegQuality, port)

   Starts an MJPEG stream and returns a Tuple of address and port for the stream

   :param int resolutionLevel: increasing this number provides higher resolution (default=0)
   :param int jpegQuality: a number from 0-10 (default=20)
   :param int port: If port is specified, the webcam service will bind to port, otherwise it will pick any available port (default=0)

### webcamAdjustQuality(resolutionLevel, jpegQuality)

   Adjusts the quality of the webcam stream while it is running

   :param int resolutionLevel: increasing this number provides higher resolution (default=0)
   :param int jpegQuality: a number from 0-10 (default=20)

### cameraStartPreview(resolutionLevel, jpegQuality, filepath)

   Start Preview Mode. Throws 'preview' events

   :param int resolutionLevel: increasing this number provides higher resolution (default=0)
   :param int jpegQuality: a number from 0-10 (default=20)
   :param str filepath: Path to store jpeg files

   :return: True if successful

### cameraStopPreview()

   Stop the preview mode


# 28 UiFacade

## 2801 Dialog

### dialogCreateInput(title, message, defaultText, inputType)

   Create a text input dialog

   :param str title: title of the input box
   :param str message: message to display above the input box
   :param str defaultText(optional): text to insert into the input box
   :param str inputType(optional): type of input data, ie number or text

### dialogCreatePassword(title, message)

   Create a password input dialog

   :param str title: title of the input box
   :param str message: message to display above the input box

### dialogGetInput(title, message, defaultText)

   Create a password input dialog

   :param str title: title of the input box
   :param str message: message to display above the input box
   :param str defaultText(optional): text to insert into the input box

### dialogGetPassword(title, message)

   Queries the user for a password

   :param str title: title of the password box
   :param str message: message to display above the input box

### dialogCreateSeekBar(start, maximum, title)

   Create seek bar dialog

   :param int start: default=50
   :param int maximum: default=100
   :param int title: title

### dialogCreateTimePicker(hour, minute, is24hour)

   Create time picker dialog

   :param int hour: default=0
   :param int miute: default=0
   :param bool is24hour: default=false

### dialogCreateDatePicker(year, month, day)

   Create date picker dialog

   :param int year: default=1970
   :param int month: default=1
   :param int day: default=1


## 2802 NFC

**Data structs**
*QPython NFC json result*
::

    {
    "role": <role>, # could be self/master/slave
    "stat": <stat>, # could be ok / fail / cancl
    "message": <message get> 
    }

### dialogCreateNFCBeamMaster(title, message, inputType)

   Create a dialog where you could create a qpython beam master

   :param str title: title of the input box
   :param str message: message to display above the input box
   :param str inputType(optional): type of input data, ie number or text

### NFCBeamMessage(content, title, message)

   Create a dialog where you could create a qpython beam master

   :param str content: message you want to sent
   :param str title: title of the input box
   :param str message: message to display above the input box
   :param str inputType(optional): type of input data, ie number or text

### dialogCreateNFCBeamSlave(title, message)

   Create a qpython beam slave

   :param str title: title of the input box
   :param str message: message to display above the input box

## 2803 Progress

### dialogCreateSpinnerProgress(message, maximumProgress)

   Create a spinner progress dialog

   :param str message(optional): message
   :param int maximunProgress(optional): dfault=100

### dialogSetCurrentProgress(current)

   Set progress dialog current value

   :param int current: current

### dialogSetMaxProgress(max)

   Set progress dialog maximum value

   :param int max: max


### dialogCreateHorizontalProgress(title, message, maximumProgress)

   Create a horizontal progress dialog

   :param str title(optional): title
   :param str message(optional): message
   :param int maximunProgress(optional): dfault=100


## 2804 Alert

### dialogCreateAlert(title, message)

   Create alert dialog

   :param str title(optional): title
   :param str message(optional): message
   :param int maximunProgress(optional): dfault=100


## 2805 Dialog Control

### dialogSetPositiveButtonText(text)

   Set alert dialog positive button text

   :param str text: text

### dialogSetNegativeButtonText(text)

   Set alert dialog negative button text

   :param str text: text

### dialogSetNeutralButtonText(text)

   Set alert dialog button text

   :param str text: text

### dialogSetItems(items)

   Set alert dialog list items

   :param list items: items

### dialogSetSingleChoiceItems(items, selected)

   Set alert dialog list items

   :param list items: items
   :param int selected: selected item index (default=0)

### dialogSetMultiChoiceItems(items, selected)

   Set dialog multiple choice items and selection

   :param list items: items
   :param int selected: selected item index (default=0)

### addContextMenuItem(label, event, eventData)

   Adds a new item to context menu

   :param str label: label for this menu item
   :param str event: event that will be generated on menu item click
   :param object eventData: event object

### addOptionsMenuItem(label, event, eventData, iconName)

   Adds a new item to context menu

   :param str label: label for this menu item
   :param str event: event that will be generated on menu item click
   :param object eventData: event object
   :param str iconName: Android system menu icon, see http://developer.android.com/reference/android/R.drawable.html

### dialogGetResponse()

   Returns dialog response

### dialogGetSelectedItems()

   This method provides list of items user selected

### dialogDismiss()

   Dismiss dialog

### dialogShow()

   Show dialog


## 2806 Layout

### fullShow(layout)

   Show Full Screen

   :param string layout: String containing View layout

### fullDismiss()

   Dismiss Full Screen

### fullQuery()

   Get Fullscreen Properties

### fullQueryDetail(id)

   Get fullscreen properties for a specific widget

   :param str id: id of layout widget

### fullSetProperty(id)

   Set fullscreen widget property

   :param str id: id of layout widget
   :param str property: name of property to set
   :param str value: value to set property to

### fullSetList(id, list)

   Attach a list to a fullscreen widget

   :param str id: id of layout widget
   :param list list: List to set

### fullKeyOverride(keycodes, enable)

   Override default key actions

   :param str keycodes: id of layout widget
   :param bool enable: List to set (default=true)



## 2807 WebView

### webViewShow()

   Display a WebView with the given URL

   :param str url: url
   :param bool wait(optional): block until the user exits the WebView

# 29 USB Host Serial Facade


SL4A Facade for USB Serial devices by Android USB Host API.

It control the USB-Serial like devices
from Andoroid which has USB Host Controller .

The sample
`demonstration is also available at youtube video <http://www.youtube.com/watch?v=EJ7qiGXaI74>`_


## Requirements

* Android device which has USB Host controller (and enabled in that firmware).
* Android 4.0 (API14) or later.
* USB Serial devices (see [Status](#Status)).
* USB Serial devices were not handled by Android kernel.

  > I heard some android phone handle USB Serial devices
  > make /dev/ttyUSB0 in kernel level.
  > In this case, Android does not be able to handle the device
  > from OS level.

  please check Android Applications be able to grab the target USB Devices,
  such as `USB Device Info <https://play.google.com/store/apps/details?id=aws.apps.usbDeviceEnumerator>`_.

Status

* probably work with USB CDC, like FTDI, Arduino or else.

* 2012/09/10: work with 78K0F0730 device (new RL78) with Tragi BIOS board.

  `M78K0F0730 <http://www.marutsu.co.jp/shohin_55296/>`_

* 2012/09/24: work with some pl2303 devcies.

Author

This facade developped by `Kuri65536 <https://bitbucket.org/kuri65536/usbhostserialfacade>`_
you can see the commit log in it.


## 2901 USB Host Serial APIs

### usbserialGetDeviceList()

   Returns USB devices reported by USB Host API.

   :return: Returns "Map of id and string information Map<String, String>


### usbserialDisconnect(connID)

   Disconnect all USB-device

   :param str connID: connection ID

### usbserialActiveConnections()

   Returns active USB-device connections.

   :return: Returns "Active USB-device connections by Map UUID vs device-name."


### usbserialWriteBinary(base64, connID)

   Send bytes over the currently open USB Serial connection.

   :param str base64:
   :param str connId:

### usbserialReadBinary(bufferSize, connID)

   Read up to bufferSize bytes and return a chunked, base64 encoded string

   :param int bufferSize:
   :param str connId:

### usbserialConnect(hash, options)

   Connect to a device with USB-Host. request the connection and exit

   :param str hash:
   :param str options:

   :return: Returns messages the request status

### usbserialHostEnable()

   Requests that the host be enable for USB Serial connections.

   :return: True if the USB Device is accesible

### usbserialWrite(String ascii, String connID)

   Sends ASCII characters over the currently open USB Serial connection

   :param str ascii:
   :param str connID:

### usbserialReadReady(connID)

   :param str connID:

   :return: True if the next read is guaranteed not to block


### usbserialRead(connID, bufferSize)

   Read up to bufferSize ASCII characters.

   :param str connID:
   :param int bufferSize:

### usbserialGetDeviceName(connID)

   Queries a remote device for it's name or null if it can't be resolved

   :param str connID:
