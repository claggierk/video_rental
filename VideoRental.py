class VideoRental(object):
    """
    a VideoRental is an abstract class (both Store and Kiosk are based from VideoRental).
    One can add inventory (add/remove a Video)
    One can add a Customer
    One can determine the videos are in inventory, which are currently rented, which are rentable
    """
    def __init__(self, description, location):
        """
        constructor; initialize the description and location
        initialize the videos/customers
        """
        self.description = description
        self.location = location
        self.videos = {}
        self.customers = {}

    def add_video(self, my_video):
        """adds a Video to the inventory"""
        if my_video.ID not in self.videos:
            print "Adding %s to inventory" % my_video
            self.videos[my_video.ID] = my_video
            return my_video.ID
        else:
            print " ##### Warning: this particular video is already in inventory"

    def remove_video(self, my_video):
        """removes a Video to the inventory"""
        if my_video.ID in self.videos:
            print "Removing %s from inventory" % my_video
            del self.videos[my_video.ID]
        else:
            print " ##### Warning: this particular video is NOT in inventory"

    def all_videos(self):
        """return a sorted list of all the videos"""
        # can you sort a dictionary?
        all_videos = []
        for video_ID in self.videos:
            all_videos.append(self.videos[video_ID])
        return sorted(all_videos, key=lambda a_video: a_video.title)

    def rented_videos(self):
        """return a sorted list of all the that are currently rented"""
        rented_video_IDs = []
        for customer_ID in self.customers:
            if len (self.customers[customer_ID].rented_videos) > 0:
                rented_video_IDs.extend(self.customers[customer_ID].rented_videos)
        rented_videos = []
        for rented_video_ID in rented_video_IDs:
            rented_videos.append(self.videos[rented_video_ID])
        return sorted(rented_videos, key=lambda a_video: a_video.title)

    def rentable_videos(self):
        """return a sorted list of all the that are currently rentable"""
        return set(all_videos) - set(rented_videos)

    def add_customer(self, a_customer):
        """add a Customer"""
        if a_customer.phone not in self.customers:
            self.customers[a_customer.phone] = a_customer
        else:
            print " ##### Warning: this customer already exists"

    def remove_customer(self, a_customer):
        """remove a Customer"""
        try:
            del self.customers[a_customer.phone]
        except KeyError:
            print " ##### Warning: Could not remove customer: %s (no entry)" % a_customer

    def rent_video(self, customer_ID, video_ID):
        """rent a video to a customer"""
        self.customers[customer_ID].rent_video(video_ID)

    def return_video(self, video_ID):
        """return a video (determines which customer rented it and returns it)"""
        for customer in customers:
            if video_ID in customer.rented_videos:
                customer.return_video(video_ID)
                print "Customer %s returned %s" % (customer.phone, video_ID)
                return
        print "No customer had rented video: %s" % video_ID

    def apply_percent_discount(self, percent):
        """apply a percent discount"""
        for video_ID in self.videos:
            self.videos[video_ID].percent_discount = percent

    def apply_amount_discount(self, amount):
        """apply an amount discount"""
        for video_ID in self.videos:
            self.videos[video_ID].amount_discount = amount

class Store(VideoRental):
    """
    unique to a Store are employees and store hours
    """
    def __init__(self, location):
        VideoRental.__init__(self, "Store", location)
        self.closed = False
        self.employees = []

        # different per day of the week
        # holidays
        self.hours = ""

    def is_closed(self):
        return self.closed

class Kiosk(VideoRental):
    """
    unique to a Kiosk is a maintenance window
    """
    def __init__(self, location):
        VideoRental.__init__(self, "Kiosk", location)
        self.maintenance = False