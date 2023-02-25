from domain.Calculator import Calculator
from repository.CalculatorMemoryRepository import CalculatorMemoryRepository
from business.CalculatorService import CalculatorService
from presentation.Console import Console


def main():
    repository = CalculatorMemoryRepository()
    service = CalculatorService(repository)
    console = Console(service, repository)
    console.run_console()


if __name__ == "__main__":
    main()
