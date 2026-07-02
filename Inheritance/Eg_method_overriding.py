# Concept: Method Overriding and super()
# Method overriding happens when a child class creates a method with the EXACT SAME NAME as a method in its parent class
#  to change its behavior. The super() function is used inside the child's method to call the parent's original version, 
# allowing you to add new features without rewriting the old code


class MediaPlayer:
    def __init__(self,media_title):
        self.media_title=media_title

    def play(self):
        print(f"Playing audio track for :{self.media_title}")

class VideoPlayer(MediaPlayer):
    def play(self):
        super().play()
        print(f"Rendereing video screen for {self.media_title}")

Video=VideoPlayer("Summer")
Video.play()