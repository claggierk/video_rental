class VideoRental(object):
    """
    a VideoRental is an abstract class (both Store and Kiosk are based from VideoRental).
    One can add inventory (add/remove a Video)
    One can add a Customer
    One can determine the videos are in inventory, which are currently rented, which are rentable

    data is stored in two member variable dictionaries:
        videos: key is a UUID (this UUID)
            a Video must have a unique ID. Each instance of the same video is a unique video (stores contain multiple instances of the same video)
        customers: key is a phone number
            a Customer has a member variable rented_video_IDs (which is a list of Video UUIDs)
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

    def add_customer(self, a_customer):
        """add a Customer"""
        if a_customer.phone not in self.customers:
            print "Adding customer: %s" % a_customer
            self.customers[a_customer.phone] = a_customer
        else:
            print " ##### Warning: this customer already exists"

    def remove_customer(self, phone):
        """remove a Customer"""
        try:
            print "Removing customer: %s" % self.customers[phone]
            del self.customers[phone]
        except KeyError:
            print " ##### Warning: Could not remove customer: %s (no entry)" % phone

    def add_video(self, my_video):
        """adds a Video to the inventory"""
        if my_video.ID not in self.videos:
            print "Adding: %s to inventory" % my_video
            self.videos[my_video.ID] = my_video
            return my_video.ID
        else:
            print " ##### Warning: this particular video is already in inventory"

    def remove_video(self, video_ID):
        """removes a Video to the inventory"""
        if video_ID in self.videos:
            print "Removing: %s from inventory" % video_ID
            del self.videos[video_ID]
        else:
            print " ##### Warning: this particular video is NOT in inventory"

    def all_video_IDs(self):
        """return a sorted list of all the videos"""
        # all the videos that are currently in the inventory are elements in the videos dictionary
        return videos.keys()

    def rented_video_IDs(self):
        """return a sorted list of all the that are currently rented"""
        # aggregate all the rented UUIDs from all the customers
        rented_video_IDs = []
        for customer_ID in self.customers:
            if len (self.customers[customer_ID].rented_video_IDs) > 0:
                rented_video_IDs.extend(self.customers[customer_ID].rented_video_IDs)
        return rented_video_IDs

    def rentable_video_IDs(self):
        """return a sorted list of all the that are currently rentable"""
        # use set theory difference to determine the current rentable videos
        return set(self.all_video_IDs()) - set(self.rented_video_IDs())

    def populate_videos(self, video_IDs):
        """given a list of video_IDs, return a sorted list of videos"""
        videos = []
        for video_ID in video_IDs:
            videos.append(self.videos[video_ID])
        return sorted(videos, key=lambda a_video: a_video.title)

    def rent_video(self, customer_ID, video_ID):
        """rent a video to a customer"""
        # ensure you do not rent a video that is currently rented!
        if video_ID not in self.rented_video_IDs():
            self.customers[customer_ID].rent_video(video_ID)
        else:
            print " ##### Warning: video %s is not available for rent" % video_ID

    def return_video(self, video_ID):
        """return a video (determines which customer rented it and returns it)"""
        # support customers dropping off their videos without having to login
        # search through all the customers to determine who had rented the video
        for customer_ID in self.customers:
            current_customer = self.customers[customer_ID]
            if video_ID in current_customer.rented_video_IDs:
                current_customer.return_video(video_ID)
                print "Customer %s returned %s" % (current_customer.phone, video_ID)
                return
        print "No customer had rented video: %s" % video_ID

    # this could become very interesting
    # support for more elaborate coupons (per video, per genre?, etc)
    def apply_percent_discount(self, percent):
        """apply a percent discount to all videos"""
        for video_ID in self.videos:
            self.videos[video_ID].percent_discount = percent

    def apply_amount_discount(self, amount):
        """apply an amount discount to all videos"""
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
        self.phone = ""

        # different per day of the week?
        # holidays? ice days?
        # different locations may have different schedules altogether
        self.hours = ""

    def is_closed(self):
        # should determine the date (day of the week) and determine whether the store is closed or not
        # check to see if a holiday applies?
        return self.closed

class Kiosk(VideoRental):
    """
    unique to a Kiosk is a maintenance window
    """
    def __init__(self, location):
        VideoRental.__init__(self, "Kiosk", location)
        self.maintenance = False # kiosks must be maintenanced (adding/removing videos at a minimum)