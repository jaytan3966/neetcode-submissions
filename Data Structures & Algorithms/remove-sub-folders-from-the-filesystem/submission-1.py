class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()

        subfolder = set()
        n = len(folder)

        ans = []
        for i, f in enumerate(folder):
            if f in subfolder:
                continue
            
            ideal = f + '/'
            for j in range(i+1, n):
                target_f = folder[j]

                if ideal in target_f:
                    subfolder.add(target_f)
                    continue
            ans.append(f)
        return ans