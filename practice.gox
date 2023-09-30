package main

import (
	"fmt"

	"rsc.io/quote/v4"
)

var age int = 10
var name string = "yo"

type Person struct {
	Name FullName
	Age  int
}

type FullName struct {
	firstname string
	lastname  string
}

var Tom Person = Person{FullName{"tom", "nguyen"}, 20}

func (p Person) Speak() {
	fmt.Println("hello from" + p.Name.firstname)
}
func doSomething(a int, b int) int {
	return a + b
}
func incrementAge(a *int) {
	*a = *a + 1
}
func main() {
	age = 20
	name = "bob"
	fmt.Println(quote.Go())
	fmt.Println(name)
	fmt.Println(Tom.Name.firstname)
	fmt.Println(doSomething(1, 2))
	incrementAge(&age)
	fmt.Println(&age)
	fmt.Println(*&age)
	Tom.Speak()
}
