# incoming_asteroid

Welcome!

I developed this Python script to request data from NASA's NeoWs API then parse the JSON data looking for potentially hazardous asteroids passing by Earth's vicinity within seven days. A message is composed containing a few attributes about each potentially hazardous asteroid. The message is then sent to a user's email. You may also send the message through SMTP to a cell phone (e.g. xxxxxxxxxx@txt.att.net) as a text message.

Setup:
Simply fill in the properties at the top of asteroid_alert.py, save, exit, then run: python asteroid_alert.py

If you wish to send more than 30 requests per hour or 50 requests per day, you will need to grab a NASA Developer API Key from https://api.nasa.gov/index.html. Otherwise, you may leave the api_key equal to "DEMO_KEY".
