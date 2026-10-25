#!/usr/bin/env python3
"""Collect SuperMimic community candidates without browser automation."""

import argparse
import datetime as dt
import hashlib
import html
import http.cookiejar
import json
import os
from pathlib import Path
import re
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parent
CACHE = ROOT / ".cache" / "community_collector"
STATE_PATH = CACHE / "state.json"
DOCUMENT_PATH = ROOT / "COMMUNITY_TASKS.md"
DEFAULT_OUTPUT = ROOT / "community_candidates.json"
COOKIE_PATH = ROOT / ".secrets" / "xiaohongshu_cookie.txt"
KEYWORDS = ("SuperMimic", "super mimic", "superminic")
SINCE = dt.datetime(2026, 10, 20, tzinfo=dt.timezone(dt.timedelta(hours=8)))
CN_TZ = dt.timezone(dt.timedelta(hours=8))
URL_RE = re.compile(r"https?://[^\s<>()\[\]{}\"'，。；！、]+", re.I)
RELEVANT_RE = re.compile(r"super\s*mimic|superminic", re.I)
MIXIN_KEY_ENC_TAB = (
    46, 47, 18, 2, 53, 8, 23, 32, 15, 50, 10, 31, 58, 3, 45, 35,
    27, 43, 5, 49, 33, 9, 42, 19, 29, 28, 14, 39, 12, 38, 41, 13,
    37, 48, 7, 16, 24, 55, 40, 61, 26, 17, 0, 1, 60, 51, 30, 4,
    22, 25, 54, 21, 56, 59, 6, 63, 57, 62, 11, 36, 20, 34, 44, 52,
)
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
)


def now_iso():
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def atomic_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temp.replace(path)


