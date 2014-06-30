phone_number_length = 12
dob_length = 3

class Customer(object):
    """
    a Customer to a DVD rental facility
    """
    def __init__(self, f_name, l_name, phone, dob, email):
        """
        constructor; initialize first and last names, phone #, date of birth, and email
        """
        self.first_name = f_name
        self.last_name = l_name
        
        if len(phone) != phone_number_length:
            print " ##### Warning: Invalid phone number. Valid format: '###-###-####'"
            self.phone = ""
        else:
            self.phone = phone
        
        if len(dob) != dob_length: # TODO could validate the month and day and the year (within reason)
            print " ##### Warning: Invalid date of birth. Valid format (use integers): '(month, day, year)'"
            self.dob = (0,0,0)
        else:
            self.dob = dob
        
        # TODO - validate email address
        self.email = email # future: support emailing customers reports (when their video(s) are due), coupons, suggested videos

        self.rented_videos = []

    def __str__(self):
        return self.print_me()

    def __repr__(self):
        return self.print_me()

    def print_me(self):
        """returns a string of the description of the Customer"""
        return "Customer: %s %s" % (self.first_name, self.last_name)

    def rent_video(self, video_ID):
        """customer rents a video (adds it to self.rented_videos"""
        if video_ID not in self.rented_videos:
            print "Customer: %s %s is now renting: %s" % (self.first_name, self.last_name, video_ID)
            self.rented_videos.append(video_ID)
        else:
            print " ##### Warning: Customer %s is already renting %s" % (self.phone, video_ID)

    def return_video(self, video_ID):
        """customer returning a video (removes it from self.rented_videos)"""
        if video_ID in self.rented_videos:
            print "Customer: %s %s has returned: %s" % (self.first_name, self.last_name, video_ID)
            self.rented_videos.remove(video_ID)
        else:
            print " ##### Warning: Unexpected video returned"