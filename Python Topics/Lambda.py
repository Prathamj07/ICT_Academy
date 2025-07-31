def op(y):
    return lambda x: x*y

prod = op(2)
print("Double the number ",prod(15))
 
    
subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

subject_marks.sort(key = lambda x:x[1])

print(subject_marks)


data = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

data.sort(key= lambda x: x['color'])

print(data)
