import os
from typing import Optional, Tuple

from robot.api.deco import keyword

try:
    import pyautogui
except Exception as e:  # pragma: no cover - environment may not support pyautogui
    pyautogui = None

try:
    from PIL import Image, ImageChops
except Exception as e:  # pragma: no cover - Pillow might be missing
    Image = None
    ImageChops = None


class GuiTestHelper:
    """Utility class for GUI screenshot testing."""

    def __init__(self, screenshot_dir: str = "screenshots") -> None:
        self.screenshot_dir = screenshot_dir
        os.makedirs(self.screenshot_dir, exist_ok=True)

    def capture(self, name: str, region: Optional[Tuple[int, int, int, int]] = None) -> str:
        """Capture a screenshot and return the path to the saved file."""
        if pyautogui is None:
            raise RuntimeError("pyautogui is not available")
        path = os.path.join(self.screenshot_dir, f"{name}.png")
        screenshot = pyautogui.screenshot(region=region)
        screenshot.save(path)
        return path

    def compare(self, expected_path: str, actual_path: str, diff_path: Optional[str] = None, threshold: int = 0) -> bool:
        """Compare two images and return True if they match within the threshold."""
        if Image is None or ImageChops is None:
            raise RuntimeError("Pillow is not available")
        expected = Image.open(expected_path)
        actual = Image.open(actual_path)
        diff = ImageChops.difference(expected, actual)
        bbox = diff.getbbox()
        if bbox is None:
            return True
        if diff_path:
            diff.save(diff_path)
        # Count the number of differing pixels
        diff_pixels = sum(diff.convert("L").point(bool).getdata())
        return diff_pixels <= threshold


def _rc_to_tuple(region: Optional[str]) -> Optional[Tuple[int, int, int, int]]:
    if region is None:
        return None
    parts = tuple(int(x) for x in region.split(','))
    if len(parts) != 4:
        raise ValueError("Region must be four comma-separated integers")
    return parts


class GuiRobotLibrary:
    """Robot Framework library wrapping :class:`GuiTestHelper`."""

    def __init__(self, screenshot_dir: str = "screenshots") -> None:
        self.helper = GuiTestHelper(screenshot_dir)

    @keyword
    def capture(self, name: str, region: Optional[str] = None) -> str:
        region_tuple = _rc_to_tuple(region)
        return self.helper.capture(name, region_tuple)

    @keyword
    def compare_screenshots(
        self,
        expected_path: str,
        actual_path: str,
        diff_path: Optional[str] = None,
        threshold: int = 0,
    ) -> bool:
        return self.helper.compare(expected_path, actual_path, diff_path, threshold)

