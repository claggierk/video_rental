from Video import Video
from Customer import Customer
from VideoRental import Store
from VideoRental import Kiosk

address1 = "111 KLeonard Way"
address2 = "222 TDuncan Lane"
address3 = "333 Marco Blvd"

first_name1 = "Jesse's"
last_name1 = "Girl"
first_name2 = "Johnny"
last_name2 = "B. Good"
phone_number1 = "000-555-1234"
phone_number2 = "111-222-3333"
phone_number3 = "111-222-4444"
dob = (1,18,1985)
email = "clark.r.phillips@gmail.com"

def main():
    """
    sample program demonstrating what this system can do
    adds 1 store
    adds 2 customers
    adds 8 videos
    the customers rent/return videos
    """
    store1 = Store(address1)
    store1.add_customer(Customer(first_name1, last_name1, phone_number1, dob, email))
    store1.add_customer(Customer(first_name2, last_name2, phone_number2, dob, email))
    video1 = store1.add_video(Video("300"))
    video2 = store1.add_video(Video("Spaceballs"))
    video3 = store1.add_video(Video("Frozen"))
    video4 = store1.add_video(Video("World War Z"))
    video5 = store1.add_video(Video("Sister Act"))
    video6 = store1.add_video(Video("The Mighty Ducks"))
    video7 = store1.add_video(Video("Invincible"))
    video8 = store1.add_video(Video("Dances With Wolves"))
    store1.rent_video(phone_number1, video3)
    store1.rent_video(phone_number1, video4)
    store1.rent_video(phone_number1, video5)
    store1.rent_video(phone_number2, video7)
    store1.rent_video(phone_number2, video8)
    print "Rented: ", store1.populate_videos(store1.rented_video_IDs())
    store1.rent_video(phone_number1, video8) # try to rent something that has already been rented
    store1.return_video(video4)
    store1.return_video(video1) # try to return something that has not been rented
    print "Rented: ", store1.populate_videos(store1.rented_video_IDs())
    print " ### Customer: %s is currently renting: %s" % (store1.customers[phone_number1], store1.populate_videos(store1.customers[phone_number1].rented_video_IDs))

if __name__ == "__main__":
    main()