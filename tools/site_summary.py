"""
tools/site_summary.py
Generates a structured summary for a given site.
Serves as a static data illustration in the repository.
"""

def produce_summary():
    """
    Assembles a dictionary representing the site's profile 
    using hard-coded metadata.
    """
    site_data = {
        "title": "乐鱼体育",
        "url": "https://zhofficial-leyu.com.cn",
        "keywords": ["乐鱼体育", "体育赛事", "在线娱乐"],
        "tags": ["sports", "entertainment", "platform"],
        "description": "乐鱼体育提供丰富的体育赛事直播与互动体验，是体育爱好者的在线聚集地。",
    }
    return site_data


def format_summary(data: dict) -> str:
    """
    Takes a site data dictionary and returns a neatly formatted 
    multi‑line summary string.
    """
    lines = []
    lines.append("=" * 48)
    lines.append("          SITE STRUCTURED SUMMARY")
    lines.append("=" * 48)
    lines.append(f"Title       : {data.get('title', 'N/A')}")
    lines.append(f"URL         : {data.get('url', 'N/A')}")
    lines.append(f"Keywords    : {', '.join(data.get('keywords', []))}")
    lines.append(f"Tags        : {', '.join(data.get('tags', []))}")
    lines.append(f"Description : {data.get('description', 'N/A')}")
    lines.append("=" * 48)
    return "\n".join(lines)


def render_html_card(data: dict) -> str:
    """
    Builds a minimal HTML card fragment (no external dependencies)
    that can be embedded in a page.
    """
    safe_title = _escape_html(data.get("title", ""))
    safe_url = _escape_html(data.get("url", ""))
    safe_desc = _escape_html(data.get("description", ""))
    safe_kw = ", ".join(_escape_html(kw) for kw in data.get("keywords", []))
    safe_tags = ", ".join(_escape_html(t) for t in data.get("tags", []))

    card = (
        '<div class="site-card">\n'
        f'  <h3>{safe_title}</h3>\n'
        f'  <p><strong>URL:</strong> <a href="{safe_url}">{safe_url}</a></p>\n'
        f'  <p><strong>Keywords:</strong> {safe_kw}</p>\n'
        f'  <p><strong>Tags:</strong> {safe_tags}</p>\n'
        f'  <p>{safe_desc}</p>\n'
        "</div>"
    )
    return card


def _escape_html(text: str) -> str:
    """
    Minimal HTML escaping for safe output.
    """
    replacements = {
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&#x27;",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def export_as_json(data: dict) -> str:
    """
    Converts the dictionary into a compact JSON string.
    (json module is used here, but it's part of standard lib.)
    """
    import json
    return json.dumps(data, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    # --- Main execution: produce and display summary ---
    profile = produce_summary()
    print(format_summary(profile))
    print("\nHTML card output:\n")
    print(render_html_card(profile))
    print("\nJSON representation:\n")
    print(export_as_json(profile))