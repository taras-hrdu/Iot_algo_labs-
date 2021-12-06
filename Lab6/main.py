class WChain:
    def read_file(file_path):
        file_open = open(file_path, "r")
        data = file_open.readlines()
        example_array = []
        for word in data:
            example_array.append(word.strip("\n"))
        return example_array

    def longestStrChain(data) -> int:
        s = set(data)
        memo = {}

        def rec(word):
            if word not in s: return 0
            if word in memo:
                return memo[word]
            else:
                N = len(word)
                mx_path = 0
                for i in range(N):
                    mx_path = max(mx_path, rec(word[:i] + word[i + 1:]) + 1)
                memo[word] = mx_path

            return mx_path

        for word in data:
            rec(word)

        return max(memo.values())
    


if __name__ == '__main__':
    data = WChain.read_file('wchain.in')
    max_chain = WChain.longestStrChain(data)
    print(f"Max chain is {max_chain}")