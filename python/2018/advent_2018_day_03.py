from advent_day import AdventDay
from collections import defaultdict

class Advent2018Day03(AdventDay):

    def _parse_input(self) -> None:
        self.claims = []
        for s in self.input_str_array:
            claim_id, claim = s.split(' @ ')
            distances, dimensions = claim.split(': ')
            col_distance, row_distance = [int(d) for d in distances.split(',')]
            cols, rows = [int(d) for d in dimensions.split('x')]
            self.claims.append(
                {
                    'id': int(claim_id[1:]),
                    'col_distance': col_distance,
                    'row_distance': row_distance,
                    'cols': cols,
                    'rows': rows,
                }
            )

    def _get_coord_claims_map(self) -> dict[tuple[int, int], list[int]]:
        coord_claims_map = defaultdict(list)

        for claim in self.claims:
            for r in range(
                claim['row_distance'],
                claim['rows'] + claim['row_distance']
            ):
                for c in range(
                    claim['col_distance'],
                    claim['cols'] + claim['col_distance']
                ):
                    coord_claims_map[(r, c)].append(claim['id'])
        return coord_claims_map

    def part_one(self) -> int:
        self._parse_input()
        multiclaimed_squares = 0
        coord_claims_map = self._get_coord_claims_map()

        for coord in coord_claims_map:
            if len(coord_claims_map[coord]) >= 2:
                multiclaimed_squares += 1

        return multiclaimed_squares

    def part_two(self) -> int:
        # self._parse_input
        coord_claims_map = self._get_coord_claims_map()
        claim_set = set([claim['id'] for claim in self.claims])
        for coord in coord_claims_map:
            claims = coord_claims_map[coord]
            if len(claims) > 1:
                claim_set -= set(claims)
        return list(claim_set)[0]


Advent2018Day03().run()