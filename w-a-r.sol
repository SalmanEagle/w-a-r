/// SPDX-License-Identifier: CC0-1.0
/// http://remix.ethereum.org/#optimize=false&runs=200&evmVersion=null&version=soljson-v0.8.7+commit.e28d00a7.js

pragma solidity ^0.8.7;

contract MyContract {
    string value;

    constructor() {
        value = "myValue";
    }

    function get() public view returns (string memory) {
        return value;
    }

    function set(string memory _value) public {
        value = _value;
    }
}
