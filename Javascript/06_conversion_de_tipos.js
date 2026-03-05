//Explicit Type Casting

const string = '42'
const integer = parseInt(string)
console.log(integer)
console.log(typeof integer)

const stringDecimal = '3.14'
const float = parseFloat(stringDecimal)
console.log(float)
console.log(typeof float)

const binary = '1010'
const decimal = parseInt(binary, 2)
console.log(decimal)
console.log(typeof decimal)


//Implicit Type Casting

const sum = '5' + 3
console.log(sum)

const sumWithBoolean = '3' + true
console.log(sumWithBoolean)

const sumWithNumber = 2 + true
console.log(sumWithNumber)

const stringValue  = '10'
const numberValue = 10
const booleanValue = true 
console.log('--------')
//Cuando es con strings, concatena
//Cuando es sin string simplemente suma

//Si hay al menos un string, JavaScript concatena.
//Si no hay ningún string, JavaScript realiza una suma.


console.log(stringValue + stringValue) //Concatena
console.log(stringValue + numberValue) //Concatena
console.log(stringValue + booleanValue) //Concatena
console.log(numberValue + stringValue) //Concatena
console.log(numberValue + numberValue) //Suma
console.log(numberValue + booleanValue) //Suma
console.log(booleanValue + stringValue) //Concatena
console.log(booleanValue + numberValue) //Suma
console.log(booleanValue + booleanValue) //Suma 
