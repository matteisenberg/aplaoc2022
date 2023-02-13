#!/usr/bin/dyalogscript

ti ← ⊃⎕NGET 'day02ti.txt' 1
pi ← ⊃⎕NGET 'day02.txt' 1

part1 ← {
    plays ← ,'ABC'∘.{⍺,' ',⍵}'XYZ' ⍝ ravel the product of XYZ and ABC
    idx ← ⍵∘≡¨plays
    scores ← 4 8 3 1 5 9 7 2 6
    idx/scores
}

⎕ ← +/part1¨pi

part2 ← {
    plays ← ,'ABC'∘.{⍺,' ',⍵}'XYZ' ⍝ ravel the product of XYZ and ABC
    idx ← ⍵∘≡¨plays
    scores ← 3 4 8 1 5 9 2 6 7
    idx/scores
}

⎕ ← +/part2¨pi