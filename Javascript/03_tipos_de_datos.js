//Tenemos 10 tipos de datos, primitivos y complejos
//Primitivos: string, number, boolean, null, undefinied, symbol, bigint
//Complejos: object, array, function

//PRIMITIVIOS

//string, son cadenas de caracteres
let nombre = 'Tere'

//number, indican un numero
let edad = '25'

//boolean, sirven para indicar si algo es verdadero o falso
let esMayorDeEdad = true

//null, indica que no hay nada y lo define el programador
let noHayValor = null

//undefined, indica que no hay nada y nos lo da javascript
let noDefinido = undefined

//symbol, indica si algo es unico 
let simboloUnico = Symbol('único')

//bigint, nos permite almacenar numeros muy grandes
let numeroGrande = 2n


//COMPLEJOS

//object, funcional para describir un objeto con las caracteristicas que decidamos
let carro = {
    marca: 'Tesla',
    modelo: 'Model S'
}

//array, conjunto o grupo de algo
let frutas = ['manzana', 'banano', 'uvas']

//function, bloques de codigo reutilizables que ejecutan una tarea específica
function saludar () {}