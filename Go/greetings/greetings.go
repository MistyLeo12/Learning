package greetings

import (
	"errors"
	"fmt"
	"math/rand"
	"time"
)

// Hello returns a greeting for the named person.
func Hello(name string) (string, error) {
	// If no name was given, return an error with a message.
	if name == "" {
		return "", errors.New("empty name")
	}
	// Create a name with a random format
	message := fmt.Sprintf(randomFormat(), name)
	return message, nil
}

// Hellos returns a map that associates each of the named people with a greeting message
func Hellos(names []string) (map[string]string, error) {
	// Initialize a map with the following syntax: make(map[key-type]value-type)
	// A map to associate names with messages
	messages := make(map[string]string)
	// Loop through slice of names, calling Hello to get a message for each name
	for _, name := range names {
		message, err := Hello(name)
		if err != nil {
			return nil, err
		}
		// In the map, associates the retrieved message with name
		messages[name] = message
	}
	return messages, nil
}

// init sets inital values for variables used in the function
func init() {
	rand.Seed(time.Now().UnixNano())
}

// randomFormat returns one of a set of greeting messages. The returned message is selected at random
func randomFormat() string {
	// A slice of message formats.
	formats := []string{
		"Hi, %v. Welcome!",
		"Great to see you, %v!",
		"What's up %v",
	}
	// Return a randomly selected message format by specifying a random index for the slice of formats
	return formats[rand.Intn(len(formats))]
}

/*

This function takes a name parameter whose type is string, and returns a string.
In Go, a function whose name starts with a capital letter can be called by a function not in the same package.
Called exported name.

 Hello(name string) string
 Function name -- Hello
 Parameter type -- name string
 Return type -- string

 := is decleration and initilization
*/
