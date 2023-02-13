{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "22d8b679",
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
     "execution_count": 1,
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
   "execution_count": 1,
   "id": "a1d3cb2e",
   "metadata": {},
   "outputs": [],
   "source": [
    "ti ← ⊃⎕NGET 'day05ti.txt'1\n",
    "pi ← ⊃⎕NGET 'day05.txt'1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "f2cca990",
   "metadata": {},
   "outputs": [],
   "source": [
    "partitioned ← {(''∘≢¨⍵)⊆⍵}pi\n",
    "rawstacks ← 1⊃partitioned\n",
    "moves ← ↓⎕CSV ('\\D+'⎕R','⊢(2⊃partitioned)) '' (0 2 2 2) \n",
    "⍝ replace non digits with commas; ignore first column"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "933d04f3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<pre class=\"language-APL\">┌────────┬────────┬─────┬───┬────────┬────┬───────┬───────┬──────┐\n",
       "│MSJLVFNR│HWJFZDNP│GDCRW│SBN│NFBCPWZM│WMRP│WSLGNTR│VBNFHTQ│FNZHML│\n",
       "└────────┴────────┴─────┴───┴────────┴────┴───────┴───────┴──────┘\n",
       "</pre>"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ns ← ' '⎕R''⊢¨↓⍉¯1↓↑('\\W'⎕R' '⊢rawstacks) \n",
    "⍝ replace chars with spaces, matrix, drop bottom row, transpose\n",
    "⍝ split to nested, remove spaces from each nested vector\n",
    "select ← ''∘≢¨ns ⍝ \n",
    "stacks ← select/ns\n",
    "stacks"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "04cedb63",
   "metadata": {},
   "outputs": [],
   "source": [
    "]dinput\n",
    "move ← {\n",
    "    qty ← 1⊃⍵\n",
    "    from ← 2⊃⍵\n",
    "    to ← 3⊃⍵\n",
    "    crates ← qty↑from⊃⍺ ⍝ reverse to simulate 1 at a time\n",
    "    new1 ← qty↓from⊃⍺\n",
    "    new2 ← crates,to⊃⍺\n",
    "    res0 ← (⊂new1)(@from)⍺\n",
    "    (⊂new2)(@to)res0\n",
    "    }"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "080874a7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<pre class=\"language-APL\">BQDNWJPVJ\n",
       "</pre>"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "⍝ ⊃¨(((move (1 2 1)) move 3 1 3) move 2 2 1) move 1 1 2\n",
    "⊃¨move foldl moves"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "48fac0e1",
   "metadata": {},
   "outputs": [],
   "source": [
    "]dinput\n",
    "foldl ← {                 ⍝ Fold (reduce) from the left.\n",
    "    ⍺ ← stacks            ⍝ Default initial value for accumulator\n",
    "    ↑⍺⍺⍨/(⌽⍵),⊂⍺        \n",
    "}"
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
