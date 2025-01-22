def stroka_split(stroka, razd):       
    stroka_split = []
    element_1 = 0
    for element in range(0, len(stroka)):
        if stroka[element:element + len(razd)] == razd:
            stroka_split.append(stroka[element_1:element+len(razd)])
            element_1 = element + len(razd) 
    stroka_split.append(stroka[element_1:])    
    return stroka_split

stroka = 'Таким образом, метод split() позволяет легко и быстро разделить строку на отдельные слова и сохранить их в списке для дальнейшей обработки.'
razd = 'мет'
print(stroka_split(stroka, razd))



    





  







