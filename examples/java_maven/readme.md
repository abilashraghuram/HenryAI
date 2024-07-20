# Code Coverage Report Generation for Java Maven Project

```bash
export OPENAI_API_KEY=your-key-goes-here
export OCTOAI_TOKEN=your-token-goes-here
mvn clean test
testwiz gen --test-command "mvn clean test" --code-coverage-report-path "target/site/jacoco/jacoco.xml" --test-file-path "src/test/java/BankAccountTest.java" --source-file-path "src/main/java/com/example/BankAccount.java" --coverage-type jacoco  --model "gpt-4o"
```
