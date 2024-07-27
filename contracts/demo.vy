# pragma version ~=0.4.0

from snekmate.auth import ownable as ow
initializes: ow
exports: ow.__interface__


stored_number: public(uint256)


@deploy
@payable
def __init__():
    """
    @dev To omit the opcodes for checking the `msg.value`
         in the creation-time EVM bytecode, the constructor
         is declared as `payable`.
    @notice The `owner` role will be assigned to
            the `msg.sender`.
    """
    # The following line assigns the `owner`
    # to the `msg.sender`.
    ow.__init__()


@external
def set_stored_number(new_number: uint256):
    ow._check_owner()
    self.stored_number = new_number