def load_json(path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return default


def clean_text(value):
    text = re.sub(r"<[^>]+>", "", str(value or ""))
    return html.unescape(text).replace("\x00", "").strip()


def clean_url(value):
    return value.rstrip(".,;:!?)]}，。；：！？、）】").replace("&amp;", "&")


def extract_links(*values):
    links = []
    for value in values:
        if not value:
            continue
        for match in URL_RE.findall(str(value)):
            url = clean_url(html.unescape(match))
            if url not in links:
                links.append(url)
    return links


def first(record, keys, default=None):
    for key in keys:
        value = record.get(key)
        if value not in (None, ""):
            return value
    return default


def parse_time(value):
    if value in (None, "", 0, "0"):
        return None
    if isinstance(value, (int, float)) or str(value).isdigit():
        timestamp = float(value)
        if timestamp > 10_000_000_000:
            timestamp /= 1000
        try:
            return dt.datetime.fromtimestamp(timestamp, CN_TZ).isoformat(timespec="seconds")
        except (OverflowError, OSError, ValueError):
            return None
    text = str(value).strip()
    try:
        parsed = dt.datetime.fromisoformat(text.replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=CN_TZ)
        return parsed.astimezone(CN_TZ).isoformat(timespec="seconds")
    except ValueError:
        return None


def time_value(iso_text):
    if not iso_text:
        return None
    try:
        return dt.datetime.fromisoformat(iso_text).timestamp()
    except ValueError:
        return None


def public_links(links):
    safe = []
    for link in links:
        parsed = urllib.parse.urlsplit(link)
        if "xiaohongshu.com" in parsed.netloc.lower():
            match = re.search(r"/(?:explore|discovery/item)/([0-9a-f]{24})", parsed.path)
            if match:
                link = f"https://www.xiaohongshu.com/explore/{match.group(1)}"
            else:
                continue
        if link not in safe:
            safe.append(link)
    return safe


class BilibiliClient:
    def __init__(self):
        self.jar = http.cookiejar.CookieJar()
        self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.jar))
        self.mixin_key = None

    def request(self, url, use_cache=False):
        request = urllib.request.Request(
            url,
            headers={"User-Agent": USER_AGENT, "Referer": "https://www.bilibili.com/"},
        )
        parsed = urllib.parse.urlsplit(url)
        stable_query = urllib.parse.urlencode(sorted(
            (key, value) for key, value in urllib.parse.parse_qsl(parsed.query)
            if key not in ("wts", "w_rid")
        ))
        cache_identity = urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, parsed.path, stable_query, ""))
        key = hashlib.sha256(cache_identity.encode()).hexdigest()
        cache_path = CACHE / "http" / f"{key}.json"
        try:
            with self.opener.open(request, timeout=30) as response:
                payload = json.loads(response.read().decode("utf-8"))
            if use_cache:
                atomic_json(cache_path, {"fetched_at": time.time(), "payload": payload})
            return payload
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
            cached = load_json(cache_path, None)
            if use_cache and cached and time.time() - cached.get("fetched_at", 0) < 86400:
                return cached["payload"]
            raise

    def bootstrap(self):
        try:
            self.request("https://www.bilibili.com/")
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
            pass
        nav = self.request("https://api.bilibili.com/x/web-interface/nav")
        images = nav.get("data", {}).get("wbi_img")
        if not images or not images.get("img_url") or not images.get("sub_url"):
            raise RuntimeError(f"Bilibili nav code {nav.get('code')}: {nav.get('message')}")
        raw = ""
        for key in ("img_url", "sub_url"):
            raw += Path(urllib.parse.urlsplit(images[key]).path).stem
        self.mixin_key = "".join(raw[index] for index in MIXIN_KEY_ENC_TAB)[:32]

    def signed(self, endpoint, params):
        if not self.mixin_key:
            self.bootstrap()
        values = {key: str(value) for key, value in params.items()}
        values["wts"] = str(int(time.time()))
        values = {key: re.sub(r"[!'()*]", "", value) for key, value in values.items()}
        query = urllib.parse.urlencode(sorted(values.items()))
        signature = hashlib.md5((query + self.mixin_key).encode()).hexdigest()
        return f"https://api.bilibili.com{endpoint}?{query}&w_rid={signature}"

    def search(self, keyword, page):
        url = self.signed(
            "/x/web-interface/wbi/search/type",
            {"search_type": "video", "keyword": keyword, "order": "pubdate", "page": page},
        )
        payload = self.request(url, use_cache=True)
        if payload.get("code") != 0:
            raise RuntimeError(f"Bilibili search code {payload.get('code')}: {payload.get('message')}")
        return payload.get("data", {}).get("result") or []

    def detail(self, bvid):
        payload = self.request(f"https://api.bilibili.com/x/web-interface/view?bvid={urllib.parse.quote(bvid)}")
        if payload.get("code") != 0:
            raise RuntimeError(f"Bilibili detail code {payload.get('code')}: {payload.get('message')}")
        return payload.get("data") or {}

    def comments(self, aid):
        params = urllib.parse.urlencode({"type": 1, "oid": aid, "sort": 2, "pn": 1, "ps": 20})
        payload = self.request(f"https://api.bilibili.com/x/v2/reply?{params}")
        if payload.get("code") != 0:
            raise RuntimeError(f"Bilibili comments code {payload.get('code')}: {payload.get('message')}")
        records = []
        for reply in (payload.get("data", {}).get("replies") or [])[:20]:
            message = clean_text(reply.get("content", {}).get("message"))
            if not message:
                continue
            records.append({
                "author": clean_text(reply.get("member", {}).get("uname")),
                "text": message,
                "published_at": parse_time(reply.get("ctime")),
                "links": public_links(extract_links(message)),
            })
        return records


def normalize_bilibili(record, keyword):
    bvid = clean_text(record.get("bvid"))
    title = clean_text(record.get("title"))
    description = clean_text(record.get("description"))
    published_at = parse_time(record.get("pubdate"))
    return {
        "platform": "bilibili",
        "id": bvid,
        "aid": record.get("aid"),
        "title": title,
        "description": description,
        "author": clean_text(record.get("author")),
        "published_at": published_at,
        "published_ts": time_value(published_at),
        "url": f"https://www.bilibili.com/video/{bvid}/",
        "matched_keywords": [keyword],
        "links": public_links(extract_links(description)),
        "comments": [],
        "comments_status": "not_requested",
    }


