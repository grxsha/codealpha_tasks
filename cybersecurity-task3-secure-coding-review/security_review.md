# Secure Coding Review Report

## Application Reviewed

Simple Python Login System

---

## Security Issues Found

### 1. SQL Injection (High)

**Description**

The application constructs SQL queries by directly concatenating user input.

**Risk**

An attacker can manipulate the query to bypass authentication or access unauthorized data.

**Recommendation**

Use parameterized SQL queries.

---

### 2. Hardcoded Database Name (Low)

**Description**

The database file is fixed inside the application.

**Recommendation**

Move configuration values to a configuration file or environment variables.

---

### 3. Plain Text Password Verification (High)

**Description**

Passwords are compared directly instead of using secure password hashes.

**Recommendation**

Use password hashing algorithms such as bcrypt or Argon2.

---

### 4. Input Validation

**Description**

No validation is performed on user input.

**Recommendation**

Validate and sanitize all user inputs.

---

### 5. Exception Handling

**Description**

Database errors are not handled.

**Recommendation**

Use try-except blocks and log errors without exposing sensitive information.

---

## Static Analysis

Tool Used:

Bandit

Command:

```bash
bandit vulnerable_app.py
```

---

## Conclusion

The reviewed application contains several common security vulnerabilities, including SQL injection and insecure password handling. 
By applying parameterized queries, secure password hashing, proper input validation, and robust exception handling, the application becomes significantly more secure.
