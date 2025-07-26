def histogram_volume(heights: list[int]) -> int:
    if not heights:
        return 0
    left, right = 0, len(heights) - 1
    left_max = right_max = vol = 0
    while left < right:
        if heights[left] < heights[right]:
            if heights[left] > left_max:
                left_max = heights[left]
            else:
                vol += left_max - heights[left]
            left += 1
        else:
            if heights[right] > right_max:
                right_max = heights[right]
            else:
                vol += right_max - heights[right]
            right -= 1
    return vol