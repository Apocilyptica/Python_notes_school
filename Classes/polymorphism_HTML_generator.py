# abstract class
class Html:
    def __init__(self, content):
        self.content = content

    def render(self):
        raise NotImplementedError("Subclass must implement render method")


class Heading(Html):
    def render(self):
        return f"<h1>{self.content}</h1>"


class Div(Html):
    def render(self):
        return f"<div>{self.content}</div>"


tags = [
    Div("Some content"),
    Heading("Some big heading"),
    Div("Another div"),
]

for tag in tags:
    print(tag.render())

print(Html.render("Other content"))
