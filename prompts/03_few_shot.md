# Few-Shot Prompting

## What It Means
Few-shot prompting is a technique where you give the AI model a few examples (typically 2-5) of how to do a task, before asking it to perform the same task on new input. It's like showing the model a pattern through examples rather than explaining it in words.

## When to Use It
Use few-shot prompting when:
- The task is complex and needs demonstration
- You want more consistent results than zero-shot
- You have specific formatting or style requirements
- One example isn't enough to show the pattern clearly

## Example
**Task:** Classify movie reviews as positive or negative.

**Few-shot prompt:**
```
Classify these movie reviews as positive or negative:

Review: "This film was amazing! The acting was superb."
Sentiment: positive

Review: "I hated this movie. It was boring and predictable."
Sentiment: negative

Review: "The special effects were incredible."
Sentiment: positive

Review: "The plot made no sense at all."
Sentiment:
```

The model learns from the first three examples and applies the pattern to classify the fourth review.

## Key Takeaway
Few-shot prompting helps AI understand complex tasks by learning from examples, leading to more accurate and consistent responses than asking without any examples.