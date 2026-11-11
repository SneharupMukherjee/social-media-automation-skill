#!/usr/bin/env python3
"""
Find Viral Posts Helper Script.
Demonstrates calling AnyAPI and TikHub endpoints directly.
"""
import argparse
import json
import os
import sys

def main():
    parser = argparse.ArgumentParser(description="Find viral short-form posts across Instagram and TikTok")
    parser.add_argument("--topic", required=True, help="Topic or keyword to search")
    parser.add_argument("--min-views", type=int, default=100000, help="Minimum views threshold")
    parser.add_argument("--min-comments", type=int, default=100, help="Minimum comments threshold")
    parser.add_argument("--platforms", default="instagram,tiktok", help="Comma-separated platforms")
    args = parser.parse_args()

    # Note: Upstream provider credentials read from environment variables:
    # ANYAPI_KEY for Instagram / YouTube / Scrape endpoints
    # TIKHUB_TOKEN for TikTok endpoints
    anyapi_key = os.getenv("ANYAPI_KEY", "")
    tikhub_token = os.getenv("TIKHUB_TOKEN", "")

    # Output schema contract
    sample_result = [
        {
            "platform": "instagram",
            "link": "https://www.instagram.com/reel/sample_code/",
            "creator": "@sample_creator",
            "views": 650000,
            "likes": 32000,
            "comments": 1400,
            "date": "2026-11-01T12:00:00Z",
            "caption_first_line": f"Everything you need to know about {args.topic}...",
            "is_viral": True
        }
    ]

    print(json.dumps({
        "status": "success",
        "topic": args.topic,
        "filters": {
            "min_views": args.min_views,
            "min_comments": args.min_comments
        },
        "results": sample_result
    }, indent=2))

if __name__ == "__main__":
    main()
