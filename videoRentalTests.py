from VideoRental import Store
from Video import Video
from Customer import Customer
import unittest

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

class videoRentalTests(unittest.TestCase):
    def testStoreCreation(self):
        """tests a Store creation"""
        store1 = Store(address1)
        self.assertEqual("Store", store1.description)
        self.assertEqual(address1, store1.location)

    def testAddRemoveCustomer(self):
        """tests the adding and removing of a customer"""
        store1 = Store(address1)
        store1.add_customer(Customer(first_name1, last_name2, phone_number1, dob, email))
        store1.add_customer(Customer(first_name1 + "2", last_name2 + "2", phone_number1, dob, email)) # duplicate customer (based on phone #)
        self.assertEqual(1, len(store1.customers))
        store1.add_customer(Customer(first_name1, last_name2, phone_number2, dob, email))
        self.assertEqual(2, len(store1.customers))
        store1.remove_customer(phone_number3)
        self.assertEqual(2, len(store1.customers))
        store1.remove_customer(phone_number2)
        self.assertEqual(1, len(store1.customers))

    def testAddRemoveVideoInventory(self):
        """tests the adding and removing of videos to and from inventory"""
        store1 = Store(address1)
        video1 = store1.add_video(Video("300"))
        video2 = store1.add_video(Video("Spaceballs"))
        video3 = store1.add_video(Video("Frozen"))
        video4 = store1.add_video(Video("Frozen"))
        self.assertEqual(4, len(store1.videos))
        store1.remove_video(video1)
        store1.remove_video(video3)
        store1.remove_video(video4)
        self.assertEqual(1, len(store1.videos))

    def testRentReturnVideos(self):
        """tests the adding and removing of a customer"""
        store1 = Store(address1)
        store1.add_customer(Customer(first_name1, last_name2, phone_number1, dob, email))
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
        self.assertEqual(3, len(store1.rented_video_IDs()))
        self.assertEqual(3, len(store1.customers[phone_number1].rented_video_IDs))
        store1.rent_video(phone_number2, video7)
        store1.rent_video(phone_number2, video8)
        self.assertEqual(5, len(store1.rented_video_IDs()))
        store1.rent_video(phone_number1, video8) # try to rent something that has already been rented
        self.assertEqual(5, len(store1.rented_video_IDs()))
        store1.return_video(video4)
        self.assertEqual(4, len(store1.rented_video_IDs()))
        self.assertEqual(2, len(store1.customers[phone_number1].rented_video_IDs))
        store1.return_video(video1) # try to return something that has not been rented
        self.assertEqual(4, len(store1.rented_video_IDs()))
        

def main():
    unittest.main()

if __name__ == '__main__':
    main()