# Privacy Policy — Bit-Bridget (personal OAuth client)

_Last updated: 2026-11-25_

This OAuth application ("the app") is a **personal, single-user client** used by one individual to let their own assistant read and manage their own Google account. It is not offered as a service to the public, has no sign-up, and has no users other than its owner.

## What the app accesses

Only after the account owner explicitly authorises it, the app may access:

- **Gmail** — to read and send email on the owner's behalf
- **Google Calendar** — to read and create calendar events
- **Google Drive** — to read files the owner chooses to open
- **Basic profile** — email address and display name, to identify the account

The app requests no access beyond these scopes.

## How data is handled

- Data is retrieved directly from Google APIs and used only to perform tasks the owner requests.
- Credentials (OAuth refresh tokens) are stored **locally on the owner's own machine**, in an encrypted local store, not on any third-party server.
- No data is sold, rented, or shared with advertisers or other third parties.
- No analytics, tracking, or profiling is performed.
- Data is not used to train machine-learning models.

## Retention and deletion

Local caches and tokens remain on the owner's machine until deleted. Access can be revoked at any time at <https://myaccount.google.com/permissions>, which immediately invalidates the stored token. Deleting the local credential store removes all remaining data.

## Contact

Questions or deletion requests: **bit.bridget.ai@gmail.com**

## Changes

Any change to this policy will be committed to this repository with a new date above.
