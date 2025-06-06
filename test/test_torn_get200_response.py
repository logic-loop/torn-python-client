# coding: utf-8

"""
    Torn API

      * The development of Torn's API v2 is still ongoing.  * If selections remain unaltered, they will default to the API v1 version.  * Unlike API v1, API v2 accepts both selections and IDs as path and query parameters.  * If any discrepancies or errors are found, please submit a [bug report](https://www.torn.com/forums.php#/p=forums&f=19&b=0&a=0) on the Torn Forums.  * In case you're using bots to check for changes on openapi.json file, make sure to specificy a custom user-agent header - CloudFlare sometimes prevents requests from default user-agents.

    The version of the OpenAPI document: 1.5.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tornclient.models.torn_get200_response import TornGet200Response

class TestTornGet200Response(unittest.TestCase):
    """TornGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TornGet200Response:
        """Test TornGet200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TornGet200Response`
        """
        model = TornGet200Response()
        if include_optional:
            return TornGet200Response(
                subcrimes = [
                    tornclient.models.torn_subcrime.TornSubcrime(
                        id = 56, 
                        name = '', 
                        nerve_cost = 56, )
                    ],
                crimes = [
                    tornclient.models.torn_crime.TornCrime(
                        id = 56, 
                        name = '', 
                        category_id = 56, 
                        category_name = '', 
                        enhancer_id = 56, 
                        enhancer_name = '', 
                        unique_outcomes_count = 56, 
                        unique_outcomes_ids = [
                            56
                            ], 
                        notes = [
                            ''
                            ], )
                    ],
                calendar = tornclient.models.torn_calendar_response_calendar.TornCalendarResponse_calendar(
                    competitions = [
                        tornclient.models.torn_calendar_activity.TornCalendarActivity(
                            title = '', 
                            description = '', 
                            start = 56, 
                            end = 56, )
                        ], 
                    events = [
                        tornclient.models.torn_calendar_activity.TornCalendarActivity(
                            title = '', 
                            description = '', 
                            start = 56, 
                            end = 56, )
                        ], ),
                hof = [
                    tornclient.models.torn_hof.TornHof(
                        id = 56, 
                        username = '', 
                        faction_id = 56, 
                        level = 56, 
                        last_action = 56, 
                        rank_name = '', 
                        rank_number = 56, 
                        position = 56, 
                        signed_up = 56, 
                        age_in_days = 56, 
                        value = null, 
                        rank = '', )
                    ],
                metadata = tornclient.models.request_metadata_with_links.RequestMetadataWithLinks(
                    links = tornclient.models.request_links.RequestLinks(
                        next = '', 
                        prev = '', ), ),
                factionhof = [
                    tornclient.models.torn_faction_hof.TornFactionHof(
                        id = 56, 
                        name = '', 
                        members = 56, 
                        position = 56, 
                        rank = '', 
                        values = tornclient.models.faction_hof_values.FactionHofValues(
                            chain = 56, 
                            chain_duration = 56, 
                            respect = 56, ), )
                    ],
                logtypes = [
                    tornclient.models.torn_log.TornLog(
                        id = 56, 
                        title = '', )
                    ],
                items = [
                    tornclient.models.torn_item.TornItem(
                        id = 56, 
                        name = '', 
                        description = '', 
                        effect = '', 
                        requirement = '', 
                        image = '', 
                        type = 'Alcohol', 
                        sub_type = 'Heavy artillery', 
                        is_masked = True, 
                        is_tradable = True, 
                        is_found_in_city = True, 
                        value = tornclient.models.torn_item_value.TornItem_value(
                            vendor = tornclient.models.torn_item_value_vendor.TornItem_value_vendor(
                                country = '', 
                                name = '', ), 
                            buy_price = 56, 
                            sell_price = 56, 
                            market_price = 56, ), 
                        circulation = 56, 
                        details = null, )
                    ],
                logcategories = [
                    tornclient.models.torn_log_category.TornLogCategory(
                        id = 56, 
                        title = '', )
                    ],
                education = [
                    tornclient.models.torn_education.TornEducation(
                        id = 56, 
                        name = '', 
                        courses = [
                            tornclient.models.torn_education_courses.TornEducationCourses(
                                id = 56, 
                                code = '', 
                                name = '', 
                                description = '', 
                                duration = 56, 
                                rewards = tornclient.models.torn_education_rewards.TornEducationRewards(
                                    working_stats = tornclient.models.torn_education_rewards_working_stats.TornEducationRewards_working_stats(
                                        manual_labor = 56, 
                                        intelligence = 56, 
                                        endurance = 56, ), 
                                    effect = '', 
                                    honor = '', ), 
                                prerequisites = tornclient.models.torn_education_prerequisites.TornEducationPrerequisites(
                                    cost = 56, 
                                    courses = [
                                        56
                                        ], ), )
                            ], )
                    ],
                bounties = [
                    tornclient.models.bounty.Bounty(
                        target_id = 56, 
                        target_name = '', 
                        target_level = 56, 
                        lister_id = 56, 
                        lister_name = '', 
                        reward = 56, 
                        reason = '', 
                        quantity = 56, 
                        is_anonymous = True, 
                        valid_until = 56, )
                    ],
                itemammo = [
                    tornclient.models.torn_item_ammo.TornItemAmmo(
                        id = 56, 
                        name = '', 
                        price = 56, 
                        types = [
                            'Standard'
                            ], )
                    ],
                faction_tree = [
                    tornclient.models.torn_faction_tree.TornFactionTree(
                        name = '', 
                        branches = [
                            tornclient.models.torn_faction_tree_branch.TornFactionTreeBranch(
                                id = 56, 
                                name = '', 
                                upgrades = [
                                    tornclient.models.torn_faction_tree_branch_upgrades_inner.TornFactionTreeBranch_upgrades_inner(
                                        name = '', 
                                        level = 56, 
                                        ability = '', 
                                        cost = 56, 
                                        challenge = tornclient.models.torn_faction_tree_branch_upgrades_inner_challenge.TornFactionTreeBranch_upgrades_inner_challenge(
                                            description = '', 
                                            amount_required = 56, 
                                            stat = 'medicalitemsused', ), )
                                    ], )
                            ], )
                    ],
                attacklog = tornclient.models.attack_log_response_attacklog.AttackLogResponse_attacklog(
                    log = [
                        tornclient.models.attack_log.AttackLog(
                            text = '', 
                            timestamp = 56, 
                            action = 'attackerhosp', 
                            icon = '', 
                            attacker = tornclient.models.attack_log_attacker.AttackLog_attacker(
                                id = 56, 
                                name = '', 
                                item = tornclient.models.attack_log_attacker_item.AttackLog_attacker_item(
                                    name = '', ), ), 
                            defender = tornclient.models.attack_log_defender.AttackLog_defender(
                                id = 56, 
                                name = '', ), )
                        ], 
                    summary = [
                        tornclient.models.attack_log_summary.AttackLogSummary(
                            id = 56, 
                            name = '', 
                            hits = 56, 
                            misses = 56, 
                            damage = 56, )
                        ], ),
                territory = [
                    tornclient.models.torn_territory.TornTerritory(
                        id = 'AAB', 
                        sector = 56, 
                        size = 56, 
                        density = 56, 
                        slots = 56, 
                        respect = 56, 
                        coordinates = tornclient.models.torn_territory_coordinates.TornTerritoryCoordinates(
                            x = 1.337, 
                            y = 1.337, ), 
                        neighbors = [
                            'AAB'
                            ], )
                    ],
                itemmods = [
                    tornclient.models.torn_item_mods.TornItemMods(
                        id = 56, 
                        name = '', 
                        description = '', 
                        dual_fit = True, 
                        weapons = [
                            'Heavy artillery'
                            ], )
                    ],
                selections = [
                    'attacklog'
                    ],
                timestamp = 56
            )
        else:
            return TornGet200Response(
                subcrimes = [
                    tornclient.models.torn_subcrime.TornSubcrime(
                        id = 56, 
                        name = '', 
                        nerve_cost = 56, )
                    ],
                crimes = [
                    tornclient.models.torn_crime.TornCrime(
                        id = 56, 
                        name = '', 
                        category_id = 56, 
                        category_name = '', 
                        enhancer_id = 56, 
                        enhancer_name = '', 
                        unique_outcomes_count = 56, 
                        unique_outcomes_ids = [
                            56
                            ], 
                        notes = [
                            ''
                            ], )
                    ],
                calendar = tornclient.models.torn_calendar_response_calendar.TornCalendarResponse_calendar(
                    competitions = [
                        tornclient.models.torn_calendar_activity.TornCalendarActivity(
                            title = '', 
                            description = '', 
                            start = 56, 
                            end = 56, )
                        ], 
                    events = [
                        tornclient.models.torn_calendar_activity.TornCalendarActivity(
                            title = '', 
                            description = '', 
                            start = 56, 
                            end = 56, )
                        ], ),
                hof = [
                    tornclient.models.torn_hof.TornHof(
                        id = 56, 
                        username = '', 
                        faction_id = 56, 
                        level = 56, 
                        last_action = 56, 
                        rank_name = '', 
                        rank_number = 56, 
                        position = 56, 
                        signed_up = 56, 
                        age_in_days = 56, 
                        value = null, 
                        rank = '', )
                    ],
                metadata = tornclient.models.request_metadata_with_links.RequestMetadataWithLinks(
                    links = tornclient.models.request_links.RequestLinks(
                        next = '', 
                        prev = '', ), ),
                factionhof = [
                    tornclient.models.torn_faction_hof.TornFactionHof(
                        id = 56, 
                        name = '', 
                        members = 56, 
                        position = 56, 
                        rank = '', 
                        values = tornclient.models.faction_hof_values.FactionHofValues(
                            chain = 56, 
                            chain_duration = 56, 
                            respect = 56, ), )
                    ],
                logtypes = [
                    tornclient.models.torn_log.TornLog(
                        id = 56, 
                        title = '', )
                    ],
                items = [
                    tornclient.models.torn_item.TornItem(
                        id = 56, 
                        name = '', 
                        description = '', 
                        effect = '', 
                        requirement = '', 
                        image = '', 
                        type = 'Alcohol', 
                        sub_type = 'Heavy artillery', 
                        is_masked = True, 
                        is_tradable = True, 
                        is_found_in_city = True, 
                        value = tornclient.models.torn_item_value.TornItem_value(
                            vendor = tornclient.models.torn_item_value_vendor.TornItem_value_vendor(
                                country = '', 
                                name = '', ), 
                            buy_price = 56, 
                            sell_price = 56, 
                            market_price = 56, ), 
                        circulation = 56, 
                        details = null, )
                    ],
                logcategories = [
                    tornclient.models.torn_log_category.TornLogCategory(
                        id = 56, 
                        title = '', )
                    ],
                education = [
                    tornclient.models.torn_education.TornEducation(
                        id = 56, 
                        name = '', 
                        courses = [
                            tornclient.models.torn_education_courses.TornEducationCourses(
                                id = 56, 
                                code = '', 
                                name = '', 
                                description = '', 
                                duration = 56, 
                                rewards = tornclient.models.torn_education_rewards.TornEducationRewards(
                                    working_stats = tornclient.models.torn_education_rewards_working_stats.TornEducationRewards_working_stats(
                                        manual_labor = 56, 
                                        intelligence = 56, 
                                        endurance = 56, ), 
                                    effect = '', 
                                    honor = '', ), 
                                prerequisites = tornclient.models.torn_education_prerequisites.TornEducationPrerequisites(
                                    cost = 56, 
                                    courses = [
                                        56
                                        ], ), )
                            ], )
                    ],
                bounties = [
                    tornclient.models.bounty.Bounty(
                        target_id = 56, 
                        target_name = '', 
                        target_level = 56, 
                        lister_id = 56, 
                        lister_name = '', 
                        reward = 56, 
                        reason = '', 
                        quantity = 56, 
                        is_anonymous = True, 
                        valid_until = 56, )
                    ],
                itemammo = [
                    tornclient.models.torn_item_ammo.TornItemAmmo(
                        id = 56, 
                        name = '', 
                        price = 56, 
                        types = [
                            'Standard'
                            ], )
                    ],
                faction_tree = [
                    tornclient.models.torn_faction_tree.TornFactionTree(
                        name = '', 
                        branches = [
                            tornclient.models.torn_faction_tree_branch.TornFactionTreeBranch(
                                id = 56, 
                                name = '', 
                                upgrades = [
                                    tornclient.models.torn_faction_tree_branch_upgrades_inner.TornFactionTreeBranch_upgrades_inner(
                                        name = '', 
                                        level = 56, 
                                        ability = '', 
                                        cost = 56, 
                                        challenge = tornclient.models.torn_faction_tree_branch_upgrades_inner_challenge.TornFactionTreeBranch_upgrades_inner_challenge(
                                            description = '', 
                                            amount_required = 56, 
                                            stat = 'medicalitemsused', ), )
                                    ], )
                            ], )
                    ],
                attacklog = tornclient.models.attack_log_response_attacklog.AttackLogResponse_attacklog(
                    log = [
                        tornclient.models.attack_log.AttackLog(
                            text = '', 
                            timestamp = 56, 
                            action = 'attackerhosp', 
                            icon = '', 
                            attacker = tornclient.models.attack_log_attacker.AttackLog_attacker(
                                id = 56, 
                                name = '', 
                                item = tornclient.models.attack_log_attacker_item.AttackLog_attacker_item(
                                    name = '', ), ), 
                            defender = tornclient.models.attack_log_defender.AttackLog_defender(
                                id = 56, 
                                name = '', ), )
                        ], 
                    summary = [
                        tornclient.models.attack_log_summary.AttackLogSummary(
                            id = 56, 
                            name = '', 
                            hits = 56, 
                            misses = 56, 
                            damage = 56, )
                        ], ),
                territory = [
                    tornclient.models.torn_territory.TornTerritory(
                        id = 'AAB', 
                        sector = 56, 
                        size = 56, 
                        density = 56, 
                        slots = 56, 
                        respect = 56, 
                        coordinates = tornclient.models.torn_territory_coordinates.TornTerritoryCoordinates(
                            x = 1.337, 
                            y = 1.337, ), 
                        neighbors = [
                            'AAB'
                            ], )
                    ],
                itemmods = [
                    tornclient.models.torn_item_mods.TornItemMods(
                        id = 56, 
                        name = '', 
                        description = '', 
                        dual_fit = True, 
                        weapons = [
                            'Heavy artillery'
                            ], )
                    ],
                selections = [
                    'attacklog'
                    ],
                timestamp = 56,
        )
        """

    def testTornGet200Response(self):
        """Test TornGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
