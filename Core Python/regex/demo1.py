import re
# data = "my name is Radha and ege is 22 or 48"
# re.findall("pattern,data")
# d = re.findall(r"\d+",data)

# d = re.search(r"\d+",data)
# d = re.match(r"\d+",data)
# print(d)
# print(d.group())

# d = re.fullmatch(r"\d+","I12345")
# print(d.group())
# print(d)

# data = "pradip sir mocks are very simple"

# print(re.sub("very simple", "tough", data))

# print(data)

print(re.findall(r'\D', "abfk7_**@"))
print(re.findall(r'\d', "abfk7_**@"))
print(re.findall(r'\w', "abfk7_**@"))
print(re.findall(r'\W', "abfk7_**@"))
print(re.findall(r"c..t","cot cot cut"))
print(re.findall('ab*', "abcd ab bd ab"))
print(re.findall('ab?', "abcd ab bd ab"))
print(re.findall(r'\w{4}', "abc ab,abcs"))
print(re.findall(r'\w{2,4}', "abc ab,abcs"))
print(re.findall("[^1-9]{2}", "I am in good in python"))
print(re.findall("[aeiou]", "I am in good in python"))
print(re.findall("[1-9]$", "I am in good in python9w"))





