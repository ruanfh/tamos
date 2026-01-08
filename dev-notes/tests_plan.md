# Test Strategy Draft

## 1. Automated Endpoint Testing

You can fully automate endpoint testing using a test framework (e.g., pytest) and HTTP client libraries (e.g., requests). The strategy should include:

- **Setup:**
  - Start the server in a test environment (can use subprocess or test fixtures).
  - Prepare test data and configuration.
  - Optionally, use an isolated database or in-memory storage for clean state.

- **Test Cases:**
  - Health endpoint: Check server status and response format.
  - Submit endpoint: Test valid and invalid submissions, edge cases, and error handling.
  - Archive endpoint: Test retrieval, filtering, and error scenarios.
  - Authentication/authorization (if applicable).
  - Rate limiting, timeouts, and other operational concerns.

- **Teardown:**
  - Stop the server and clean up resources.
  - Remove or reset test data.

- **Automation:**
  - Integrate tests with CI/CD pipelines for continuous validation.
  - Use fixtures for setup/teardown to ensure isolation and repeatability.
  - Optionally, use tools like Postman/Newman for API collections, or pytest for Python-based tests.

## 2. Protocol Conformance Testing

- Use the protocol schema (gem.schema.json) to validate data structures.
- Write tests that check example files and real submissions against the schema.
- Ensure any implementation (client/server) passes these tests for compliance.
- Automate schema validation using jsonschema or similar tools.
- Maintain a suite of example files for regression testing.

### Folders

conformance/
│
├── cases/
│   ├── submissions/
│   │   ├── valid/
│   │   │   ├── minimal.json
│   │   │   └── with_author.json
│   │   └── invalid/
│   │       ├── missing_description.json
│   │       ├── missing_url.json
│   │       ├── extra_fields.json
│   │       ├── id_in_submission.json
│   │       └── date_in_submission.json
│   │
│   ├── stored/
│   │   ├── valid/
│   │   │   ├── minimal.json
│   │   │   └── with_author.json
│   │   └── invalid/
│   │       ├── missing_date.json
│   │       ├── missing_required_field.json
│   │       ├── extra_fields.json
│   │       ├── malformed_json.json
│   │       └── wrong_types.json
│   │
│   └── archives/
│       ├── valid/
│       │   ├── simple_archive/
│       │   │   ├── 1.json
│       │   │   └── 2.json
│       │   └── mixed_archive/
│       │       ├── 1.json
│       │       ├── 2.json
│       │       └── 3.json
│       └── invalid/
│           ├── mutated_archive/
│           │   ├── before/
│           │   │   ├── 1.json
│           │   │   └── 2.json
│           │   └── after/
│           │       ├── 1.json   ← mutated
│           │       └── 2.json
│           ├── duplicate_ids/
│           ├── malformed_files/
│           └── non_json_files/
│
├── tests/
│   ├── test_submission_schema.py
│   ├── test_stored_schema.py
│   ├── test_archive_structure.py
│   ├── test_append_only.py
│   ├── test_immutability.py
│   ├── test_no_extra_fields.py
│   ├── test_date_format.py
│   └── test_type_consistency.py
│
└── tools/
    ├── validate_submission.py
    ├── validate_stored.py
    ├── validate_archive.py
    └── helpers.py



---

Add more details or specific test cases as needed for your project.

## 3. Automated Client Testing

Client tests focus on ensuring a robust user experience and correct client behavior. Strategies include:

- **Input Validation:**
  - Test that the client validates user input before sending to the server (e.g., required fields, URL format).

- **Submission Logic:**
  - Verify the client correctly formats and sends requests to the server.
  - Mock server responses to test client handling of success, validation errors, and server errors.

- **Error Handling and Feedback:**
  - Ensure the client displays clear messages for invalid input, network errors, and server-side errors.

- **Configuration:**
  - Test loading and applying configuration options (e.g., server URL, user settings).

- **Integration:**
  - Optionally, run end-to-end tests with a test server to ensure the full flow works as expected.

- **Edge Cases:**
  - Handle timeouts, retries, and unexpected server responses gracefully.


**Recommended tools for client tests:**
- Use `pytest` as the main test runner and framework.
- Use `subprocess` to run and test the CLI client as an external process.
- Use `requests-mock` or a tiny fake server to simulate HTTP responses for client-side network tests.

Automate client tests using these tools to ensure robust, isolated, and repeatable testing of all client behaviors.

---

Server tests protect the protocol.
Client tests protect the user.
