def stroka_split (stroka, razd):
    stroka_split = []
    element = 0
    element_1 = 0
    while element <= len(stroka):
        if stroka[element:element + len(razd)] == razd:
            stroka_split.append(stroka[element_1:element + len(razd)])
            element_1 = element + len(razd)
            stroka_split.append(stroka[element_1:])
        element += 1
    return(stroka_split)

stroka = 'На этом курсе вы изучите основы SQL - языка запросов к базам данных.'
razd = 'изу'
print(stroka_split(stroka, razd))
   
