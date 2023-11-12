# Patrones Creacionales
link repo: https://github.com/anagarciasaiz/entrega
## Justificacion uso builder:
Al implementar el patrón Builder, se logra una separación clara entre el proceso de construcción y la representación final del objeto. Algunas razones clave para justificar su uso y cómo contribuye a la robustez y adaptabilidad del sistema:

-Separación de responsabilidades: Permite dividir la construcción del objeto complejo (pizzas) de su representación final, facilitando la gestión del código.

-Flexibilidad en la construcción: Los métodos de construcción permiten personalizar pizzas paso a paso, adaptándose a diferentes preferencias de los clientes.

-Adaptabilidad:La interfaz común y la flexibilidad del Builder permiten la introducción de nuevos tipos de pizzas o modificaciones sin afectar al código existente.

-Recomendaciones personalizadas:Facilita la implementación de un sistema de recomendaciones basadas en elecciones previas del cliente, mejorando la experiencia del usuario.

-Persistencia y manejo de datos:Simplifica la persistencia de datos en un formato como CSV, contribuyendo a la integridad de los datos y permitiendo futuras ampliaciones.

-Escalabilidad:El diseño permite la fácil incorporación de nuevos tipos de pizzas, ingredientes o cambios en el proceso de construcción, haciendo el sistema altamente escalable.

-Facilidad de mantenimiento: El código resultante es modular y fácil de mantener, permitiendo cambios y ampliaciones sin afectar otras partes del sistema.

En resumen, el patrón Builder ofrece una solución robusta y adaptable para la creación de pizzas personalizadas, destacando por su flexibilidad, escalabilidad y capacidad para gestionar cambios en el sistema de manera eficiente.

Otros patrones creacionales no serían tan adecuados por las siguientes razones:

-Factory Method:El patrón Factory Method podría ser limitado para la creación de pizzas personalizadas, ya que se centra en la creación de una instancia de una clase particular. No proporciona la misma flexibilidad para la construcción paso a paso y la personalización de las pizzas según las preferencias del cliente.

-Abstract Factory: Aunque el patrón Abstract Factory maneja la creación de familias de objetos relacionados, su estructura podría ser más rígida y menos adaptable a las diversas combinaciones de ingredientes y preferencias de los clientes en el contexto de las pizzas personalizadas.

-Singleton:El patrón Singleton, que asegura una única instancia de una clase, no es apropiado para la creación de pizzas personalizadas, ya que la pizzería necesita manejar múltiples pedidos y pizzas simultáneamente. La limitación a una única instancia podría ser restrictiva.

-Prototype:El patrón Prototype, basado en la clonación de objetos existentes, podría no ser eficiente ni flexible para la creación de pizzas personalizadas, donde cada pizza puede tener combinaciones únicas de ingredientes y no se beneficia de la clonación
