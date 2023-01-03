{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "67978eed",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "* Unable to rebuild user command cache: the path of \\UserCommand20.cache does \n",
      "not exist\n",
      "* Command Execution Failed: VALUE ERROR\n",
      "Init[4] ⎕SE.UCMD'←box on -f=on -t=tree' ⍝ TryAPL's boxing settings\n",
      "        ∧\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<span style=\"white-space:pre; font-family: monospace\">* Command Execution Failed: VALUE ERROR\n",
       "</span>"
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
   "id": "9f49a7ec",
   "metadata": {},
   "outputs": [],
   "source": [
    "ti ← ⊃⎕NGET 'day09ti.txt' 1\n",
    "ti2 ← ⊃⎕NGET 'day09ti2.txt' 1\n",
    "pi ← ⊃⎕NGET 'day09.txt' 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "753a993b",
   "metadata": {},
   "outputs": [],
   "source": [
    "]dinput\n",
    "moveh ← {\n",
    "    ⍺ ← ⊂0 0   ⍝ start in the origin\n",
    "    0=≢⍵: ⍺   ⍝ if right arg is empty, return accumulator\n",
    "    x ← ⊃⊃¯1↑⍺\n",
    "    y ← 2⊃⊃¯1↑⍺\n",
    "    dir ← ⊃⊃⍵\n",
    "    mag ← 2⊃⊃⍵\n",
    "    \n",
    "    'R'=dir: ⍺,(↓⍉↑(⊂x+¨⍳mag),⊂y⍨¨⍳mag)∇1↓⍵\n",
    "    'U'=dir: ⍺,(↓⍉↑(⊂x⍨¨⍳mag),⊂y+¨⍳mag)∇1↓⍵\n",
    "    'L'=dir: ⍺,(↓⍉↑(⊂x-¨⍳mag),⊂y⍨¨⍳mag)∇1↓⍵\n",
    "    'D'=dir: ⍺,(↓⍉↑(⊂x⍨¨⍳mag),⊂y-¨⍳mag)∇1↓⍵\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "f56311f2",
   "metadata": {},
   "outputs": [],
   "source": [
    "motions ← {↓⍉↑(⊃¨⍵) (⍎¨2↓¨⍵)}pi ⍝ convert magnitudes to integers, remix\n",
    "hmoves ← moveh motions"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "316665b3",
   "metadata": {},
   "source": [
    "If the head is ever **two steps directly up, down, left, or right** from the tail, the tail must also move **one** step in that direction so it remains close enough:\n",
    "\n",
    "Otherwise, if the head and tail **aren't touching** and **aren't in the same row or column**, the tail always moves **one step diagonally** to keep up:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "7044ec5d",
   "metadata": {},
   "outputs": [],
   "source": [
    "]dinput\n",
    "movet ← {\n",
    "    ⍺ ← ⊂0 0   ⍝ start in the origin\n",
    "    0=≢⍵: ⍺   ⍝ if right arg is empty, return accumulator\n",
    "    tx ← ⊃⊃¯1↑⍺ ⋄ ty ← 2⊃⊃¯1↑⍺\n",
    "    hx ← ⊃⊃⍵ ⋄ hy ← 2⊃⊃⍵\n",
    "    d ← ⌈/|¨-⌿↑(⊃⍵)(⊃¯1↑⍺) ⍝ get the max of the differences in xs and ys\n",
    "    hmoves ← (⊂¯1 0), (⊂0 ¯1), (⊂1 0), (⊂0 1)\n",
    "    tmoves ← (⊂¯1 0), (⊂¯1 1), (⊂0 ¯1), (⊂1 0), (⊂0 1),  (⊂¯1 ¯1), (⊂1 ¯1),  (⊂1 1)\n",
    "    a ← (⊂⊃⍵)+hmoves\n",
    "    b ← (¯1↑⍺)+tmoves\n",
    "    k ← (⊂⊃⍵)+tmoves\n",
    "    \n",
    "    ⍝ learn to write an if statement the right way\n",
    "    tm ← {⍵: 1↑(k∩b) ⋄ 1↑(a∩b)} 0=≢(a∩b)\n",
    "    \n",
    "    d>1: (⍺,tm)∇1↓⍵\n",
    "        ⍺,(¯1↑⍺)∇1↓⍵\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "7de0131a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<span style=\"white-space:pre; font-family: monospace\">2661\n",
       "</span>"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "≢∪movet⍣9 ⊢ hmoves"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f50c1e8f",
   "metadata": {},
   "outputs": [],
   "source": []
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
