def ft_tqdm(lst: range) -> None:
    print_block = round(int(lst[-1]) / 24)
    print_percent = round(int(lst[-1]) / 100)
    step_percent = print_percent
    count = 0

    for elem in lst:
        loading_bar = [

        ]
        count += 1
        if count == print_block:
            # f"100%|████████████████████████| 333/333 [00:01<00:00, 171.42it/s]"
            f"{percent}%|{loading_bar}| {passed_elements}/{total_elements} [00:01<00:00, 171.42it/s]"
            print(f"\r{str(print_percent)}%|", end="", flush=True)
            print_percent += step_percent
            print('\u2588', end="", flush=True)
            count = 0
        yield lst