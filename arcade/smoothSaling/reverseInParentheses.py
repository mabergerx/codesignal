def reverseInParentheses(inputString):
        
        if "(" not in inputString:
                return inputString
        else:
                last_opening_index = 0
                corresponding_closing_index = 0
                startIndex = None
                results = []

                reversedString = ""

                for i, c in enumerate(inputString):
                    if c == '(':
                        last_opening_index = i

                for index in range(last_opening_index, len(inputString)):
                    if inputString[index] == ')':
                        corresponding_closing_index = index
                        break


                string_between = inputString[last_opening_index+1:corresponding_closing_index]
                string_between_reversed = string_between[::-1]
                reversedString = inputString[:last_opening_index] + string_between_reversed + inputString[corresponding_closing_index+1:]

                return reverseInParentheses(reversedString)
