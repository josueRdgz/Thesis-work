---
marp: true
theme: gaia
paginate: true
_class: lead
backgroundImage: url('https://marp.app/assets/hero-background.jpg')
---

# Proceso de Evaluación Automática en Problemas de Enrutamiento de Vehículos

Autor: Josué Rodríguez Ramírez
Tutor: Fernando Raúl Rodríguez Flores
Cotutor: Lic. Rodrigo García Gómez

<style>
.column {
  float: left;
  padding: 10px;
  box-sizing: border-box;
}

.clearfix::after {
  content: "";
  display: table;
  clear: both;
}
</style>

<div class="clearfix">

<div class="column">

 <a href="https://t.me/josue_rdgz" target="_blank"> @josue_rdgz</a>
</div>
<div class="column" style="margin-left: 25px;">

<a href="mailto:josuerdgz.ramirez@gmail.com"> josuerdgz.ramirez@gmail.com</a>
</div>
<div class="column" style="margin-left: 25px;">

  <a href="https://wa.me/+525533242336" target="_blank"> +52 (55) 3324 2336</a>
</div>
</div>

---
## <center>Introducción</center>

Problemas de Enrutamiento de Vehículos:

- Son problemas logísticos.

---
## <center>Introducción</center>

Problemas de Enrutamiento de Vehículos:

- Son problemas logísticos.

<style>
.column2 {
  float: left;
  padding: 20px;
  box-sizing: border-box;
}

</style>
<div class="column2">
<img src="/Users/josue/Desktop/Imagen1.png" height="300" >
</div>
<div class="column2" style="margin-left: 30px;">


- Depósito(s)  <br>
- Flota de vehículos <br>
- Conjunto de clientes <br>
</div>

---


## <center>Introducción</center>

Problemas de Enrutamiento de Vehículos:

- Son problemas logísticos.

<style>
.column2 {
  float: left;
  padding: 20px;
  box-sizing: border-box;
  word-wrap: break-word;
}

</style>
<div class="column2">
<img src="/Users/josue/Desktop/Imagen1.png" height="300" >
</div>
<div class="column2" style="margin-left: 30px;">
<strong>Objetivo:</strong> <br>
Encontrar rutas de costo mínimo<br>
desde depósitos hasta clientes <br>
</div>

---

## <center>Introducción</center>

Problemas de Enrutamiento de Vehículos:

- Son problemas logísticos.
- Generan gastos millonarios diarios.

---
## <center>Introducción</center>

Problemas de Enrutamiento de Vehículos:

- Son problemas logísticos.
- Generan gastos millonarios diarios.
- Optimizar estos problemas significaría ahorros considerables.

---
## <center>Introducción</center>

Problemas de Enrutamiento de Vehículos:

- Son problemas logísticos.
- Generan gastos millonarios diarios.
- Optimizar estos problemas significaría ahorros considerables.
- Múltiples variantes.

---
## <center>Introducción</center>

- Múltiples variantes

  -  VRP con restricciones de capacidad (CVRP)
  
---
## <center>Introducción</center>

- Múltiples variantes

  -  VRP con restricciones de capacidad (CVRP)
  - VRP con recogida y entrega (VRPPD)

---
## <center>Introducción</center>

- Múltiples variantes

  -  VRP con restricciones de capacidad (CVRP)
  - VRP con recogida y entrega (VRPPD)
  - VRP con ventanas de tiempo (VRPTW)

---
## <center>Introducción</center>

- Múltiples variantes

  -  VRP con restricciones de capacidad (CVRP)
  - VRP con recogida y entrega (VRPPD)
  - VRP con ventanas de tiempo (VRPTW)
  - VRP con más de un depósito (MDVRP)

---
## <center>Introducción</center>

Problemas de Enrutamiento de Vehículos:

- Son problemas logísticos.
- Generan gastos millonarios diarios.
- Optimizar estos problemas significaría ahorros considerables.
- Múltiples variantes
- NP-Duros

---
## <center>Introducción</center>

Problemas de Enrutamiento de Vehículos:

- NP-Duros
  - Algoritmos basados en poblaciones
---
## <center>Introducción</center>

Problemas de Enrutamiento de Vehículos:

- NP-Duros
  - Algoritmos basados en poblaciones
  - Algoritmos basados en Búsqueda Local
---
## <center>Introducción</center>

- Algoritmos basados en Búsqueda Local
    <br>
    + Se parte de una solución inicial.
---
## <center>Introducción</center>

- Algoritmos basados en Búsqueda Local
  <br>
    + Se parte de una solución inicial.
    + Se modifica para obtener el conjunto de soluciones vecinas.
