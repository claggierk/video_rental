from Customer import Customer
from Video import Video
import unittest

first_name = "Lionel"
last_name = "Messi"
phone_number = "777-321-1234"
dob = (6,11,1980)
email = "clark.r.phillips@gmail.com"

class customerTests(unittest.TestCase):
    def testCustomerCreation(self):
        """tests a valid customer is created"""
        c1 = Customer(first_name, last_name, phone_number, dob, email)
        self.assertEqual(first_name, c1.first_name)
        self.assertEqual(last_name, c1.last_name)
        self.assertEqual(phone_number, c1.phone)
        self.assertEqual(dob, c1.dob)
        self.assertEqual(email, c1.email)

    def testInvalidPhoneNumber(self):
        """tests an invalid phone number is perceived as invalid"""
        phone_number = "9792295854"

        result = ""
        
        c1 = Customer(first_name, last_name, phone_number, dob, email)
        self.assertEqual(result, c1.phone)

    def testInvalidDOB(self):
        """tests an invalid date of birth is perceived as invalid"""
        dob = "01181985"

        result = (0,0,0)
        
        c1 = Customer(first_name, last_name, phone_number, dob, email)
        self.assertEqual(result, c1.dob)

    def testRentVideo(self):
        """tests the renting of a video"""
        video_title = "Braveheart"
        video = Video(video_title)
        
        c1 = Customer(first_name, last_name, phone_number, dob, email)
        c1.rent_video(video.ID)

        self.assertEqual(1, len(c1.rented_video_IDs))
        self.assertEqual(video.ID, c1.rented_video_IDs[0])

    def testReturnVideo(self):
        """tests the returning of a video"""
        video_title = "Braveheart"
        video = Video(video_title)
        
        c1 = Customer(first_name, last_name, phone_number, dob, email)
        c1.rent_video(video.ID)
        self.assertEqual(1, len(c1.rented_video_IDs))
        c1.return_video(video.ID)
        self.assertEqual(0, len(c1.rented_video_IDs))

    def testRentReturnVideo(self):
        """tests the renting and returning of a video (tests duplicate rents and returns)"""
        video1 = Video("Braveheart")
        video2 = Video("The Matrix")
        video3 = Video("Forrest Gump")
        
        c1 = Customer(first_name, last_name, phone_number, dob, email)
        c1.rent_video(video1.ID)
        c1.rent_video(video2.ID)
        c1.rent_video(video3.ID)
        self.assertEqual(3, len(c1.rented_video_IDs))
        c1.return_video(video2.ID)
        self.assertEqual(2, len(c1.rented_video_IDs))
        c1.rent_video(video2.ID)
        c1.rent_video(video2.ID) # duplicate rental videos (same UUID)
        self.assertEqual(3, len(c1.rented_video_IDs))
        c1.return_video(video3.ID)
        c1.return_video(video3.ID) # duplicate return videos (same UUID)
        self.assertEqual(2, len(c1.rented_video_IDs))

def main():
    unittest.main()

if __name__ == '__main__':
    main()