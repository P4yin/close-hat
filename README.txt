This is only really useful when using sunglasses's IGT restorer and having saving turned on.
Doka has only approved this to be used in All Time Pieces.

Adding characters to keys.txt will allow you to press that key to forcefully close the game.
Adding a string of characters will allow pressing any character in that string to close the game.
However, having certain special strings will allow you to press certain keys, such as space.

For example, having keys.txt contain:
space
tsj

will close the game if you press spacebar, t, s, or j.

Having keys.txt contain:
spacetsj

will close the game if you press s, p, a, c, e, t, or j.

Adding new lines makes a difference!
If you would like the add more key functionality, edit <_special_keys> in close_hat.py.

Default keys.txt contains <tab> and <p>.
The current special keys it supports are (these are the names the program will recognize them under):
space
escape
tab
enter
alt
ctrl
f1 to f12

If there is nothing in keys.txt, the program will not run correctly (definitely intentional)