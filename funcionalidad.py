def ganancia (costo_producto,precio_de_venta):
    costo_producto = int(input("Ingrese el costo del producto: "))
    precio de venta = int (input("Ingrese el precio de venta: "))

    return costo_producto - precio_de_venta

materia_prima =input('Ingresa el nombre de la materia prima que se va a entregar'))
envase-=int(input('Ingresa el tipo del envase que se va a entregar'))
tapas-=int(input('Ingresa el tipo de tapa que quieres'))
costo_de_energia=int(input('Ingresa el costo de la energia este mes'))
costo_de_mano_de_obra=int(input('Ingresa el costo de la mano de obra este mes'))
costo_de_material=int(input('Ingresa el costo de material este mes'))
tamaño_del_envase=int(input('Ingresa el tamaño del envase'))
tipo_de_producto=input('Que producto deseas?. 1.Shampoo  2. Limpiador 3.Jugo Natural')


if tipo_de_producto =='1':
    tipo_de_producto='Shampoo'
    break
elif tipo_de_producto =='2':
    tipo_de_producto='Limpiador'
    break
elif tipo_de_producto =='3':
    tipo_de_producto='Jugo Natural'
    break
else:
    print('Ingresa una opcion valida')
    tipo_de_producto=input('1.Shampoo  2. Limpiador 3.Jugo Natural')
    break

if tipo_de_producto =='Shampoo':

  sub_tipo_de_producto=["Durazno","Manzana","Almiscle","Nutribella"]
  print(f'Tenemos los siguientes productos{sub_tipo_de_producto}')
  sub_tipo_de_producto=input('Que subtipo de producto deseas?')
  if sub_tipo_de_producto =='Durazno':
    sub_tipo_de_producto='Durazno'
    break
  elif sub_tipo_de_producto =='Manzana':
    sub_tipo_de_producto='Manzana'
    break
  elif sub_tipo_de_producto =='Almiscle':
    sub_tipo_de_producto='Almiscle'
    break
  elif sub_tipo_de_producto =='Nutribella':
    sub_tipo_de_producto='Nutribella'
    break
  else:
    print('Ingresa una opcion valida')
    sub_tipo_de_producto=input('Que subtipo de producto deseas?')


tipo_de_envase=input('Que tipo de envase deseas?')