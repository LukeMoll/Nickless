Nickless
===

## Introduction

Okay, this is a niche one. A bit of backstory, first.

[HackSoc] communicate via Slack and IRC, with the Freenode channel #hacksoc being linked to the #general channel on their Slack. This is an arrangement that mostly works well for IRC and Slack users alike, except for those who use both Slack and IRC. A message sent in Slack by `ldm`, and forwarded to IRC by hackbot might look something like this:

```
hackbot: <ldm> huh that's weird...
```

If by convenient chance `ldm` had a Freenode account by the same name, it would highlight them on IRC by the message that was just sent - by them! How mildly frustrating!

*Nickless* works by making sure that messages forwarded in the style shown above don't highlight the user if their nick is in the angled brackets - if `ldm` used Nickless, then the above message would look like the following on their IRC client:

```
hackbot: [me] huh that's weird...
```

## Requirements
Nickless is a Python module for [ZNC]. ZNC needs to be connected to the IRC channel you want to strip nicks from, and your client needs to be connected to ZNC. It is installed and loaded [as normal modules are][loadmod]. There are no configuration options, but if your nick changes then you may wish to reload the module for Nickless to follow this change. 

[HackSoc]: https://www.hacksoc.org/
[ZNC]: https://wiki.znc.in/ZNC
[loadmod]: https://wiki.znc.in/Modules#.28Un.29Loading_Modules