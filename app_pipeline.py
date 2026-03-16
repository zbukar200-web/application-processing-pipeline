from collections import deque

# ----------------------------------------
# Application Processing Pipeline
# Demonstrates Queue (FIFO) and Stack (LIFO)
# ----------------------------------------

# 1. Initialize an empty queue and stack
application_inbox = deque()
processed_history = []

# 2. Ingest messy startup application names
messy_startups = [" TechCorp ", "bio-gen", "  GreenSpark  ", "AI Nexus "]

print("Incoming startup applications (messy data):")
print(messy_startups)
print()

# Clean the data and add it to the queue
for startup in messy_startups:
    cleaned_startup = startup.strip().lower()
    application_inbox.append(cleaned_startup)

print("Cleaned applications added to queue:")
print(list(application_inbox))
print()

# 3. Process applications in FIFO order
print("Processing applications...")
while application_inbox:
    current_application = application_inbox.popleft()
    print(f"Approving: {current_application}")
    processed_history.append(current_application)

print()

# Show approval history after processing
print("Processed history (stack):")
print(processed_history)
print()

# 4. Undo the most recent approval (LIFO)
if processed_history:
    reverted_application = processed_history.pop()
    print(f"Reverting approval for: {reverted_application}")
else:
    print("No processed applications to revert.")