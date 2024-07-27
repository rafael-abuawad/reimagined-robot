import boa

def test_fees_only_owner_can_call(demo, accounts):
    assert demo.stored_number() == 0
    with boa.reverts(""):
        with boa.env.prank(accounts[0]):
            demo.set_stored_number(1999) 
    assert demo.stored_number() == 1999
