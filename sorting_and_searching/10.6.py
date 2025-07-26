import heapq

def external_sort(input_file, output_file, chunk_size):
    chunks = []
    with open(output_file, 'w') as out:
        files = [open(chunk, 'r') for chunk in chunks]
        heap = []
        for i,f in enumerate(files):
            line = f.readline().strip()
            if line:
                heapq.heappush(heap, (line, i))
        while heap:
            line, i = heapq.heappop(heap)
            out.write(line + '\n')
            new_line = files[i].readline().strip()
            if new_line:
                heapq.heappush(heap, (new_line, i))
        for f in files:
            f.close()
