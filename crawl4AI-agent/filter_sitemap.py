import xml.etree.ElementTree as ET

# Carregar o arquivo XML
input_file = 'C:\\Users\\marce\\Downloads\\elastic-guide-sitemap.xml'
output_file = 'C:\\Users\\marce\\OneDrive\\Documentos\\code\\pydanticai\\ottomator-agents\\crawl4AI-agent\\filtered_elastic-guide-sitemap.xml'

try:
    tree = ET.parse(input_file)
    root = tree.getroot()

    # Namespace do sitemap
    namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

    # Filtrar URLs
    filtered_urls = []
    for url in root.findall('ns:url', namespace):
        loc = url.find('ns:loc', namespace)
        if loc is not None and loc.text.startswith("https://www.elastic.co/guide/en/kibana"):
            filtered_urls.append(url)

    # Contar URLs restantes
    remaining_urls_count = len(filtered_urls)
    print(f"Remaining URLs: {remaining_urls_count}")

    # Criar novo XML com URLs filtradas
    new_root = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    for url in filtered_urls:
        new_root.append(url)

    # Salvar novo arquivo XML
    new_tree = ET.ElementTree(new_root)
    new_tree.write(output_file, encoding='UTF-8', xml_declaration=True)
    print(f"Filtered sitemap saved to {output_file}")

except Exception as e:
    print(f"Error processing file: {e}")
