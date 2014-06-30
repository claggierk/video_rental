from VideoRental import VideoRental
import unittest

class videoRentalTests(unittest.TestCase):
    def testVideoTMDBID(self):
        """tests that the movie Braveheart is found in TMDB"""
        video_title = "Braveheart"
        result = 197
        video = Video(video_title)
        self.assertEqual(result, video.TMDB_ID)

def main():
    unittest.main()

if __name__ == '__main__':
    main()