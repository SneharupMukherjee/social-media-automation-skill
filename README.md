# social-media-automation

An agent skill for Claude Code, Codex and other coding agents. It finds viral short-form posts on Instagram and TikTok, breaks them into hook, tension and payoff, tracks creators for breakout posts, sorts comments into competitor, question, complaint and praise, then posts A/B variants after a human approves the preview.

## Demo

[![demo](media/preview.gif)](https://github.com/SneharupMukherjee/social-media-automation-skill/raw/main/media/demo.mp4)

click the preview for the full video with sound.

## Steps

1. **Find**: viral posts above your thresholds (default 100K+ views, 100+ comments, last 30 days)
2. **Decode**: captions and transcripts split into hook, tension, payoff
3. **Track**: creator median views, flags posts at 3x or more
4. **Listen**: up to 200 comments per post, tagged by intent
5. **Post**: Instagram, YouTube, X, LinkedIn, TikTok drafts, with stats checked at 1h, 6h, 24h and 48h

## Install

```bash
git clone https://github.com/SneharupMukherjee/social-media-automation-skill ~/.claude/skills/social-media-automation
```

Set `ANYAPI_KEY` (Instagram, YouTube) and `TIKHUB_TOKEN` (TikTok). Full API contract: [docs/social-media-automation.md](docs/social-media-automation.md).

## Files

- `SKILL.md`: the skill the agent reads
- `scripts/find_viral.py`: search helper
- `docs/`: architecture and API details
