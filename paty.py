print(&quot;lu ma mi ju vi sa do&quot;)
for i in range (1,32):
    # tranformo el valor de i en un texto
    d=str(i)
   
    #si el valor es menor que 10, agrega un espacio antes
    if i&lt;10:
        d=&#39; &#39;+d  #para i==1 --&gt; d=&#39; 1&#39;
       
   
    #para cada valor multiplo de 7, escribe el valor y salta linea
    if i%7 == 0:
        print(d)
        # para cada valor no multiplo de 7, escribe el valor y salta espacio
    else:
        print(d, end=&quot; &quot;)
       
print ()