// use mongoCourse, Creates a new database type
db.createUser({
    user: 'Jordon',
    pwd: 'password',
    customData: { startDate: new Date() },
    roles: [
        { role: 'clusterAdmin', db: 'admin' },
        { role: 'readAnyDatabase', db: 'admin' },
        'readWrite'
    ]
}
)
// Creates Second User
db.createUser({
    user: 'Jon',
    pwd: 'password',
    customData: { startDate: new Date() },
    roles: [
        { role: 'clusterAdmin', db: 'admin' },
        { role: 'readAnyDatabase', db: 'admin' },
        'readWrite'
    ]
}
)
// Get All Users
db.getUser()
// Delete User
db.dropUser('Jon')