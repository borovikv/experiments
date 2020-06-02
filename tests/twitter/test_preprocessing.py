import twitter.preprocessing as subjuct


def test_clean_text():
    text = (
        "RT @SteveTSN: :L :-/ \U0001F600 Tom Brady \u201cwants all the smoke!\u201d\n\n"
        "From today\u2019s SPORTS AM by TSN, @Kayla_Grey talks about the great rivalry that continues off\u2026")

    result = subjuct.clean_text(text)

    expected = 'rt stevetsn tom brady smoke today sports tsn kayla_grey talks great rivalry continues'
    assert result == expected
