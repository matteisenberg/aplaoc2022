{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "e72f5466",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<pre class=\"language-APL\">┌→────────────────┐\n",
       "│Was ON -style=max│\n",
       "└─────────────────┘\n",
       "</pre>"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "]box on -style=max"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f6febfd1",
   "metadata": {},
   "outputs": [],
   "source": [
    "ti ← ⊃⎕NGET 'day04ti.txt'1\n",
    "pi ← ⊃⎕NGET 'day04.txt'1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 181,
   "id": "9a6aa691",
   "metadata": {},
   "outputs": [],
   "source": [
    "mat ← ⎕CSV ('\\W+'⎕R','⊢pi) '' 4 ⍝ ⎕R find and replace the input stream, \n",
    "                          ⍝ default encoding, ignore characters"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 168,
   "id": "1199391d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<pre class=\"language-APL\">┌→──────┐\n",
       "│2 4 6 8│\n",
       "└~──────┘\n",
       "</pre>"
      ]
     },
     "execution_count": 168,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "text/html": [
       "<pre class=\"language-APL\">┌→──────┐\n",
       "│6 8 2 4│\n",
       "└~──────┘\n",
       "</pre>"
      ]
     },
     "execution_count": 168,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "row ← 1⌷mat\n",
    "row\n",
    "2⌽row"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "id": "770f137d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<pre class=\"language-APL\"> \n",
       "1\n",
       " \n",
       "</pre>"
      ]
     },
     "execution_count": 128,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "btw ← {(⊃⍵≥3⊃⍵)∧(⊃⍵≤4⊃⍵)}∧{(2⊃⍵≥3⊃⍵)∧(2⊃⍵≤4⊃⍵)} ⍝ straightforward \"between\"\n",
    "con ← {btw ⍵∨btw 2⌽⍵} ⍝ contains for the first two columns, rotate for the second two\n",
    "con row"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "id": "2f95ad7f",
   "metadata": {},
   "outputs": [],
   "source": [
    "part1 ← +/con¨↓mat"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 179,
   "id": "5a400634",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<pre class=\"language-APL\"> \n",
       "0\n",
       " \n",
       "</pre>"
      ]
     },
     "execution_count": 179,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "range ← {(1⊃⍵),(1⊃⍵)+⍳(2⊃⍵-1⊃⍵)} ⍝ given two ascending integers, return vector of ints\n",
    "ovlp ← {⍬≢(range ⍵) ∩ (range 2⌽⍵)} \n",
    "ovlp row"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 182,
   "id": "d98d1ed8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<pre class=\"language-APL\">   \n",
       "798\n",
       "   \n",
       "</pre>"
      ]
     },
     "execution_count": 182,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "part2 ← +/ovlp¨↓mat\n",
    "part2"
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
