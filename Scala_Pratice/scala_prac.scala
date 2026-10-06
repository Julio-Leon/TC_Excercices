import scala.util.Try

object prac_1 extends App {

  // Task 1

  var employeeSalaries = List(400, 230, 500, 600, 600, 700)

  val increasedSalaries: List[Int] = employeeSalaries.map(salary => (salary * 1.1).toInt)

  println(increasedSalaries)

  val filteredList = increasedSalaries.filter(salary => salary > 600)

  println(filteredList)

  val departments = Set(
    "Engineering",
    "Sales",
    "Marketing",
    "Engineering",
    "Sales",
    "HR"
  )

  println(departments)

  // The duplicates get removed.


  var workers = Map(
    1 -> "Math",
    2 -> "English",
    3 -> "Social"
  )

  workers.foreach(worker => println(worker))

  for (i <- 1 to workers.size) {
    println(workers(i))
  }


  // Task 2

  val departments2 = List("HR", "Math", "Finance", "Sales")

  val categorizedDepartments = departments2.map(department => {
    department match {
      case "Engineering" => "Math"
      case "HR" => "Business"
      case "Finance" => "Math"
      case "Legal" => "Business"
      case "Sales" => "Business"
      case _ => "Unknown"
    }
  })
  println(categorizedDepartments)


  // Task 3

  val salaries2 = List(500, 600, None, 300, 400, 200)
  val salaries3 = List(Some(500), Some(600), None, Some(300), Some(400), Some(200))

  println(salaries2)

  val filteredSalaries2 = salaries2.map(salary => if (salary != None) salary else 0)
  val filteredSalaries3 = salaries3.map(salary => salary.getOrElse(0))

  println(filteredSalaries2)
  println(filteredSalaries3)

  // It helps prevent NullPointerExceptions and makes missing data easier to handle safely.
  // Option also works naturally with Scala functions like map, filter, and getOrElse.
  // This makes data pipelines more predictable, readable, and resilient when dealing with missing values.

  // Task 4

  trait Validator {
    def validateSalary(): Boolean
  }

  case class EmployeeValidator(salary: Int, name: String) extends Validator {
    def validateSalary(): Boolean = {
      salary >= 0
    }
  }

  val employee1 = EmployeeValidator(20, "Julito")
  val employee2 = EmployeeValidator(-2, "Roger")
  val employee3 = EmployeeValidator(0, "Anas")

  println(employee1.validateSalary())
  println(employee2.validateSalary())
  println(employee3.validateSalary())


  // Task 5

  var pracList = List("10","20","abc","40","not_available")

  var accepted: List[String] = pracList.filter(item => Try(item.toInt).isSuccess)
  var acceptedInts: List[Int] = accepted.map(item => item.toInt)

  var rejected = pracList.filter(item => Try(item.toInt).isFailure)

  println(pracList)
  println(accepted)
  println(acceptedInts)
  println(rejected)
  println(rejected.length)




}
