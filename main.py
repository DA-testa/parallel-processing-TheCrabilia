def heapify_down(heap, index):
    while True:
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest_child_index = index

        if (
            left_child_index < len(heap)
            and heap[left_child_index] < heap[smallest_child_index]
        ):
            smallest_child_index = left_child_index

        if (
            right_child_index < len(heap)
            and heap[right_child_index] < heap[smallest_child_index]
        ):
            smallest_child_index = right_child_index

        if smallest_child_index == index:
            break

        heap[index], heap[smallest_child_index] = (
            heap[smallest_child_index],
            heap[index],
        )
        index = smallest_child_index


def heapify_up(heap, index):
    while True:
        parent_index = (index - 1) // 2

        if index == 0 or heap[parent_index] < heap[index]:
            break

        heap[index], heap[parent_index] = heap[parent_index], heap[index]
        index = parent_index


def heappop(heap):
    if len(heap) == 0:
        raise IndexError("pop from empty heap")

    heap[0], heap[-1] = heap[-1], heap[0]
    popped_node = heap.pop()
    heapify_down(heap, 0)
    return popped_node


def heappush(heap, item):
    heap.append(item)
    heapify_up(heap, len(heap) - 1)


def parallel_processing(n, m, data):
    threads = [(0, i) for i in range(n)]
    jobs = [(data[i], i) for i in range(m)]
    output = []

    while jobs:
        time, thread_index = heappop(threads)
        processing_time, job_index = heappop(jobs)
        output.append((thread_index, job_index))
        heappush(threads, (time + processing_time, thread_index))

    return output


def main():
    n, m = map(int, input().strip().split())
    data = list(map(int, input().strip().split()))

    result = parallel_processing(n, m, data)

    for thread_index, job_index in result:
        print(thread_index, job_index)


if __name__ == "__main__":
    main()