---

## <center>Introducción</center>

- Algoritmos basados en Búsqueda Local
  <br>
    + Se parte de una solución inicial.
    + Se modifica para obtener el conjunto de soluciones vecinas.
    + Se usan estructuras de entorno o criterios de vecindad.
---
## <center>Introducción</center>

- Estructuras de entorno o criterios de vecindad
  <br>
  - Intercambiar dos clientes
  - Cambiar un cliente de posición
  - Cambiar un vehículo de ruta 
  - Insertar un nuevo cliente en una ruta

---
## <center>Preguntas científicas</center>

<p style="font-size: 50px;">¿Cómo se puede automatizar el proceso de evaluación de todas las soluciones?</p>

<p style="font-size: 50px;"> ¿Cómo generalizar ese proceso para todos los Problemas de Enrutamiento de Vehículos? </p>

---
## <center>Objetivo</center>
<p style="font-size: 50px;"> Desarrollar estructura para evaluar de forma autómatica 
soluciones vecinas de cualquier problema de enrutamiento 
de vehículos, a partir del grafo de evaluación. <br>
</p>

---
## <center>Preliminares</center>

- Grafo de evaluación
  <br>
  - Grafo dirigido
---

## <center>Preliminares</center>

- Grafo de evaluación
  <br>
  - Grafo dirigido
  - Nodos principales: Variables iniciales (clientes, depósitos)
---
## <center>Preliminares</center>

- Grafo de evaluación
  <br>
  - Grafo dirigido
  - Nodos principales: Variables iniciales (clientes, depósitos)
  - Nodos secundarios: Variables intermedias y operacionales
  
---
## <center>Preliminares</center>

- Grafo de evaluación
  <br>
  - Grafo dirigido
  - Nodos principales: Variables iniciales (clientes, depósitos)
  - Nodos secundarios: Variables intermedias y operacionales
  - Arcos: entradas y las salidas de las operaciones
  
---
## <center>Preliminares</center>

- Grafo de evaluación (Inicialización)

<center>
    <img src="/Users/josue/Desktop/Init.png" height="350">
</center>

---
## <center>Preliminares</center>

- Grafo de evaluación (Evaluación de la solución inicial)
<center>
    <img src="/Users/josue/Desktop/evaluación ruta.png" height="350">
</center>

---
## <center>Preliminares</center>

- Grafo de evaluación (Evaluación de la solución inicial)
<center>
    <img src="/Users/josue/Desktop/evaluacion total.png" height="350">
</center>

---
## <center>Preliminares</center>
- Grafo de evaluación (Encontrar soluciones vecinas)
  - Eliminar un cliente de una ruta
  
<center>
    <img src="/Users/josue/Desktop/eliminar cliente.png" height="350">
</center>

---
## <center>Preliminares</center>
- Grafo de evaluación (Encontrar soluciones vecinas)
  - Insertar un cliente en una ruta
  
<center>
    <img src="/Users/josue/Desktop/insertar cliente.png" height="350">
</center>

---
## <center> ¿Cómo evaluar de manera eficiente? </center>

<p style="font-size: 40px;"> Para eso se implementa una cinta computacional basada en la 
idea de la Diferenciación Automática. </p>

---
## <center> Diferenciación Automática </center>
<br>

- Se evalúa la derivada de una función automáticamente.

---
## <center> Diferenciación Automática </center>
<br>

- Se evalúa la derivada de una función automáticamente.
- La relación de las variables se presentan en un grafo.

---
## <center> Diferenciación Automática </center>
<br>

- Se evalúa la derivada de una función automáticamente.
- La relación de las variables se presentan en un grafo.
- Guarda el procedimiento de evaluación en una cinta.

---
## <center> Diferenciación Automática </center>
<br>

- Se evalúa la derivada de una función automáticamente.
- La relación de las variables se presentan en un grafo.
- Guarda el procedimiento de evaluación en una cinta.
- Se evalúa en modo *forward* o *reverse*.

---


<div class="column2" style="margin-left: 60px;">

## <center> $y=sen(x_{1})*x_{2}$ </center>


---

<div class="column2" style="margin-left: 60px;">

## <center> $y=sen(x_{1})*x_{2}$ </center>

<center>

|                                                                 |
| --------------------------------------------------------------- |
| <center> $v_{-1}=x_{1}$ <br> $v_{0}=x_{2}$ </center>            |
| <center> $v_{1}=sen(v_{-1})$ <br> $v_{2}=v_{1}*v_{0}$ </center> |
| <center>$y=v_{2}$</center>                                      |

