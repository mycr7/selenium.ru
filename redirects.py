import os
import re

source_dir = '_blog'
target_dir = 'pages/redirects_blog'
base_url = '/blog'

for f in [x for x in os.listdir(source_dir) if os.path.isfile('%s/%s' % (source_dir, x))]:
    with open('%s/%s' % (source_dir, f)) as r:
        content = r.read()
        joomla_id = re.search('joomla_id: (\d+)', content).group(1)
        joomla_url = re.search('joomla_url: (.+)$', content, flags=re.MULTILINE).group(1)
        with open('%s/%s-%s.html' % (target_dir, joomla_id, joomla_url), 'w') as w:
            w.write('---\n')
            w.write('layout: redirect\n')
            w.write('sitemap: false\n')
            w.write('joomla_id: %s\n' % joomla_id)
            w.write('joomla_url: %s\n' % joomla_url)
            w.write('permalink: %s/%s-%s.html\n' % (base_url, joomla_id, joomla_url))
            w.write('redirect_to:  %s/%s/\n' % (base_url, re.sub('.md', '', f)))
            w.write('---\n')
