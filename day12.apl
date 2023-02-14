#!/usr/bin/dyalogscript

    ti ← ⊃⎕NGET 'data/day12ti.txt' 1
    pi ← ⊃⎕NGET 'data/day12.txt' 1
    ⎕IO ← 0
    ⍝]box on -style=min
    ⍝]rows on -style=wrap
    
    cmat ← ↑ti
    spoint ← ⊃⍸'S'=cmat
    epoint ← ⊃⍸'E'=cmat
    getelev ← {⍵='S': 0 ⋄ ⍵='E': 25 ⋄ 'abcdefghijklmnopqrstuvwxyz'⍳⍵}
    emat ← getelev¨cmat
    valpos ← ,⍳⍴cmat ⍝ valid coordinates in the matrix

    neighbors ← {
        ⍝ given a coordinate point, return possible neighbors
        ce ← (⊂⍵)⊃emat      ⍝ current elevation via reach indexing
        allns ← ⍵∘+¨(1 0) (0 1) (¯1 0) (0 ¯1)  
        ns←allns∩valpos ⍝ return possible NSEW neighbors 
        es ← {(⊂⍵)⊃emat}¨ns ⍝ get the neighbors' elevations
        emask ← {1≥(⍵-ce)}¨es ⍝ target - current elev is no more than 1!!!
        emask/ns ⍝ filter for valid elevations
    }

    md ← {(|(⊃⍺ - ⊃⍵)) + (|(1⊃⍺ - 1⊃⍵))} ⍝ manhattan distance
    
    dijkstra ← {
        frontier ← ⊃⍵
        camefrom ← 1⊃⍵
        costsofar ← 2⊃⍵
        0=≢frontier: 1⊃⍵
        
        current ← ⊃frontier
        ns ← neighbors current
        nextnotin ← ns ~ ⊃¨costsofar
        costs ← costsofar
        ncosts ← (↑next), costs
        cf ← next,⍤0 1 ⊢ ⊂2↑⊃↓current
        newfrontier ← ncosts⍪1↓frontier
        newfrontier
        sortedfrontier ← (2)(⊢⌷⍨∘⊂∘⍋⌷⍤1)newfrontier
        newcamefrom ← camefrom,↓cf
        (⊂sortedfrontier), ⊂newcamefrom
    }

    camefrom ← dijkstra⍣1 ⊢ (spoint 0) (⊂spoint 'None') (⊂spoint 0) ⍝ {0=≢⊃⍵}
    ]display camefrom
    
    cfmat ← (⍴cmat)⍴0
    cf2 ← 'N'@(⊂0 0) ⊢ cfmat
    (⊂0 1)⊃cf2
    
    findpath ← {
        ⍵
        current ← ⊃⍵
        path ← 1⊃⍵
        camefrom ← 2⊃⍵
        (current)≡(spoint): 1⊃⍵
        
        np ← path,⊂current
        (⊃((0⌷⍉camefrom))⍳⊂current)
        nc ← 1⊃(⊃((0⌷⍉camefrom))⍳⊂current)⌷camefrom
        nc np camefrom
    }
    
    y ← findpath⍣{(⊃⍵)≡(spoint)} ⊢ (epoint '' (↑(1⊃camefrom)))
    ≢1⊃y
