from html import escape

from jinja2 import Template, Environment, FileSystemLoader, FunctionLoader

# name = "Федор"
# age = 28
#
# tm = Template("Привет {{ n.upper() }}, мне {{ a*2 }} лет")
# msg = tm.render(a=age, n=name)
#
# print(msg)
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def getName(self):
#         return self.name
#
#     def getAge(self):
#         return self.age
#
# per = Person("Федор", 30)
#
# tm = Template("Привет, меня зовут {{ p.name }}, мне {{ p.age }} лет")
# msg = tm.render(p=per)
#
# print(msg)
#
# tm = Template("Привет, меня зовут {{ p.getName() }}, мне {{ p.getAge() }} лет")
# msg = tm.render(p=per)
#
# print(msg)
#
# per = {"name": "Nik", "age": 28}
#
# tm = Template("Привет, меня зовут {{ p.name }}, мне {{ p.age }} лет")
# msg = tm.render(p=per)
#
# print(msg)
#
# tm = Template("Привет, меня зовут {{ p['name']}}, мне {{ p['age'] }} лет")
# msg = tm.render(p=per)
#
# print(msg)




# data = """{% raw %} Модуль  Jinja вместо
# определения {{ name }}
# подставляет соответствующее значение {% endraw %}"""
#
# tm = Template(data)
# msg = tm.render(name="Федор")
#
# print(msg)


#
# link = '''В HTML-документе ссылки определяются так:
# <a href="#">Ссылка</a>'''
#
# tm = escape(link)
# # msg = tm.render(link=link)
#
# print(tm)



# cities = [
#     {"id": 1, "city": " Москва"},
#     {"id": 2, "city": "Санкт-Петербург"},
#     {"id": 3, "city": " Казань"},
#     {"id": 4, "city": " Самара"},
# ]
#
#
# link = '''<select name="cities">
# {% for city in cities -%}
# {% if city.id > 2 -%}
#     <option value="{{ city['id'] }}">{{ city['city'] }}</option>
# {% elif city.city == "Москва" -%}
#     <option>{{ city['id'] }}</option>
# {% else -%}
#     {{ city.city }}
# {% endif -%}
# {% endfor -%}
# </select>
# '''
#
# tm = Template(link)
# msg = tm.render(cities=cities)
#
# print(msg)




# cars = [
#     {"model": "Audi", "price": 6000000},
#     {"model": "BMW", "price": 5000000},
#     {"model": "Mersedes", "price": 12000000},
#     {"model": "ГАЗ 2107", "price": 200000},
# ]

# tpl = "Суммарная цена автомобилей: {{ cs | sum(attribute='price') }}"
# tm = Template(tpl)
# msg = tm.render(cs=cars)

# digs = [1, 2, 3, 4, 5]
#
# tpl = "Суммарная цена автомобилей: {{ cs | sum }}"
# tm = Template(tpl)
# msg = tm.render(cs=digs)
#
# print(msg)





# cars = [
#     {"model": "Audi", "price": 6000000},
#     {"model": "BMW", "price": 5000000},
#     {"model": "Mersedes", "price": 12000000},
#     {"model": "ГАЗ 2107", "price": 200000},
# ]
#
# tpl = '''
# {%- for model in cars -%}
# {% filter upper %}{{ model.model }}{% endfilter %}
# {% endfor -%}
# '''
#
# tm = Template(tpl)
# msg = tm.render(cars=cars)
#
# print(msg)





# html = '''
# {% macro input(name, value='', type='text', size=20) -%}
#     <input type="{{ type }}" name="{{ name }}" value="{{ value | e }}" size="{{ size }}">
# {%- endmacro %}
# <p>{{ input('username') }}
# <p>{{ input('email') }}
# <p>{{ input('password') }}
# '''
#
#
# tm = Template(html)
# msg = tm.render()
#
# print(msg)




# person = [
#     {"name": "Dima", "age": 28, "weight": 185},
#     {"name": "Nikola", "age": 18, "weight": 170},
#     {"name": "Renat", "age": 32, "weight": 183},
# ]
#
# html = '''
# {% macro list_users(list_of_user) -%}
# <ul>
# {% for u in list_of_user -%}
#     <li>{{ u.name }} {{ caller(u) }}
# {%- endfor %}
# </ul>
# {%- endmacro %}
#
#
# {% call(user) list_users(users) %}
#     <ul>
#     <li>age: {{user.age}}
#     <li>weight: {{user.weight}}
#     </ul>
# {% endcall -%}
# '''
#
# tm = Template(html)
# msg = tm.render(users=person)
#
# print(msg)


# person = [
#     {"name": "Dima", "age": 28, "weight": 185},
#     {"name": "Nikola", "age": 18, "weight": 170},
#     {"name": "Renat", "age": 32, "weight": 183},
# ]
#
# def loadTpl(path):
#     if path == "index":
#         return '''Имя {{u.name}}, возраст {{u.age}}'''
#     else:
#         return '''Данные: {{u}}'''
#
#
# # file_loader = FileSystemLoader('templates')
# file_loader = FunctionLoader(loadTpl)
# env = Environment(loader=file_loader)
#
#
# tm = env.get_template('index2')
# msg = tm.render(u=person[0])
#
# print(msg)



# person = [
#     {"name": "Dima", "age": 28, "weight": 185},
#     {"name": "Nikola", "age": 18, "weight": 170},
#     {"name": "Renat", "age": 32, "weight": 183},
# ]
#
# file_loader = FileSystemLoader('templates')
# env = Environment(loader=file_loader)
#
#
# tm = env.get_template('page.html')
# msg = tm.render(users=person)
#
# print(msg)
