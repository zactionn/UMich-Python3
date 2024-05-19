Junior = {'SI 206': 4, 'SI 310': 4, 'BL 300': 3, 'TO 313': 3, 'BCOM 350': 1, 'MO 300': 3}
credits = 0

# Use a different variable name for iteration to avoid confusion
for course_credits in Junior.values():
    credits += course_credits

print(credits)