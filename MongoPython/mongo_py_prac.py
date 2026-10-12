from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['school']


db.students.insert_one({
    "name": "Bob",
    "age": 18,
    "grade": "12th"
})
db.students.insert_one({
    "name": "Adam",
    "age": 24,
    "grade": "11th"
})


# for student in db.students.find():
#     print(student)
db = client['de_practice']

db.runs.insert_many([
  { 'name': 'orders_etl',   'status': 'success', 'records': 14500, 'duration': 32, 'env': 'prod' },
  { 'name': 'users_sync',   'status': 'failed',  'records': 0,     'duration': 5,  'env': 'prod' },
  { 'name': 'stock_etl',    'status': 'success', 'records': 8900,  'duration': 18, 'env': 'prod' },
  { 'name': 'orders_etl',   'status': 'success', 'records': 15200, 'duration': 35, 'env': 'prod' },
  { 'name': 'test_pipeline','status': 'success', 'records': 100,   'duration': 2,  'env': 'dev'  },
  { 'name': 'users_sync',   'status': 'success', 'records': 3210,  'duration': 9,  'env': 'prod' },
])

db.runs.insert_one({
    'name': 'payments_etl',
    'status': 'success',
    'records': 500,
    'duration': 12,
    'env': 'prod'
})

for run in db.runs.find():
    print(run)

print('Less than 8000 records\n')
for run in db.runs.find({'records': {'$lt': 8000}}):
    print(run)

print('\nSuccess runs\n')
for run in db.runs.find({'status': 'success'}, {'_id': 0, 'name': 1, 'status': 1}):
    print(run)

print(db.runs.find({'name': 'stock_etl'}, {'duration': 1, '_id': 0, 'name': 1})[0])
db.runs.update_one(
    {'name': 'stock_etl'},
    {'$set': {'duration': 20}}
)
print(db.runs.find({'name': 'stock_etl'}, {'duration': 1,  '_id': 0, 'name': 1})[0])


db.runs.update_many({'env': 'prod'}, {'$push': {'reviewed': True}})
for run in db.runs.find({'env': 'prod'}, {'_id': 0, 'name': 1, 'reviewed': 1}):
    print(run)

db.runs.delete_many({'env': 'dev'})
for run in db.runs.find():
    print(run)

print(len(list(db.runs.find())))