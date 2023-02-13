{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 128,
   "id": "6e3ead09",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<span style=\"white-space:pre; font-family: monospace\">Was ON\n",
       "</span>"
      ]
     },
     "execution_count": 128,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ti ← ⊃⎕NGET 'day10ti.txt' 1\n",
    "pi ← ⊃⎕NGET 'day10.txt' 1\n",
    "⎕IO ← 0\n",
    "]rows on"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 191,
   "id": "cef1ab81",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<span style=\"white-space:pre; font-family: monospace\">17380\n",
       "</span>"
      ]
     },
     "execution_count": 191,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ops ← {{(+/''∘≢¨⍵)≥1: ⍎⍵ ⋄ 0}¨5↓¨⍵}pi\n",
    "part1 ← +/(20+¨40×¨⍳6)×18⌷⍉6 40⍴(1+¨+\\∊{0≠⍵: 0,⍵ ⋄ ⍵}¨ops) ⍝ 18 because we're 0 based plus start counting at cycle 1\n",
    "part1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 196,
   "id": "35fcd272",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<span style=\"white-space:pre; font-family: monospace\">####..##...##..#..#.####.###..####..##..\n",
       "#....#..#.#..#.#..#....#.#..#.#....#..#.\n",
       "###..#....#....#..#...#..#..#.###..#....\n",
       "#....#.##.#....#..#..#...###..#....#....\n",
       "#....#..#.#..#.#..#.#....#.#..#....#..#.\n",
       "#.....###..##...##..####.#..#.####..##..\n",
       "</span>"
      ]
     },
     "execution_count": 196,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "xreg ← 1,(1+¨+\\∊{0≠⍵: 0,⍵ ⋄ ⍵}¨ops)\n",
    "sprites ← {(¯1+⍵),⍵,(⍵+1)}¨xreg\n",
    "part2 ← {⍵: '#' ⋄ '.'}¨6 40⍴{(40|⍵)∊⊃⍵⌷sprites}¨⍳240\n",
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
