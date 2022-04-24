from pymongo import *

if __name__ == '__main__':
    client = MongoClient()
    db = client.demo
    collection = db.crud

    # 增加
    # 单条数据
    student = {
        'sno': 1,
        'sname': '张三',
        'ssex': 1,
        'sage': 22
    }
    collection.insert_one(student)
    # 多条数据
    students = [
        {
            'sno': 2,
            'sname': '李四',
            'ssex': 0,
            'sage': 22
        },
        {
            'sno': 3,
            'sname': '王五',
            'ssex': 1,
            'sage': 22
        }
    ]
    collection.insert_many(students)

    # 删除
    collection.delete_one({ 'sname': '李四' })

    # 修改
    collection.update_one({ 'sname': '张三' }, { '$set': { 'sname': '张三三' } })

    # 查询
    # 非条件查询
    res = collection.find()
    print('Non-Criteria Queries:')
    for item in res:
        print(item)
    # 条件查询
    res = collection.find_one({}, { 'sname': '李四' })
    print('Criteria Queries:')
    print(res)