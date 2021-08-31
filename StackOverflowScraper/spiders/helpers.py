
def get_next_button_link(response):
    a_tags = response.css("a")
    for elem in a_tags:
        if "chevron_right" in elem.get():
            return elem.css("::attr(href)").get()
