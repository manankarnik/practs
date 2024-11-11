from random import randint
from typing import List


class Candidate:
    def __init__(self, id, quality):
        self.id = id
        self.quality = quality

    def __str__(self):
       return f"{{Id: {self.id}, Quality: {self.quality}}}"


def hire_by_threshold(candidates: List[Candidate], threshold: int) -> Candidate:
    for candidate in candidates:
        if candidate.quality > threshold: return candidate
    return candidates[-1]


def hire_by_phase(candidates: List[Candidate], rejection_count: int) -> Candidate:
    observation_phase = candidates[:rejection_count]
    hiring_phase = candidates[rejection_count:]
    best_candidate = max(observation_phase, key=lambda candidate: candidate.quality)
    for candidate in hiring_phase:
        if candidate.quality > best_candidate.quality: return candidate
    return candidates[-1]


candidates = [Candidate(i, randint(0, 100)) for i in range(20)]
for i, candidate in enumerate(candidates):
    print(f"Candidate {i+1}: {candidate}")

print("\nhire_by_threshold")
print(hire_by_threshold(candidates, 80))
print("\nhire_by_phase")
print(hire_by_phase(candidates, 10))
