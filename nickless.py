"""
    Nickless
        by Luke Moll
        For use with an IRC bridging bot (like slack-irc) - will prevent you from getting highlighted
        by messages you sent from the bridged channel (ie Slack).

        Yes, I know it's a niche usecase.

"""
import re
import znc

class nickless(znc.Module):
    module_types = [znc.CModInfo.NetworkModule]
    description = "Strips nick from proxied messages"

    regex = None

    def OnLoad(self, sArgsi, sMessage): # let's hope this is the same as CModule::OnLoad
        nick = self.GetNetwork().GetIRCNick().GetNick()
        self.PutModule("Stripping nick from messages starting with <{}>".format(nick))
        self.regex = re.compile(r"^<.{,2}" + nick + r".{,2}>")
        return True

    def OnChanTextMessage(self, Message):
        if self.regex is not None:
            txt = re.sub(self.regex, "[me]", Message.GetText())
            Message.SetText(txt)
        else:
            self.PutModule("`self.regex` was not set -- was OnChanTextMessage called before OnLoad???")
        return znc.CONTINUE
