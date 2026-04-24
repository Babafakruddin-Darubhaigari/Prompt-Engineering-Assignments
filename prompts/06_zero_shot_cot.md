## **06_zero_shot_cot_notes.md**

### 🧠 What the Topic Means

**Zero-Shot Chain of Thought (Zero-Shot CoT)** is a prompting technique where you **do not give any examples**, but you guide the model to solve a problem by asking it to **think step by step**.

---

### 📌 When to Use It

Use this technique when:

* You want **better reasoning** without writing examples
* The problem involves **calculations or logic**
* You need **clear step-by-step answers**

---

### 💡 Small Example Explanation

👉 Problem: A person earns ₹20,000 and spends ₹15,000. Find savings.

Prompt:

```
A person earns ₹20,000 per month and spends ₹15,000.

How much does he save?

Let's think step by step.
```

✔️ The model will:

* Subtract expenses from income
* Give the final savings with reasoning

---

### 🚀 Key Takeaway

👉 You can improve model reasoning **just by adding "Let's think step by step"**, even without giving examples.

---
