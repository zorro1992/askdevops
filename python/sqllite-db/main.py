from sqlalchemy import create_engine

engine = create_engine('sqlite:///census.sqlite')
connection = engine.connect()

print(engine.table_names())

stmt = 'SELECT * FROM census limit 10'
result_proxy=connection.execute(stmt)
results=result_proxy.fetchall()
print(results)

print(type(results))

for x in results:
    print(x)