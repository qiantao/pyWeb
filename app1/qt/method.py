from django.http import HttpResponse

class cat(object):
    def __init__(self,age,color):
        self.age = age
        self.color = color
    def speak(self):
        return str(self.color)+"的猫: 我"+str(self.age)+"岁了"


def qt(cat):
    content = cat.speak();
    return HttpResponse(content)
