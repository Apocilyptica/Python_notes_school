//  builds a collection and shows what is in it
db.createCollection('books')
// show collection, command that shows all the collections in database

//  Inserting Documents into a MongoDB Collection object
db.books.insert({
    "title": "OOP Programming",
    "startDate": new Date(),
    "authors": [
        { "name": "Jon Snow Jr." },
    ]
})

// Insert Many Documents into a MongoDB Collection takes an array
db.books.insertMany([
    {
        "name": "Confident Ruby",
        "publishedDate": new Date(),
        "authors": [
            { "name": "Avdi Grimm" }
        ]
    },
    {
        "name": "The War of Art",
        "publishedDate": new Date(),
        "authors": [
            { "name": "Steven Pressfield" }
        ]
    },
    {
        "name": "Blink",
        "publishedDate": new Date(),
        "authors": [
            { "name": "Malcolm Gladwell" }
        ]
    }
])

// Query All Documents in a MongoDB Collection with the find() Method
db.books.find()
//  or
db.books.find().pretty()

// Query for Specific Documents in a MongoDB Collection
db.books.find({ name: "The War of Art" }).pretty()
// Returns many back because we have many in the database collection with that name
db.books.find({ name: "OOP Programming" }).pretty() 
