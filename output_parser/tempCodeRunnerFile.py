prompt = template.format()
result = model.invoke(prompt)
result = parser.parse(result.content)

print(result)