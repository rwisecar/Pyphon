# Pyphon
[![Build Status](https://travis-ci.org/pyphonic/Pyphon.svg?branch=development)](https://travis-ci.org/pyphonic/Pyphon)
[![Coverage Status](https://coveralls.io/repos/github/pyphonic/Pyphon/badge.svg?branch=development)](https://coveralls.io/github/pyphonic/Pyphon?branch=development)



The Pyphon [pronounced py-phone] is a smartphone built on a Raspberry Pi and the Django Framework.

# Build Your Own
git clone the repo

pip install -r requirements

Set up a Twilio account

Set these environment variables:

## On a Raspberry Pi
Update/Upgrade/install pip

prepare ssh




Start using your phone!


# Website
[Pyphon](http://ec2-52-39-22-59.us-west-2.compute.amazonaws.com)

# Major Components
- Login
- Touch screen
- Voice
- Text messaging
- Address Book


# Tools used
Django, Django Rest framework, Postgres, JQuery, Twilio, Ngrok, AWS, Unittest, Travis CI, Coveralls

# Planned features
1) Email

2) Camera

3) Spotify

4) GPS navigation

# Current URL routes:
- /
- /login
- /logout
- /admin
- /api/texts/
- /api/calls/
- /api/contacts/list/
- /api/contact/retrieve/[number]
- /calls/dial/
- /calls/token/
- /calls/call/
- /calls/recent/
- /contacts/
- /contacts/[pk]
- /contacts/new/
- /contacts/[pk]/edit/
- /texts/
- /texts/new/
- /texts/hook/
- /texts/contact/[pk]/


# License
Apache2 License


# Create Your Own PyPhon

## First, gather your materials. 

1. Raspberry Pi3 (and case, if desired)

2. PiTFT Touch Screen

3. Mini USB Microphone

4. Lots of ice cream


## Next, get the app set up on your local device.

1. Clone it on your local machine.

```
git clone https://github.com/pyphonic/Pyphon.git
```

2. Set up a virtual environment on your local device.

3. Download all dependencies.

```
pip install -r requirements.pip
```

4. Set up ngrok so you can run the OS on your browser.
[Download ngrok](https://ngrok.com/download)

In a separate terminal, unzip ngrok:

```
unzip /path/to/ngrok.zip
```

Then run it on that terminal.

```
ngrok http 8000
```

Grab the second ngrok forwarding address, and save it. Twilio needs a public url in order to make successful phone calls and texts, and this is the address that you will use. Be careful here; if you exit out of the ngrok server, or close the terminal, your ngrok forwarding address will change, and you will need to change more configurations.

5. Set up your account on Twilio. Get a paid phone number.

6. Set up your Twilio configuration to use that ngrok instance you captured. 

On the phone numbers page in your console, make sure you're configured with Webhooks/TwiML.

Set the 'A Call Comes In' setting to use Webhooks, and forward to your base ngrok forwarding address. Use POST requests.

Set the 'Primary Handler Fails' setting to use Webhooks, and forward to your ngrok forwarding address with the following url route at the end: 

```
/calls/call
```
Make sure this setting uses GET requests.

7. Set up your TwiML application on the Twilio TwiML app page. Name your TwIML app, and go into the detail view. Configure the Voice request url to your base ngrok forwarding address + /calls/call, using the POST request setting. Open the optional settings, and configure the "Fallback URL" to the same url, using the GET request setting.

8. In a new terminal (*not* the one running ngrok), run your localhost on port 8000. Check that the OS works as desired.

## Now, get the OS loaded on to the PyPhon



# Team
[Ford Fowler](https://github.com/fordf)

[Avery Pratt](https://github.com/averypratt)

[Maelle Vance](https://github.com/ellezv)

[Julien Wilson](https://github.com/julienawilson)

[Rachael Wisecarver](https://github.com/rwisecar)

# Special Thanks
[Nicholas Hunt-Walker](https://github.com/nhuntwalker)

[David Smith](github.com/bl41r)

[Ben Garnaat](github.com/bgarnaat)

[Duncan Marsh](https://github.com/slugbyte)

[Judy Vue](https://github.com/JudyVue)

[Go Django tutorial on Ngrok](https://godjango.com/55-webhooks-django-and-ngrok/)

[Raspberry Pi kiosk mode tutorial by Dan Purdy](https://www.danpurdy.co.uk/web-development/raspberry-pi-kiosk-screen-tutorial/)

[Twilio tutorials](https://www.twilio.com/docs/tutorials?filter-language=node.js&filter-platform=server)

[On screen keyboard by Sam Deering](https://github.com/sdeering/onscreenkeyboard)

**Daily Ice Cream team meetings**
