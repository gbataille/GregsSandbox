Todos.TodosController = Ember.ArrayController.extend({
  actions: {
    createTodo: function () {
      // Get the todo title set by the "New Todo" text field
      var title = this.get('newTitle');
      if (!title.trim()) { return; }

      // Create the new Todo model
      var todo = this.store.createRecord('todo', {
        title: title,
        isCompleted: false
      });

      // Clear the "New Todo" text field
      this.set('newTitle', '');

      // Save the new model
      todo.save();
    },
    clearCompleted: function () {
      var completed = this.filterBy('isCompleted', true);
      completed.invoke('deleteRecord');
      completed.invoke('save');
    }
  },

  remaining: function () {
    console.log("remaining");
    return this.filterBy('isCompleted', false).get('length');
  }.property('@each.isCompleted'),

  inflection: function () {
    var remaining = this.get('remaining');
    console.log("inflection");
    return remaining === 1 ? 'item' : 'items';
  }.property('remaining'),

  completed: function () {
    return this.filterBy('isCompleted', true).get('length');
  }.property('@each.isCompleted'),

  hasCompleted: function () {
    return this.get('completed') > 0;
  }.property('completed'),

  allAreDone: function (key, value) {
    if (value === undefined) {
      return !!this.get('length') && this.everyBy('isCompleted', true);
    } else {
      this.setEach('isCompleted', value);
      this.invoke('save');
      return value;
    }
  }.property('@each.isCompleted')
});