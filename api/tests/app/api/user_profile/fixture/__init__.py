import pytest

from tests.app.api.package_profile.fixture.package_profile_util import util


@pytest.fixture(scope="session", autouse=True)
async def package_profile():
    package_profiles = {
        "id": "a3ced43d-c299-45f9-8a0f-586ef10044b1",
        "display_name": "Test Display Name",
        "grouping_id": "group_1",
        "package_sizes": [
            {
                "id": "298de5cb-7e9f-4ee0-a75b-5a45257a41af",
                "package_profile_id": "a3ced43d-c299-45f9-8a0f-586ef10044b1",
                "display_name": "Test Display Name",
                "grouping_id": "group_1",
                "order": 0,
                "side_range_low": 0,
                "side_range_high": 0,
                "weight_range_low": 0,
                "weight_range_high": 0,
                "distance_range_low": 0,
                "distance_range_high": 0,
                "base_price": 0,
                "total_side_rate": 0,
                "range_side_rate": 0,
                "range_side_rate_divisor": 0,
                "total_weight_rate": 0,
                "range_weight_rate": 0,
                "range_weight_rate_divisor": 0,
                "total_distance_rate": 0,
                "range_distance_rate": 0,
                "range_distance_rate_divisor": 0,
                "created_at": 1689125504.0000000,
                "updated_at": 1689125504.0000000,
            },
        ],
        "created_at": 1689231616.0000000,
        "updated_at": 1689231616.0000000,
        "deleted": False
    }

    await util.create_package_profile(package_profiles)
    await util.create_package_sizes(package_profiles)

    return package_profiles


@pytest.fixture(scope="session", autouse=True)
async def package_profile_2():
    package_profiles = {
        "id": "0d357ed0-5a3f-4200-96e8-9b8047cd2586",
        "display_name": "Test Display Name",
        "grouping_id": "group_1",
        "package_sizes": [
            {
                "id": "e7509a53-0353-42e7-9724-7ef93b0374a1",
                "package_profile_id": "0d357ed0-5a3f-4200-96e8-9b8047cd2586",
                "display_name": "Test Display Name",
                "grouping_id": "group_1",
                "order": 0,
                "side_range_low": 0,
                "side_range_high": 0,
                "weight_range_low": 0,
                "weight_range_high": 0,
                "distance_range_low": 0,
                "distance_range_high": 0,
                "base_price": 0,
                "total_side_rate": 0,
                "range_side_rate": 0,
                "range_side_rate_divisor": 0,
                "total_weight_rate": 0,
                "range_weight_rate": 0,
                "range_weight_rate_divisor": 0,
                "total_distance_rate": 0,
                "range_distance_rate": 0,
                "range_distance_rate_divisor": 0,
                "created_at": 1689125504.0000000,
                "updated_at": 1689125504.0000000,
            },
        ],
        "created_at": 1689231616.0000000,
        "updated_at": 1689231616.0000000,
        "deleted": False
    }

    await util.create_package_profile(package_profiles)
    await util.create_package_sizes(package_profiles)

    return package_profiles
