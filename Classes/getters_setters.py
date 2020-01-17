# Getter and Setter Functions
class Invoice:
    def __init__(self, client, total):
        self.client = client
        self.total = total

    """ Getter Function in everyother language
    def get_client(self):
        return self.client
    """

    def formatter(self):
        return f"{self.client} owes: ${self.total}"


google = Invoice("Google", 100)
print(google.client)

# Setter Process everyother language needed to have a setter fucntion within the class object to change a value
# print(google.get_client())
google.client = "Yahoo"
print(google.client)
