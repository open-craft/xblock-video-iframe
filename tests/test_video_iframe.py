"""
Tests for VideoIframeXBlock
"""

import unittest
from xblock.field_data import DictFieldData
from xblock.test.toy_runtime import ToyRuntime
from video_iframe import VideoIframeXBlock


class TestVideoIframeXBlock(unittest.TestCase):
    """Tests for VideoIframeXBlock"""

    def test_basics(self):
        """Test the basic view loads."""
        data = {
            'display_name': 'My Video',
            'iframe_link': 'https://example.com/test_iframe_link',
            'video_download_link': 'https://example.com/test_video_download_link',
            'captions_download_link': 'https://example.com/test_captions_download_link'
        }
        block = VideoIframeXBlock(ToyRuntime(), DictFieldData(data), None)
        frag = block.student_view()
        json_init_args = frag.json_init_args
        self.assertEqual(data, json_init_args)
        self.assertIn('<div class="video_iframe_block">', frag.content)
