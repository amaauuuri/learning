// 1. Tipo entero y decimal
const entero = 42
const decimal = 3.14
console.log(typeof entero, typeof decimal)

// 2. Notacion cientifica
const cientifico = 5e3

// 3. Infinitos y Nan (not a number) no es un numero
const infinito = Infinity 
const noEsUnNumero = NaN


//Operaciones aritmeticas

// 1. Suma, resta, multiplicacion y division
const suma = 3 + 4
const resta = 4 - 3
const multiplicacion = 4 * 5
const division = 16 / 2

// 2.  Modulo y exponenciacion
const modulo = 15 % 8 
const exponenciacion = 2 ** 3

// Precision
const resultado = 0.1 + 0.2
console.log(resultado)
console.log(resultado.toFixed(1))
console.log(resultado === 0.3)   //sirve para validar tanto el numero como el tipo de dato

// Operaciones avanzadas
const raizCuadrada = Math.sqrt(625)
const valorAbsoluto = Math.abs(-7)
const aleatorio = Math.random()
console.log(raizCuadrada)
console.log(valorAbsoluto)
console.log(aleatorio)
