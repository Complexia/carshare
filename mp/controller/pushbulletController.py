from pushbullet import Pushbullet

class PushbulletController:

    def __init__(self):
        self.__pb = Pushbullet('o.ZsHeeLnFuB0xUUWs6lqpshRWCYniVD6B')

    def notifyEngineer(self, title, note):
        self.__pb.push_note(title, note)

    def main(self):
        self.notifyEngineer()

    

if __name__ == '__main__':
    PushbulletController.notifyEngineer(PushbulletController())