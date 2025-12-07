from collections import defaultdict


def get_claims(input_arr: list[str]) -> list[dict]:
    claims = []
    for s in input_arr:
        claim_id, claim = s.split(" @ ")
        distances, dimensions = claim.split(": ")
        col_distance, row_distance = [int(d) for d in distances.split(",")]
        cols, rows = [int(d) for d in dimensions.split("x")]
        claims.append(
            {
                "id": int(claim_id[1:]),
                "col_distance": col_distance,
                "row_distance": row_distance,
                "cols": cols,
                "rows": rows,
            }
        )
    return claims


def get_coord_claims_map(claims: list[dict]) -> dict[tuple[int, int], list[int]]:
    coord_claims_map = defaultdict(list)

    for claim in claims:
        for r in range(claim["row_distance"], claim["rows"] + claim["row_distance"]):
            for c in range(
                claim["col_distance"], claim["cols"] + claim["col_distance"]
            ):
                coord_claims_map[(r, c)].append(claim["id"])
    return coord_claims_map


def part_one(input_arr: list[str]) -> int:
    claims = get_claims(input_arr)
    multiclaimed_squares = 0
    coord_claims_map = get_coord_claims_map(claims)

    for coord in coord_claims_map:
        if len(coord_claims_map[coord]) >= 2:
            multiclaimed_squares += 1

    return multiclaimed_squares


def part_two(input_arr: list[str]) -> int:
    claims = get_claims(input_arr)
    coord_claims_map = get_coord_claims_map(claims)
    claim_set = set([claim["id"] for claim in claims])
    for coord in coord_claims_map:
        claims = coord_claims_map[coord]
        if len(claims) > 1:
            claim_set -= set(claims)
    return list(claim_set)[0]


input_arr: list[str] = open("advent_2018_day_03.txt").read().splitlines()

print("Advent of Code 2018 - Day 03")
print(f"Part One: {part_one(input_arr)}")
print(f"Part Two: {part_two(input_arr)}")
