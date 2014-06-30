from video import Video
from customer import Customer
from videoRental import Store
from videoRental import Kiosk


def PrintVideos(video_rental):
	print video_rental.description
	print video_rental.location
	print "All videos:"
	for a_video in video_rental.all_videos():
		print "   %s" % (a_video.title)

	print "Rented videos:"
	for a_video in video_rental.rented_videos():
		print "   %s" % (a_video.title)

	print "Rentable videos:"
	for a_video in video_rental.rentable_videos():
		print "   %s" % (a_video.title)

def main():
	store1 = Store("111 KLeonard Way")
	addedVideoID1 = store1.add_video(Video("Braveheart"))
	addedVideoID2 = store1.add_video(Video("Gladiator"))
	store1.add_video(Video("300"))
	store1.add_video(Video("Spaceballs"))
	store1.add_video(Video("Frozen"))
	store1.add_video(Video("The Lion King"))
	store1.add_video(Video("The Lion King"))
	store1.add_video(Video("The Lion King"))
	
	store1.add_customer(Customer("Clark", "Phillips", "9792295854", "01181985", "clark.r.phillips@gmail.com"))
	store1.add_customer(Customer("Bandit", "Phillips", "5121112222", "01191985", "bandit@gmail.com"))
	store1.add_customer(Customer("Nugget", "Phillips", "5121113333", "01201985", "nugget@gmail.com"))

	store1.customers["9792295854"].rent_video(addedVideoID1)
	store1.customers["9792295854"].rent_video(addedVideoID2)

	PrintVideos(store1)

	store1.customers["9792295854"].return_video(addedVideoID1)
	PrintVideos(store1)

	'''store2 = Store("222 TDuncan Lane")
	store2.add_video(Video("Born on the 4th of July", "R"))
	store2.add_video(Video("Juno", "PG13"))
	store2.add_video(Video("22 Jump Street", "R"))
	store2.add_video(Video("Forrest Gump", "PG13"))
	store2.add_video(Video("Top Gun", "G"))
	store2.add_video(Video("Cinderalla Story", "PG13"))
	store2.add_video(Video("Saving Private Ryan", "R"))
	store2.add_video(Video("Captain Phillips", "PG13"))
	store2.add_video(Video("Big", "PG13"))
	PrintVideos(store2)

	kiosk1 = Kiosk("333 Marco Blvd")
	kiosk1.add_video(Video("Kill Bill", "R"))
	kiosk1.add_video(Video("The Avengers", "PG13"))
	kiosk1.add_video(Video("Jack Reacher", "R"))
	kiosk1.add_video(Video("Skyfall", "PG13"))
	kiosk1.add_video(Video("GI Joe", "PG13"))
	PrintVideos(kiosk1)'''

if __name__ == "__main__":
	main()