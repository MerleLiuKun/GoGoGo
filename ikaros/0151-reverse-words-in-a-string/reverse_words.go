package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(reverseWords("  hello world!  "))
}

func reverseWords(s string) string {
	array := strings.Split(strings.TrimSpace(s), " ")

	length := len(array)
	words := make([]string, 0, length)

	for i := length - 1; i >= 0; i-- {
		if len(array[i]) != 0 {
			words = append(words, array[i])
		}
	}

	return strings.Join(words, " ")
}
