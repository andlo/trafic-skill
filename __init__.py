from mycroft import MycroftSkill, intent_file_handler


class Trafic(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('trafic.intent')
    def handle_trafic(self, message):
        self.speak_dialog('trafic')


def create_skill():
    return Trafic()

