# Introducing Scheduled Tasks 2.0 — Manus

**Source:** [Manus Blog](https://manus.im/blog/manus-schedules) — May 18, 2026

## TL;DR
Manus (now part of Meta) upgrades Scheduled Tasks to v2.0, allowing recurring automation to run with persistent context across tasks, Projects, and web apps. Key changes: scheduled runs can continue inside the same task (preserving context/files/history), web apps can have their own scheduled actions, and improved visibility via side panel/calendar views.

## Key Points

### Continue Inside the Same Task
- Previously each scheduled run spawned a new standalone task, losing context
- Now runs can stay within the original task's conversation, instructions, files, and results
- Projects: scheduled tasks can reuse shared setup (files, skills, connectors, output standards)

### Web App Scheduled Actions
- Web apps built with Manus can now include scheduled actions (data refresh, dashboard update, reminders, summaries)
- Scheduling becomes part of the app's behavior — no need to open the page to keep routine work moving

### Better Visibility
- Side panel shows scheduled work and connected runs
- Schedule and calendar views for upcoming/past runs
- Run cards link back to the related task for inspection

### Run Controls
- Choose: continue in same task OR new separate task per run
- "Skip confirmations" for trusted workflows (send/publish/post without approval)
- Connectors for data source integration
- Agent selection, Project attachment, cloud computer resources

## Example Prompts
- "Every weekday at 9 AM, summarize the open action items in this task"
- "Every Monday, update the customer feedback summary in this Project"
- "In this web app, refresh the dashboard data every morning"

## Relevance to Engineering-Forward
Persistent-context scheduling is a critical capability for production agent deployments. Manus's approach mirrors what enterprise agent platforms need: context-carrying recurring tasks that maintain state across runs.
