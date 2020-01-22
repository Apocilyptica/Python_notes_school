db.books.insert(
    {
        "name": "Deep Work: Rules for Focused Success in a Distracted World",
        "publishedDate": new Date(),
        "reviews": 100,
        "authors": [
            { "name": "Cal Newport" }
        ]
    }
)



// check wether a field exists or not
db.books.find({ reviews: { $exists: false } }).pretty()

db.books.find({ reviews: { $exists: true } }).pretty()