def collect_bilibili(pages, detail_limit, known_ids):
    result = {"status": "ok", "entries": [], "errors": []}
    client = BilibiliClient()
    entries = {}
    try:
        client.bootstrap()
        for keyword_index, keyword in enumerate(KEYWORDS):
            for page in range(1, pages + 1):
                try:
                    records = client.search(keyword, page)
                    for record in records:
                        if not isinstance(record, dict) or not record.get("bvid"):
                            continue
                        entry = normalize_bilibili(record, keyword)
                        text = f"{entry['title']} {entry['description']}"
                        if not RELEVANT_RE.search(text):
                            continue
                        if entry["published_ts"] and entry["published_ts"] < SINCE.timestamp():
                            continue
                        bvid = entry["id"]
                        if bvid in entries:
                            if keyword not in entries[bvid]["matched_keywords"]:
                                entries[bvid]["matched_keywords"].append(keyword)
                        else:
                            entries[bvid] = entry
                except Exception as exc:
                    result["errors"].append(f"{keyword} page {page}: {exc}")
                    result["status"] = "partial"
                    break
                if keyword_index < len(KEYWORDS) - 1 or page < pages:
                    time.sleep(2)
            if result["status"] == "partial" and any("412" in error or "429" in error for error in result["errors"]):
                break
    except Exception as exc:
        return {"status": "failed", "entries": [], "errors": [str(exc)]}

    ordered = sorted(entries.values(), key=lambda item: item["published_ts"] or 0, reverse=True)
    new = [entry for entry in ordered if entry["id"] not in known_ids][:detail_limit]
    for index, entry in enumerate(new):
        try:
            detail = client.detail(entry["id"])
            entry["aid"] = detail.get("aid", entry["aid"])
            entry["description"] = clean_text(detail.get("desc")) or entry["description"]
            entry["links"] = public_links(extract_links(entry["description"]))
        except Exception as exc:
            entry["detail_error"] = str(exc)
        try:
            if entry["aid"]:
                entry["comments"] = client.comments(entry["aid"])
                entry["comments_status"] = "ok"
                for comment in entry["comments"]:
                    for link in comment["links"]:
                        if link not in entry["links"]:
                            entry["links"].append(link)
            else:
                entry["comments_status"] = "missing_aid"
        except Exception as exc:
            entry["comments_status"] = "failed"
            entry["comments_error"] = str(exc)
        if index < len(new) - 1:
            time.sleep(2)
    result["entries"] = ordered
    return result


def xhs_binary():
    local = ROOT / "tools" / "bin" / "xhs"
    if local.is_file() and os.access(local, os.X_OK):
        return str(local)
    from shutil import which
    return which("xhs")


def xhs_environment():
    env = os.environ.copy()
    if not env.get("XHS_COOKIE") and not env.get("XHS_COOKIE_FILE") and COOKIE_PATH.is_file():
        env["XHS_COOKIE_FILE"] = str(COOKIE_PATH)
    env["XHS_CACHE_DIR"] = str(CACHE / "xhs" / "cache")
    env["XHS_CONFIG_DIR"] = str(CACHE / "xhs" / "config")
    (CACHE / "xhs" / "cache").mkdir(parents=True, exist_ok=True)
    (CACHE / "xhs" / "config").mkdir(parents=True, exist_ok=True)
    return env


def sanitize_error(text):
    text = re.sub(r"(?i)(xsec_token=)[^\s&]+", r"\1[redacted]", text or "")
    text = re.sub(r"(?i)(cookie(?:-file)?\s+)[^\s]+", r"\1[redacted]", text)
    return text[-500:]


def run_xhs(binary, args, timeout=120):
    command = [binary] + args + ["--rate", "2s", "--retries", "0", "-q"]
    completed = subprocess.run(
        command,
        cwd=ROOT,
        env=xhs_environment(),
        capture_output=True,
        text=True,
        timeout=timeout,
        check=False,
    )
    records = []
    if completed.returncode == 0:
        for line in completed.stdout.splitlines():
            try:
                value = json.loads(line)
                if isinstance(value, dict):
                    records.append(value)
            except json.JSONDecodeError:
                continue
    return completed.returncode, records, sanitize_error(completed.stderr)


