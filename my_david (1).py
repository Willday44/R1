import webbrowser

while True:
     print('What size would you like the titties - big, medium, or small?(Type exit to quit)')
     size_input = input().lower()
     if size_input == "exit":
         webbrowser.open('https://www.youtube.com/watch?v=owu0Q_F0IDk')
         print("Exiting the program.")
         break

     size_mapping = {
         'big': 3,
         'medium': 2,
         'small': 1
     }
     size = size_mapping.get(size_input, size_mapping['medium'])
     x = " " * size
     print(f'({x}.{x}Y{x}.{x})')
