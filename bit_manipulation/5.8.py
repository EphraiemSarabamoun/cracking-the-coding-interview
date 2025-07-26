def draw_line(screen: list[int], width: int, x1: int, x2: int, y: int) -> None:
    height = len(screen) * 8 // width
    if y >= height or x1 > x2:
        return
    bytes_per_row = width // 8
    start_offset = y * bytes_per_row
    start_byte = start_offset + (x1 // 8)
    end_byte = start_offset + (x2 // 8)
    start_mask = 0xFF >> (x1 % 8)
    end_mask = (0xFF << (7 - (x2 % 8))) & 0xFF
    if start_byte == end_byte:
        mask = start_mask & end_mask
        screen[start_byte] |= mask
    else:
        screen[start_byte] |= start_mask
        for i in range(start_byte + 1, end_byte):
            screen[i] = 0xFF
        screen[end_byte] |= end_mask

if __name__ == "__main__":
    screen = [0] * 8
    draw_line(screen, 8, 0, 7, 0)
    print(screen)
