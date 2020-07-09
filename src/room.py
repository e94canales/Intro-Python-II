# Implement a class to hold room information. This should have name and
# description attributes.
class Room():
    def __init__(self, name, description, w_to = None, d_to = None, s_to = None, a_to = None):
        self.name = name
        self.description = description
        self.w_to = w_to
        self.d_to = d_to
        self.s_to = s_to
        self.a_to = a_to

    def __str__(self):
        return f"Current Location: {self.name}\nDescription: {self.description}"
    
    def compass(self):
        return f"\nCurrent Room: {self.name} -- N: {self.w_to}, E: {self.d_to}, S: {self.s_to}, W: {self.a_to}"

    def description(self):
        return f"Room Description: {self.description}"