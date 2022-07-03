---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
---

{% if site.data.pass %}
    {{ site.data.pass.text }}
    {{ site.data.pass.num }}
    {% for i in site.data.pass.list %}
        {{ i }}
    {% endfor %}
{% else %}
    WE FAILED, PLS FIX
{% endif %}
