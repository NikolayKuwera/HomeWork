immutable_var = (1, 2.0, 'String', True, [1, 2, 3, 4] )
print('immutable_var :',immutable_var)
#immutable_var[0] = 'one'
#TypeError: 'tuple' object does not support item assignment
# Главное свойство кортежа - это невозможность его изменения после создания.

mutable_list = (1, 2.0, 'String', True, [1, 2, 3, 4] )
mutable_list[4][1] = 6
# можно изменять в кортеже , если в нем присутствует список ( изменения вносятся по индексу внутри списка)
print('mutable_list :',mutable_list)
