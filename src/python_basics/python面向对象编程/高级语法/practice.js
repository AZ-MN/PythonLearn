const isValue = new Date();
console.log(isValue)
const expectedValue = isValue.toISOString().split('T')[0];
console.log(expectedValue)