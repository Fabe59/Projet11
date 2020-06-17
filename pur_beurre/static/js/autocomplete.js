let autocomplete_url = "{% url 'autocomplete:complete' %}";

$("#searchbox").autocomplete({
    source: autocomplete_url,
    minLength: 3,
});