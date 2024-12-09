import re

def find_pattern_positions(text, patterns):
    print(f"\n\nDEBUG in find_pattern_positions: \n\n {'-'*100}\n\n input_text: {text}\n\n{'='*100}")
    print(f"\n\nDEBUG in find_pattern_positions: \n\n {'-'*100}\n\n input_patterns: {patterns}\n\n{'='*100}")
    
    results = {pattern: [] for pattern in patterns}
    print(f"\n\nDEBUG in find_pattern_positions: \n\n {'-'*100}\n\n initial_results: {results}\n\n{'='*100}")
    
    for pattern in patterns:
        print(f"\n\nDEBUG in find_pattern_positions: \n\n {'-'*100}\n\n checking_pattern: {pattern}\n\n{'='*100}")
        
        for match in re.finditer(pattern, text):
            start = match.start()
            end = match.end()
            matched_text = text[start:end]
            
            print(f"\n\nDEBUG in find_pattern_positions: \n\n {'-'*100}\n\n found_match: '{matched_text}' start: {start} end: {end}\n\n{'='*100}")
            results[pattern].append({"start": start, "end": end})
            
            print(f"\n\nDEBUG in find_pattern_positions: \n\n {'-'*100}\n\n updated_results_for_pattern: {pattern} -> {results[pattern]}\n\n{'='*100}")
    
    print(f"\n\nDEBUG in find_pattern_positions: \n\n {'-'*100}\n\n final_results: {results}\n\n{'='*100}")
    return results

