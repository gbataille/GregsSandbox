var carPrototype = {
    gas: function gas(amount) {
      amount = amount || 10;
      this.mph += amount;
      return this;
    },
    brake: function brake(amount) {
      amount = amount || 10;
      this.mph = ((this.mph - amount) < 0)? 0 : this.mph - amount;
      return this;
    },
    color: 'pink',
    direction: 0,
    mph: 0
  },

  car = function car(options) {
    return $.extend(Object.create(carPrototype), options);
  },

  extendCar = function extendCar(options) {
    return $.extend({}, carPrototype, options);
  },

  myCar = car({
    color: 'red'
  }),
  myExtendCar = extendCar({
    color: 'red'
  });

console.log(myCar);
console.log(myExtendCar);

test('Flyweight factory with cloning', function () {
  ok(myCar.__proto__.gas,
    'Prototype methods are shared.');
});

carPrototype.mph = 10;

test('myCar mph was changed due to the prototype update', function () {
  equal(10, myCar.mph, 'myCar updated through it\'s prototype');
});
test('myExtendCar mph was not changed since it is not using the prototype', function () {
  equal(0, myExtendCar.mph, 'myExtendCar not changed as it got a copy of the' +
    'prototype, not the prototype itself');
});

carPrototype.color = 'blue';

test('myCar color was not changed since it overrides the prototype value', function () {
  equal('red', myCar.color, 'myCar color not changed as overriding its proto');
});

// This is what the output gives you (as shown in DevTools for example)

// Object {color: "red", gas: function, brake: function, color: "pink", direction: 0…}
//   color: "red"
//   __proto__: Object
//     brake: function brake(amount) {
//     color: "pink"
//     direction: 0
//     gas: function gas(amount) {
//     mph: 0
//     __proto__: Object
// 
// Object {gas: function, brake: function, color: "red", direction: 0, mph: 0}
//   brake: function brake(amount) {
//   color: "red"
//   direction: 0
//   gas: function gas(amount) {
//   mph: 0
//   __proto__: Object
//     __defineGetter__: function __defineGetter__() { [native code] }
//     __defineSetter__: function __defineSetter__() { [native code] }
//     ...
