heading = "Python: An Introduction"

# variable deconstruction 'header, _, subheader'
# _ is a varible that wont be used, common practice
header, _, subheader = heading.partition(': ') # Returns a Tuple collection

print(header)
print(subheader)