class Box:
    def __init__(self, w: int, h: int, d: int):
        self.w = w
        self.h = h
        self.d = d

def stack_boxes(boxes: list[Box]) -> int:
    boxes.sort(key=lambda b: b.h, reverse=True)
    dp = [0] * len(boxes)
    max_h = 0
    for i in range(len(boxes)):
        dp[i] = boxes[i].h
        for j in range(i):
            if boxes[i].w < boxes[j].w and boxes[i].d < boxes[j].d:
                dp[i] = max(dp[i], dp[j] + boxes[i].h)
        max_h = max(max_h, dp[i])
    return max_h

if __name__ == "__main__":
    boxes = [Box(1, 2, 3), Box(4, 5, 6), Box(7, 8, 9)]
    print(stack_boxes(boxes))
    