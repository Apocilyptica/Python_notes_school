db.books.insert({
    "name": "Deep Work: Rules for Focused Success in a Distracted World",
    "publishedDate": new Date(),
    "authors": [
        { "name": "Cal Newport" }
    ]
});

// Regular expression to findOne the "i" makes it case insensitive"
db.books.findOne({ name: /.*deep work.*/i })