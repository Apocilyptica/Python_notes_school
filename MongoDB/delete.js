// Only removes one item
db.books.remove({
    name: "OOP Programming", 1
})
// Removes all items
db.books.remove({
    name: "OOP Programming"
})