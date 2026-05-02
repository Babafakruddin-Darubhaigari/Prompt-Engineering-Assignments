## 🧠 JSON Prompting (Structured Output)

### What it means
JSON prompting is a technique where you ask the model to return output in a **strict structured format (JSON)**.

This makes the response:
- Easy to parse
- Consistent
- Machine-readable

---

### When to use it
- When building **applications or APIs**
- When you need **structured data output**
- When working with **automation or pipelines**
- When parsing responses in Python (like using `json.loads()`)

---

### 💡 Example

👉 Prompt:
```
Generate a learning plan.

Return only valid JSON.

Structure:
{
  "topic": "string",
  "days": [
    {
      "day": 1,
      "task": "string"
    }
  ]
}
```

👉 What happens:
- Model returns structured JSON  
- You can directly parse it in Python  

---

### 🚀 Key Takeaway

👉 **Always enforce structure when you need reliable outputs**

Clear JSON format = predictable and usable response.