</center>
</div>
<div class="column2" style="margin-left: 50px;">
<br>
<img src="/Users/josue/Desktop/ad.png" height="300" >
</div>

---

<div class="column2" style="margin-left: 60px;">

## <center> $y=sen(x_{1})*x_{2}$ </center>

<center>

|                                                                  |
| ---------------------------------------------------------------- |
| <center> $v_{-1}=x_{1}$ <br> $v_{0}=x_{2}$ </center>             |
| <center>  $v_{1}=sen(v_{-1})$ <br> $v_{2}=v_{1}*v_{0}$ </center> |
| <center>$y=v_{2}$</center>                                       |

</center>
</div>



<div class="column2" style="margin-left: 100px;">


|                                                                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <center> $v_{-1}=x_{1}$ <br> $\overline{v_{-1}}=x_{1}'$ <br> $v_{0}=x_{2}$ <br> $\overline{v_{0}}=x_{2}'$</center>                                                                             |
| <center> $v_{1}=sen(v_{-1})$ <br> $\overline{v_{1}}=cos(v_{-1})* \overline{v_{-1}}$  <br> $v_{2}=v_{1}*v_{0}$ <br> $\overline{v_{2}}=\overline{v_{1}}* v_{0} + \overline{v_{0}}*v{1}$</center> |
| <center>$y=v_{2}$ <br> $y´=\overline{v_{2}}$ </center>                                                                                                                                         |
</div>

---

## <center> Cinta automática </center>
<br>
<center>
    <img src="/Users/josue/Desktop/tape.png" height="500">
</center>

---
## <center> Propuesta de cinta automática para VRP </center>
<br>

- Lista de Variables penalizadas
- Operaciones de los criterios de vecindad a realizar
- Verificación
- Evaluación eficiente

---

## <center> Cinta automática para VRP </center>



    var clientes_penalizados
    Insertar cliente (2,2)
    por cada cliente_i en clientes_penalizados:
        si cliente_i en ruta 2  
            si posición cliente_i < posición cliente 2
                Evaluar ruta 2
                terminar
    Reevaluar (2,2)
<br>
<center>
<img src="/Users/josue/Desktop/insertar cliente.png" height="180" >
</center>

---

## <center> Resultados </center>

- VRP con ventanas de tiempo
<center>
<img src="/Users/josue/Desktop/vrptw.png" height="400" >
 </center>

 ---
 ## <center> Resultados </center>

- VRP con recogida y entrega simultánea
<center>
<img src="/Users/josue/Desktop/vrpspd.png" height="400" >
 </center>

 ---
## <center> Conclusiones </center>
- La cinta computacional extiende la evaluación a cualquier VRP.
- Resuelve la limitante del grafo de evaluación.
- Permite evaluar eficientemente las soluciones vecinas.
- No se necesita código adicional.
---
## <center> Recomendaciones </center>
- Variantes de VRP con rutas mezcladas
- Comprobar con problemas reales.
-  Incorporar esta extensión al sistema propuesto en la tesis:
   - Sistema para la integración de herramientas para la solución ágil de problemas de enrutamiento de vehículos. Rodrigo García Gómez.

---

<center>

# Proceso de Evaluación Automática en Problemas de Enrutamiento de Vehículos

Autor: Josué Rodríguez Ramírez
Tutor: Fernando Raúl Rodríguez Flores
Cotutor: Lic. Rodrigo García Gómez
</center>
<style>
.column {
  float: left;
  padding: 10px;
  box-sizing: border-box;
}

.clearfix::after {
  content: "";
  display: table;
  clear: both;
}
</style>

<div class="clearfix">

<div class="column">

 <a href="https://t.me/josue_rdgz" target="_blank"> @josue_rdgz</a>
</div>
<div class="column" style="margin-left: 25px;">

<a href="mailto:josuerdgz.ramirez@gmail.com"> josuerdgz.ramirez@gmail.com</a>
</div>
<div class="column" style="margin-left: 25px;">

  <a href="https://wa.me/+525533242336" target="_blank"> +52 (55) 3324 2336</a>
</div>
</div>

---
## <center> Pregunta 1 </center>

### <center> Diferenciación automática </center>

- Está basada en una definición informática de la función a derivar.
- Algoritmo de descomposición computacional de una función $F:X \subset \Re^{n} \to \Re^{m},  y= F(x)$.
- $F(x)$ se podrá descomponer en N–n sentencias o funciones elementales (denotadas por $f_{i}<x_{j}>$) , y que dependerán de las n variables independientes.
---
### <center> Diferenciación automática </center>

