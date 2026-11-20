You get one bug report and the Python file.
Write exactly ONE pytest test that proves the bug.
Rules:
- Answer with Python code only. No markdown, no ``` fences, no explanation.
- One function whose name starts with test_.
- Do not import the exercise functions: they are already imported.
- Use the input from the Example line and assert the EXPECTED value, not the current output.
- The test must FAIL on the buggy code and PASS after the Fix.
- If the expected behavior is an error, use: with pytest.raises(ErrorType):
