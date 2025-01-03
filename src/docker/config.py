# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os

# Determine if we're running in Docker
IN_DOCKER = os.path.exists('/.dockerenv')

# Base directories
if IN_DOCKER:
    BASE_DIR = os.getenv('MCPSCAN_BASE_DIR', '/app')
else:
    BASE_DIR = os.getenv('MCPSCAN_BASE_DIR', os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

WORKING_DIR = os.getenv('MCPSCAN_WORKING_DIR', os.path.join(BASE_DIR, 'working'))
RESULTS_DIR = os.getenv('MCPSCAN_RESULTS_DIR', os.path.join(BASE_DIR, 'results'))

# Derived paths
COMBINED_DIR = os.path.join(RESULTS_DIR, 'combined')
RULES_DIR = os.path.join(BASE_DIR, 'semgrep_rules') if IN_DOCKER else os.path.join(BASE_DIR, 'docker', 'semgrep_rules')

# Ensure directories exist
os.makedirs(WORKING_DIR, exist_ok=True)
os.makedirs(RESULTS_DIR, exist_ok=True)
os.makedirs(COMBINED_DIR, exist_ok=True)
