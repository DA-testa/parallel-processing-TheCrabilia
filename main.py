def parallel_processing(n, m, data):
    threads = [(0, i) for i in range(n)]
    output = []

    for i in range(m):
        time = data[i]
        thread_start_time, thread_idx = min(threads)
        output.append((thread_idx, thread_start_time))
        threads[thread_idx] = (
            thread_start_time + time,
            thread_idx,
        )

    return output


def main():
    # n - threads, m - jobs
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(n, m, data)

    for thread_idx, start_time in result:
        print(f"{thread_idx} {start_time}")


if __name__ == "__main__":
    main()
