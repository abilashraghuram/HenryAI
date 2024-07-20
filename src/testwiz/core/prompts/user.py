TEST_GEN_USER_PROMPT = """
## Overview
You are a code assistant that accepts a {{ language }} source file and test file. Your goal is to generate additional unit tests to complement the existing test suite and increase line coverage against the source file.

## Guidelines:
- Analyze the provided code to understand its purpose, inputs, outputs, and key logic.
- Brainstorm test cases to fully validate the code and achieve 100% line coverage.
- Ensure the tests cover all scenarios, including exceptions or errors.
- If the original test file has a test suite, integrate new tests consistently in terms of style, naming, and structure.
- Ensure unit tests are independent and do not rely on the system's state or other tests.
- Include clear assertions in each test to validate expected behavior.
- Mock or stub external dependencies to keep tests isolated and repeatable.

## Source File
Here is the source file for which you will write tests, called `{{ source_file_name }}`. Note that line numbers have been manually added for reference. Do not include these line numbers in your response.
```{{ language }}
{{ source_file_numbered }}
```

## Test File
Here is the file that contains the existing tests, called `{{ test_file_name }}.
```{{ language }}
{{ test_file }}
```

## Line Coverage
The following line numbers are not covered by the existing tests. Your goal is to write tests that cover as many of these lines as possible.
{{ lines_to_cover }}

## Response 
The output must be a JSON object wrapped in json. Do not generate more than 5 tests in a single response.
```json
{
  "language": {{ language }},
  "insertion_point_marker": {
    "class_name": "The name of the class after which the test should be inserted.",
    "method_name": "The last method name after which the test should be inserted in the class."
  },
  "new_tests": [
    {
      "test_behavior": "Short description of the behavior the test covers.",
      "lines_to_cover": "List of line numbers, currently uncovered, that this specific new test aims to cover.",
      "test_name": "A short unique test name reflecting the test objective.",
      "test_code": "A single test function testing the behavior described in 'test_behavior'. Write it as part of the existing test suite, using existing helper functions, setup, or teardown code.",
      "new_imports_code": "New imports required for the new test function, or an empty string if none. Use 'import ...' lines if relevant.",
      "test_tags": ["happy path", "edge case", "other"]
    }
  ]
}
```
{{ failed_tests_section }}
"""

MUTATION_TEST_PROMPT = """
## Overview
You are a code assistant that accepts a {{ language }} source file and test file. The current code has a line coverage of {{ line_coverage }}% and a mutation coverage of {{ mutation_coverage }}%.

Your goal is to generate additional unit tests to kill the survived mutants in the source code. To kill a mutant, you need to write a test that triggers the fault introduced by the mutant but passes for the original code.

## Source File
Here is the source file you will be writing tests against, called `{{ source_file_name }}`.
```{{ language }}
{{ source_code }}
```
## Test File
Here is the file that contains the existing tests, called `{{ test_file_name }}`
```{{ language }}
{{ test_file }}
```

## Survived Mutants
Below is a list of survived mutants. Your goal is to write tests that will detect faults based on these mutants.
```json
{{ survived_mutants }}
```

## Response
The output must be a JSON object wrapped in json. Do not generate more than 5 tests in a single response.
``json
{
  "language": {{ language }},
  "insertion_point_marker": {
    "class_name": "The name of the class after which the test should be inserted.",
    "method_name": "The last method name after which the test should be inserted in the class."
  },
  "new_tests": [
    {
      "test_behavior": "Short description of the behavior the test covers.",
      "mutant_id": "The ID of the mutant this test aims to kill.",
      "test_name": "A short unique test name reflecting the test objective.",
      "test_code": "A single test function that tests the behavior described in 'test_behavior'. Write it as part of the existing test suite, using existing helper functions, setup, or teardown code.",
      "new_imports_code": "New imports required for the new test function, or an empty string if none. Use 'import ...' lines if relevant.",
      "test_tags": ["happy path", "edge case", "other"]
    }
  ]
}
```
{{ weak_tests_section }}

{{ failed_tests_section }}
"""

MUTATION_WEAK_TESTS_TEXT = """
## Previous Iterations Passes But Fails to Kill Mutants
Below is a list of tests that pass but fail to kill the mutants. Do not generate the same tests again, and take these tests into account when generating new tests.
```json
{{ weak_tests }}
```
"""

FAILED_TESTS_TEXT = """
## Previous Iterations Failed Tests
Below is a list of failed tests that you generated in previous iterations. Do not generate the same tests again, and take the failed tests into account when generating new tests.
```json
{{ failed_test }}
```
"""

REPORT_PROMPT = """
## Overview
You are a code assistant that accepts a {{ language }} source file and test file. Your goal is to analyze the existing test suite and generate a report that provides insights into the quality and effectiveness of the tests based on the surviving mutants and failed tests.

Here is the source file that you will be writing tests against, called `{{ source_file_name }}`.
```{{ language }}
{{ source_code }}
```
## Test File
Here is the file that contains the existing tests, called `{{ test_file }}`
```{{ language }}
{{ test_code }}
```

## Survived Mutants
{{survived_mutants_section}}

Based on the surviving mutants that could not be killed by the existing tests, there might be bugs in the source code or weaknesses in the test file. Please identify potential bugs in the source code or weaknesses in the test file. The report must be in markdown format and no more than 400 words. Use concise bullet points to summarize the key insights and recommendations.
"""
