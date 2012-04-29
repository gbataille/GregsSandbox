class Person(first_name: String) {
    println("Outer Constructor")
    def this(first_name: String, last_name: String) {
        this(first_name)
        println("Inside Constructor")
    }
    def talk() = println("Hi")
}

val bob = new Person("Bob")
val bobTate = new Person("Bob", "Tate")