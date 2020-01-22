// returns how many documemnts with the name "Blink" in that query
db.books.find({ name: "Blink" }).length()
// Only returns one item and returns in the "pretty() function"
db.books.findOne({ name: "Blink" })