def xhs_author(record):
    user = first(record, ("user", "user_info", "userInfo", "author"), {})
    if isinstance(user, str):
        return clean_text(user)
    if isinstance(user, dict):
        return clean_text(first(user, ("nickname", "nick_name", "name", "user_name"), ""))
    return ""


def normalize_xhs(record, keyword=None):
    note_id = clean_text(first(record, ("note_id", "noteId", "id", "note_id_str"), ""))
    title = clean_text(first(record, ("title", "display_title", "name"), ""))
    description = clean_text(first(record, ("desc", "description", "content"), ""))
    published_at = parse_time(first(record, ("time", "create_time", "createTime", "publish_time", "publishTime", "last_update_time")))
    return {
        "platform": "xiaohongshu",
        "id": note_id,
        "title": title,
        "description": description,
        "author": xhs_author(record),
        "published_at": published_at,
        "published_ts": time_value(published_at),
        "url": f"https://www.xiaohongshu.com/explore/{note_id}" if note_id else "",
        "matched_keywords": [keyword] if keyword else [],
        "links": public_links(extract_links(title, description)),
        "comments": [],
        "comments_status": "not_requested",
    }


def xhs_error_status(code):
    return {3: "needs_auth", 5: "blocked", 6: "network_error"}.get(code, "failed")


def collect_xiaohongshu(limit, detail_limit, known_ids):
    binary = xhs_binary()
    if not binary:
        return {"status": "unavailable", "entries": [], "errors": ["xhs 0.2.0 binary not found at tools/bin/xhs or PATH"]}
    env = xhs_environment()
    if not env.get("XHS_COOKIE") and not env.get("XHS_COOKIE_FILE"):
        return {
            "status": "needs_auth",
            "entries": [],
            "errors": [f"Configure a local cookie at {COOKIE_PATH} (chmod 600) or set XHS_COOKIE_FILE"],
        }
    result = {"status": "ok", "entries": [], "errors": [], "auth": "local_cookie"}
    entries = {}
    tokens = {}
    for keyword in KEYWORDS:
        try:
            code, records, error = run_xhs(binary, ["search", keyword, "-n", str(limit), "-o", "jsonl"])
        except subprocess.TimeoutExpired:
            result["status"] = "partial"
            result["errors"].append(f"{keyword}: timeout")
            continue
        if code != 0:
            result["status"] = "partial" if entries else xhs_error_status(code)
            result["errors"].append(f"{keyword}: exit {code}: {error}")
            if code in (3, 5):
                break
            continue
        for record in records:
            entry = normalize_xhs(record, keyword)
            if not entry["id"] or not re.fullmatch(r"[0-9a-f]{24}", entry["id"]):
                continue
            if not RELEVANT_RE.search(f"{entry['title']} {entry['description']}"):
                continue
            if entry["published_ts"] and entry["published_ts"] < SINCE.timestamp():
                continue
            token = first(record, ("xsec_token", "xsecToken"), "")
            if token:
                tokens[entry["id"]] = token
            if entry["id"] in entries:
                old = entries[entry["id"]]
                if keyword not in old["matched_keywords"]:
                    old["matched_keywords"].append(keyword)
            else:
                entries[entry["id"]] = entry

    ordered = sorted(entries.values(), key=lambda item: item["published_ts"] or 0, reverse=True)
    new = [entry for entry in ordered if entry["id"] not in known_ids][:detail_limit]
    for entry in new:
        token = tokens.get(entry["id"], "")
        note_args = ["note", entry["id"], "-o", "jsonl"]
        if token:
            note_args += ["--token", token]
        try:
            code, records, error = run_xhs(binary, note_args)
            if code == 0 and records:
                detail = normalize_xhs(records[0])
                for field in ("title", "description", "author", "published_at", "published_ts", "links"):
                    if detail.get(field):
                        entry[field] = detail[field]
            elif code != 0:
                entry["detail_error"] = f"exit {code}: {error}"
            comment_args = ["comments", entry["id"], "--deep", "-n", "100", "-o", "jsonl"]
            if token:
                comment_args += ["--token", token]
            code, records, error = run_xhs(binary, comment_args)
            if code == 0:
                entry["comments_status"] = "ok"
                for record in records[:100]:
                    text = clean_text(first(record, ("content", "text", "comment"), ""))
                    if not text:
                        continue
                    comment = {
                        "author": xhs_author(record),
                        "text": text,
                        "published_at": parse_time(first(record, ("time", "create_time", "createTime"))),
                        "links": public_links(extract_links(text)),
                    }
                    entry["comments"].append(comment)
                    for link in comment["links"]:
                        if link not in entry["links"]:
                            entry["links"].append(link)
            else:
                entry["comments_status"] = "failed"
                entry["comments_error"] = f"exit {code}: {error}"
        except subprocess.TimeoutExpired:
            entry["comments_status"] = "failed"
            entry["comments_error"] = "timeout"
    result["entries"] = ordered
    return result


