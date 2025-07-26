def towers_of_hanoi(n: int, src: str, dest: str, aux: str):
    def move(disk, from_peg, to_peg):
        print(f"Move disk {disk} from {from_peg} to {to_peg}")

    def hanoi(disks, src, dest, aux):
        if disks == 1:
            move(1, src, dest)
            return
        hanoi(disks - 1, src, aux, dest)
        move(disks, src, dest)
        hanoi(disks - 1, aux, dest, src)
    hanoi(n, src, dest, aux)

if __name__ == "__main__":
    towers_of_hanoi(3, "A", "C", "B")