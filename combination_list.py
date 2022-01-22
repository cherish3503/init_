def combination(arr, result, depth, k, limit, visited):
  if depth == limit:
    print(' '.join(map(str, result)))
    return

  for i in range(k, len(arr)):
    if not visited[i]:
      visited[i] = True
      result.append(arr[i])
      combination(arr, result, depth+1, i+1, limit, visited)
      result.pop()
      visited[i] = False
      
combination(arr, result, 0, 0, limit, visited)
