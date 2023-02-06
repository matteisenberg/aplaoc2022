#!/usr/bin/dyalogscript

ti ← ⊃⎕NGET 'day01ti.txt' 1
pi ← ⊃⎕NGET 'day01.txt' 1

part1 ← {⌈/+/¨⍎¨¨(''∘≢¨⍵)⊆⍵} pi
⎕ ← part1

part2 ← {sums ← (+/¨⍎¨¨(''∘≢¨⍵)⊆⍵) ⋄ +/3↑sums[⍒sums]} pi
⎕ ← part2