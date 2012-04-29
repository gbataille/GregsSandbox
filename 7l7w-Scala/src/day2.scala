/**
 * Created by IntelliJ IDEA.
 * User: gregou
 * Date: 12/4/11
 * Time: 9:35 AM
 * To change this template use File | Settings | File Templates.
 */
/*Total Size of a list of strings*/
val myList = List("Greg", "mange", "du", "chocolat")

val totalSizeFolded = myList.foldLeft(0)((sum, nextElem) => sum + nextElem.size)
val totalSize = (0 /: myList) {(sum, nextElem) => sum + nextElem.size}

println(totalSize)
println(totalSizeFolded)

trait Censor {
  val censoredWords = Map("darn" -> "beans", "shoot" -> "pucky")

  def applyCensorShip(text:String) {
    val words = text.split(" ")
    var censoredText = ""
    words.foreach(word => {
      if (censoredWords.keySet.contains(word.toLowerCase)) {
        censoredText += censoredWords(word.toLowerCase)
      } else {
        censoredText += word
      }
      censoredText += " "
    })
    println(censoredText)
  }
}

class Comment(text: String) extends Censor {
  val comment = text
}

val myComment = new Comment("Shoot ! What a darn mess !")
myComment.applyCensorShip(myComment.comment)