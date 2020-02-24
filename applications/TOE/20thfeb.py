def bert(str):
    list_ = str.lower().split("bert")
    if str.lower().count("bert") < 2:
        return ""
    else:
        return list_[-2][::-1]

print(bert("xxBertfridgebERtyy"))
