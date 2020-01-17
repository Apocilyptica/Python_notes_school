"""
__init__ # Private and Protected methods
"""


class Invoice:
    def __init__(self, client, total):
        self.client = client
        self.total = total

    def __str__(self):
        return f"Invoice from {self.client} for ${self.total}"

    def __repr__(self):
        return f"Invoice <value: {self.client}, total: ${self.total}>"


inv = Invoice("Google", 500)
# The __str__ method can be very helpful when trying to troubleshoot or look thru api info in a class method
print(str(inv))
# The __repr__ is more the true raw data from the class better to use for a large class
print(repr(inv))
