---
name: social-media-automation
description: Discover viral short-form posts across Instagram and TikTok, deconstruct their narrative hooks, track creators and breakout outliers, dissect audience comments, and automate multi-platform posting with telemetry tracking.
---

# Social Media Automation Skill

Run an end-to-end short-form content research and automated distribution workflow across Instagram, TikTok, YouTube, Facebook, LinkedIn, and X.

## Workflow Pipeline

The workflow consists of 5 modular steps executed sequentially or independently:

1. **Find**: Discover viral posts exceeding view thresholds (default: 100K+ views, 100+ comments, last 30 days).
2. **Decode**: Extract captions/transcripts and deconstruct structure into Hook, Tension, and Payoff.
3. **Track**: Evaluate creator profile baseline, calculate median views, and flag 3x+ breakout posts.
4. **Listen**: Ingest and classify up to 200 comments into Competitor, Question, Complaint, and Praise tags.
5. **Post**: Schedule/publish A/B variants with human-in-the-loop approval, and track telemetry at 1h, 6h, 24h, and 48h.

---

## Step 01: Find — Search Viral Posts

### Agent Instructions
1. Interview the user for their target topic, platforms (default: Instagram, TikTok), and filters (default: 100K+ views, 100+ comments, last 30 days).
2. Query candidate posts via API:
   - **Instagram Reels & Hashtags**: AnyAPI (`/instagram/reels/search`, `/instagram/hashtag/posts`)
   - **TikTok Video Search**: TikHub (`/tiktok/api/v1/search/item`)
   - *Or run the helper script:*
     ```bash
     python3 scripts/find_viral.py --topic "<TOPIC>" --min-views 100000 --min-comments 100
     ```
3. Filter candidates:
   - `views >= 100,000`
   - `comments >= 100`
   - `date >= now - 30 days`
   - Flag as `Viral` if `views >= 500,000`
4. Return a sorted markdown table: `Link | Creator | Views | Likes | Comments | Date | Caption (First Line) | Viral Status`.

---

## Step 02: Decode — Narrative Structure

### Agent Instructions
1. Prompt the user for which post to analyze (default: most-viewed candidate from Step 1).
2. Retrieve the transcript using platform endpoints:
   - **Instagram**: AnyAPI (`/instagram/reel/transcript`)
   - **TikTok**: AnyAPI (`/tiktok/video/transcript`)
   - **YouTube**: AnyAPI (`/youtube/video/transcript`)
   - *Priority Fallback*: Native Closed Captions $\rightarrow$ Audio Speech-to-Text $\rightarrow$ Post Caption.
3. Segment the text into three structural elements:
   - **Hook**: First 1–3 seconds stopping the scroll.
   - **Tension**: Problem agitation, friction, or controversy.
   - **Payoff**: High-value resolution, recommendation, or takeaway.
4. Output the transcript with timestamps and a one-line operational rationale for why each section succeeded.

---

## Step 03: Track — Creator Baselines & Outliers

### Agent Instructions
1. Prompt user to select up to 5 creators to inspect.
2. Fetch creator profile metrics and the last 20 recent posts:
   - **Instagram**: AnyAPI (`/instagram/user/profile`, `/instagram/user/reels`)
   - **TikTok**: TikHub (`/tiktok/api/v1/user/profile`), AnyAPI (`/tiktok/user/search`)
   - **YouTube**: AnyAPI (`/youtube/search`, `/youtube/channel/details`)
3. Calculate baseline metrics:
   $$\text{Median Views} = \operatorname{median}(\{V_1, V_2, \dots, V_N\})$$
   $$\text{Breakout Multiplier} = \frac{\text{Post Views}}{\text{Median Views}} \ge 3.0$$
4. Output one creator card per profile with followers, bio, cross-platform links, median views, and flagged breakout posts.

---

## Step 04: Listen — Comment Dissection

### Agent Instructions
1. Ask user which post's comments to read (default: decoded post), sample size (up to 200), and optional focus terms (e.g., specific competitors or features).
2. Ingest comments via AnyAPI (`/instagram/media/comments`, `/tiktok/video/comments`, `/youtube/video/comments`).
3. Classify comments with multi-label tagging:
   - `Competitor`: Mentions rival brands or products.
   - `Question`: Inquiries, compatibility, specs, buying advice.
   - `Complaint`: Flaws, quality issues, pricing, hardware breakages.
   - `Praise`: Positive validation, purchase enthusiasm, content appreciation.
4. Output: Count per tag, top 3 themes per tag, and 2 verbatim quotes per tag.

---

## Step 05: Post — Auto Post & Telemetry Tracking

### Agent Instructions
1. Ask the user for connected accounts, schedule time, and two creative variants to test (A and B) with public media URLs.
2. **Human-in-the-Loop Safeguard**: Render full previews of both variants. Do NOT publish until the user explicitly responds with confirmation.
3. Dispatch confirmed posts:
   - **Instagram / Facebook**: Meta Graph API direct Reels publishing.
   - **YouTube Shorts**: YouTube Data API v3 video insert.
   - **LinkedIn & X**: Direct REST posting endpoints.
   - **TikTok**: Use TikTok Content Posting API. If direct publishing is restricted, send as draft to TikTok Creator Inbox and instruct user to finalize sound/filters in app.
4. Read back and report views, likes, comments, and shares at snapshot intervals: **1h, 6h, 24h, and 48h** in a side-by-side comparison table.
