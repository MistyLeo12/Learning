package main

import (
	"errors"
	"fmt"
)

// Tree struc to define the tree
type Tree struct {
	Value  int
	Left   *Tree
	Right  *Tree
	Repeat int
	Parent *Tree
}

// Insert method to add values to the tree
func (t *Tree) Insert(v int) error {
	switch {
	case v == t.Value:
		t.Repeat++

		// if val is less than val at the node and if Left is empty, add node here only
		// if left !empty--recursion
	case v < t.Value:
		if t.Left == nil {
			t.Left = &Tree{v, nil, nil, 1, t}
			return nil
		}
		return t.Left.Insert(v)

		// if val is greater than the val at the node and if right is empty, add node
		// if right !empty--recursion
	case v > t.Value:
		if t.Right == nil {
			t.Right = &Tree{v, nil, nil, 1, t}
			return nil
		}
		return t.Right.Insert(v)
	}

	return nil
}

// Search for a val in binary tree return (int, bool)
// *Tree in return is the sub tree with root node as Value
func (t *Tree) Find(v int) (int, *Tree, bool) {
	switch {
	case v == t.Value:
		return t.Repeat, t, true

	case v < t.Value:
		if t.Left == nil {
			return 0, nil, false
		}
		return t.Left.Find(v)

	case v > t.Value:
		if t.Right == nil {
			return 0, nil, false
		}
		return t.Right.Find(v)
	}

	return 0, nil, false
}

// Maximum Function for returning max integer in the tree
func (t *Tree) Maximum() int {

	if t.Right == nil {
		return t.Value
	}
	return t.Right.Maximum()

}

// Minimum Function for returning min integer in the tree
func (t *Tree) Minimum() int {

	if t.Left == nil {
		return t.Value
	}
	return t.Left.Minimum()
}

// Delete a value from binary tree
func (t *Tree) Delete(v int) error {
	_, tree, present := t.Find(v)

	if !present {
		return errors.New("Value is not in the tree")
	}
	return tree.Replace(v)
}

// Replace replace a value with another
func (t *Tree) Replace(v int) error {
	if t.Right == nil && t.Left == nil {
		t.Parent = nil
		return nil
	}

	switch {
	case t.Right == nil:
		t.Parent.Left = t.Left
	case t.Left == nil:
		t.Parent.Right = t.Right
	default:
		// When subtree has a val which is going to be deleted but has a left and right subtree
		// Find min in right subtree and replace it with to be deleted value
		min := t.Right.Minimum()
		t.Value = min
		t.Right.Delete(min)
	}

	return nil

}

// BinaryTree struct which makes a binary tree out of the integer array
func BinaryTree(numbers []int) *Tree {
	root := numbers[0]
	tree := Tree{root, nil, nil, 0, nil}
	for _, value := range numbers[1:] {
		tree.Insert(value)
	}
	return &tree
}

type Traversal interface {
	Initialize() []int
	PrintTraversal(stack []*Tree, res []int, visited map[int]bool) []int
	util(stack []*Tree, res []int, visited map[int]bool) ([]int, []*Tree)
}

type defImplement struct {
}

func (*defImplement) Initialize() []int {
	return []int{}
}

func (*defImplement) PrintTraversal(stack []*Tree, res []int, visited map[int]bool) []int {
	return []int{}
}

func (*defImplement) util(stack []*Tree, res []int, visited map[int]bool) ([]int, []*Tree) {
	visited[stack[len(stack)-1].Value] = true
	res = append(res, stack[len(stack)-1].Value)
	stack = stack[:len(stack)-1]
	return res, stack
}

// Inorder DFS -- intialize struct with defImplement as Traversal type to  inherit util implementation
type Inorder struct {
	tree *Tree
	Traversal
}

func (ord *Inorder) Initialize() []int {
	stack := []*Tree{}
	stack = append(stack, ord.tree)
	result := []int{}
	visited := map[int]bool{}
	return ord.PrintTraversal(stack, result, visited)

}

func (ord *Inorder) PrintTraversal(stack []*Tree, res []int, visited map[int]bool) []int {
	if len(stack) == 0 {
		return res
	}

	subTree := stack[len(stack)-1] // acessing last element
	switch {
	case subTree.Left != nil && visited[subTree.Left.Value] != true:
		stack = append(stack, subTree.Left)
		return ord.PrintTraversal(stack, res, visited)

	case subTree.Right != nil && visited[subTree.Right.Value] != true:

		res, stack = ord.util(stack, res, visited)
		stack = append(stack, subTree.Right)
		return ord.PrintTraversal(stack, res, visited)

	default:
		res, stack = ord.util(stack, res, visited)
		return ord.PrintTraversal(stack, res, visited)

	}

}

type Postorder struct {
	tree *Tree
	Traversal
}

func (ord *Postorder) Initialize() []int {
	stack := []*Tree{}
	stack = append(stack, ord.tree)
	result := []int{}
	visited := map[int]bool{}
	return ord.PrintTraversal(stack, result, visited)

}

// PrintTraversal to print traversal of the binary tree
func (ord *Postorder) PrintTraversal(stack []*Tree, res []int, visited map[int]bool) []int {
	if len(stack) == 0 {
		return res
	}

	subTree := stack[len(stack)-1] // acessing last element
	switch {
	case subTree.Left != nil && visited[subTree.Left.Value] != true:
		stack = append(stack, subTree.Left)
		return ord.PrintTraversal(stack, res, visited)

	case subTree.Right != nil && visited[subTree.Right.Value] != true:

		stack = append(stack, subTree.Right)
		return ord.PrintTraversal(stack, res, visited)

	default:
		res, stack = ord.util(stack, res, visited)
		return ord.PrintTraversal(stack, res, visited)

	}

}

type Preorder struct {
	tree *Tree
	Traversal
}

func (ord *Preorder) Initialize() []int {
	stack := []*Tree{}
	stack = append(stack, ord.tree)
	result := []int{ord.tree.Value}
	visited := map[int]bool{
		ord.tree.Value: true,
	}

	return ord.PrintTraversal(stack, result, visited)

}

func (ord *Preorder) PrintTraversal(stack []*Tree, res []int, visited map[int]bool) []int {
	if len(stack) == 0 {
		return res
	}

	subTree := stack[len(stack)-1] // acessing last element
	switch {
	case subTree.Left != nil && visited[subTree.Left.Value] != true:

		res = append(res, subTree.Left.Value)
		visited[subTree.Left.Value] = true
		stack = append(stack, subTree.Left)
		return ord.PrintTraversal(stack, res, visited)

	case subTree.Right != nil && visited[subTree.Right.Value] != true:
		res = append(res, subTree.Right.Value)
		visited[subTree.Right.Value] = true
		stack = append(stack, subTree.Right)
		return ord.PrintTraversal(stack, res, visited)

	default:
		stack = stack[:len(stack)-1]
		return ord.PrintTraversal(stack, res, visited)

	}

}

func main() {

	numbers := []int{78, 2, 1, 5, 88, 12, 444, 89, 124, 122, 89, 1003, 5869, 410, 555}

	tree := BinaryTree(numbers)

	f := Inorder{tree, &defImplement{}}
	fmt.Printf("Inorder Tree traversal %v\n", f.Initialize())

	post := Postorder{tree, &defImplement{}}
	fmt.Printf("Post Tree traversal %v\n", post.Initialize())

	pre := Preorder{tree, &defImplement{}}
	fmt.Printf("Pre Tree traversal %v\n", pre.Initialize())

}
