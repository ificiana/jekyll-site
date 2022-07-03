---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
---

{% if site.data.test %}
{% assign test=site.data.test %}
    {{ test.pass..text }}
    {{ test.pass.num }}
    {% for i in test.pass.list %}
        {{ i }}
    {% endfor %}
{% else %}
    WE FAILED, PLS FIX
{% endif %}
