# You are given a list of folders folder, return the folders after removing all sub-folders in those folders.
# You may return the answer in any order.
#
# If a folder[i] is located within another folder[j], it is called a sub-folder of it. A sub-folder of folder[j]
# must start with folder[j], followed by a "/". For example, "/a/b" is a sub-folder of "/a", but "/b" is not a
# sub-folder of "/a/b".
#
# The format of a path is one or more concatenated strings of the form: '/' followed by one or more lowercase English
# letters.
#
# For example, "/neetcode" and "/neetcode/practice" are valid paths while an empty string "" and "/" are not.

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = [folder[0]]
        for i in range(1, len(folder)):
            last_folder = res[-1] + '/'
            #if not folder[i].startswith(last_folder):
            if folder[i][:len(last_folder)] != last_folder:
                res.append(folder[i])
        return res

if __name__ == '__main__':
    folder = ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"] # ["/a","/c/d","/c/f"]
    print(Solution().removeSubfolders(folder))