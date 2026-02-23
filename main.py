"""
Extract browser cookies for a given website into a Netscape-format cookies.txt file
which e.g. gallery-dl or other programs can use to authenticate to a website.

Uses yt-dlp's cookies functionality to extract browser cookies.

Safari requires 'Full Disk Access' for the terminal you're running this script in.

Outputs path of cookies.txt file to stdout.
"""

import argparse
import io
import logging
import tempfile
from pathlib import Path

from yt_dlp import cookies


def grab_cookies_from_browser(browser_name: str, domain: str) -> str:
    """Extract cookies from a specified browser for the given domain and return as a string"""
    # Extract all cookies from the browser.
    # Note: This requires Full Disk Access for your Terminal/IDE on macOS.
    jar = cookies.extract_cookies_from_browser(browser_name)

    # Create a new jar to hold only the filtered cookies
    filtered_jar = cookies.YoutubeDLCookieJar()
    for cookie in jar:
        if domain in cookie.domain:
            filtered_jar.set_cookie(cookie)

    # Save the filtered cookies in Netscape format
    output = io.StringIO()
    # ignore_discard=True ensures session cookies (often used for auth) are included
    filtered_jar.save(output, ignore_discard=True, ignore_expires=True)
    return output.getvalue()


def write_cookies_txt(cookies_contents: bytes) -> Path:
    """Write cookies.txt in a temp dir and return the path"""
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as temp_file:
        temp_file.write(cookies_contents)
        return Path(temp_file.name)


def main():
    # Only show the path to stdout.
    # All logs (info, warning, error) will be sent to stderr.
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "browser",
        choices=sorted(cookies.SUPPORTED_BROWSERS),
        help="The browser to extract cookies from",
    )
    parser.add_argument(
        "domain", help="The domain to extract cookies for (e.g. patreon.com)"
    )
    args = parser.parse_args()

    try:
        cookies_str = grab_cookies_from_browser(args.browser, args.domain)
        if not cookies_str.strip() or args.domain not in cookies_str:
            logger.warning(
                f"No cookies found for {args.domain} in {args.browser}. Make sure you are logged in."
            )
        path = write_cookies_txt(cookies_str.encode())
        print(path)
        logger.info(
            f"Cookies for {args.domain} extracted from {args.browser} to: '{path}'\n\n"
            f"Usage: gallery-dl --cookies '{path}' <URL>"
        )
    except PermissionError:
        logger.error(
            "Ensure you are running this script with 'Full Disk Access' permissions.\n"
            "System Settings > Privacy & Security > Full Disk Access -> Toggle on your Terminal/IDE."
        )
        raise


if __name__ == "__main__":
    main()
