var testProto = {
  fun: function () { return 2;},
  aString: "aString",
  aSecondString: 'aSecondString',
  anArray: [1, 2, 3]
},

  testObject1 = $.extend({}, testProto),
  testObject2 = $.extend({}, testProto),
  testObject3 = $.extend(true, {}, testProto);

test('Both objects have access to the aString through the copy of the proto', function () {
  ok(testObject1.aString,
    'Prototype properties are shared.');
  ok(testObject2.aString,
    'Prototype properties are shared.');
});

//The entire field is replaced by a new string
//Strings are immutable in JS anyway!
testObject1.aString = "anotherString";

test('They each have a copy. Changing the property of one does not change the other',
    function () {
      equal(testObject2.aString, 'aString', 'the second object is not touched');
    });

//Here I don't change the field to point to a new array but rather change the content
//of an existing array.
//The first and second object actually each have a copy of the reference to the array
//not a copy of the array itself
testObject1.anArray[1] = 5;

test('But the copy is shallow, changing an element in the array changes both the objects',
    function () {
      equal(testObject2.anArray[1], 5, 'The second object is changed too');
    });

test('Passing a boolean true as first argument to extend indicates you want a deep copy',
    function () {
      equal(testObject3.anArray[1], 2, 'The third object is not changed');
    });
