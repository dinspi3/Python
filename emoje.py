
message = input (">")
words = message.split(' ')
emoje = {
    ":)" : "😊",
    ":(" : "😒"
}
output =" "
for word in words:
    output += emoje.get(word, word) + " "
print (output)


