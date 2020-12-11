from commenUtils import get_input_data
import logging
import argparse
from collections import Counter

parser = argparse.ArgumentParser()
parser.add_argument("--log", default="info")

options = parser.parse_args()

level = logging.INFO

if options.log.lower() == "info":
    level = logging.INFO
elif options.log.lower() == "debug":
    level = logging.DEBUG

logging.basicConfig(format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
                    level=level)

logger = logging.getLogger(__name__)


def prepare_input(file_name: str) -> list[int]:
    numbers: list[int] = get_input_data(file_name)
    numbers.append(0)
    numbers.sort()
    numbers.append(numbers[-1] + 3)
    logger.debug(numbers)
    logger.debug(len(numbers))
    return numbers


def solution_part_1(file_name: str) -> int:
    numbers: list[int] = prepare_input(file_name)
    differences: list[int] = []
    logger.debug(numbers)
    for i in range(len(numbers) - 1):
        differences.append(numbers[i + 1] - numbers[i])
    logger.debug(differences)
    counts: Counter = Counter(differences)
    logger.debug(counts)
    return counts[1] * counts[3]


def solution_part_2(file_name: str) -> int:
    numbers: list[int] = prepare_input(file_name)
    numbers.reverse()
    memo: dict[int, int] = {numbers[1]: 1}
    for n in range(2, len(numbers)):
        logger.debug(memo)
        memo[numbers[n]] = 0
        for k in range(1, 4):
            if n-k > 0 and numbers[n-k] - numbers[n] <= 3:
                memo[numbers[n]] += memo[numbers[n-k]]
    logger.debug(memo)
    return memo[numbers[-1]]


if __name__ == '__main__':
    logger.info(solution_part_1("inputData.txt"))
    logger.info(solution_part_2("inputData.txt"))
