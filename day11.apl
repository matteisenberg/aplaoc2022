{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "70d137fb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<pre class=\"language-APL\">Was OFF\n",
       "</pre>"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ti ← ⊃⎕NGET 'day11ti.txt' 1\n",
    "pi ← ⊃⎕NGET 'day11.txt' 1\n",
    "⎕IO ← 0\n",
    "]rows on"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c7e8d201",
   "metadata": {},
   "outputs": [],
   "source": [
    "]dinput\n",
    "parsem ← {\n",
    "    ⍺ ← '' '' '' '' '' '' ⍝ itemlists, operation, test, iftrue, iffalse, num inspected\n",
    "    0=≢⍵: ⍺   ⍝ if right arg is empty, return accumulator\n",
    "    itemlists  ← 0⊃⍺\n",
    "    ops        ← 1⊃⍺\n",
    "    tests      ← 2⊃⍺\n",
    "    trues    ← 3⊃⍺\n",
    "    falses   ← 4⊃⍺\n",
    "    inspected ← 5⊃⍺\n",
    "    \n",
    "    head ← ⊃⍵\n",
    "    startitems ← ⍎18↓1⊃head\n",
    "    op  ←  '\\*'⎕R'×' ⊢ 22↓2⊃head ⍝ replace * with ×\n",
    "    test ← ⍎21↓3⊃head\n",
    "    true ← ⍎29↓4⊃head\n",
    "    false ← ⍎29↓5⊃head\n",
    "    \n",
    "    (itemlists,⊂startitems) (ops,⊂op) (tests,test) (trues,true) (falses,false) (inspected,0)∇1↓⍵ ⍝ starting items\n",
    "    }"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a4f34b0c",
   "metadata": {},
   "outputs": [],
   "source": [
    "]dinput\n",
    "round ← {\n",
    "    ⍺ ← 0 ⍝ monkey we are working on\n",
    "    ⍺=≢⊃⍵: ⍵ ⍝ if tally of monkeys = ⍺, return state\n",
    "    \n",
    "    newms ← ⍺ turn ⍵ ⍝ new monkey state\n",
    "\n",
    "    (⍺+1)∇newms\n",
    "    }"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "e0e15d49",
   "metadata": {},
   "outputs": [],
   "source": [
    "]dinput\n",
    "turn ← {\n",
    "    items ← ⍺⊃⊃⍵\n",
    "    0=≢items: ⍵\n",
    "    op ← ⍺⊃1⊃⍵\n",
    "    new ← {⌊(⍎('old ',op))÷3 ⊣ old ← ⍵}¨items ⍝ return a new list of items based on the operation\n",
    "    test ← ⍺⊃2⊃⍵\n",
    "    passes ← 0=test|¨new\n",
    "    fails  ← 0≠test|¨new\n",
    "    true ← ⍺⊃3⊃⍵\n",
    "    false ← ⍺⊃4⊃⍵\n",
    "    titems ← (true⊃⊃⍵),(passes/new)\n",
    "    fitems ← (false⊃⊃⍵),(fails/new)\n",
    "    ws1 ← (⊂titems)@(⊂0 true)⊢⍵\n",
    "    ws2 ← (⊂fitems)@(⊂0 false)⊢ws1\n",
    "    ws3 ← (⊂'')@(⊂0 ⍺)⊢ws2 ⍝ empty out this monkey's items\n",
    "    inspected ← ⍺⊃5⊃⍵\n",
    "    ws4 ← (⊂inspected+≢items)@(⊂5 ⍺)⊢ws3\n",
    "    ws4\n",
    "    }"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "c588e728",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<pre class=\"language-APL\">95472\n",
       "</pre>"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ms ← parsem {(''∘≢¨⍵)⊆⍵}pi\n",
    "part1 ← ×/2↑insps[⍒insps] ⊣ insps ← 5⌷↑round⍣20 ⊢ ms\n",
    "part1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "f45fce3d",
   "metadata": {},
   "outputs": [],
   "source": [
    "]dinput\n",
    "round2 ← {\n",
    "    ⍺ ← 0 ⍝ monkey we are working on\n",
    "    ⍺=≢⊃⍵: ⍵ ⍝ if tally of monkeys = ⍺, return state\n",
    "    \n",
    "    newms ← ⍺ turn2 ⍵ ⍝ new monkey state\n",
    "\n",
    "    (⍺+1)∇newms\n",
    "    }"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "b36cadf0",
   "metadata": {},
   "outputs": [],
   "source": [
    "]dinput\n",
    "turn2 ← {\n",
    "    items ← ⍺⊃⊃⍵\n",
    "    0=≢items: ⍵\n",
    "\n",
    "    op ← ⍺⊃1⊃⍵\n",
    "    new0 ← {(⍎('old ',op)) ⊣ old ← ⍵}¨items ⍝ return a new list of items based on the operation\n",
    "    test ← ⍺⊃2⊃⍵\n",
    "    new ←  1+⌈/¨factors¨new0\n",
    "    \n",
    "    passes ← 0=test|¨new\n",
    "    fails  ← 0≠test|¨new\n",
    "    true ← ⍺⊃3⊃⍵\n",
    "    false ← ⍺⊃4⊃⍵\n",
    "    titems ← (true⊃⊃⍵),(passes/new)\n",
    "    fitems ← (false⊃⊃⍵),(fails/new)\n",
    "    ws1 ← (⊂titems)@(⊂0 true)⊢⍵\n",
    "    ws2 ← (⊂fitems)@(⊂0 false)⊢ws1\n",
    "    ws3 ← (⊂'')@(⊂0 ⍺)⊢ws2 ⍝ empty out this monkey's items\n",
    "    inspected ← ⍺⊃5⊃⍵\n",
    "    ws4 ← (⊂inspected+≢items)@(⊂5 ⍺)⊢ws3\n",
    "    ws4\n",
    "    }"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "id": "9a9a1676",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<pre class=\"language-APL\">49997 49999 3 50001\n",
       "</pre>"
      ]
     },
     "execution_count": 97,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "text/html": [
       "<pre class=\"language-APL\">2499999999\n",
       "</pre>"
      ]
     },
     "execution_count": 97,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ms ← parsem {(''∘≢¨⍵)⊆⍵}ti\n",
    "r2 ← ↑round2⍣10000 ⊢ ms\n",
    "insps ← 5⌷r2\n",
    "insps\n",
    "part2 ← ×/2↑insps[⍒insps]\n",
    "part2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "b480e31e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<pre class=\"language-APL\">┌───────────────────────────────┬────────────────────────┬───────────┬───────┬───────┬───────┐\n",
       "│┌─────┬───────────┬────────┬──┐│┌─────┬────┬──────┬────┐│23 19 13 17│2 2 1 0│3 0 3 1│0 0 0 0│\n",
       "││79 98│54 65 75 74│79 60 97│74│││ × 19│ + 6│ × old│ + 3││           │       │       │       │\n",
       "│└─────┴───────────┴────────┴──┘│└─────┴────┴──────┴────┘│           │       │       │       │\n",
       "└───────────────────────────────┴────────────────────────┴───────────┴───────┴───────┴───────┘\n",
       "</pre>"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "text/html": [
       "<pre class=\"language-APL\">49996 50000 3 50000\n",
       "</pre>"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'factors' ⎕CY 'dfns'\n",
    "ms\n",
    "insps"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "01051c91",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<pre class=\"language-APL\">0 0\n",
       "</pre>"
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "23|23×⌊/¨factors¨19×(79 98)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "b5fb4bb0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<pre class=\"language-APL\">┌──────────────┬───────┬──────┬─────┐\n",
       "│2 11 2 11 2 11│2 5 5 2│      │     │\n",
       "├──────────────┼───────┼──────┼─────┤\n",
       "│ × 19         │ + 6   │ × old│ + 3 │\n",
       "├──────────────┼───────┼──────┼─────┤\n",
       "│23            │19     │13    │17   │\n",
       "├──────────────┼───────┼──────┼─────┤\n",
       "│2             │2      │1     │0    │\n",
       "├──────────────┼───────┼──────┼─────┤\n",
       "│3             │0      │3     │1    │\n",
       "├──────────────┼───────┼──────┼─────┤\n",
       "│49996         │50000  │3     │50000│\n",
       "└──────────────┴───────┴──────┴─────┘\n",
       "</pre>"
      ]
     },
     "execution_count": 89,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "r2\n"
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