def known_content_ids():
    text = DOCUMENT_PATH.read_text(encoding="utf-8") if DOCUMENT_PATH.exists() else ""
    return {
        "bilibili": set(re.findall(r"BV[0-9A-Za-z]{10}", text)),
        "xiaohongshu": set(re.findall(r"xiaohongshu\.com/explore/([0-9a-f]{24})", text)),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--bilibili-pages", type=int, default=3)
    parser.add_argument("--xhs-limit", type=int, default=40)
    parser.add_argument("--detail-limit", type=int, default=20)
    parser.add_argument("--skip-bilibili", action="store_true")
    parser.add_argument("--skip-xiaohongshu", action="store_true")
    args = parser.parse_args()
    CACHE.mkdir(parents=True, exist_ok=True)
    known = known_content_ids()
    state = load_json(STATE_PATH, {"seen": {}})
    platforms = {}
    if not args.skip_bilibili:
        platforms["bilibili"] = collect_bilibili(max(1, min(args.bilibili_pages, 5)), args.detail_limit, known["bilibili"])
    if not args.skip_xiaohongshu:
        platforms["xiaohongshu"] = collect_xiaohongshu(args.xhs_limit, args.detail_limit, known["xiaohongshu"])

    output = {
        "schema_version": 1,
        "fetched_at": now_iso(),
        "since": SINCE.isoformat(timespec="seconds"),
        "browser_required": False,
        "platforms": {},
        "new_candidates": [],
        "new_since_last_run": [],
    }
    for platform, result in platforms.items():
        entries = result.pop("entries")
        result["count"] = len(entries)
        result["known_in_document"] = sum(entry["id"] in known.get(platform, set()) for entry in entries)
        output["platforms"][platform] = result
        for entry in entries:
            key = f"{platform}:{entry['id']}"
            seen = state["seen"].get(key, {})
            first_seen = seen.get("first_seen_at", output["fetched_at"])
            state["seen"][key] = {
                "first_seen_at": first_seen,
                "last_seen_at": output["fetched_at"],
                "url": entry["url"],
            }
            if entry["id"] not in known.get(platform, set()):
                output["new_candidates"].append(entry)
            if "first_seen_at" not in seen:
                output["new_since_last_run"].append(entry)
        output["platforms"][platform]["entries"] = entries
    output["new_candidate_count"] = len(output["new_candidates"])
    output["new_since_last_run_count"] = len(output["new_since_last_run"])
    atomic_json(args.output, output)
    atomic_json(STATE_PATH, state)
    summary = {
        platform: {key: value for key, value in result.items() if key != "entries"}
        for platform, result in output["platforms"].items()
    }
    summary["new_candidates"] = output["new_candidate_count"]
    summary["new_since_last_run"] = output["new_since_last_run_count"]
    summary["output"] = str(args.output)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
