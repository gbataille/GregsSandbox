class PlayersChoice(val x: Int, val y: Int) {
    if((x > 3) || (x < 0) || (y > 3) || (y < 0)) {
        println("Error x and y must be between 1 and 3")
    }

    val xval = x
    val yval = y
}

class XChoice (override val x:Int, override val y: Int) extends PlayersChoice(x,y) {
    val choice = "X"
}


class YChoice (override val x:Int, override val y: Int) extends PlayersChoice(x,y) {
    val choice = "Y"
}

val x1 = new XChoice(1,1)
println(x1.choice)

object TicTacToe {
    def validate() = println("Test")
}


TicTacToe.validate()
