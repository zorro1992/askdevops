def divide(a,b):
    try:
      return a/b
    expcet ZeroDivisionError:
      return "Wrong division"

  
divide(2/0)