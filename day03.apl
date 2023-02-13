#!/usr/bin/dyalogscript

    ti ← ⊃⎕NGET 'data/day03ti.txt' 1
    pi ← ⊃⎕NGET 'data/day03.txt' 1

    i2p ← {
        'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'⍳⊃∊∩/↓2 ((≢⍵)÷2)⍴⍵
    }

    ⎕ ← +/i2p¨pi

    part2 ← {
        ⍺ ← 0        ⍝ Left arg defaults to 0 if not given
        0=≢⍵: ⍺      ⍝ If right arg is empty, return left arg
        
        p ← ⊃'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'⍳⊃∩/3↑⍵
        (⍺+p)∇3↓⍵   ⍝ Add head to acc, recur over tail
    }

    ⎕ ← part2 pi
