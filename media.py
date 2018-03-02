import webbrowser

class Movie () :

  def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

  def __init__(self,movie_title,story,image,youtube):
     self.title=movie_title
     self.storyline=story
     self.poster_image_url=image
     self.trailer_youtube_url=youtube

