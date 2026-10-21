class Solution:
    def isValid(self, s: str) -> bool:
        # we need to use a stack to see the order of the things that are being added
        # if the length of the stack is 0 then all elements have been seen
        stack = []
        # but how do we know what the complement of something is, this is something we need to define
        # stacks are list in first out, so we look at the complements first anyway
        pairs = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        # we are gonna wanna iterate the chars now
        for char in s:
            # check is the char is a closing or an opening
            # we only start checking when the chars are the closing
            # we add to the list till then
            if char in pairs:
                if stack and stack[-1] == pairs[char]:
                     stack.pop()
                else:
                    # is the closing does not have a matching open at the end then we return false
                    return False
            else:
                stack.append(char)

        return True if not stack else False