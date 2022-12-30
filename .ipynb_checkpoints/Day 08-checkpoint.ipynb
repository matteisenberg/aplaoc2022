{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5aabe45c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<pre class=\"language-APL\">Was ON -style=min\n",
       "</pre>"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "]box on -style=min"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f17a582b",
   "metadata": {},
   "outputs": [],
   "source": [
    "ti ← ⊃⎕NGET 'day08ti.txt' 1\n",
    "pi ← ⊃⎕NGET 'day08.txt' 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "438a06fe",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "⍝ ⍉grid ⍝ north\n",
    "⍝ ⌽grid ⍝ east\n",
    "⍝ ⌽⍉grid ⍝ south"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "7d8de41f",
   "metadata": {},
   "outputs": [],
   "source": [
    "]dinput\n",
    "vis ← {\n",
    "    ⍺ ← '' '' ⍝ \"visible\" \"seen\"\n",
    "    0=≢⍵: ⍺   ⍝ If right arg is empty, return left arg\n",
    "    \n",
    "    visible ← 1⊃⍺\n",
    "    seen ← 2⊃⍺\n",
    "    \n",
    "    0=≢seen: visible,1 (seen,⊃⍵)∇1↓⍵ ⍝ if seen is empty, tree is visible; add current tree to seen    \n",
    "        (visible,∧/seen<⊃⍵) (seen,⊃⍵)∇1↓⍵ ⍝ otherwise, tree is visible if greater than seen\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "id": "2ce6b3ea",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<pre class=\"language-APL\">1713\n",
       "</pre>"
      ]
     },
     "execution_count": 111,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "⍝ part 1\n",
    "grid ← ⍎¨↑pi\n",
    "west ← ↑⊃¨vis¨↓grid\n",
    "north ← ⍉↑⊃¨vis¨↓⍉grid\n",
    "east ← ⌽↑⊃¨vis¨↓⌽grid \n",
    "south ← ⍉⌽↑⊃¨vis¨↓⌽⍉grid \n",
    "all ← west ∨ north ∨ east ∨ south\n",
    "≢(∊all)/∊↓grid"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 167,
   "id": "cac086e0",
   "metadata": {},
   "outputs": [],
   "source": [
    "]dinput\n",
    "vis2 ← {\n",
    "    ⍺ ← '' '' ⍝ \"viewing distances\" \"seen\"\n",
    "    0=≢⍵: ⍺   ⍝ If right arg is empty, return left arg\n",
    "    \n",
    "    vds ← 1⊃⍺\n",
    "    seen ← 2⊃⍺\n",
    "    \n",
    "    0=≢seen: vds,0 (seen,⊃⍵)∇1↓⍵\n",
    "        (vds,⊂(0 (1⊃⍵) vd ⌽seen)) (seen,⊃⍵)∇1↓⍵ \n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 192,
   "id": "e74047df",
   "metadata": {},
   "outputs": [],
   "source": [
    "]dinput\n",
    "vd ← {\n",
    "    ⍺ ← 0 '' ⍝ View Distance, the tree height\n",
    "    0=≢⍵: 1⊃⍺   ⍝ If right arg is empty, return left arg\n",
    "    \n",
    "    vd ← 1⊃⍺\n",
    "    th ← 2⊃⍺\n",
    "    \n",
    "    th > ⊃⍵: (vd + 1) th∇1↓⍵ \n",
    "        vd + 1\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 191,
   "id": "eb09ae2b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<pre class=\"language-APL\">3\n",
       "</pre>"
      ]
     },
     "execution_count": 191,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "(0 5) vd (3 5 3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 196,
   "id": "4c42413d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<pre class=\"language-APL\">268464\n",
       "</pre>"
      ]
     },
     "execution_count": 196,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "⍝ part 2\n",
    "grid ← ⍎¨↑pi\n",
    "west ← ↑⊃¨vis2¨↓grid\n",
    "north ← ⍉↑⊃¨vis2¨↓⍉grid\n",
    "east ← ⌽↑⊃¨vis2¨↓⌽grid \n",
    "south ← ⍉⌽↑⊃¨vis2¨↓⌽⍉grid \n",
    "all ← ×/west north east south\n",
    "⌈/∊all"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Dyalog APL",
   "language": "apl",
   "name": "dyalog-kernel"
  },
  "language_info": {
   "file_extension": ".apl",
   "mimetype": "text/apl",
   "name": "APL"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
