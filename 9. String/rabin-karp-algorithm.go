package main

import "fmt"

func rabinKarp(text, pattern string) int {
	textLen := len(text)
	patternLen := len(pattern)
	if patternLen > textLen {
		return -1
	}

	base := 256 // number of characters
	mod := 101  // prime number

	h := precomputedPower(patternLen, base, mod)

	pHash, tHash := 0, 0
	// Calculate initial hash of window
	for i := range patternLen {
		pHash = (base*pHash + int(pattern[i])) % mod
		tHash = (base*tHash + int(text[i])) % mod
	}

	for i := 0; i <= textLen-patternLen; i++ {
		if pHash == tHash {
			if pattern == text[i:i+patternLen] {
				return i
			}
		}

		if i < textLen-patternLen {
			// newHash = (base*(oldHash−leadingChar*h) + trailingChar) % mod
			tHash = (base*(tHash-int(text[i])*h) + int(text[i+patternLen])) % mod
			// Modulus operator can return negative so make hash positive
			// Eg: x := -5 % 101  // result is -5, not 96
			// -5 + 101 = 96
			// Hash should be 0 <= hash < mod
			if tHash < 0 {
				tHash += mod
			}
		}
	}
	return -1
}

func precomputedPower(patternLen, base, mod int) int {
	// h = (base^(m−1)) % mod
	h := 1
	for i := 0; i < patternLen-1; i++ {
		h = (h * base) % mod
	}
	return h
}

func main() {
	text := "ABCCDDAEFG"
	pattern := "CDD"

	idx := rabinKarp(text, pattern)
	if idx != -1 {
		fmt.Printf("Pattern found at index %d\n", idx)
	} else {
		fmt.Println("Pattern not found")
	}
}
