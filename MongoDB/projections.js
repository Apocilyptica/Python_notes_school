// Only Prints Out objects that you want to See, if you do not want to see default values ie the ID than a 0 is needed
db.books.find(
    {
        name: "Confident Ruby"
    },
    {
        _id: 0,
        name: 1,
        authors: 1
    }
).pretty()

// Diving down deeper, Query for a Portion of a Nested Array Element in a Document Using $slice
db.books.insert({
    "name": "Blink",
    "publishedDate": new Date(),
    "authors": [
        { "name": "Malcolm Gladwell" },
        { "name": "Ghost Writer" }
    ]
});

db.books.find(
    {
        name: "Blink"
    },
    {
        publishedDate: 1,
        name: 1,
        authors: { $slice: 2 }
    }
).pretty()