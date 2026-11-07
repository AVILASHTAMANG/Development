# You are given an array asteroids of integers representing asteroids in a row. The indices of the asteriod in the
# array represent their relative position in space.
#
# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning
# right, negative meaning left). Each asteroid moves at the same speed.
#
# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode.
# If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # O(n) space
        # stack=[]
        # for ast in asteroids:
        #     while stack and ast<0<stack[-1]:
        #         if stack[-1]<-ast:
        #             stack.pop()
        #             continue
        #         elif stack[-1] == -ast:
        #             stack.pop()
        #         break
        #     else:
        #         stack.append(ast)
        # return stack

        #O(1) space
        w = 0  # Points to the write position (top of stack is w - 1)

        for ast in asteroids:
            alive = True

            # Collision only if current moves left (ast < 0) and top moves right (asteroids[w - 1] > 0)
            while alive and ast < 0 and w > 0 and asteroids[w - 1] > 0:
                diff = asteroids[w - 1] + ast  # Arithmetic shortcut

                # If top is smaller or equal (diff <= 0), top explodes (decrement pointer)
                if diff <= 0:
                    w -= 1

                # If top is larger or equal (diff >= 0), incoming asteroid explodes
                if diff >= 0:
                    alive = False

            if alive:
                asteroids[w] = ast
                w += 1

        del asteroids[w:]  # Truncate array to the surviving elements in-place
        return asteroids

if __name__=='__main__':
    asteroids = [2, 4, -4, -1]
    print(Solution().asteroidCollision(asteroids))