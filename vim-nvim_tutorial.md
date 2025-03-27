# Motions

h - left
j - down
k - up
l - right

w - word
e - end of word
o - add new line, enter INSERT mode

**NOTE:** *hold for repetition*

# Quit

:q! - quit, no save
:wq - write (save) and quit
:x - same as :wq

# Command structure

(operator)(*optional: number of repetitions*)(motion)

# Basic text functions

## Copy and Paste

y - copy (yoink)
p - paste

## Insertion

esc - NORMAL mode
i - insert before cursor
A - append after end (goes to the end of the line and enters INSERT mode)

## Deletion

*format = d(number)(motion)

### Examples:

dd - delete line
(move to beginning of word) dw - delete untill the start of the next word, EXCLUDING its first character
d$ - delete to the end of the line, INCLUDING the last character.
de - to the end of the current word, INCLUDING the last character.
caw - delete word under cursor and put back into INSERT mode

# Execution
:so - source file (*updates system to the current file*)

# NVIM-specific

## NEWTRW
d - create directory
% - create file

## COMMAND mode
:Ex or (space)pv - file explorer (newtrw)

## Find and Replace
<leader>sb - telescope
<leader>sg - grep
