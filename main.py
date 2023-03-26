def calculate(x,y,operation):
  """გამომთვლელი ფუნქცია

	Args:
			x (int): პირველი რიცხვი
			y (int): მეორე რიცხვი
			operation (Str): მოქმედება

	Returns:
			float: მოქმედების შედეგი
	"""
  result = 0
  if operation == 'მიმატება':
      result=x+y
  elif operation == 'გამოკლება':
      result = x-y
  elif operation == 'გამრავლება':
      result = x*y
  elif operation == 'გაყოფა':
      result = x/y
  elif operation == 'ახარისხება':
      result = x**y
  else:
      result = "Invalid input"
  return result


while True:
    x = float(input("პირველი რიცხვი:"))
    y = float(input("მეორე რიცხვი:"))
    operation = input("მოქმედება:")
    print(calculate(x,y,operation))
    if x == "მორჩა" or y == "მორჩა": #თუ ერთ-ერთი არგუმენტი "მორჩა"-ს უდრის, მაშინ ციკლი წყდება
        break