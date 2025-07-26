def sparse_similarity(docs: dict[int, list[int]]) -> list[str]:
    result = []
    doc_ids = sorted(docs.keys())
    for i in range(len(doc_ids)):
        for j in range(i + 1, len(doc_ids)):
            list1 = docs[doc_ids[i]]
            list2 = docs[doc_ids[j]]
            intersect = 0
            a = b = 0
            while a < len(list1) and b < len(list2):
                if list1[a] == list2[b]:
                    intersect += 1
                    a += 1
                    b += 1
                elif list1[a] < list2[b]:
                    a += 1
                else:
                    b += 1
            union = len(list1) + len(list2) - intersect
            sim = intersect / union if union > 0 else 0
            if sim > 0:
                result.append(f"{doc_ids[i]}:{doc_ids[j]}:{sim:.4f}")
    return result