package greetings

import (
	"regexp"
	"testing"
)

// TestHelloName calls greetings.Hello with a name, checking for valid return val
func TestHelloName(t *testing.T) {
	name := "Thad"
	want := regexp.MustCompile(`\b` + name + `\b`)
	msg, err := Hello("Thad")
	if !want.MatchString(msg) || err != nil {
		t.Fatalf(`Hello("Thad") = %q, %v, want match for %#q, nil`, msg, err, want)
	}
}

// TestHelloEmpty calls greetings.Hello with an empty string, checking for error
func TestHelloEmpty(t *testing.T) {
	msg, err := Hello("")
	if msg != "" || err == nil {
		t.Fatalf(`Hello("") = %q, %v, want "", error`, msg, err)
	}
}

/*
Test function names have the form TestName, where Name is specific to the test.
Also, test functions take a pointer to the testing package's testing.T as a parameter.
You use this parameter's methods for reporting and logging from your test.
*/