<pre><code> 
for i= n+1,n+2,...,N+m
       x<sub>i</sub> = f<sub>i</sub>&lt;x<sub>j</sub>&gt;<sub> j &isin; J<sub>i</sub> </sub>
end
for i= 1,2,...,m
        y<sub>i</sub> = x<sub>N+i</sub>
end
</code></pre>

$J_{i}$ es el conjunto de subíndices anteriores al de la variable considerada $x_{i}$.

---

### <center> ¿Diferenciación Automática y VRP? </center>

<pre><code> 
for i= n+1,n+2,...,N+m
       x<sub>i</sub> = f<sub>i</sub>&lt;x<sub>j</sub>&gt;<sub> j &isin; J<sub>i</sub> </sub>
end
for i= 1,2,...,m
        y<sub>i</sub> = x<sub>N+i</sub>
end
</code></pre>

- Cada $x_{i}$ representa la solución vecina de un VRP al aplicarle una operación que pertence a alguna estructura de entorno.
- Deben comprobarse las variables penalizadas.
- Al final se evalúa eficientemente.


---

## <center> Pregunta 2 </center>

### <center> Modo reverse </center>
- La información de las derivadas se propaga en sentido contrario al flujo de ejecución del programa.
- Por cada variable intermedia $v_{i}$ se genera una variable _adjunta_ $\overline{v_{i}}$.
- Acumula incrementalmente los valores $\overline{v_{i}}* \frac{\partial{y_{j}}}{\partial{v_{i}}}$
- Ocurre para todas las variables $v_{j}$ que dependen de $v_{i}$ donde $y_{j}$ es una función de dependencia.
- En una ejecución se obtienen todas las derivadas parciales de la función dependiente escogida.
---
 $y = tan(x1) * \frac{x1}{x2} + sen(x2) * cos(x1)$


<div style="display: flex; justify-content: space-between;">

<div style="flex: 1;">
<center>

|                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| $v_{-1} = x_{1}$ <br> $v_{0} = x_{2}$                                                                                                                                                   |
| $v_{1} = tan(v_{-1})$ <br> $v_{2} = v_{-1}/v_{0}$ <br> $v_{3} = v_{1}*v_{2}$ <br> $v_{4} = sen(v_{0})$ <br> $v_{5} = cos(v_{-1})$ <br> $v_{6} = v_{4}*v_{5}$ <br> $v_{7} = v_{3}+v_{6}$ |
| $y = v_{7}$                                                                                                                                                                             |
</center>
</div>

<div style="flex: 1;">
<center>

|                                                                                                                                                                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| $v_{7}^{*} = y^{*}$                                                                                                                                                                                                                                                                                                                    |
| $v_{6}^{*} += v_{7}^{*}$ <br> $v_{3}^{*} += v_{7}^{*}$ <br> $v_{5}^{*} += v_{4}*v_{6}^{*}$ <br> $v_{4}^{*} += v_{5}*v_{6}^{*}$ <br> $v_{-1}^{*} += -v_{5}^{*}*sen(v_{-1})$ <br> $v_{0}^{*} += v_{4}^{*}*cos(v_{0})$ <br> $v_{2}^{*} += v_{3}^{*}*v_{1}$ <br> $v_{1}^{*} += v_{3}^{*}*v_{2}$ <br> $v_{0}^{*} += -v_{2}^{*}*v_{2}/v_{0}$ |
</center>
</div>

<div style="flex: 1;">
<center>

|                                                                                |
| ------------------------------------------------------------------------------ |
| $v_{-1}^{*} += v_{2}^{*}/v_{0}$ <br> $v_{-1}^{*} += v_{1}^{*}/cos^{2}(v_{-1})$ |
| $x_{2}^{*} = v_{0}^{*}$ <br> $x_{1}^{*} = v_{-1}^{*}$                          |

</center>
</div>

</div>

---

## <center> Pregunta 3 </center>
### <center> Propuesta de implementación </center>

- Se implementa en lenguaje Lisp.
- Se utiliza macro-expansión para la creación de la cinta computacional.

---

## <center> Pregunta 3 </center>
### <center> Propuesta de implementación </center>

```lisp
(defmacro process-tape (nodes operations)
    `(let ((eval-pos 0))
       (dolist (operation ,operations)
         (eval `(funcall ,operation))
         (let ((route (car operation))
              (op-position (cadr operation)))
         (when (every (lambda (node)
                          (or (not (member node route))
                              (< (position node route) op-position)))
                         ,nodes)
            (setq eval-pos op-position))))
          (evaluate route eval-pos)))
```
