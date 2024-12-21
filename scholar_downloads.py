from scholarly import scholarly
import yaml

def scrape_scholar_papers(author_name):
    """
    Simple function to scrape Google Scholar papers for a given author
    """
    papers_list = []
    
    # Search for the author
    search_query = scholarly.search_author(author_name)
    author = next(search_query)
    
    # Fill in author details
    author = scholarly.fill(author)
    
    # Process each publication
    for pub in author.get('publications', []):
        pub_filled = scholarly.fill(pub)
        
        # Format paper data according to specified structure
        paper = {
            'authors': pub_filled.get('bib', {}).get('author', ''),
            'title': pub_filled.get('bib', {}).get('title', ''),
            'details': f"{pub_filled.get('bib', {}).get('journal', '')} {pub_filled.get('bib', {}).get('volume', '')}".strip(),
            'year': pub_filled.get('bib', {}).get('pub_year', ''),
            'image': '',
            'imagealt': '',
            'pmid': '',
            'pmcid': '',
            'openaccess': pub_filled.get('pub_url', ''),
            'doi': '',
            'file': '',
            'filetype': '',
            'github': '',
            'biorxiv': '',
            'psyarxiv': '',
            'contentshare': '',
            'preregistered': '',
            'opendata': '',
            'openmaterials': ''
        }
        papers_list.append(paper)
    
        # Save to YAML file
    with open('papers_jyo.yml', 'w', encoding='utf-8') as f:
        yaml.safe_dump(papers_list, f, allow_unicode=True, sort_keys=False)
    
    return papers_list

# Usage
papers = scrape_scholar_papers("Jyotirmoy V. Deshmukh")