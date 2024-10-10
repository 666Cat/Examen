# Preguntas sobre Lenguajes de Programación

## 1. ¿Cómo se define un lenguaje de programación?
Un lenguaje de programación es un conjunto de reglas y normas que se utilizan para escribir instrucciones que una computadora puede ejecutar. Estas instrucciones se utilizan para crear programas que realizan tareas específicas, como procesar datos, interactuar con el usuario o controlar dispositivos.

## 2. ¿Qué es la sintaxis en un lenguaje de programación?
La sintaxis en un lenguaje de programación se refiere a las reglas que definen la estructura y la forma en que se escriben las instrucciones.

## 3. Explica la diferencia entre sintaxis y semántica en los lenguajes de programación.
La sintaxis se refiere a la forma en que se escriben las instrucciones, mientras que la semántica se refiere al significado de esas instrucciones.

## 4. ¿Qué cambios trajo la evolución de la programación estructurada a la programación orientada a objetos?
La programación estructurada se enfoca en la secuencia de instrucciones y el uso de funciones para organizar el código. La Programación Orientada a Objetos (POO) introduce conceptos como clases, objetos, herencia y polimorfismo, lo que permite una mayor abstracción y reutilización de código.

## 5. ¿Cuáles son los pilares fundamentales de la Programación Orientada a Objetos (POO)?
Los pilares fundamentales de la Programación Orientada a Objetos (POO) son:
1. **Encapsulamiento**: Oculta los detalles internos de una clase y expone solo lo necesario a través de métodos públicos.
2. **Abstracción**: Permite representar conceptos complejos mediante modelos simplificados, enfocándose en los aspectos relevantes.
3. **Herencia**: Permite crear nuevas clases basadas en clases existentes, reutilizando y extendiendo su funcionalidad.
4. **Polimorfismo**: Permite que diferentes clases sean tratadas como instancias de la misma clase a través de una interfaz común, facilitando la flexibilidad y la extensibilidad del código.

## 6. ¿Qué son los modificadores de acceso y para qué se utilizan en una clase?
Los modificadores de acceso son palabras clave que se utilizan para controlar el acceso a los miembros de una clase. Los modificadores de acceso comunes son:
- **Público**: Acceso que permite ser utilizado por cualquier clase.
- **Privado**: Acceso privado; solo la clase que lo define puede acceder a él.
- **Protegido**: Acceso protegido; solo la clase que lo define y sus subclases pueden acceder.

## 7. ¿Qué es un constructor en una clase y cuál es su propósito?
Un constructor es un método especial que se llama cuando se crea un objeto de una clase. Su propósito es inicializar los miembros de la clase y establecer el estado inicial del objeto.

## 8. Definición de Clase y Objeto
- **Clase**: Es un modelo que define las propiedades (atributos) y el comportamiento (métodos) que tendrán a partir de ella.
- **Objeto**: Es una instancia de una clase, que contiene valores específicos para los atributos definidos en las clases. La clase es el diseño y el objeto es la realización del diseño.

## 9. ¿Qué es UML?
UML (Lenguaje Unificado de Modelado) es un lenguaje de modelado que se utiliza para crear diagramas y modelos de software. UML proporciona una forma estandarizada de representar la estructura y el comportamiento de un sistema, generalmente representado con diagramas. Existen varios tipos.

## 10. ¿Qué nos permite la modularidad?
La modularidad nos permite dividir un sistema en partes más pequeñas y manejables, conocidas como módulos, que pueden funcionar de manera independiente. Esto facilita la reutilización del código, mejora la legibilidad, evita colapsos en el sistema y hace que el código sea más mantenible. Además, permite una resolución más rápida de problemas al aislar componentes específicos.









# Examen
 

## Paso 1: Instalar `virtualenv` (opcional)

Si no tienes `virtualenv` instalado, puedes hacerlo con pip. Aunque desde Python  en adelante, puedes usar el módulo `venv` que viene incluido.

### Usando `virtualenv`

bash

Copiar código

`pip install virtualenv` 

## Paso 2: Crear un Entorno Virtual

### Usando `venv`

Para crear un entorno virtual con `venv`, ejecuta el siguiente comando:

bash

Copiar código

`python -m venv nombre_del_entorno` 

o, si usas Python 3:

bash

Copiar código

`python3 -m venv nombre_del_entorno` 

### Usando `virtualenv`

Si decidiste usar `virtualenv`, el comando es similar:

bash

Copiar código

`virtualenv nombre_del_entorno` 

## Paso 3: Activar el Entorno Virtual

Para empezar a usar el entorno virtual, necesitas activarlo.

### En Windows

bash

Copiar código

`nombre_del_entorno\Scripts\activate` 

### En macOS y Linux

bash

Copiar código

`source nombre_del_entorno/bin/activate` 

Después de activar el entorno, deberías ver el nombre del entorno al inicio de la línea de tu terminal.

## Paso 4: Instalar Dependencias

Con el entorno virtual activado, puedes instalar las bibliotecas que necesites usando pip. Por ejemplo:

bash

Copiar código

`pip install nombre_del_paquete` 

## Paso 5: Desactivar el Entorno Virtual

Cuando hayas terminado de trabajar, puedes desactivar el entorno virtual con el siguiente comando:

bash

Copiar código

`deactivate` 

## Consejos Adicionales

-   **Requisitos de Proyecto**: Es una buena práctica mantener un archivo `requirements.txt` en tu proyecto para documentar las dependencias. Puedes generar este archivo con:
    
    bash
    
    Copiar código
    
    `pip freeze > requirements.txt` 
    
-   **Instalar desde `requirements.txt`**: Para instalar las dependencias de un proyecto, usa:
    
    bash
    
    Copiar código
    
    `pip install -r requirements.txt` 
    

## Conclusión

Crear y utilizar entornos virtuales te ayudará a mantener tus proyectos de Python organizados y libres de conflictos de dependencias. ¡Feliz codificación!
