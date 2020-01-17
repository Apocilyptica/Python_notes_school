class Invoice:
    def __init__(self, client, total):
        self._client = (
            client  # one underscore means protected, two underscores means private
        )
        self._total = total

    def formatter(self):
        return f"{self._client} owes: ${self._total}"

    @property  # Lets everyone else know that having access to this variable is ok later on.
    def client(self):
        return self._client

    @client.setter
    def client(self, client):
        self._client = client

    @property
    def total(self):
        return self._total


google = Invoice("Google", 100)
print(google.formatter())
print(google.client)

google.client = "Yahoo"
print(google.client)
