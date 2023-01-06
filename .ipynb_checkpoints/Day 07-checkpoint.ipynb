{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "ec7adf78",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<pre class=\"language-APL\">Was OFF\n",
       "</pre>"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ti ← ⊃⎕NGET 'day07ti.txt' 1\n",
    "pi ← ⊃⎕NGET 'day07.txt' 1\n",
    "]rows on"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "96755d55",
   "metadata": {},
   "outputs": [],
   "source": [
    "]dinput\n",
    "makePaths ← {\n",
    "    ⍺ ← '' ''         ⍝ Left arg defaults\n",
    "    0=≢⍵: ⍺               ⍝ If right arg is empty, return left arg\n",
    "    curpath ← 1⊃⍺\n",
    "    files ← 2⊃⍺\n",
    "    \n",
    "    '$ ls'≡4↑⊃⍵: (⍺)∇1↓⍵                ⍝ skip the ls statements \n",
    "    ⍝'dir '≡4↑⊃⍵: (⍺)∇1↓⍵                ⍝ skip the dirs they are 0\n",
    "    '$ cd ..'≡7↑⊃⍵: (¯1↓curpath) files∇1↓⍵ ⍝ pop one off the end of path \n",
    "    '$ cd'≡4↑⊃⍵: (curpath,⊂(5↓⊃⍵),'/') files∇1↓⍵ ⍝ add dir to the path\n",
    "    'dir '≡4↑⊃⍵: curpath (files, (⊂(∊curpath) 0))∇1↓⍵\n",
    "    \n",
    "    file ← ⍎((⊃⍵)⍳' ')↑⊃⍵ ⍝ take everything left of the space, convert to int\n",
    "    curpath (files, (⊂(∊curpath) file))∇1↓⍵          ⍝ else, Add head to acc, \n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "83b64a47",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<pre class=\"language-APL\">1555642\n",
       "</pre>"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fs ← makePaths pi\n",
    "files ← 2⊃fs\n",
    "paths ← 1⌷⍉↑files\n",
    "files ← 2⌷⍉↑files\n",
    "totals ← {+/(⍵∘≡¨(≢⍵)↑¨paths)/files}¨∪paths\n",
    "+/(100000≥totals)/totals"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "838af052",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<pre class=\"language-APL\">5974547\n",
       "</pre>"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "delta ← 30000000 - 70000000 - ⌈/totals\n",
    "⌊/(delta≤totals)/totals"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e9b1bac4",
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
