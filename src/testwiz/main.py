import argparse

from testwiz.core.entities.config import UnittestGeneratorConfig
from testwiz.core.unittest_generator import UnittestGenerator


def parse_arguments():

    parser = argparse.ArgumentParser(
        description="TestWiz: A tool for generating unit tests for any programming languages."
    )
    subparsers = parser.add_subparsers(title="commands", dest="command")

    # Main command arguments
    main_parser = subparsers.add_parser("gen", help="Generate unit tests.")
    main_parser.add_argument(
        "--test-file-path",
    )
    main_parser.add_argument(
        "--source-file-path",
    )
    main_parser.add_argument(
        "--code-coverage-report-path",
        type=str,
        required=False,
        help="The path to the code coverage report file. Optional.",
    )
    main_parser.add_argument(
        "--mutation-coverage-report-path",
        type=str,
        required=False,
        help="The path to the mutation coverage report file. Optional.",
    )
    main_parser.add_argument(
        "--coverage-type",
        type=str,
        default="cobertura",
        required=False,
        choices=["cobertura", "jacoco", "lcov"],
        help="The type of code coverage report to parse. Default is 'cobertura'.",
    )
    main_parser.add_argument(
        "--test-command",
        type=str,
        default=None,
        required=True,
        help="The command to run the tests (e.g., 'pytest'). This argument is required.",
    )
    main_parser.add_argument(
        "--model",
        type=str,
        default="gpt-3.5-turbo",
        help="The LLM model to use for mutation generation. Default is 'gpt-3.5-turbo'.",
    )
    main_parser.add_argument(
        "--api-base",
        type=str,
        default="",
        help="The base URL for the API if using a self-hosted LLM model.",
    )
    main_parser.add_argument(
        "--target-line-coverage-rate",
        type=float,
        default=0.9,
        help="The target line coverage rate. Default is 0.9.",
    )

    return parser.parse_args()


def run():
    args = parse_arguments()
    config = UnittestGeneratorConfig(
        model=args.model,
        api_base=args.api_base,
        test_file_path=args.test_file_path,
        source_file_path=args.source_file_path,
        test_command=args.test_command,
        code_coverage_report_path=args.code_coverage_report_path,
        mutation_coverage_report_path=args.mutation_coverage_report_path,
        coverage_type=args.coverage_type,
        target_line_coverage_rate=args.target_line_coverage_rate,
    )
    runner = UnittestGenerator(config=config)
    runner.run()


if __name__ == "__main__":
    run()
