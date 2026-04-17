# Multi-Shot Prompting

## What It Means
Multi-shot prompting is a technique where you give the AI model many examples (typically 5 or more) of how to perform a task before asking it to handle new input. It strengthens pattern recognition by showing a wider variety of cases instead of just a few.

## When to Use It
Use multi-shot prompting when:

The task requires strong pattern understanding
You want highly consistent and accurate outputs
The inputs can vary in wording or structure
Few-shot examples are not enough to capture all variations

## Example
Task: Classify movie reviews as positive or negative.

Multi-shot prompt:

Classify these movie reviews as positive or negative:

Review: "This film was amazing! The acting was superb."
Sentiment: positive

Review: "I hated this movie. It was boring and predictable."
Sentiment: negative

Review: "The special effects were incredible."
Sentiment: positive

Review: "The plot made no sense at all."
Sentiment: negative

Review: "Absolutely loved the soundtrack and visuals!"
Sentiment: positive

Review: "It was too long and very dull."
Sentiment: negative

Review: "The characters were well developed and engaging."
Sentiment: positive

Review: "Not worth watching, very disappointing."
Sentiment: negative

Review: "The storyline was okay but nothing special."
Sentiment:

The model learns from multiple examples and applies the pattern more reliably to classify the final review.

## Key Takeaway
Multi-shot prompting improves reliability by exposing the model to more examples, helping it generalize better and produce more consistent results than few-shot prompting.