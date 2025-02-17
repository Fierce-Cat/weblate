# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

from typing import TYPE_CHECKING

from weblate.trans.util import split_plural

if TYPE_CHECKING:
    from weblate.lang.models import Language

CATEGORY_FILE = 1
CATEGORY_SHARED = 2
CATEGORY_PRIVATE_OFFSET = 10000000
CATEGORY_USER_OFFSET = 20000000


def parse_category(category):
    """
    Parse category field.

    Returns tuple with from_file, shared, project_id, user_id.
    """
    if category == CATEGORY_FILE:
        return True, False, None, None
    if category == CATEGORY_SHARED:
        return False, True, None, None
    if CATEGORY_PRIVATE_OFFSET <= category < CATEGORY_USER_OFFSET:
        return False, False, category - CATEGORY_PRIVATE_OFFSET, None
    return False, False, None, category - CATEGORY_USER_OFFSET


def is_valid_entry(
    source: str,
    target: str,
    source_language: Language,
    target_language: Language,
    origin: str,
    **kwargs,
):
    """Validates whether translation memory entry has content."""
    return any(split_plural(source)) and any(split_plural(target))
