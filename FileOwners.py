def group_by_owners(files: dict) -> dict:
  """
  Group files by their respective owner

  Args:
    files (dict): files individually referencing their owner.
  
  Returns:
    file_dict (dict): dictionary grouping files by each owner.
  """
  file_dict = {}
  for key in files.keys():
    if not file_dict.get(files[key]):
      file_dict[files[key]] = [key]
    else:
      file_dict[files[key]].append(key)
  
  return file_dict

if __name__ == "__main__":    
  files = {
      'Input.txt': 'Randy',
      'Code.py': 'Stan',
      'Output.txt': 'Randy'
  }   
  print(group_by_owners(files))
