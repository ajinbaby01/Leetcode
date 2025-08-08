package main

import "fmt"

// Set represents a set data structure.
type Set struct {
	elements map[string]struct{}
}

// NewSet creates and returns a new empty Set.
func NewSet() *Set {
	return &Set{
		elements: make(map[string]struct{}),
	}
}

// Add adds an element to the set.
func (s *Set) Add(element string) {
	s.elements[element] = struct{}{}
}

// Remove removes an element from the set.
func (s *Set) Remove(element string) {
	delete(s.elements, element)
}

// Contains checks if an element exists in the set.
func (s *Set) Contains(element string) bool {
	_, exists := s.elements[element]
	return exists
}

// Size returns the number of elements in the set.
func (s *Set) Size() int {
	return len(s.elements)
}

// ToSlice returns all elements of the set as a string slice.
func (s *Set) ToSlice() []string {
	keys := make([]string, 0, len(s.elements))
	for k := range s.elements {
		keys = append(keys, k)
	}
	return keys
}

func main() {
	mySet := NewSet()

	mySet.Add("apple")
	mySet.Add("banana")
	mySet.Add("orange")
	mySet.Add("apple") // Adding a duplicate has no effect

	fmt.Println("Set elements:", mySet.ToSlice())
	fmt.Println("Set size:", mySet.Size())

	fmt.Println("Contains 'banana'?", mySet.Contains("banana"))
	fmt.Println("Contains 'grape'?", mySet.Contains("grape"))

	mySet.Remove("banana")
	fmt.Println("Set elements after removing 'banana':", mySet.ToSlice())
	fmt.Println("Set size after removing 'banana':", mySet.Size())
}
