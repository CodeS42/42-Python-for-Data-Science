from shutil import get_terminal_size
from time import time


def ft_tqdm(lst: range) -> None:
    nb_elem = len(lst)
    term_width = get_terminal_size().columns
    done = 0
    time_start = time()
    last_print = 0

    for elem in lst:
        done += 1
        if elem == 0 or elem == nb_elem - 1 or (time() - last_print) >= 0.1:
            percent = int((done / nb_elem) * 100)
            elapsed = time() - time_start
            it_per_sec = done / elapsed
            time_left = (nb_elem - done) / it_per_sec

            hours = int(elapsed // 3600)
            minutes = int((elapsed % 3600) // 60)
            seconds = int(elapsed % 60)
            if hours >= 1:
                str_elapsed = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            else:
                str_elapsed = f"{minutes:02d}:{seconds:02d}"

            hours = int(time_left // 3600)
            minutes = int((time_left % 3600) // 60)
            seconds = int(time_left % 60)
            if hours >= 1:
                str_time_left = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            else:
                str_time_left = f"{minutes:02d}:{seconds:02d}"

            if percent < 100:
                str_percent = f"{percent: 3d}%"
            else:
                str_percent = f"{percent}%"

            str_it_per_sec = f"{it_per_sec:.2f}it/s"
            str_done = f"{done}/{nb_elem}"

            size_load_bar = term_width - len(str_percent) - len(str_elapsed) -\
                len(str_it_per_sec) - len(str_done) - len(str_time_left) - 9
            n_blocks = int((size_load_bar * done) / nb_elem)

            loading_bar = '█' * n_blocks + ' ' * (size_load_bar - n_blocks)
            line = f"{str_percent}|{loading_bar}| {str_done} "
            line += f"[{str_elapsed}<{str_time_left}, {str_it_per_sec}]"
            print('\r' + line, end='')
            last_print = time()
        yield elem
