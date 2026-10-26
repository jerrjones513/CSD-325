def country_info(city, country, population=None, language=None):
    result = f"{city}, {country}"
    if population is not None:
        result += f" - population {population}"
    if language is not None:
        result += f", {language}"

    return result

if __name__ == "__main__":
    print(country_info("Rome", "Italy"))
    print(country_info("Vancouver", "Canada", 14200000))
    print(country_info("Johannesburg", "South Africa", 6500000, "Multilingual"))
