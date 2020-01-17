tags = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
  'computer science'
]

tag_range = tags[1:-1]
print(tag_range)

tag_range = tags[:-1:2]
print(tag_range)

tag_range = tags[::-1]
print(tag_range)

tags.sort(reverse=True)
print(tags)

sorted_tags = tags.sort(reverse=True)
print(sorted_tags)