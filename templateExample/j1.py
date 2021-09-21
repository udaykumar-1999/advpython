from jinja2 import Template

name = input("Enter name: ")
tm = Template("hello {{ name }}")
msg = tm.render(name=name)
print(msg)

name = "uday"
age = 25
tm = Template("my name is {{name}} and Iam {{age}}")
msg = tm.render(name=name, age=age)
print(msg)
