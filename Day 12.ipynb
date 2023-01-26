{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "99f68610",
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
    },
    {
     "data": {
      "text/html": [
       "<pre class=\"language-APL\">Was OFF -style=wrap\n",
       "</pre>"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ti ← ⊃⎕NGET 'day12ti.txt' 1\n",
    "pi ← ⊃⎕NGET 'day12.txt' 1\n",
    "⎕IO ← 0\n",
    "]box on -style=min\n",
    "]rows on -style=wrap"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "1c237753",
   "metadata": {},
   "outputs": [],
   "source": [
    "cmat ← ↑ti\n",
    "spoint ← ⊃⍸'S'=cmat\n",
    "epoint ← ⊃⍸'E'=cmat\n",
    "getelev ← {⍵='S': 0 ⋄ ⍵='E': 25 ⋄ 'abcdefghijklmnopqrstuvwxyz'⍳⍵}\n",
    "emat ← getelev¨cmat\n",
    "valpos ← ,⍳⍴cmat ⍝ valid coordinates in the matrix"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "b179e4dd",
   "metadata": {},
   "outputs": [],
   "source": [
    "]dinput\n",
    "neighbors ← {\n",
    "    ⍝ given a coordinate point, return possible neighbors\n",
    "    ce ← (⊂⍵)⊃emat      ⍝ current elevation via reach indexing\n",
    "    allns ← ⍵∘+¨(1 0) (0 1) (¯1 0) (0 ¯1)  \n",
    "    ns←allns∩valpos ⍝ return possible NSEW neighbors \n",
    "    es ← {(⊂⍵)⊃emat}¨ns ⍝ get the neighbors' elevations\n",
    "    emask ← {1≥(⍵-ce)}¨es ⍝ target - current elev is no more than 1!!!\n",
    "    emask/ns ⍝ filter for valid elevations\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "f33428ea",
   "metadata": {},
   "outputs": [],
   "source": [
    "md ← {(|(⊃⍺ - ⊃⍵)) + (|(1⊃⍺ - 1⊃⍵))} ⍝ manhattan distance"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bc44636d",
   "metadata": {},
   "source": [
    "```\n",
    "frontier = PriorityQueue()\n",
    "frontier.put(start, 0)\n",
    "came_from = dict()\n",
    "cost_so_far = dict()\n",
    "came_from[start] = None\n",
    "cost_so_far[start] = 0\n",
    "\n",
    "while not frontier.empty():\n",
    "   current = frontier.get()\n",
    "\n",
    "   if current == goal:\n",
    "      break\n",
    "   \n",
    "   for next in graph.neighbors(current):\n",
    "      new_cost = cost_so_far[current] + graph.cost(current, next)\n",
    "      if next not in cost_so_far or new_cost < cost_so_far[next]:\n",
    "         cost_so_far[next] = new_cost\n",
    "         priority = new_cost\n",
    "         frontier.put(next, priority)\n",
    "         came_from[next] = current\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "b512ac83",
   "metadata": {},
   "outputs": [],
   "source": [
    "]dinput\n",
    "dijkstra ← {\n",
    "    frontier ← ⊃⍵\n",
    "    camefrom ← 1⊃⍵\n",
    "    costsofar ← 2⊃⍵\n",
    "    0=≢frontier: 1⊃⍵\n",
    "    \n",
    "    current ← ⊃frontier\n",
    "    ns ← neighbors current\n",
    "    nextnotin ← ns ~ ⊃¨costsofar\n",
    "    costs ← costsofar\n",
    "    ncosts ← (↑next), costs\n",
    "    cf ← next,⍤0 1 ⊢ ⊂2↑⊃↓current\n",
    "    newfrontier ← ncosts⍪1↓frontier\n",
    "    newfrontier\n",
    "    sortedfrontier ← (2)(⊢⌷⍨∘⊂∘⍋⌷⍤1)newfrontier\n",
    "    newcamefrom ← camefrom,↓cf\n",
    "    (⊂sortedfrontier), ⊂newcamefrom\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "1c163ae3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<pre class=\"language-APL\">┌───────┬───────┬───────┐\n",
       "│┌───┬─┐│┌───┬─┐│┌───┬─┐│\n",
       "││0 0│0│││1 0│1│││0 1│1││\n",
       "│└───┴─┘│└───┴─┘│└───┴─┘│\n",
       "└───────┴───────┴───────┘\n",
       "</pre>"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "csf ← ((0 0) 0)((1 0) 1)((0 1) 1)\n",
    "csf"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "422a0076",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<pre class=\"language-APL\">┌→────────────┐\n",
       "│ ┌→──┐ ┌→──┐ │\n",
       "│ │1 0│ │0 1│ │\n",
       "│ └~──┘ └~──┘ │\n",
       "└∊────────────┘\n",
       "</pre>"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "camefrom ← dijkstra⍣1 ⊢ (spoint 0) (⊂spoint 'None') (⊂spoint 0) ⍝ {0=≢⊃⍵}\n",
    "]display camefrom"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "94092daf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<pre class=\"language-APL\">0\n",
       "</pre>"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cfmat ← (⍴cmat)⍴0\n",
    "cf2 ← 'N'@(⊂0 0) ⊢ cfmat\n",
    "(⊂0 1)⊃cf2"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cd727be8",
   "metadata": {},
   "source": [
    "```\n",
    "current = goal \n",
    "path = []\n",
    "while current != start: \n",
    "   path.append(current)\n",
    "   current = came_from[current]\n",
    "path.append(start) # optional\n",
    "path.reverse() # optional\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "b7a5ae93",
   "metadata": {},
   "outputs": [],
   "source": [
    "]dinput\n",
    "findpath ← {\n",
    "    ⍵\n",
    "    current ← ⊃⍵\n",
    "    path ← 1⊃⍵\n",
    "    camefrom ← 2⊃⍵\n",
    "    (current)≡(spoint): 1⊃⍵\n",
    "    \n",
    "    np ← path,⊂current\n",
    "    (⊃((0⌷⍉camefrom))⍳⊂current)\n",
    "    nc ← 1⊃(⊃((0⌷⍉camefrom))⍳⊂current)⌷camefrom\n",
    "    nc np camefrom\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "ec1a3a82",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "VALUE ERROR: Undefined name: dijkstra\n",
      "      camefrom←dijkstra⍣{0=≢⊃⍵}⊢(1 3⍴spoint,0)(spoint'None')(spoint 0)\n",
      "               ∧\n",
      "VALUE ERROR: Undefined name: camefrom\n",
      "      y←findpath⍣{(⊃⍵)≡(spoint)}⊢(epoint''(↑(1⊃camefrom)))\n",
      "                                               ∧\n",
      "VALUE ERROR: Undefined name: y\n",
      "      ≢1⊃y\n",
      "         ∧\n"
     ]
    }
   ],
   "source": [
    "\n",
    "y ← findpath⍣{(⊃⍵)≡(spoint)} ⊢ (epoint '' (↑(1⊃camefrom)))\n",
    "≢1⊃y"
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
