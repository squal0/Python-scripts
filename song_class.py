class Song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

strawberry_swing = Song(["We were talking into strawberry swing",
	"Every moment was so special, wouldn't wanna waste a thing",
	"Cold, cold water take me high"])

exist_song = Song(["How do they exist if we dont know who they are",
	"They could be you, they could be me, they could be Kings and Gods"])

strawberry_swing.sing_me_a_song()
exist_song.sing_me_a_song()