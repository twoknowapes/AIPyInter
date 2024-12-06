class SQLQueryBuilder:
    def __init__(self, base_query) -> None:
        self.base_query = base_query

    def __call__(self, **kwargs):
        query = self.base_query
        for key, value in kwargs.items():
            palceholder = f"{{{key}}}"
            query = query.replace(palceholder, str(value))
        return query
    

# 创建 SQLQueryBuilder 类的实例
base_query = "SELECT * FROM users WHERE age > {age} AND city = {coty}"
query_builder = SQLQueryBuilder(base_query)

# 像调用函数一样调用该实例来生成不同的 SQL 查询
query1 = query_builder(age=30, city="New York")
query2 = query_builder(age=25, city="San Francisco")

print(query1)
print(query2)
       